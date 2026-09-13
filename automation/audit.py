"""Read-only, evidence-first job discovery. Python 3.11+, standard library only.
No application submission, credentials, inferred screening answers, or browser control.
"""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import html
from html.parser import HTMLParser
import ipaddress
import json
from pathlib import Path
import re
import socket
from urllib.parse import urlparse, urljoin
from urllib.request import Request, build_opener, HTTPRedirectHandler
from urllib.error import HTTPError

ROOT = Path(__file__).resolve().parents[1]
ATS = {'job-boards.greenhouse.io': 'greenhouse', 'boards.greenhouse.io': 'greenhouse',
       'jobs.lever.co': 'lever', 'jobs.ashbyhq.com': 'ashby'}
SKILLS = ('hplc', 'nmr', 'spectroscopy', 'chromatography', 'sample preparation', 'glp',
          'organic synthesis', 'quality control')
DOCS = {
    'greenhouse': 'https://docs.greenhouse.io/job-board.html',
    'lever': 'https://github.com/lever/postings-api',
    'ashby': 'https://developers.ashbyhq.com/docs/public-job-posting-api',
}


def now():
    return datetime.now(timezone.utc).isoformat()


def public_url(url):
    p = urlparse(url)
    if p.scheme != 'https' or not p.hostname or p.username or p.password or p.port not in (None, 443):
        raise ValueError('Only public HTTPS URLs without credentials are allowed')
    addresses = socket.getaddrinfo(p.hostname, 443, type=socket.SOCK_STREAM)
    if not addresses or any(not ipaddress.ip_address(a[4][0]).is_global for a in addresses):
        raise ValueError('Non-public destination blocked')
    return url


class SafeRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        public_url(newurl)
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def fetch(url):
    """One GET, bounded size/time, no retries of denied or rate-limited requests."""
    result = {'url': url, 'checked_at': now(), 'status': None}
    try:
        public_url(url)
        request = Request(url, headers={'User-Agent': 'JobSearchSF-EvidenceAudit/1.0',
                                        'Accept': 'application/json,text/html'})
        with build_opener(SafeRedirect()).open(request, timeout=15) as response:
            body = response.read(4_000_001)
            if len(body) > 4_000_000:
                raise ValueError('Response exceeds 4 MB limit')
            result.update(status=response.status, final_url=response.url,
                          sha256=hashlib.sha256(body).hexdigest(),
                          content_type=response.headers.get('Content-Type', ''),
                          body=body.decode('utf-8', errors='replace'))
    except HTTPError as exc:
        result.update(status=exc.code, error='HTTP error; not proof of closure')
    except Exception as exc:
        result['error'] = type(exc).__name__ + ': ' + str(exc)[:180]
    return result


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.urls = []

    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if value and (tag, key) in {('a', 'href'), ('iframe', 'src')}:
                self.urls.append(value)


def board(url):
    p = urlparse(url)
    parts = p.path.strip('/').split('/')
    if p.scheme == 'https' and p.hostname in ATS and re.fullmatch(r'[A-Za-z0-9_-]+', parts[0]):
        return ATS[p.hostname], parts[0]
    return None


def api_url(kind, token):
    return {'greenhouse': f'https://boards-api.greenhouse.io/v1/boards/{token}/jobs?content=true',
            'lever': f'https://api.lever.co/v0/postings/{token}?mode=json',
            'ashby': f'https://api.ashbyhq.com/posting-api/job-board/{token}'}[kind]


def plain(text):
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', html.unescape(text or ''))).strip()


