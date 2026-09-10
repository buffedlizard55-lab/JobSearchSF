# -*- coding: utf-8 -*-
"""Update index.html, app.js, style.css, sitemap.xml, README.md for 120 entries (Pass 6)."""
import os
import re

ROOT = os.path.dirname(os.path.abspath(__file__))


def rw(path, fn):
    p = os.path.join(ROOT, path)
    s = open(p, encoding="utf-8").read()
    out = fn(s)
    if out != s:
        open(p, "w", encoding="utf-8").write(out)
        return True
    return False


MISSES = []


def rep(s, old, new, must=True):
    if old not in s:
        MISSES.append(old[:110])
        return s
    return s.replace(old, new, 1)


# ------------------------------------------------------------------ index.html
def patch_index(s):
    s = rep(s, "<title>JobSearchSF — 100 Verified SF Chemistry & Lab Jobs (N Judah Commute)</title>",
            "<title>JobSearchSF \U0001f9ea — 120 Verified SF Chemistry & Lab Jobs (N Judah Commute)</title>")
    s = rep(s, 'content="100 verified San Francisco chemistry', 'content="120 verified San Francisco chemistry')
    s = rep(s, "<h1>JobSearchSF \U0001f9ea — 100 Verified SF Jobs</h1>",
            "<h1>JobSearchSF \U0001f9ea — 120 Verified SF Jobs</h1>")
    s = rep(s, '<span class="badge batch5">20 new in Pass 5</span></div>',
            '<span class="badge batch5">20 in Pass 5</span> <span class="badge batch6">20 new in Pass 6</span></div>')
    s = rep(s, "Verified: <strong>100 entries + official sources</strong>",
            "Verified: <strong>120 entries + official sources</strong>")
    s = rep(s, "<strong>This page lists 100 verified, SF-located lab-science opportunities</strong> (20 Pass 1 + 20 Pass 2 + 20 Pass 3 + 20 Pass 4 + 20 new in Pass 5, quintuple-verified Sept 9-10, 2026)",
            "<strong>This page lists 120 verified, SF-located lab-science opportunities</strong> (20 Pass 1 + 20 Pass 2 + 20 Pass 3 + 20 Pass 4 + 20 Pass 5 + 20 new in Pass 6, verified Sept 9-10, 2026)")
    s = rep(s, "and a subpage with step-by-step apply guide + tailored resume/cover letter downloads.",
            "and a subpage with a step-by-step apply guide plus resume/cover letter downloads.")
    s = rep(s, "Highest chemistry-fit across all 100 verified entries.", "Highest chemistry-fit across all 120 verified entries.")
    s = rep(s, "Verified opportunities — sortable table (100 jobs)", "Verified opportunities — sortable table (120 jobs)")
    s = rep(s, '<button class="f-status active" data-status="all">All 100</button>',
            '<button class="f-status active" data-status="all">All 120</button>')
    s = rep(s, '<button class="f-batch active" data-batch="all">Pass 1+2+3+4+5</button>',
            '<button class="f-batch active" data-batch="all">Pass 1+2+3+4+5+6</button>')
    s = rep(s, '<button class="f-batch" data-batch="5">New: Pass 5 (81-100)</button>',
            '<button class="f-batch" data-batch="5">Pass 5 (81-100)</button>\n        '
            '<button class="f-batch" data-batch="6">New: Pass 6 (101-120)</button>')
    s = rep(s, "SF-transit-commutable bench roles above (100 verified, direct-apply)",
            "SF-transit-commutable bench roles above (120 verified, direct-apply)")

    # pass-4 / pass-5 stale LIVE claims corrected after the 2026-09-09 re-check
    s = rep(s, "General Proximity 5660523004 LIVE, Anthropic 5285248008 LIVE,",
            "General Proximity 5660523004 LIVE, Anthropic 5285248008 (LIVE in Pass 4; official board shows "
            "\u201cno longer open\u201d on the 2026-09-09 re-check \u2014 row job-73 corrected to monitor),")
    s = rep(s, "City Chemist 2486 REF60430L via careers.sf.gov LIVE,",
            "City Chemist 2486 REF60430L via careers.sf.gov (window was Apr 27\u2013May 8, 2026 \u2014 row job-92 "
            "corrected to monitor on the 2026-09-09 re-check),")
    s = rep(s, '          <li><strong>\u2713 No recruiters / 3rd-party \u201ceasy apply\u201d as apply channel:</strong>',
            '          <li><strong>\u2713 Official apply channel only (Pass 6, new):</strong> 14 live UCSF recruitments read '
            'straight from the official \u201cBrowse Open Recruitments\u201d list at aprecruit.ucsf.edu/apply (JPF06065, JPF05785, '
            'JPF06131, JPF05798, JPF06179, JPF06193, JPF06056, JPF06049, JPF06073, JPF05968, JPF05881, JPF06050, JPF05770, '
            'JPF05544) \u2014 each with the open / review / accept-until dates printed by UCSF; 3 City of SF lab classes from '
            'careers.sf.gov role pages (2402 Laboratory Technician I, 2416 Laboratory Technician II SFDPH, 2463 Microbiologist I); '
            'plus 3 documented alternates verified on the employers\u2019 own boards (Plasmidsaurus Ashby 1dea5cc2 published '
            '2026-08-26; Addition Therapeutics Greenhouse 5216310007 and 5208635007 published Aug 2026) \u2014 the last three are '
            'flagged, not targets, because the worksites are South San Francisco. All direct-apply, no recruiters.</li>\n'
            '          <li><strong>\u2713 What Pass 6 changed on purpose:</strong> six employers were checked and produced '
            '<em>no</em> SF entry-level opening, so nothing was added for them (SFMOMA Lever board, NCIRE board, Vir Biotechnology '
            'SF reqs \u2014 director-level only, BridgeBio, Jushi, Ring Therapeutics, Personalis, Gladstone public board). Those are '
            'recorded under \u201cReviewed but excluded\u201d rather than padded with weak rows. Two stale \u201cLIVE\u201d claims from '
            'earlier passes (job-73 Anthropic, job-92 City Chemist) were corrected to monitor.</li>\n'
            '          <li><strong>\u2713 No recruiters / 3rd-party \u201ceasy apply\u201d as apply channel:</strong>')

    # documents section - no "tailored" meta, no commute in letters
    s = rep(s, '<h2 class="sec">Resume & cover letter — tailored, downloadable, beginner-friendly</h2>\n        '
               '<p class="sec-sub">Each job subpage has step-by-step apply guide + tailored resume & cover letter (brief, polite, easy to read for hiring manager).</p>',
               '<h2 class="sec">Resume &amp; cover letter — downloadable, beginner-friendly</h2>\n        '
               '<p class="sec-sub">Every job subpage carries the step-by-step apply guide plus a resume, cover letter and '
               'intro email written as ordinary application documents: no transit or commute content, no \u201cthis resume is '
               'tailored\u201d language, no placeholders, nothing that is not on your real r\u00e9sum\u00e9.</p>')
    s = rep(s, '<strong>Master resume & cover letter (base):</strong> These are tailored to B.S. Chemistry + HPLC/NMR/synthesis and are short so a hiring manager can quickly approve an interview.<br><br>',
            '<strong>Master resume &amp; cover letter (base):</strong> One page, written from your actual background '
            '(B.S. Chemistry + HPLC/NMR/synthesis + GLP/QC), short enough for a hiring manager to approve an interview in '
            'under a minute. The base letter is company-neutral: add today\u2019s date and the employer line before sending. '
            'Each job page also has a version whose summary and skills order follow that posting\u2019s language.<br><br>')
    s = rep(s, '<li><strong>Tailored resume:</strong> Emphasizes the skills that match that specific role (e.g., HPLC for Anresco, synthesis for UCSF Pharmaceutical Chemistry, GLP/QC for Vitalant).</li>\n          '
               '<li><strong>Tailored cover letter:</strong> Brief (3 short paragraphs), polite, professional, references SF location and N Judah commute, explains why you\u2019re a good fit, asks for interview.</li>',
               '<li><strong>Resume:</strong> same real experience in every version, with the skills and bullets ordered so the '
               'techniques the posting leads with appear first (HPLC and purification for Anresco, sample prep and records for '
               'Vitalant, solution prep and instrument care for the UCSF core-facility roles).</li>\n          '
               '<li><strong>Cover letter:</strong> three short paragraphs \u2014 what you bring, how it maps to this posting, and a '
               'request to talk. It never mentions how you get to work; that stays in the \u201cGetting there\u201d section of the page.</li>\n          '
               '<li><strong>Intro email:</strong> subject line plus a five-sentence body for the message box or a listed contact '
               'address; anything marked as an internal note is for you, not for sending.</li>')

    # subpage link list: add pass 6
    s = rep(s, '<a href="jobs/job-100.html">job-100</a></p>',
            '<a href="jobs/job-100.html">job-100</a></p>\n        '
            '<p><strong>Pass 6 (new — 101-120):</strong> '
            + " · ".join('<a href="jobs/job-%d.html">job-%d</a>' % (i, i) for i in range(101, 121)) + "</p>")
    s = rep(s, 'Research snapshot <span id="today"></span> (Pass 1 + Pass 2 + Pass 3 + Pass 4 quadruple-verified Sept 9-10, 2026) · Branch <code>arena/01a0882a-jobsearchsf</code> · 100 verified SF entries, each with official sources. Verification logs: <a href="assets/verification/VERIFICATION_LOG_PASS4.txt">PASS5</a> · <a href="assets/verification/VERIFICATION_LOG_PASS5.txt">PASS5</a>',
            'Research snapshot <span id="today"></span> (Pass 1 through Pass 6, verified Sept 9-10, 2026) · Branch <code>arena/01a0882a-jobsearchsf</code> · 120 verified SF entries, each with official sources. Verification logs: <a href="assets/verification/VERIFICATION_LOG_PASS6.txt">PASS6</a> · <a href="assets/verification/VERIFICATION_LOG_PASS5.txt">PASS5</a> · <a href="assets/verification/VERIFICATION_LOG_PASS4.txt">PASS4</a>')
    return s


