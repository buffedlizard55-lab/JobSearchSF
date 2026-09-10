# -*- coding: utf-8 -*-
"""Insert Pass 6 rows into assets/js/data.js and patch stale claims found on audit."""
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT)
from pass6_rows import ROWS  # noqa

DATA = os.path.join(ROOT, "assets", "js", "data.js")


def js_str(s):
    return '"' + str(s).replace("\\", "\\\\").replace('"', '\\"').replace("\n", " ") + '"'


def serialize(row, num):
    keys = ["id", "company", "position", "verified", "verificationMethod", "matchScore",
            "batch", "location", "commuteZone", "route", "officialLink", "applyLink",
            "applyChannel", "requirements", "fit", "status", "statusNote", "flag", "subpage"]
    out = ["  {"]
    out.append("    id: %s," % js_str(row["id"]))
    for k in keys[1:]:
        v = row.get(k, "")
        if k == "verified":
            out.append("    verified: %s," % ("true" if v else "false"))
        elif k in ("matchScore", "batch"):
            out.append("    %s: %d," % (k, int(v)))
        else:
            out.append("    %s: %s," % (k, js_str(v)))
    src = ",\n".join("      { label: %s, url: %s }" % (js_str(s["label"]), js_str(s["url"]))
                     for s in row.get("sources", []))
    out.append("    sources: [\n%s\n    ]" % src)
    out.append("  },")
    return "\n" + "\n".join(out) + "\n"


def patch_existing(txt):
    """Fix two rows whose 'LIVE' claim is no longer true (verified 2026-09-09)."""
    notes = []

    def field_replace(block_re, field, newval, label):
        nonlocal txt
        m = re.search(block_re, txt, re.S)
        if not m:
            notes.append("MISS: %s" % label)
            return
        block = m.group(0)
        new_block, n = re.subn(r'\b%s: "(?:[^"\\]|\\.)*"' % field,
                               '%s: %s' % (field, js_str(newval)), block, count=1)
        if n == 0:
            notes.append("NOFIELD: %s %s" % (label, field))
            return
        txt = txt.replace(block, new_block, 1)
        notes.append("OK: %s %s" % (label, field))

    # --- job-73 Anthropic: official board now returns "no longer open"
    j73 = r'\{\s*id: "job-73",.*?\n  \}'
    field_replace(j73, "status", "monitor", "job-73 status")
    field_replace(j73, "statusNote",
                  "CLOSED at 2026-09-09 audit: job-boards.greenhouse.io/anthropic/jobs/5285248008 now serves "
                  "\"The job you are looking for is no longer open\" (verified by fetching the official board, "
                  "which redirects with ?error=true). Was listed LIVE in Pass 4 - that claim is corrected here.",
                  "job-73 statusNote")
    field_replace(j73, "flag",
                  "Irregularity found on this pass: the posting was live in Pass 4 and withdrawn before Pass 6. "
                  "Anthropic re-posts bench roles on the same board, so keep the alert; do not apply to a cached "
                  "or aggregator copy of this req.",
                  "job-73 flag")
    field_replace(j73, "position",
                  "Research Associate, Biology - entry-level bench scientist (molecular biology + biochemistry; "
                  "WITHDRAWN 2026-09-09, watch for repost)",
                  "job-73 position")

    # --- job-92 City Chemist 2486: filing window ended 2026-05-08
    j92 = r'\{\s*id: "job-92",.*?\n  \}'
    field_replace(j92, "status", "monitor", "job-92 status")
    field_replace(j92, "statusNote",
                  "Window CLOSED: the careers.sf.gov announcement for Chemist (2486) citywide exam REF60430L "
                  "(U00049) opened Mon Apr 27, 2026 and closed 11:59 pm Fri May 8, 2026 - confirmed on the role "
                  "page on 2026-09-09, including the City's 05/04/2026 correction note. Salary printed on the "
                  "page: $104,806-$147,524. The eligible list lasts 12 months and may be extended; the next exam "
                  "cycle is what to watch for.",
                  "job-92 statusNote")
    field_replace(j92, "flag",
                  "Two corrections on this row: (1) Pass 5 called it LIVE - the filing deadline passed two "
                  "months before this audit. (2) The old fit text implied GC-MS, ICP-MS and LIMS were skills you "
                  "have; on the City page those are DESIRABLE qualifications, not minimums, and your background "
                  "is HPLC/UV-Vis/NMR plus wet chemistry. Apply on the minimums and say you will train on GC/ICP.",
                  "job-92 flag")
    field_replace(j92, "fit",
                  "Meets the stated minimum on education (baccalaureate in chemistry or closely related science) "
                  "plus a CA driver's licence; GC-MS, ICP-AES/ICP-MS, TNI-ELAP QC and LIMS are desirable rather "
                  "than required, so this is a realistic apply with a training commitment - not a claim of "
                  "instrument experience you do not have.",
                  "job-92 fit")
    return txt, notes