def normalize(kind, token, payload):
    rows = payload if kind == 'lever' else payload['jobs']
    if not isinstance(rows, list):
        raise ValueError('Unexpected API schema')
    for row in rows:
        if kind == 'greenhouse':
            if row.get('internal_job_id', 'unknown') is None:
                continue  # Talent pools are not vacancies.
            title, location = row['title'], row.get('location', {}).get('name', '')
            description, url = plain(row.get('content', '')), row['absolute_url']
            identifier = str(row['id'])
        elif kind == 'lever':
            title, location = row['text'], row.get('categories', {}).get('location', '')
            description = plain(row.get('descriptionPlain', '') + ' ' + row.get('description', '') +
                                ' ' + ' '.join(x.get('content', '') for x in row.get('lists', [])))
            url, identifier = row['hostedUrl'], str(row['id'])
        else:
            if row.get('isListed') is False:
                continue
            title, location = row['title'], row.get('location', '')
            description = plain(row.get('descriptionPlain') or row.get('descriptionHtml', ''))
            url = row['jobUrl']
            identifier = urlparse(url).path.strip('/').split('/')[-1]
        if urlparse(url).scheme != 'https':
            continue
        yield {'key': f'{kind}:{token.lower()}:{identifier}', 'platform': kind,
               'board': token, 'requisition': identifier, 'title': title, 'location': location,
               'url': url, 'description': description}


def assess(job):
    """Keyword overlap is triage, never a qualification or probability score."""
    text = (job['title'] + ' ' + job['description']).lower()
    hits = [skill for skill in SKILLS if re.search(r'\b' + re.escape(skill) + r'\b', text)]
    sf = bool(re.search(r'\bsan francisco\b', job['location'], re.I)) and not bool(
        re.search(r'\bsouth san francisco\b', job['location'], re.I))
    flags = ['REQUIREMENTS_NOT_FULLY_VERIFIED', 'NO_SUBMISSION_ADAPTER', 'PROFILE_PROVENANCE_REQUIRED']
    if not job.get('employer_link_evidence'):
        flags.append('EMPLOYER_ATS_RELATIONSHIP_UNVERIFIED')
    if not sf:
        flags.append('LOCATION_OR_REMOTE_ELIGIBILITY_UNVERIFIED')
    else:
        flags.append('TRANSIT_TO_WORKSITE_UNVERIFIED')
    if re.search(r'\b(ph\.?d|senior|principal|director|licensed|phlebotom|animal|in vivo)', text):
        flags.append('ADVANCED_OR_SPECIALIST_REQUIREMENTS_REVIEW')
    if not hits:
        flags.append('NO_CORE_SKILL_OVERLAP')
    return {'skill_overlap': hits, 'sf_location_text': sf,
            'triage': 'potential_match' if hits and sf else 'not_shortlisted',
            'state': 'blocked', 'flags': flags}


def profile_audit(profile, path='$'):
    """Every leaf has a source path; existing generated profile is not primary evidence."""
    rows = []
    if isinstance(profile, dict):
        for key, value in profile.items():
            rows.extend(profile_audit(value, path + '.' + key))
    elif isinstance(profile, list):
        for i, value in enumerate(profile):
            rows.extend(profile_audit(value, f'{path}[{i}]'))
    else:
        flag = 'MISSING' if profile in ('', None) else 'SOURCE_IS_EXISTING_PROFILE_NOT_PRIMARY_EVIDENCE'
        if any(k in path.lower() for k in ('workauth', 'sponsor', 'veteran', 'disability', 'driverlicense',
                                           'salary', 'startdate', 'noticeperiod', 'publication')):
            flag = 'DO_NOT_AUTOFILL_WITHOUT_PRIMARY_EVIDENCE'
        rows.append({'field': path, 'source': 'assets/profile/Brian_Profile.json', 'flag': flag})
    return rows