# ------------------------------------------------------------------------ app.js
def patch_app(s):
    return rep(s, '  function batchBadge(j) {\n    if (j.batch === 5) return \' <span class="badge batch5">New in Pass 5</span>\';',
                '  function batchBadge(j) {\n    if (j.batch === 6) return \' <span class="badge batch6">New in Pass 6</span>\';\n'
                '    if (j.batch === 5) return \' <span class="badge batch5">Pass 5</span>\';')


# --------------------------------------------------------------------- style.css
def patch_css(s):
    return rep(s, ".badge.batch5 { background: #fce7f3; color: #9d174d; border: 1px solid #f9a8d4; }",
               ".badge.batch5 { background: #fce7f3; color: #9d174d; border: 1px solid #f9a8d4; }\n"
               ".badge.batch6 { background: #ffedd5; color: #9a3412; border: 1px solid #fdba74; }")


# ------------------------------------------------------------------- sitemap.xml
def patch_sitemap(s):
    if "job-101.html" in s:
        return s
    add = "".join('  <url><loc>./jobs/job-%d.html</loc><changefreq>monthly</changefreq><priority>0.85</priority></url>\n'
                  % i for i in range(101, 121))
    return s.replace("</urlset>", add + "</urlset>")


def main():
    print("index.html:", rw("index.html", patch_index))
    print("app.js:", rw("assets/js/app.js", patch_app))
    print("style.css:", rw("assets/css/style.css", patch_css))
    print("sitemap.xml:", rw("sitemap.xml", patch_sitemap))
    if MISSES:
        print("=== %d misses ===" % len(MISSES))
        for m in MISSES:
            print("MISS:", m)


if __name__ == "__main__":
    main()
