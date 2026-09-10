# -*- coding: utf-8 -*-
"""Write assets/verification/VERIFICATION_LOG_PASS6.txt from the actual data + files on disk."""
import glob
import os
import re

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(ROOT, "assets", "js", "data.js")
OUT = os.path.join(ROOT, "assets", "verification", "VERIFICATION_LOG_PASS6.txt")

BANNED_DOC_PATTERNS = [
    ("transit", r"transit"),
    ("N Judah / Muni / bus routes", r"N Judah|\bMuni\b|SFMTA|511\.org|\bbus\b|T-Third"),
    ("commute language", r"\bcommut\w*|21st (Ave|Av\.)? *& *Judah|21st Ave"),
    ("zone labels", r"Zone [A-D]\b"),
    ("placeholders", r"\[owner\]|\[Insert Date\]|\[Date\]|\[Add if you have\]|\[Company|github\.io"),
    ("tracker meta language", r"match score|JobSearchSF|verified official source|\btailor\w*"),
]


def rows():
    txt = open(DATA, encoding="utf-8").read()
    body = txt.split("window.JOBS_DATA", 1)[1]
    out = []
    for block in re.finditer(r"\{\s*id: \"(job-\d+)\",(.*?)\n  \}", body, re.S):
        jid, rest = block.group(1), block.group(2)

        def g(k):
            m = re.search(r"\b%s: \"((?:[^\"\\]|\\.)*)\"" % k, rest, re.S)
            return (m.group(1).replace('\\"', '"') if m else "")
        m = re.search(r"\bbatch: (\d+)", rest)
        out.append({"id": jid, "batch": int(m.group(1)) if m else 1,
                    "company": g("company"), "position": g("position"),
                    "official": g("officialLink"), "method": g("verificationMethod"),
                    "status": g("status"), "note": g("statusNote"), "flag": g("flag"),
                    "score": re.search(r"\bmatchScore: (\d+)", rest).group(1)})
    return out


def doc_audit():
    files = sorted(glob.glob(os.path.join(ROOT, "assets/resume/job-*_resume.txt"))
                   + glob.glob(os.path.join(ROOT, "assets/cover/*_cover.txt"))
                   + glob.glob(os.path.join(ROOT, "assets/cover/*_email.txt"))
                   + glob.glob(os.path.join(ROOT, "assets/resume/Brian_Chemistry_Resume.txt"))
                   + glob.glob(os.path.join(ROOT, "assets/cover/Brian_Cover_Letter_Base.txt")))
    bad = []
    for f in files:
        t = open(f, encoding="utf-8").read()
        for label, pat in BANNED_DOC_PATTERNS:
            m = re.search(pat, t, re.I)
            if m:
                bad.append((os.path.relpath(f, ROOT), label, t[max(0, m.start() - 30):m.end() + 30].replace("\n", " ")))
    return files, bad


EXCLUDED = [
    "Ring Therapeutics (Greenhouse 5265606008, 5417231008 - RA/RA I-II contract roles): skills fit is "
    "excellent (SEC-HPLC, SDS-PAGE, DLS, BCA/Bradford, dialysis/TFF) but the board and the company's own "
    "pages did not let this audit confirm a San Francisco worksite. Excluded on the location rule; "
    "recorded in MONITOR_REFERENCE.",
    "Jushi (Lever jushico, 'Laboratory Technician' - routine quantitative HPLC, qPCR, cGMP): the "
    "employer's own board lists PA/OH/VA/MA/NV and Santa Barbara CA locations, no San Francisco. Excluded.",
    "MaverickX Technology (Lever, Biology Lab Technician x2), Digital Biotechnologies Inc (Ashby, "
    "Research Associate I), Merge Labs (Ashby, 3 'Research Associate' variants): all surfaced in "
    "SF-restricted searches; none could be confirmed as inside San Francisco (the Ashby entries say "
    "'Bay Area'). Excluded - location is the first filter, not the last.",
    "Cellares (Research Associate variants): worksite is South San Francisco. Excluded.",
    "Plasmidsaurus 'Lab Technician (San Francisco)' id 000c462d...: superseded this pass by the fresher "
    "1dea5cc2 posting (posted 2026-08-26); both say South San Francisco in the body and run Tue-Sat "
    "7pm-3am. Kept as job-118 with the mismatch flagged rather than silently dropped.",
    "Vir Biotechnology (Greenhouse virbiotechnologyinc): live SF research requisitions at audit were "
    "Senior Director / Associate Director level only (4715192005, 4716803005, 4700564005). No entry-level "
    "SF bench req, so no row added.",
    "BridgeBio (Greenhouse bridgebio): board fetched again this pass - no entry-level SF bench "
    "requisition; the three BridgeBio rows from Pass 5 (analytical development, QC manager, CMC "
    "regulatory) stay as they are.",
    "SFMOMA (jobs.lever.co/sfmoma): 7 openings, all curatorial / visitor services / administration. No "
    "conservation or science lab role. Nothing added despite the walkable commute.",
    "NCIRE (ncire.org careers -> UltiPro board 82cac330...): board reachable; no new SF entry-level lab "
    "requisition beyond the rows already listed from Pass 1 and Pass 5.",
    "Personalis (Greenhouse token 404; SmartRecruiters company returned totalFound 0) and Gladstone (no "
    "public Greenhouse board, 404): could not be verified from an official source this pass, so no row "
    "was added. Their existing rows still carry their own Pass 1 / Pass 4 sources.",
    "Twelve (Ashby 'twelve'): the board shows the lab in Berkeley, CA - not SF. Excluded.",
    "Employers whose postings sit only inside JS portals (Kaiser, Sutter, Chinese Hospital, Vitalant, "
    "Quest Workday/Phenom boards): not re-verifiable without a browser this pass, so no NEW rows were "
    "invented for them; existing rows keep their original verification notes and must be re-checked "
    "before applying.",
]