def audit(live=False):
    legacy = json.loads((ROOT / 'assets/profile/All_Jobs_Easy_Apply.json').read_text())
    profile = json.loads((ROOT / 'assets/profile/Brian_Profile.json').read_text())
    urls = sorted({j[k] for j in legacy for k in ('officialLink', 'applyLinkClean') if j.get(k)})
    evidence = {}
    if live:
        with ThreadPoolExecutor(max_workers=4) as pool:
            evidence = dict(zip(urls, pool.map(fetch, urls)))
    boards = {}
    for url in urls:
        b = board(url)
        if b:
            boards.setdefault(b, set())
    # A link in a legacy-designated employer page is stronger than an ATS URL alone,
    # but is not a certification that the employer domain itself is authentic.
    for job in legacy:
        source = job['officialLink']
        ev = evidence.get(source, {})
        if board(source) or ev.get('status') != 200:
            continue
        parser = Links()
        parser.feed(ev.get('body', ''))
        for link in parser.urls:
            b = board(urljoin(ev.get('final_url', source), link))
            if b:
                boards.setdefault(b, set()).add(source)
    discovered = {}
    board_checks = []
    for (kind, token), sources in sorted(boards.items()):
        endpoint = api_url(kind, token)
        ev = fetch(endpoint) if live else {'url': endpoint, 'error': 'Not checked (offline run)'}
        check = {k: v for k, v in ev.items() if k != 'body'}
        check.update(platform=kind, board=token, documentation=DOCS[kind])
        try:
            if ev.get('status') == 200:
                jobs = list(normalize(kind, token, json.loads(ev['body'])))
                check['listing_count'] = len(jobs)
                for job in jobs:
                    job.update(source=endpoint, checked_at=ev['checked_at'],
                               source_sha256=ev['sha256'], employer_link_evidence=sorted(sources))
                    job.update(assess(job))
                    discovered[job['key']] = job
        except (ValueError, KeyError, TypeError) as exc:
            check['error'] = 'API schema/parse error: ' + str(exc)[:160]
        board_checks.append(check)
    rows = []
    for j in legacy:
        url = j['applyLinkClean']
        ev = evidence.get(url, {})
        flags = ['LEGACY_MATCH_SCORE_UNVALIDATED', 'EXACT_LIVE_REQUISITION_NOT_VERIFIED']
        b = board(url)
        if (b and len(urlparse(url).path.strip('/').split('/')) == 1) or urlparse(url).path in ('', '/'):
            flags.append('BOARD_OR_HOME_PAGE_NOT_A_JOB')
        if j.get('status') == 'monitor':
            flags.append('MONITOR_NOT_CONFIRMED_OPENING')
        if ev.get('status') != 200:
            flags.append('SOURCE_UNREACHABLE_OR_NOT_CHECKED')
        if j.get('flag'):
            flags.append('EXISTING_REVIEW_FLAG: ' + j['flag'])
        rows.append({'id': j['id'], 'company': j['company'], 'title': j['position'],
                     'source': 'assets/profile/All_Jobs_Easy_Apply.json#' + j['id'],
                     'official_url': j['officialLink'], 'apply_url': url,
                     'http_status': ev.get('status'), 'flags': flags, 'state': 'blocked'})
    candidates = sorted(discovered.values(), key=lambda j: (-len(j['skill_overlap']), j['key']))
    # Avoid publishing complete job descriptions or any candidate contact information.
    for job in candidates:
        job['skill_evidence'] = [job['description'][max(0, m.start()-80):m.end()+120]
                                 for skill in job['skill_overlap']
                                 for m in [re.search(re.escape(skill), job['description'], re.I)] if m]
        del job['description']
    return {'generated_at': now(), 'mode': 'live_read_only' if live else 'offline',
            'submission_enabled': False, 'applications_submitted': 0,
            'limitations': ['HTTP 200 is reachability, not proof of vacancy or employer authenticity.',
                            'Legacy employer domains are seeds, not newly certified identities.',
                            'Keyword overlap is not full requirements verification.',
                            'No complete legal name or primary profile evidence available.',
                            'No credentials, CAPTCHA bypass, or applications sent.'],
            'summary': {'legacy_entries': len(rows), 'api_listings': len(candidates),
                        'potential_matches': sum(j['triage'] == 'potential_match' for j in candidates),
                        'ready_to_submit': 0},
            'profile_audit': profile_audit(profile), 'legacy_audit': rows,
            'source_checks': [{k: v for k, v in e.items() if k != 'body'} for e in evidence.values()],
            'board_checks': board_checks, 'queue': candidates}