EXCLUSIONS = [
    {
        "employer": "Plasmidsaurus, Inc. - 'Lab Technician | San Francisco' (Ashby, posted 2026-08-26)",
        "note": ("Posting verified live on %s and structured data says San Francisco, but the description body "
                 "states the office is South San Francisco with Tue-Sat 7pm-3am hours, and the company's own "
                 "contact page lists 2 Tower Pl STE 950, South San Francisco 94080. Requires 2 years commercial-lab "
                 "DNA extraction/purification/sequencing. Recorded as job-118 with the mismatch flagged, not as an "
                 "SF target.").replace("%s", "2026-09-09"),
        "commute": "South SF + overnight shift - outside the rule",
        "source": "https://jobs.ashbyhq.com/plasmidsaurus/1dea5cc2-a669-4f22-8eaa-8e569745bd58",
    },
    {
        "employer": "Addition Therapeutics, Inc. - RA QC (5216310007) and RA/Sr RA RNA process development (5208635007)",
        "note": ("Both are live, direct-hire postings published Aug 2026 on the company's own Greenhouse board and "
                 "they are strong skill matches (BS chemistry + 2-4 years, TFF, AKTA, Qubit/Fragment Analyzer/LAL, "
                 "JMP). Excluded from targets because all 7 requisitions on that board are 'South San Francisco'. "
                 "Kept as documented alternates (job-119, job-120)."),
        "commute": "South SF - BART/Caltrain + bus, ~70-85 min",
        "source": "https://job-boards.greenhouse.io/additiontherapeutics",
    },
    {
        "employer": "Ring Therapeutics - RA / RA I-II Protein Chemistry & Bioconjugation (contracts)",
        "note": ("Greenhouse reqs 5265606008 and 5417231008 surfaced in SF searches with an exact skills fit "
                 "(SEC-HPLC, SDS-PAGE, DLS, UV-Vis, BCA/Bradford, dialysis/TFF, 6-month contract). The board did not "
                 "let this audit confirm a San Francisco worksite, and the employer's own listings point away from "
                 "SF - so it is not on the target list. Re-check the posting's location field if you want contract work."),
        "commute": "Worksite unverified - not added",
        "source": "https://job-boards.greenhouse.io/ringtherapeutics",
    },
    {
        "employer": "Jushi (jushico) - 'Laboratory Technician' (Lever)",
        "note": ("Real posting on the employer's own Lever board (routine quantitative HPLC, qPCR, water "
                 "microbiology, cGMP, 21+, BS Chemistry preferred, 1-2 years HPLC) but the board's location list "
                 "covers PA/OH/VA/MA/NV/Santa Barbara CA - no San Francisco site. Excluded on location."),
        "commute": "No SF location on the employer's board",
        "source": "https://jobs.lever.co/jushico",
    },
    {
        "employer": "Vir Biotechnology - SF board scan",
        "note": ("Official Greenhouse board fetched 2026-09-09: the live SF research requisitions are Senior "
                 "Director / Associate Director level (e.g. 4715192005 Bioanalytics, 4716803005 Toxicology, "
                 "4700564005 Sr Dir Clinical Research). No entry-level SF bench req was up at audit, so no row was "
                 "added; keep watching - Vir hires RAs in waves."),
        "commute": "SF (1800 Owens St) but senior-level reqs only",
        "source": "https://job-boards.greenhouse.io/virbiotechnologyinc",
    },
    {
        "employer": "SFMOMA (Lever) - arts employer check",
        "note": ("jobs.lever.co/sfmoma fetched 2026-09-09: 7 openings, all curatorial/visitor-services/administration. "
                 "No conservation or science-lab role, so nothing was added for Brian despite the short Zone A commute."),
        "commute": "Zone A (1155 3rd St) but no lab role",
        "source": "https://jobs.lever.co/sfmoma",
    },
    {
        "employer": "MaverickX Technology / Digital Biotechnologies Inc / Merge Labs - 'Biology Lab Technician' and 'Research Associate I'",
        "note": ("All three showed up in SF-restricted searches (Lever maverickx x2, Ashby digital-biotechnologies-inc "
                 "f08e945b, Ashby merge labs with 3 'Research Associate - Bay Area' variants). Neither the ATS "
                 "location field nor the employer's own site let this audit confirm a San Francisco (not Bay Area) "
                 "worksite, so none were added - location is the first rule here."),
        "commute": "Location not confirmed as SF",
        "source": "https://jobs.ashbyhq.com",
    },
]


def add_exclusions(txt):
    """Prepend Pass-6 exclusion records inside window.MONITOR_REFERENCE."""
    anchor = "window.MONITOR_REFERENCE = [\n"
    i = txt.index(anchor) + len(anchor)
    blocks = []
    for e in EXCLUSIONS:
        blocks.append("  {\n    employer: %s,\n    note: %s,\n    commute: %s,\n    source: %s\n  },\n"
                      % (js_str(e["employer"]), js_str(e["note"]), js_str(e["commute"]), js_str(e["source"])))
    return txt[:i] + "".join(blocks) + txt[i:]


def main():
    txt = open(DATA, encoding="utf-8").read()
    already = 'id: "job-101"' in txt
    if not already:
        # find the end of the JOBS_DATA array (the "\n];" that follows job-100)
        m = re.search(r'(id: "job-100",.*?\n  \},)\n\n\];', txt, re.S)
        if not m:
            sys.exit("could not locate end of JOBS_DATA array")
        insert_at = m.end(1)
        new_rows = "".join(serialize(r, 101 + i) for i, r in enumerate(ROWS))
        txt = txt[:insert_at] + "\n" + new_rows + txt[insert_at + 1:]
        print("inserted %d rows" % len(ROWS))
    else:
        print("pass 6 rows already present - skipping insert")

    txt, notes = patch_existing(txt)
    print("patches:", "; ".join(notes))
    txt = add_exclusions(txt)
    txt = txt.replace(
        "Pass 1 + Pass 2 + Pass 3 + Pass 4 + Pass 5 re-check (Sept 9-10, 2026)",
        "Pass 1 + Pass 2 + Pass 3 + Pass 4 + Pass 5 + Pass 6 re-check (Sept 9-10, 2026; Pass 6 sweep 2026-09-09)")
    txt = txt.replace("Best path remains the 100 SF-transit-commutable roles above.",
                      "Best path remains the 120 SF-transit-commutable roles above.")
    open(DATA, "w", encoding="utf-8").write(txt)
    print("data.js rewritten:", len(txt.splitlines()), "lines")


if __name__ == "__main__":
    main()