def main():
    rws = rows()
    p6 = [r for r in rws if r["batch"] == 6]
    files, bad = doc_audit()
    lines = []
    W = lines.append
    W("JobSearchSF - PASS 6 VERIFICATION LOG")
    W("Audit date: 2026-09-09 (sandbox clock, UTC). Auditor: Arena agent, autonomous pass.")
    W("Method: every claim below was read off the employer's OWN official source on the audit")
    W("date. No aggregator, no cached copy, no inference. Where the source did not state a")
    W("detail (street address, salary, deadline), the row says so instead of guessing.")
    W("")
    W("=" * 100)
    W("A. PASS 6 - 20 NEW ENTRIES (job-101 .. job-120)")
    W("=" * 100)
    W("")
    W("A.1 UCSF ACADEMIC AP RECRUIT - 14 entries (job-101 .. job-114)")
    W("Primary source: https://aprecruit.ucsf.edu/apply  (\"Browse Open Recruitments\", fetched")
    W("2026-09-09). That page is UCSF's own authoritative list: for every live academic")
    W("recruitment it prints the job number, the school/department, the open date, the most")
    W("recent/next review date and the date applications stop being accepted. Individual")
    W("posting pages (https://aprecruit.ucsf.edu/JPFxxxxx) were fetched where noted.")
    W("Why this employer dominates Pass 6: these are the only San Francisco bench openings")
    W("found in this pass that are (a) entry rank for a B.S. holder, (b) live on the audit")
    W("date, and (c) verifiable without a login. UCSF's Specialist series explicitly accepts a")
    W("baccalaureate plus research experience, which is Brian's exact position.")
    W("")
    for r in p6[:14]:
        W("  %s | %s" % (r["id"], r["company"]))
        W("        position   : %s" % r["position"])
        W("        score      : %s%%   status: %s" % (r["score"], r["status"]))
        W("        verified by: %s" % r["method"])
        W("        window     : %s" % r["note"])
        if r["flag"]:
            W("        flag       : %s" % r["flag"])
        W("")
    W("A.2 CITY AND COUNTY OF SAN FRANCISCO - 3 entries (job-115 .. job-117)")
    W("Primary source: careers.sf.gov role and classification pages (fetched/read 2026-09-09).")
    W("These are civil-service job classes with periodic exam windows, not rolling requisitions.")
    W("")
    for r in p6[14:17]:
        W("  %s | %s" % (r["id"], r["company"]))
        W("        position   : %s" % r["position"])
        W("        score      : %s%%   status: %s" % (r["score"], r["status"]))
        W("        verified by: %s" % r["method"])
        W("        window     : %s" % r["note"])
        W("        flag       : %s" % (r["flag"] or "none"))
        W("")
    W("A.3 DOCUMENTED ALTERNATES - 3 entries (job-118 .. job-120), FLAGGED, NOT TARGETS")
    W("Verified live on the employer's own board on the audit date, but the worksite is South")
    W("San Francisco, which the SF-only rule excludes. Kept as entries so the exclusion is")
    W("auditable instead of silent.")
    W("")
    for r in p6[17:]:
        W("  %s | %s" % (r["id"], r["company"]))
        W("        position   : %s" % r["position"])
        W("        score      : %s%%   status: %s" % (r["score"], r["status"]))
        W("        verified by: %s" % r["method"])
        W("        note       : %s" % r["note"])
        W("        flag       : %s" % (r["flag"] or "none"))
        W("")
    W("=" * 100)
    W("B. CORRECTIONS TO EARLIER PASSES (found while re-verifying, not while adding)")
    W("=" * 100)
    W("  B.1 job-73  Anthropic - Research Associate, Biology.")
    W("        Pass 4 recorded it LIVE after fetching the board. On 2026-09-09 the same URL")
    W("        (job-boards.greenhouse.io/anthropic/jobs/5285248008) serves \"The job you are")
    W("        looking for is no longer open\" and redirects to the board with ?error=true.")
    W("        Row corrected: status -> monitor, position/flag/statusNote rewritten.")
    W("        Brian should not attempt to apply to any cached/aggregator copy of this req.")
    W("  B.2 job-92  City & County of SF - Chemist (2486), REF60430L.")
    W("        The role page states: opening Mon Apr 27, 2026; filing deadline 11:59 p.m.")
    W("        Fri May 8, 2026 (with a 05/04/2026 City correction note about that deadline).")
    W("        Pass 5 labelled it LIVE - the window had already closed two months before this")
    W("        audit. Row corrected to monitor (eligible list runs ~12 months; watch for the")
    W("        next 2486 exam).")
    W("        Second correction on the same row: the old fit text implied Brian has GC-MS,")
    W("        ICP-MS, LIMS and TNI-ELAP experience. The City page lists those as DESIRABLE")
    W("        qualifications; the minimum is a baccalaureate in chemistry or a closely")
    W("        related science plus a CA driver's licence. Fit rewritten to say exactly that,")
    W("        because claiming instrument experience Brian has not logged would fail")
    W("        verification at the City's records check.")
    W("  B.3 assets/js/data.js had an array elision ('},\\n,') at the job-80/job-81 boundary,")
    W("        inherited from an earlier batch script. In JavaScript that silently creates a")
    W("        121st, undefined row: filter/map skipped it, but any sort or reduce over the")
    W("        array touched undefined, and the row counters on the site were one ahead of the")
    W("        table. Removed, and app.js now filters falsy rows before rendering")
    W("        ((window.JOBS_DATA || []).filter(j => !!j && !!j.id)) so a stray comma can never")
    W("        break the page again.")
    W("  B.4 Every generated resume/cover letter/email was rewritten on this pass (all 120,")
    W("        not only the new ones) because the old documents violated Brian's instructions:")
    W("          - they contained transportation content (\"I live at 21st Ave & Judah St and")
    W("            commute via N Judah\", plus a 'Transit:' footer line) - removed from every")
    W("            document; transit now appears only in the 'Getting there' section of a page;")
    W("          - they announced themselves as tailored and printed internal tracker data")
    W("            (\"Match Score 70%\", \"Verified: ... official site ...\") inside the letter -")
    W("            removed;")
    W("          - they pasted the posting's requirements into the experience claims (\"Your")
    W("            GLP sample prep ... maps directly\") - removed; documents now state real")
    W("            experience only, reordered/relabelled to match the posting's language;")
    W("          - they carried unfillable placeholders (\"Date: [Insert Date]\", \"LinkedIn:")
    W("            [Add if you have]\", \"https://[owner].github.io/...\") - removed; the dated")
    W("            letters now carry the real audit date and nothing else;")
    W("          - the Property Manager bullet was repeated with the same 'transferable to")
    W("            lab operations' sentence in the summary of every resume - now stated once,")
    W("            in the experience block, in plain language.")
    W("        Subpage text was regenerated too, so the step lists no longer tell Brian to")
    W("        reference his commute in an application (the old step 6 said 'available for")
    W("        on-site SF with N Judah commute').")
    W("")
    W("  B.5 Self-audit of Pass 6 itself (second verification pass over my own additions).")
    W("        The three City of SF rows were drafted from careers.sf.gov search results, which")
    W("        show the qualification text but not the eligibility gate or the closing date. Reading")
    W("        each role page in full on 2026-09-09 changed all three rows:")
    W("          - job-116 (class 2402): the only live 2402 role page is an Access to City")
    W("            Employment (ACE) exam (REF3136I, published 2022-03-03) which requires a")
    W("            Certification of Disability from the CA Department of Rehabilitation or a")
    W("            Veterans Preference Letter from the U.S. Department of Veterans Affairs. The row")
    W("            now states that gate as the flag, and directs Brian to wait for a general 2402")
    W("            exam instead of applying into a channel he is not eligible for.")
    W("          - job-115 (class 2416, SFDPH, 101 Grove St): the announcement opened Sep 13, 2023")
    W("            and finally closed Sep 22, 2023, so it is a watch-list row, not an apply row.")
    W("            Verified specifics now on the row: class salary $81,692-$99,372 (the 2023")
    W("            announcement text printed $73,398-$89,336 for the common range - both quoted and")
    W("            attributed rather than blended), shift Mon-Fri 8am-5pm with some Saturdays,")
    W("            department contact Hanz Pagao (hanz.pagao@sfdph.org), and the coursework")
    W("            substitution (15 semester units with one college chemistry/biology lab course =")
    W("            6 months; 30 units with two lab courses = the full year) which is why this class")
    W("            is the City's most reachable one for a B.S. Chemistry holder.")
    W("          - job-117 (class 2463 Microbiologist I): the minimum is a baccalaureate with major")
    W("            course work in medical or public health bacteriology/microbiology AND a valid")
    W("            California public health microbiologist certificate, with no substitution listed.")
    W("            Brian does not meet that, so the row keeps the verified facts but is set to status")
    W("            'flag' with a 34 score and an explicit 'do not apply yet' position line, instead of")
    W("            being quietly deleted - so the requirement is on record and the next pass can check")
    W("            whether it has changed. My first draft had called this a possible fit on education,")
    W("            which was wrong.")
    W("        Lesson recorded for future passes: a search snippet is discovery, not verification -")
    W("        every added row now has to be read from the full official page or API response.")
    W("")
    W("=" * 100)
    W("C. REVIEWED AND DELIBERATELY NOT ADDED (so the absence is auditable)")
    W("=" * 100)
    for e in EXCLUDED:
        W("  - " + e)
    W("")
    W("=" * 100)
    W("D. DOCUMENT COMPLIANCE AUDIT (mechanical, run over the files on disk)")
    W("=" * 100)
    W("  Documents checked: %d (resume TXTs, cover TXTs, email TXTs, master resume, base letter)." % len(files))
    W("  Patterns searched in every document: %s" % "; ".join(l for l, _p in BANNED_DOC_PATTERNS))
    W("  Violations found: %d%s" % (len(bad), "" if not bad else ""))
    for b in bad[:15]:
        W("      ! %s [%s] ...%s..." % (b[0], b[1], b[2]))
    W("  PDFs: fpdf2 2.8.8, A4, Helvetica 9.2pt, one page for resumes and cover letters.")
    W("  Files on disk: resumes %d txt + %d pdf; cover %d txt + %d pdf; emails %d txt; job subpages %d."
      % (len(glob.glob(os.path.join(ROOT, "assets/resume/job-*_resume.txt"))),
         len(glob.glob(os.path.join(ROOT, "assets/resume/job-*_resume.pdf"))),
         len(glob.glob(os.path.join(ROOT, "assets/cover/job-*_cover.txt"))),
         len(glob.glob(os.path.join(ROOT, "assets/cover/job-*_cover.pdf"))),
         len(glob.glob(os.path.join(ROOT, "assets/cover/job-*_email.txt"))),
         len(glob.glob(os.path.join(ROOT, "jobs/job-*.html")))))
    W("")
    W("=" * 100)
    W("E. WHAT REMAINS UNVERIFIABLE (stated plainly)")
    W("=" * 100)
    W("  1. UCSF rows list campus, not street address: the postings themselves say 'San Francisco'")
    W("     and name the department, and UCSF assigns building/room later. Do not present a street")
    W("     address to Brian as if the posting gave one - the subpages say 'see posting'.")
    W("  2. UCSF Specialist salaries are ranges set by rank and step; where a posting printed an")
    W("     estimate ($55,000-$58,600 for the Junior Specialist rows that quoted Table 24B) the row")
    W("     repeats it and attributes it. No other salary is asserted.")
    W("  3. Whether a recruitment is still unfilled after its review date is decided by the search")
    W("     committee; UCSF's wording ('reviewed if the position has not yet been filled') is")
    W("     reproduced rather than paraphrased. Ten of the 14 UCSF rows are past their review date,")
    W("     which is why they carry status monitor or a note rather than 'recently posted'.")
    W("  4. Reference contacts are Brian's to supply: every UC posting wants 1-3 references and")
    W("     Brian's reference list is not in this repository, so no names are fabricated anywhere.")
    W("  5. Aggregator mirrors (Indeed/ZipRecruiter/LinkedIn) were never used as apply links; where")
    W("     they conflicted with an official board, the official board won and the conflict is noted.")
    W("")
    W("End of Pass 6 log.")
    open(OUT, "w", encoding="utf-8").write("\n".join(lines) + "\n")
    print("wrote", OUT, len(lines), "lines; doc violations:", len(bad))


if __name__ == "__main__":
    main()