def render(report):
    esc = lambda x: html.escape(str(x))
    def link(url, label='Source'):
        if urlparse(url).scheme != 'https':
            return esc(url)
        return f'<a href="{esc(url)}" target="_blank" rel="noopener noreferrer">{esc(label)}</a>'
    rows = ''.join(f'<tr><td>{esc(j["id"])}</td><td>{esc(j["company"])}<br>{esc(j["title"])}</td>'
                   f'<td>{link(j["official_url"], "Employer seed")}<br>{link(j["apply_url"], "Apply source")}</td>'
                   f'<td>{esc(j["http_status"] or "Not checked")}</td><td>{esc("; ".join(j["flags"]))}</td></tr>'
                   for j in report['legacy_audit'])
    queue = ''.join(f'<article><h3>{esc(j["title"])}</h3><p>{esc(j["location"])} · {esc(j["board"])}</p>'
                    f'<p>{link(j["url"], "Official ATS listing")} · {link(j["source"], "API evidence")}</p>'
                    f'<p>Skill keywords: {esc(", ".join(j["skill_overlap"]))}</p>'
                    f'<p class="muted">Blocked: {esc("; ".join(j["flags"]))}</p></article>'
                    for j in report['queue'] if j['triage'] == 'potential_match')
    fields = ''.join(f'<tr><td>{esc(p["field"])}</td><td>{esc(p["flag"])}</td></tr>' for p in report['profile_audit'])
    return f'''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Autonomy audit — JobSearchSF</title><style>
body{{font:16px/1.6 system-ui;margin:0;background:#f3f6fa;color:#172b42}}main{{max-width:1200px;margin:auto;padding:30px}}
a{{color:#075f9b}}h1{{font-size:2.4rem}}article,.notice{{padding:20px;background:white;border:1px solid #ccd6e0;border-radius:12px;margin:12px 0}}
.notice{{border-left:6px solid #bb6514}}table{{border-collapse:collapse;width:100%;background:white;font-size:14px}}td,th{{padding:12px;border:1px solid #ddd;text-align:left;overflow-wrap:anywhere}}
.scroll{{overflow:auto}}.muted{{color:#526173;font-size:14px}}.stats{{font-weight:bold;font-size:20px}}</style><main>
<a href="../../index.html">← JobSearchSF</a><h1>Autonomous application readiness</h1>
<p>Evidence-first discovery · {esc(report['generated_at'])} · {esc(report['mode'])}</p>
<div class="notice"><strong>No applications submitted. Submission is disabled.</strong><br>
This report supersedes legacy “verified” badges. Career pages are leads, not verified vacancies.
Missing facts are flagged, never guessed. This is an automated audit, not a running application bot.</div>
<p class="stats">{report['summary']['legacy_entries']} legacy entries audited · {report['summary']['api_listings']} API listings ·
{report['summary']['potential_matches']} potential matches · 0 ready to submit</p>
<p><a href="autonomy-report.json">Download full evidence JSON</a> · <a href="../../automation/README.md">Capabilities and roadmap</a></p>
<h2>Potential matches from live API listings</h2><p>Keyword triage only; location text is not a verified commute. All requirements still need evidence.</p>{queue or '<p>No potential matches discovered in this run. See board errors in the JSON; this does not prove no jobs exist.</p>'}
<h2>All legacy entries — row-by-row audit</h2><div class="scroll"><table><thead><tr><th>ID</th><th>Legacy claim</th><th>Review links</th><th>HTTP</th><th>Irregularities</th></tr></thead><tbody>{rows}</tbody></table></div>
<h2>Profile — field-by-field provenance audit</h2><p>Values are intentionally omitted. Source: existing assets/profile/Brian_Profile.json. Existing generated information is not independently verified evidence.</p>
<div class="scroll"><table><thead><tr><th>Field</th><th>Finding</th></tr></thead><tbody>{fields}</tbody></table></div>
<h2>Separate official-page review</h2><p><a href="../../automation/official-source-review.md">Read the dated employer and API findings</a>. These observations used a separate retrieval tool and do not replace failed automated checks.</p>
<h2>Official API documentation</h2><ul>{''.join('<li>' + link(v, k) + '</li>' for k,v in DOCS.items())}</ul>
</main></html>'''


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--live', action='store_true', help='GET official source pages and public ATS APIs')
    parser.add_argument('--output', type=Path, default=ROOT / 'assets/verification')
    args = parser.parse_args()
    report = audit(args.live)
    args.output.mkdir(parents=True, exist_ok=True)
    (args.output / 'autonomy-report.json').write_text(json.dumps(report, indent=2) + '\n')
    (args.output / 'autonomy-report.html').write_text(render(report))
    print(json.dumps(report['summary']))


if __name__ == '__main__':
    main()
