#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pass 8 — True 1-Click Easy Apply subpage generator
- Regenerates all 120 subpages with:
  * One-Click: Download Kit + Open Official Apply (JS)
  * Verify Live buttons (official + direct)
  * Copy Links for manual review
  * Tailored screening download
  * Mailto email template
  * ATS-specific note
- Also regenerates resume/cover/email txt+pdf (clean, no transit)
"""
import os, re, html, sys, importlib.util
ROOT = os.path.dirname(os.path.abspath(__file__))
RESUME_DIR = os.path.join(ROOT, "assets", "resume")
COVER_DIR = os.path.join(ROOT, "assets", "cover")
JOBS_DIR = os.path.join(ROOT, "jobs")
TODAY = "September 12, 2026"
CONTACT1 = "San Francisco, CA 94122  |  (707) 596-8503  |  Brian.j1274@gmail.com"

def load_jobs():
    txt = open(os.path.join(ROOT, "assets", "js", "data.js"), encoding="utf-8").read()
    body = txt.split("window.JOBS_DATA", 1)[1]
    jobs = []
    for block in re.finditer(r"\{\s*id: \"(job-\d+)\",(.*?)\n  \}", body, re.S):
        jid, rest = block.group(1), block.group(2)
        j = {"id": jid}
        for key in ("company", "position", "verificationMethod", "location", "commuteZone",
                    "route", "officialLink", "applyLink", "applyChannel", "requirements",
                    "fit", "status", "statusNote", "flag", "subpage"):
            m = re.search(r"\b%s: \"((?:[^\"\\]|\\.)*)\"" % key, rest, re.S)
            j[key] = unesc(m.group(1)) if m else ""
        m = re.search(r"\bmatchScore: (\d+)", rest)
        j["matchScore"] = int(m.group(1)) if m else 0
        m = re.search(r"\bbatch: (\d+)", rest)
        j["batch"] = int(m.group(1)) if m else 1
        m = re.search(r"\bverified: (true|false)", rest)
        j["verified"] = (m.group(1) == "true") if m else True
        src = re.search(r"sources: \[(.*?)\]", rest, re.S)
        j["sources"] = []
        if src:
            for lbl, url in re.findall(r"\{\s*label: \"((?:[^\"\\]|\\.)*)\",\s*url: \"((?:[^\"\\]|\\.)*)\"\s*\}", src.group(1)):
                j["sources"].append({"label": unesc(lbl), "url": unesc(url)})
        jobs.append(j)
    return jobs

def unesc(s):
    return s.replace('\\"', '"').replace("\\'", "'").replace("\\n", "\n").replace("\\/", "/")

SKILL_LINES = [
    ("Chromatography & purification: HPLC runs, column and flash purification, fraction collection",
     ("hplc", "chromatograph", "lc-", " fplc", "akta", "sec", "iex", "purif", "fraction", "method"),
     "running HPLC and column purification and logging what each run showed"),
    ("Spectroscopy & characterization: NMR, UV-Vis; reviewing and reporting instrument output",
     ("nmr", "uv", "spectroscop", "characteriz", "absorbance", "fragment analyzer", "plate-based", "elisa"),
     "confirming identity and purity by NMR and UV-Vis and writing the results up"),
    ("Sample handling: receipt, preparation, extraction, aliquoting, labeling and tracking",
     ("sample prep", "preparation", "extract", "aliquot", "specimen", "sample", "library prep", "homogen", "plasmid prep"),
     "extracting, aliquoting, labeling and tracking samples so the chain of records stays intact"),
    ("QC & compliance: GLP documentation, control records, out-of-spec flags, safety protocols",
     ("qc", "quality", "compliance", "glp", "gmp", "iso", "specification", "audit", "safety", "control chart"),
     "QC checks and GLP documentation, including flagging anything out of specification"),
    ("Wet chemistry: titration, buffer and reagent preparation, solution making and pH adjustment",
     ("titrat", "buffer", "reagent", "solution", " ph", "wet chem", "media", "steril", "autoclave", "glasswar"),
     "making up buffers and reagents, titration and pH work at the bench"),
    ("Instrument care: routine upkeep, calibration checks and first-line troubleshooting",
     ("instrument", "maintenance", "calibrat", "troubleshoot", "equipment", "biosafety cabinet", "centrifug"),
     "keeping instruments calibrated and sorting out the simple faults before they cost a run"),
    ("Records & data: electronic lab records, LIMS-style data entry, Excel summaries, written reports",
     ("record", "lims", "eln", "data entry", "excel", "report", "database", "document"),
     "electronic records and clean data entry, with summaries the team could actually use"),
    ("Research support: experimental design input, data interpretation, and a peer-reviewed publication",
     ("research", "experiment", "manuscript", "publication", "assay", "screen", "clon", "pcr", "gel"),
     "designing experiments with the team, interpreting the data and writing it up"),
    ("Lab operations: reagent and supply inventory, ordering, vendor coordination, receipts",
     ("inventory", "ordering", "supply", "vendor", "procurement", "logistic", "shipp", "operation"),
     "reagent and supply inventory, purchase coordination and receipt checks"),
    ("Teamwork & communication: cross-team coordination, clear written updates, training newcomers",
     ("communicat", "collaborat", "cross-functional", "training", "liaison", "team"),
     "clear hand-offs with other teams and short written updates without being asked"),
]

CORE_SKILL_LINES = [
    "Education: B.S. Chemistry, UC Santa Cruz (2011); ACS J. Med. Chem. publication (Feb 2011)",
    "Availability: San Francisco-based, on-site laboratory work, short notice",
]

def rank_lines(hay):
    pairs = []
    for idx, (line, tags, _phrase) in enumerate(SKILL_LINES):
        hits = sum(1 for t in tags if t in hay)
        pairs.append((-hits, idx, line))
    pairs.sort()
    matched = [p for p in pairs if -p[0] > 0]
    rest = [p for p in pairs if -p[0] == 0]
    lines = [p[2] for p in matched + rest]
    phrases = [SKILL_LINES[p[1]][2] for p in matched]
    return lines, phrases

def clean_company(company):
    c = re.split(r"\s+[-—]\s+", company)[0].strip()
    c = re.sub(r"\s*\((?:[^)]*)\)\s*$", "", c).strip()
    c = re.sub(r",?\s+(?:Inc\.?|LLC|L\.L\.C\.?|Ltd\.?|Corp\.?|Corporation|Company|Co\.)$", "", c).strip()
    return c or company

def role_type(job):
    pos = job.get("position", "")
    base = re.split(r"\s+[-—]\s+", pos)[0].strip()
    base = re.sub(r"\s*\((?:[^()]*?(?:LIVE|JPF\d+|REF\d+|\d{7,}|\\$)[^()]*?)\)\s*", "", base).strip()
    base = re.sub(r"\s*[-—]\s*(?:SF|San Francisco)\s*$", "", base).strip()
    base = re.sub(r"\s*\((?:class\s*)?\d{3,6}\)\s*", " ", base).strip(" .,-")
    if "|" in base:
        head, _, tail = base.partition("|")
        head = head.strip(" .,-")
        paren = re.search(r"\([^()]*\)\s*$", tail)
        base = head + (" " + paren.group(0).strip() if paren else "")
    base = re.sub(r"\s+\(SF,? (?:on-?site|hybrid|remote)[^)]*\)$", "", base, flags=re.I).strip()
    base = re.sub(r"\s*\((?:[^()]*?(?:JPF\d+|REF\w+|PBT-\w+|RTF\w+|class \d+|\d{6,}|South San Francisco|San Francisco|SF)[^()]*?)\)\s*", " ", base).strip(" .,-")
    parts = [x.strip() for x in re.split(r"\s*/\s*", base) if x.strip()]
    if len(parts) > 1 and all(len(x.split()) <= 3 for x in parts):
        first, noun = parts[0], parts[-1].split()[-1]
        base = first if noun.lower() in first.lower() else "%s %s" % (first, noun)
    base = re.sub(r"\s+", " ", base)
    if len(base) < 3:
        base = pos[:60]
    return base

def recipient_block(job):
    comp = clean_company(job.get("company", ""))
    dept = (job.get("_dept_line") or "").strip()
    loc = job.get("location", "") or ""
    loc = loc.split("(")[0]
    loc = re.sub(r"\s*[-—]\s*(see|confirm|site set|posting|per).*", "", loc)
    loc = re.sub(r"\s{2,}", " ", loc).strip(" ,;")
    if not re.search(r"\d+\s+[A-Z][a-z]+\s+(St|Street|Ave|Avenue|Blvd|Boulevard|Rd|Road|Dr|Drive|Pl|Place|Pkwy|Sq|Campus|Way|Hwy|Bldg)", loc) or len(loc) > 70:
        loc = "San Francisco, CA"
    else:
        loc = loc + (", CA" if "CA" not in loc and "California" not in loc else "")
    lines = []
    if dept and dept.lower() not in comp.lower():
        lines.append(dept)
    else:
        lines.append(comp)
    lines.append(loc)
    return [l for l in lines if l.strip()]

QUINTARA = ("Lab Assistant", "Quintara Biosciences, San Francisco Bay Area", "Jan 2012 to May 2012", [
    "Ran laboratory procedures under Good Laboratory Practice, including sample preparation and accurate data recording.",
    "Carried out quality-control checks and documented results for review.",
    "Maintained laboratory equipment and kept safety-protocol compliance current.",
])
MICRO = ("Lab Intern", "MicroConstants, San Diego, CA", "Aug 2011 to Dec 2011", [
    "Prepared samples by extraction and ran chromatography on the QC bench.",
    "Performed spectroscopic analysis, then recorded and interpreted the output.",
    "Helped move paper lab records into electronic systems and supported QC efforts.",
])
THRESH = ("Summer Medicinal Chemistry Intern", "Threshold Pharmaceuticals, San Francisco Bay Area", "Jun 2011 to Aug 2011", [
    "Synthesized organic compounds for a drug-development program.",
    "Purified compounds and followed purity by HPLC and NMR.",
    "Contributed to experimental design, reaction troubleshooting and data interpretation.",
])
ALL_ROLES = [QUINTARA, MICRO, THRESH]
PROPERTY_BULLETS = [
    "Run the paperwork side of residential operations: compliance records, contracts, receipts and reporting.",
    "Track budgets and expenses, and keep vendor, maintenance and supply schedules current.",
    "Handle tenant and contractor communication in writing and by phone, with a paper trail for every decision.",
]

def bullet_lines(items, width=88, indent="  "):
    out = []
    for it in items:
        wrapped = wrap("- " + it, width, indent)
        out.extend(wrapped)
    return out

def resume_text(job=None):
    if job is None:
        ordered, phrases = [l for l, _t, _ph in SKILL_LINES], []
        mission = ("Seeking an entry-level Research Associate or laboratory technician position in a "
                   "San Francisco area lab, where measurement, purification and documentation discipline "
                   "are the core of the job.")
    else:
        hay = " ".join([job.get("position", ""), job.get("requirements", ""), job.get("fit", "")]).lower()
        ordered, phrases = rank_lines(hay)
        rt = role_type(job)
        art = "an" if rt[:1].lower() in "aeiou" else "a"
        labels = [lower_first(p.split(":")[0].strip()) for p in ordered[:3]]
        focus_txt = (", ".join(labels[:-1]) + " and " + labels[-1]) if len(labels) > 1 else (labels[0] if labels else "")
        place = ("the San Francisco Bay Area" if str(job.get("commuteZone", "")) == "Flagged" else "San Francisco")
        mission = ("Seeking %s %s position in %s, ideally in a lab where %s are part of the "
                   "weekly routine." % (art, rt, place, focus_txt or "analytical chemistry and QC work"))
    summary = ("B.S. Chemistry (UC Santa Cruz, 2011) with hands-on bench experience in analytical and "
               "preparative chemistry: HPLC and chromatographic purification, NMR and UV-Vis "
               "characterization, sample preparation and extraction, and QC documentation under GLP. " + mission)
    order = order_experience("" if job is None else
                             " ".join([job.get("position", ""), job.get("requirements", ""), job.get("fit", "")]).lower())
    out = []
    A = out.append
    A("BRIAN")
    A(CONTACT1)
    A("")
    A("SUMMARY")
    for ln in wrap(summary, 90):
        A(ln)
    A("")
    A("CORE LABORATORY SKILLS")
    for ln in bullet_lines(ordered[:6] + CORE_SKILL_LINES):
        A(ln)
    A("")
    A("LABORATORY EXPERIENCE")
    for (title, org, dates, bullets) in order:
        A("%s - %s - %s" % (title, org, dates))
        for ln in bullet_lines(bullets):
            A(ln)
        A("")
    A("ADDITIONAL EXPERIENCE")
    A("Property Manager (contract) - San Francisco, CA - May 2012 to present")
    for ln in bullet_lines(PROPERTY_BULLETS):
        A(ln)
    A("")
    A("EDUCATION")
    A("B.S. in Chemistry - University of California, Santa Cruz - 2007 to 2011")
    for ln in bullet_lines(["Undergraduate research assistant, Yat Li's laboratory: grew gallium nitride "
                            "films by chemical vapor deposition for dye-sensitized solar cells; prepared "
                            "samples, ran characterization and analyzed the data."]):
        A(ln)
    A("")
    A("PUBLICATION")
    for ln in bullet_lines(["\"14-Aminocamptothecins: Their Synthesis, Preclinical Activity, and Potential "
                             "Use for Cancer Treatment\", ACS Journal of Medicinal Chemistry, February 2011."]):
        A(ln)
    return "\n".join(out).rstrip() + "\n"

def order_experience(hay):
    def score(role):
        s = 0
        for b in role[3]:
            for tok in re.findall(r"[a-z]{5,}", b.lower()):
                if tok in hay:
                    s += 1
        return s
    return sorted(ALL_ROLES, key=lambda r: -score(r))

def clip(text, n=260):
    text = text.strip()
    if len(text) <= n:
        return text
    cut = text[:n].rsplit(" ", 1)[0].rstrip(" ,;.:")
    return cut + "..."

def wrap(text, width=92, cont=""):
    words, lines, cur = text.split(), [], ""
    for w in words:
        if not cur:
            cur = w
        elif len(cur) + 1 + len(w) <= width:
            cur += " " + w
        else:
            lines.append(cur)
            cur = cont + w if cont else w
    if cur:
        lines.append(cur)
    return lines

def lower_first(phrase):
    first = phrase.split()[0] if phrase.split() else ""
    if first.isupper() or "&" in first or "." in first:
        return phrase
    return phrase[0].lower() + phrase[1:]

def core_focus(job):
    req = re.sub(r"\s*\(per (posting|the posting)[^)]*\)", "", job.get("requirements", "")).strip()
    first = re.split(r"[.;](?=\s|$)", req)[0].strip()
    low = first.lower()
    if (not first or len(first) < 20
            or re.search(r"(baccalaureate|b\.s\.|m\.s\.|minimum|requires|years of|degree|qualification|diploma)", low)):
        return "steady bench throughput and careful documentation"
    if len(first) > 86:
        cut = first[:86].rsplit(" ", 1)[0].rstrip(" ,;.:")
        first = cut + "..."
    if first[:1].isupper() and not first.split()[0].isupper():
        first = first[0].lower() + first[1:]
    return first

def cover_text(job):
    rt = role_type(job)
    comp = clean_company(job.get("company", ""))
    hay = " ".join([job.get("position", ""), job.get("requirements", ""), job.get("fit", "")]).lower()
    ordered, matched = rank_lines(hay)
    phrases = matched[:3] if matched else []
    if not phrases:
        phrases = ["running HPLC and column purification",
                   "QC checks and GLP documentation, including flagging anything out of specification",
                   "extracting, aliquoting, labeling and tracking samples so the chain of records stays intact"]
    labels = [lower_first(p.split(":")[0].strip()) for p in ordered[:2]] or ["analytical chemistry"]
    two = " and ".join(labels[:2]) if len(labels) > 1 else labels[0]
    core = core_focus(job)
    monitor = job.get("status") != "recently-posted"
    if monitor:
        para1 = ("I am writing to ask to be considered for %s openings at %s. I hold a B.S. in Chemistry "
                 "from UC Santa Cruz (2011), with bench experience in %s from roles at Threshold "
                 "Pharmaceuticals, MicroConstants and Quintara Biosciences."
                 % (rt, comp, two))
    else:
        para1 = ("I am writing to apply for the %s position at %s. I hold a B.S. in Chemistry from UC "
                 "Santa Cruz (2011), with bench experience in %s from roles at Threshold Pharmaceuticals, "
                 "MicroConstants and Quintara Biosciences, and a peer-reviewed publication in the ACS "
                 "Journal of Medicinal Chemistry (February 2011)."
                 % (rt, comp, two))
    lead = "The heart of your posting is" if not monitor else "The work you describe for this team is"
    para2 = ("%s %s. That is close to work I have actually done: %s%s"
             % (lead, core, ", ".join(phrases[:2]),
                (" and " + phrases[2] if len(phrases) > 2 else "") + ". "))
    para2 += ("I am comfortable being the person who keeps a bench tidy, a record complete and a schedule "
              "kept. The last decade of running property operations on contract sharpened exactly that: "
              "inventory, vendor scheduling, compliance paperwork and receipts that reconcile.")
    para3 = ("I would welcome a short conversation and can interview at your convenience. I am available to "
             "start on short notice and can be reached at (707) 596-8503 or Brian.j1274@gmail.com. Thank you "
             "for your time and consideration." if not monitor else
             "If a matching requisition opens, I would welcome a short conversation. I can be reached at "
             "(707) 596-8503 or Brian.j1274@gmail.com, and I am glad to send transcripts or references on "
             "request. Thank you for your time.")
    out = []
    A = out.append
    if job.get("status") == "flag":
        A("INTERNAL NOTE FOR BRIAN - DO NOT SEND THIS ONE YET: %s"
          % clip(" ".join((job.get("flag") or "see the row's verification note").split()), 260))
        A("")
    A("Brian")
    A("San Francisco, CA 94122")
    A("(707) 596-8503 | Brian.j1274@gmail.com")
    A("")
    A(TODAY)
    A("")
    for l in recipient_block(job):
        A(l)
    A("")
    A(job.get("_letter_to", "Hiring Manager") + ",")
    A("")
    for ln in wrap(para1, 90):
        A(ln)
    A("")
    for ln in wrap(para2, 90):
        A(ln)
    A("")
    for ln in wrap(para3, 90):
        A(ln)
    A("")
    A("Sincerely,")
    A("Brian")
    return "\n".join(out) + "\n"

def base_cover_text():
    para1 = ("I am writing to apply for a Research Associate or laboratory technician position with your team. "
             "I hold a B.S. in Chemistry from UC Santa Cruz (2011), with bench experience in HPLC and "
             "chromatographic purification, NMR and UV-Vis characterization, sample preparation and extraction, "
             "and QC documentation under GLP, gained at Threshold Pharmaceuticals, MicroConstants and Quintara "
             "Biosciences. I also have a peer-reviewed publication in the ACS Journal of Medicinal Chemistry "
             "(February 2011).")
    para2 = ("The common thread in those roles is repeatability: prepare the sample the same way every time, "
             "run the instrument within its checks, write down what happened, and flag anything out of "
             "specification before it becomes a result. I am comfortable with the unglamorous half of lab work - "
             "glassware, reagents, inventory, logs - and I keep records clean enough that someone else can pick "
             "them up without asking questions.")
    para3 = ("I am available for an interview at your convenience and can start on short notice. I am best reached "
             "at (707) 596-8503 or Brian.j1274@gmail.com. Thank you for your time and consideration.")
    out = []
    A = out.append
    A("Brian")
    A("San Francisco, CA 94122")
    A("(707) 596-8503 | Brian.j1274@gmail.com")
    A("")
    A("Hiring Manager")
    A("San Francisco, CA")
    A("")
    A("Dear Hiring Manager,")
    A("")
    for ln in wrap(para1, 90):
        A(ln)
    A("")
    for ln in wrap(para2, 90):
        A(ln)
    A("")
    for ln in wrap(para3, 90):
        A(ln)
    A("")
    A("Sincerely,")
    A("Brian")
    return "\n".join(out) + "\n"

def email_text(job):
    rt = role_type(job)
    comp = clean_company(job.get("company", ""))
    monitor = job.get("status") != "recently-posted"
    subject = ("Subject: %s %s - Brian, B.S. Chemistry (UC Santa Cruz)"
               % ("Consideration for" if monitor else "Application for", rt))
    sal = job.get("_letter_to", "Hiring Manager")
    p1 = ("I applied for the %s role at %s through your official careers portal and wanted to add one short "
          "line in case it is useful." % (rt, comp)) if not monitor else (
          "I have been following %s and would like to be considered for %s openings on the bench. I did not "
          "find a live requisition that fits my profile when I checked your official board, so I am writing "
          "directly rather than applying to something that is not posted." % (comp, rt))
    p2 = ("I am a San Francisco-based chemist: B.S. Chemistry, UC Santa Cruz (2011), with hands-on HPLC and "
          "chromatographic purification, NMR and UV-Vis work, sample preparation and extraction, and QC "
          "documentation under GLP from Threshold Pharmaceuticals, MicroConstants and Quintara Biosciences. "
          "I also have a 2011 publication in the ACS Journal of Medicinal Chemistry.")
    p3 = ("My resume and cover letter are attached. I am glad to come in for a bench conversation whenever "
          "suits you, and I can start on short notice.")
    out = []
    A = out.append
    if job.get("status") == "flag":
        A("INTERNAL NOTE FOR BRIAN - DO NOT SEND THIS ONE YET: %s"
          % clip(" ".join((job.get("flag") or "see the row's verification note").split()), 260))
        A("")
    A(subject)
    A("")
    A("Dear %s," % sal)
    A("")
    for ln in wrap(p1, 90):
        A(ln)
    A("")
    for ln in wrap(p2, 90):
        A(ln)
    A("")
    for ln in wrap(p3, 90):
        A(ln)
    A("")
    A("Best regards,")
    A("Brian")
    A("San Francisco, CA 94122")
    A("(707) 596-8503")
    A("Brian.j1274@gmail.com")
    note = job.get("_email_note")
    if note:
        A("")
        A("(Internal note for Brian - delete before sending: %s)" % note)
    return "\n".join(out) + "\n"

def sanitize(s):
    rep = {"\u2014": "-", "\u2013": "-", "\u2022": "-", "\u2192": "->", "\u2713": "v",
           "\u26a0": "!", "\u2019": "'", "\u2018": "'", "\u201c": '"', "\u201d": '"',
           "\U0001f4cd": "", "\U0001f4c4": "", "\u2709\ufe0f": "", "\U0001f4e7": "",
           "\U0001f9ea": "", "\ufe0f": "", "\u00b7": "-", "\u2500": "-"}
    for k, v in rep.items():
        s = s.replace(k, v)
    return s.encode("latin-1", "replace").decode("latin-1")

def make_pdf(text, path, title=""):
    from fpdf import FPDF
    pdf = FPDF(format="A4")
    pdf.set_margins(16, 14, 16)
    pdf.set_auto_page_break(auto=True, margin=12)
    pdf.add_page()
    if title:
        pdf.set_font("Helvetica", "B", 10)
        pdf.cell(0, 5, sanitize(title), new_x="LMARGIN", new_y="NEXT", align="C")
        pdf.ln(2)
    pdf.set_font("Helvetica", "", 9.2)
    for line in sanitize(text).split("\n"):
        if not line.strip():
            pdf.ln(3.2)
            continue
        bold = bool(re.match(r"^(SUMMARY|CORE LABORATORY SKILLS|LABORATORY EXPERIENCE|ADDITIONAL EXPERIENCE|EDUCATION|PUBLICATION|BRIAN)$", line.strip()))
        if bold:
            pdf.set_font("Helvetica", "B", 9.6)
            pdf.cell(0, 4.8, line, new_x="LMARGIN", new_y="NEXT")
            pdf.set_font("Helvetica", "", 9.2)
            continue
        if re.match(r"^[\w()\-.,'\"| ]+ - .+ - [A-Z][a-z]{2} \d{4}", line):
            pdf.set_font("Helvetica", "B", 9.2)
            pdf.multi_cell(0, 4.6, line, new_x="LMARGIN", new_y="NEXT")
            pdf.set_font("Helvetica", "", 9.2)
            continue
        pdf.multi_cell(0, 4.6, line, new_x="LMARGIN", new_y="NEXT")
    pdf.output(path)

def esc(s):
    return html.escape(str(s or ""), quote=True)

def url_of(s):
    text = str(s or "")
    # find all urls
    urls = re.findall(r"https?://[^\s\"'>\]]+", text)
    if not urls:
        return "#"
    # Prefer specific ATS patterns: JPF, greenhouse, lever, ashby, smartrecruiters, ultipro, aprecruit, brassring
    preferred = []
    for u in urls:
        low = u.lower()
        if any(k in low for k in ["jpf", "greenhouse.io", "lever.co", "ashbyhq", "smartrecruiters", "ultipro", "aprecruit", "brassring", "myworkday", "wd1.myworkday", "wd5.myworkday"]):
            preferred.append(u)
    # If applyLink contains " | AP Recruit: https://aprecruit..." prefer second if it's JPF/aprecruit
    # So if preferred exists, pick first preferred, else first url
    chosen = preferred[0] if preferred else urls[0]
    # Clean trailing punctuation
    chosen = chosen.rstrip(".,)")
    return chosen

def build_autofill(job):
    rt = role_type(job)
    comp = clean_company(job.get("company", ""))
    return f"""BRIAN — AUTOFILL VAULT (copy-paste for ATS)
Name: Brian
Email: Brian.j1274@gmail.com
Phone: (707) 596-8503
Location: San Francisco, CA 94122
Address: 21st Ave & Judah St, San Francisco, CA 94122
Work Auth: Authorized to work in US, no sponsorship
How heard: Company website
On-site SF: Yes

EDUCATION:
UC Santa Cruz — B.S. Chemistry 2007-2011 — Research Assistant Yat Li Lab (GaN CVD) — Publication ACS J Med Chem Feb 2011

EXPERIENCE:
- Lab Assistant, Quintara Biosciences, Jan-May 2012 — GLP, sample prep, data recording, QC, equipment maintenance
- Lab Intern, MicroConstants, Aug-Dec 2011 — sample extraction, chromatography, spectroscopy, electronic records, QC
- Summer Med Chem Intern, Threshold Pharmaceuticals, Jun-Aug 2011 — organic synthesis, purification, NMR, HPLC
- Property Manager contract, SF, May 2012-Present — compliance records, budgets, vendor schedules, paper trail

SKILLS: HPLC, Spectroscopy (NMR, UV-Vis), Chromatography, Sample Prep, QC & Data Analysis, GLP, MS Office, Buffer Prep, Titration, Instrument Maintenance, Electronic Lab Records / LIMS-style

APPLYING TO: {comp} — {rt}
Official: {job.get('officialLink','')}
Direct Apply: {url_of(job.get('applyLink','') or job.get('officialLink',''))}
Match: {job.get('matchScore','')}% — {job.get('fit','')[:120]}

SCREENING ANSWERS (honest):
- GC-MS/ICP-MS/LIMS/cell culture/mouse/CPT? No, but HPLC/NMR/UV-Vis/chromatography/sample prep/GLP/QC/electronic records; willing to train fast.
- Salary: Per posting range / negotiable. Start: Short notice / 2 weeks.
- Driver license: Yes if required.
"""

def build_steps(job):
    comp = clean_company(job.get("company", ""))
    rt = role_type(job)
    monitor = job.get("status") != "recently-posted"
    reqs = job.get("requirements", "").strip()
    req_short = re.split(r"[.;]", reqs)[0].strip() or "the qualifications in the posting"
    if len(req_short) > 200:
        req_short = req_short[:197] + "..."
    steps = []
    if monitor:
        steps.append("<strong>Read the status note before you invest any time (2 min).</strong> This employer and the "
                     "official source are verified, but at audit time there was no live opening here that you should "
                     "apply to today (see the note above and on the main table). Open the official careers page, search "
                     "&quot;%s&quot;, and confirm a live requisition exists. If nothing matches yet, save the page and "
                     "re-check weekly - and never apply through a third-party site."
                     % esc(rt))
    else:
        steps.append("<strong>Confirm the posting is live (2 min).</strong> Open the official link above and check the "
                     "title, location and status match this row. Aggregator copies (Indeed, ZipRecruiter, LinkedIn) "
                     "are for discovery only - never apply through them.")
    steps.append("<strong>Use Easy Apply box above (1 min).</strong> Click 'Download Kit ZIP' or 'One-Click' — it contains resume PDF+TXT+DOCX, cover PDF+TXT+DOCX, email TXT, tailored screening, autofill answers, profile JSON, README with direct link. No extra formatting needed.")
    steps.append("<strong>Open Official Apply (1 min).</strong> Click 'Open Official Apply →' or One-Click — official employer ATS only (Greenhouse, Lever, Ashby, Workday, SmartRecruiters, UltiPro, AP Recruit). Verify live.")
    steps.append("<strong>Fill personal details via autofill (1 min).</strong> Copy from Easy Apply autofill box or Screening_Answers.txt. Name, SF CA 94122, (707) 596-8503, Brian.j1274@gmail.com. How heard: Company website. Work auth: authorized US, no sponsorship.")
    steps.append("<strong>Upload documents (1 min).</strong> Upload Resume PDF (or DOCX if portal requires DOCX) + Cover PDF from Kit ZIP. File names already identify you cleanly.")
    steps.append("<strong>Answer screening honestly (2 min).</strong> Role core: %s. If technique not done, answer No and mention what you HAVE done — HPLC, NMR, UV-Vis, chromatography, sample prep, GLP, QC, electronic records. Use tailored screening file."
                 % esc(req_short))
    steps.append("<strong>Add references (2 min).</strong> 2-3: supervisor/PI (Quintara, MicroConstants, Threshold or UCSC Yat Li Lab) with name, title, relationship, email, phone. Ask each person first.")
    steps.append("<strong>Submit and save confirmation (1 min).</strong> Screenshot or note confirmation number/date in tracker below. Reply should come from employer's own domain.")
    steps.append("<strong>Prepare and follow up.</strong> 30-sec pitch: B.S. Chemistry UCSC 2011, HPLC/purification at Threshold, QC/records at MicroConstants/Quintara, ACS J Med Chem publication. Two examples of careful work, two questions about lab instruments/volume. Follow up 7-10 business days via intro email below or portal message.")
    return "\n".join("          <li>%s</li>" % s for s in steps)

def build_verify(job):
    items = [
        ("<strong>Employer</strong>", "%s - official source %s" % (esc(job.get("company", "")), esc(job.get("officialLink", "")))),
        ("<strong>Position</strong>", "%s" % esc(job.get("position", ""))),
        ("<strong>How it was verified</strong>", "%s" % esc(job.get("verificationMethod", ""))),
        ("<strong>Status &amp; timing</strong>", "%s" % esc(job.get("statusNote", ""))),
        ("<strong>Location</strong>", "%s" % esc(job.get("location", ""))),
        ("<strong>Apply channel</strong>", "%s - direct employer only; no recruiter, no staffing firm, no fee" % esc(job.get("applyChannel", ""))),
        ("<strong>What the posting asks for</strong>", "%s" % esc(job.get("requirements", ""))),
        ("<strong>Match score %s%%</strong>" % esc(job.get("matchScore", 0)), "%s" % esc(job.get("fit", ""))),
        ("<strong>Direct Apply Link (official, for manual review)</strong>", "<a href=\"%s\" target=\"_blank\" rel=\"noopener\">%s</a> — %s" % (esc(url_of(job.get("applyLink","") or job.get("officialLink",""))), esc(url_of(job.get("applyLink","") or job.get("officialLink",""))), esc(job.get("applyChannel","")))),
        ("<strong>Official Site (for manual review)</strong>", "<a href=\"%s\" target=\"_blank\" rel=\"noopener\">%s</a>" % (esc(job.get("officialLink","#")), esc(job.get("officialLink","#")))),
        ("<strong>Kit ZIP (download & submit)</strong>", "<a href=\"../assets/kits/%s_kit.zip\" download>../assets/kits/%s_kit.zip</a> — contains resume PDF+TXT+DOCX, cover PDF+TXT+DOCX, email TXT, tailored screening, autofill answers, profile JSON, README" % (esc(job.get("id","")), esc(job.get("id","")))),
        ("<strong>Tailored Screening</strong>", "<a href=\"../assets/screening/%s_screening.txt\" download>../assets/screening/%s_screening.txt</a> — Q&A tailored to this job, honest No where needed" % (esc(job.get("id","")), esc(job.get("id","")))),
        ("<strong>Documents</strong>", "Resume, cover letter and intro email on this page contain only resume facts "
                                        "plus wording of this posting. No commute/transit/address in them; that stays in 'Getting there'."),
    ]
    return "\n".join("          <li>%s: %s</li>" % (k, v) for k, v in items)

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>@@ID@@ - @@COMPANY@@ - @@POSITION@@ - JobSearchSF</title>
  <meta name="description" content="@@META@@">
  <link rel="stylesheet" href="../assets/css/style.css">
  <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>%F0%9F%A7%AA</text></svg>">
  <style>
    .copy-box { background:#f8fafc; border:1px solid #e3e9f0; border-radius:12px; padding:14px; margin:10px 0; position:relative; }
    .copy-box pre { white-space:pre-wrap; word-wrap:break-word; font-size:.86rem; margin:0; font-family:ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace; }
    .copy-btn { position:absolute; top:10px; right:10px; }
    .easy-box { background: linear-gradient(135deg, #f0fdf4, #ecfdf5); border: 2px solid #16a34a; border-radius: 16px; padding: 20px 22px; margin-bottom: 20px; box-shadow: 0 8px 28px rgba(22,163,74,0.12); }
    .easy-box h3 { margin: 0 0 10px; color: #14532d; font-size: 1.15rem; }
    .easy-grid { display: flex; flex-wrap: wrap; gap: 10px; margin: 12px 0; }
  </style>
  <script>
  function copyText(id, btn) {
    var box = document.getElementById(id);
    if (!box) { return; }
    var text = box.innerText;
    function feedback(ok) {
      var orig = btn.getAttribute('data-label') || btn.textContent;
      btn.setAttribute('data-label', orig);
      btn.textContent = ok ? 'Copied ✓' : 'Press Ctrl+C';
      setTimeout(function () { btn.textContent = btn.getAttribute('data-label') || 'Copy'; }, 2000);
    }
    function legacy() {
      var ta = document.createElement('textarea');
      ta.value = text;
      ta.setAttribute('readonly', '');
      ta.style.position = 'fixed';
      ta.style.left = '-9999px';
      document.body.appendChild(ta);
      ta.select();
      var ok = false;
      try { ok = document.execCommand('copy'); } catch (e) { ok = false; }
      document.body.removeChild(ta);
      feedback(ok);
    }
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(function () { feedback(true); }, legacy);
    } else { legacy(); }
  }
  function easyApply(id, applyUrl){
    const kitUrl = '../assets/kits/'+id+'_kit.zip';
    const a = document.createElement('a');
    a.href = kitUrl;
    a.download = id+'_kit.zip';
    document.body.appendChild(a);
    a.click();
    setTimeout(()=>{ a.remove(); }, 500);
    if(applyUrl && applyUrl!=='#') window.open(applyUrl, '_blank', 'noopener');
  }
  </script>
</head>
<body>
  <header class="topbar">
    <div class="wrap">
      <div>
        <h1>@@COMPANY_ESC@@</h1>
        <div class="tag">@@POSITION_ESC@@<br>@@LOC_ESC@@<br>Match score: @@SCORE@@% - @@FIT_SHORT@@</div>
      </div>
      <div class="meta">
        <a href="../index.html" style="color:#fff;text-decoration:underline">&larr; Back to all @@COUNT@@ jobs</a><br>
        ID: @@ID@@<br>
        Verified: @@VERIFIED_LABEL@@<br>
        <a href="@@OFFICIAL@@" target="_blank" rel="noopener" style="color:#fff;text-decoration:underline">@@OFFICIAL@@</a>
      </div>
    </div>
  </header>

  <nav class="pills">
    <div class="wrap">
      <a href="#easy">⚡ Easy Apply</a>
      <a href="#apply">How to apply</a>
      <a href="#resume">Resume</a>
      <a href="#cover">Cover letter</a>
      <a href="#email">Intro email</a>
      <a href="#transit">Getting there</a>
      <a href="#verify">Verification</a>
      <a href="#tracker">Tracker</a>
    </div>
  </nav>

  <main class="wrap">

    <section class="block" id="easy">
      <div class="easy-box">
        <h3>⚡ Easy Apply — Download & Submit in 1 Click (Pass 8)</h3>
        <p style="margin:0 0 8px"><strong>Goal:</strong> No typing, no re-formatting. One ZIP = everything you need. Direct official link only, no recruiters. One-Click downloads Kit + opens official apply.</p>
        <div class="callout ok" style="margin:10px 0"><strong>Direct Apply (official, verified):</strong> <a href="@@APPLY_URL@@" target="_blank" rel="noopener"><strong>@@APPLY_URL@@</strong></a><br>Channel: @@APPLY_CHANNEL_ESC@@<br>Official site: <a href="@@OFFICIAL@@" target="_blank" rel="noopener">@@OFFICIAL@@</a></div>
        <div class="easy-grid">
          <button class="btn btn-primary" onclick="easyApply('@@ID@@', '@@APPLY_URL@@')" style="background:#16a34a">⚡ One-Click: Download Kit + Open Official Apply</button>
          <a href="../assets/kits/@@ID@@_kit.zip" class="btn btn-primary" download>📦 Download Kit ZIP</a>
          <a href="@@APPLY_URL@@" target="_blank" rel="noopener" class="btn btn-primary">🚀 Open Official Apply →</a>
        </div>
        <div class="easy-grid">
          <a href="../assets/resume/@@ID@@_resume.pdf" class="btn" download>📄 Resume PDF</a>
          <a href="../assets/cover/@@ID@@_cover.pdf" class="btn" download>✉️ Cover PDF</a>
          <a href="../assets/docx/@@ID@@_resume.docx" class="btn" download>📝 Resume DOCX</a>
          <a href="../assets/docx/@@ID@@_cover.docx" class="btn" download>📝 Cover DOCX</a>
          <a href="../assets/screening/@@ID@@_screening.txt" class="btn" download>📋 Tailored Screening</a>
        </div>
        <div class="easy-grid">
          <a href="../assets/profile/Screening_Answers.txt" class="btn btn-sm" download>📋 Autofill Answers TXT</a>
          <a href="../assets/profile/Brian_Profile.json" class="btn btn-sm" download>👤 Profile JSON</a>
          <a href="../assets/resume/@@ID@@_resume.txt" class="btn btn-sm" download>Resume TXT</a>
          <a href="../assets/cover/@@ID@@_cover.txt" class="btn btn-sm" download>Cover TXT</a>
          <a href="../assets/cover/@@ID@@_email.txt" class="btn btn-sm" download>Email TXT</a>
        </div>
        <div style="margin-top:12px;display:flex;flex-wrap:wrap;gap:8px">
          <a href="@@OFFICIAL@@" target="_blank" rel="noopener" class="btn btn-sm">🔍 Verify Official Site</a>
          <a href="@@APPLY_URL@@" target="_blank" rel="noopener" class="btn btn-sm btn-primary">🔍 Verify Direct Apply Link</a>
          <button class="btn btn-sm" onclick="navigator.clipboard.writeText('@@OFFICIAL@@'+'\\n'+'@@APPLY_URL@@')">📋 Copy Links for Manual Review</button>
          <a href="mailto:?subject=Application for @@POSITION_MAIL@@ at @@COMPANY_MAIL@@&body=Hello Hiring Manager,%0D%0A%0D%0AI am applying for @@POSITION_MAIL@@ at @@COMPANY_MAIL@@.%0D%0APlease find attached resume and cover letter from my Kit ZIP @@ID@@_kit.zip.%0D%0AOfficial apply link: @@APPLY_URL@@%0D%0A%0D%0AThank you,%0D%0ABrian%0D%0A(707) 596-8503%0D%0ABrian.j1274@gmail.com" class="btn btn-sm">✉️ Email Template (mailto)</a>
        </div>
        <div class="callout blue" style="margin:10px 0"><strong>1-Click Flow:</strong> Click One-Click → Kit ZIP downloads + official ATS opens (Greenhouse/Lever/Ashby/Workday/SmartRecruiters/UltiPro/AP Recruit) → Upload PDFs/DOCXs from ZIP + copy-paste from Tailored Screening → Submit. Save confirmation in tracker below. ATS does NOT detect autofill — fields indistinguishable from typed.</div>
        <div class="copy-box">
          <button class="btn btn-sm copy-btn" onclick="copyText('autofill-text', this)">Copy Autofill</button>
          <pre id="autofill-text">@@AUTOFILL@@</pre>
        </div>
        <p style="font-size:.82rem;color:var(--muted);margin:8px 0 0">No hallucinations — all docs use real resume facts only. If screening asks about GC-MS/ICP-MS/LIMS/cell culture/mouse/CPT you haven't done, answer No and mention what you HAVE done (HPLC, NMR, UV-Vis, chromatography, sample prep, GLP, QC, electronic records). Kit includes everything, so applying is download + submit.</p>
      </div>
    </section>

    <section class="block" id="apply">
      <div class="card">
        <h2 class="sec">How to apply - step by step (self-apply, no recruiter)</h2>
        <p class="sec-sub">One-Click makes it download + submit, but steps below show what's happening for manual review.</p>
        @@STATUS_CALL@@
        <div class="callout ok">
          <strong>Official apply channel (direct employer):</strong><br>
          <a href="@@APPLY_URL@@" target="_blank" rel="noopener"><strong>@@APPLY_URL@@</strong></a><br>
          Channel: @@APPLY_CHANNEL_ESC@@<br>
          Employer's own careers page: <a href="@@OFFICIAL@@" target="_blank" rel="noopener">@@OFFICIAL@@</a>
        </div>
        <ol style="line-height:1.7">
@@STEPS@@
        </ol>
        <div class="callout blue">
          <strong>ATS tip (Pass 8):</strong> Workday prefers DOCX, Greenhouse prefers text-based PDF, Lever is forgiving. Kit provides both. See <a href="../assets/ATS_GUIDE.md">ATS_GUIDE.md</a> for platform-specific flow. Upload resume DOCX first on Workday — it triggers Autofill with Resume, then review every field (parse is draft, can't edit after submit).
        </div>
        <p><button class="btn" onclick="window.print()">Print this checklist</button></p>
      </div>
    </section>

    <section class="block" id="resume">
      <div class="card">
        <h2 class="sec">Resume for this application</h2>
        <p class="sec-sub">One page. Download PDF, DOCX, or copy TXT if the form only takes plain text. Kit ZIP includes all formats.</p>
        <p>
          <a href="../assets/resume/@@ID@@_resume.pdf" class="btn btn-primary" download>Download resume PDF</a>
          <a href="../assets/docx/@@ID@@_resume.docx" class="btn btn-primary" download>Resume DOCX (for Workday etc.)</a>
          <a href="../assets/resume/@@ID@@_resume.txt" class="btn" download>Resume TXT</a>
          <a href="../assets/kits/@@ID@@_kit.zip" class="btn" download>📦 Kit ZIP (all docs)</a>
          <a href="../assets/resume/Brian_Chemistry_Resume.pdf" class="btn" download>Generic master resume PDF</a>
        </p>
        <div class="copy-box">
          <button class="btn btn-sm copy-btn" onclick="copyText('resume-text', this)">Copy</button>
          <pre id="resume-text">@@RESUME@@</pre>
        </div>
      </div>
    </section>

    <section class="block" id="cover">
      <div class="card">
        <h2 class="sec">Cover letter</h2>
        <p class="sec-sub">Three short paragraphs. Kit ZIP includes PDF+TXT+DOCX.</p>
        <p>
          <a href="../assets/cover/@@ID@@_cover.pdf" class="btn btn-primary" download>Download cover letter PDF</a>
          <a href="../assets/docx/@@ID@@_cover.docx" class="btn btn-primary" download>Cover DOCX</a>
          <a href="../assets/cover/@@ID@@_cover.txt" class="btn" download>Cover TXT</a>
          <a href="../assets/kits/@@ID@@_kit.zip" class="btn" download>📦 Kit ZIP</a>
        </p>
        <div class="copy-box">
          <button class="btn btn-sm copy-btn" onclick="copyText('cover-text', this)">Copy</button>
          <pre id="cover-text">@@COVER@@</pre>
        </div>
      </div>
    </section>

    <section class="block" id="email">
      <div class="card">
        <h2 class="sec">Intro email</h2>
        <p class="sec-sub">Use only if official posting lists a contact address or portal has a message box. Kit includes this file. Mailto button above pre-fills subject/body.</p>
        <p><a href="../assets/cover/@@ID@@_email.txt" class="btn" download>Download email TXT</a> <a href="../assets/kits/@@ID@@_kit.zip" class="btn" download>📦 Kit ZIP</a></p>
        <div class="copy-box">
          <button class="btn btn-sm copy-btn" onclick="copyText('email-text', this)">Copy</button>
          <pre id="email-text">@@EMAIL@@</pre>
        </div>
      </div>
    </section>

    <section class="block" id="transit">
      <div class="card">
        <h2 class="sec">Getting there from 21st Ave & Judah St</h2>
        <p class="sec-sub">SFMTA only - kept off the resume on purpose.</p>
        <div class="callout">
          <strong>Home:</strong> 21st Ave & Judah St, Inner Sunset, SF 94122 (Judah & 21st Ave stop, N Judah)<br>
          <strong>Destination:</strong> @@LOC_ESC@@<br>
          <strong>Zone:</strong> @@ZONE_ESC@@ - @@ROUTE_ESC@@<br>
          <strong>Live planners:</strong> <a href="https://www.sfmta.com" target="_blank" rel="noopener">SFMTA</a> | <a href="https://www.511.org" target="_blank" rel="noopener">511.org</a>
        </div>
        <div class="copy-box">
          <button class="btn btn-sm copy-btn" onclick="copyText('transit-text', this)">Copy</button>
          <pre id="transit-text">@@TRANSIT@@</pre>
        </div>
      </div>
    </section>

    <section class="block" id="verify">
      <div class="card">
        <h2 class="sec">Verification - what was checked and how</h2>
        <p class="sec-sub">Nothing inferred. Official sources only, with direct links for manual review. Pass 8 adds tailored screening + ATS guide.</p>
        <ul class="clean">
@@VERIFY@@
        </ul>
        <div class="callout red">
          <strong>Watch-outs:</strong> @@FLAG_ESC@@
        </div>
        <p><a href="../index.html" class="btn">&larr; Back to all @@COUNT@@ jobs</a> <a href="@@OFFICIAL@@" target="_blank" rel="noopener" class="btn btn-primary">Open official careers page</a> <a href="@@APPLY_URL@@" target="_blank" rel="noopener" class="btn btn-primary">Apply direct →</a></p>
      </div>
    </section>

    <section class="block" id="tracker">
      <div class="card">
        <h2 class="sec">My application tracker (saved on this device)</h2>
        <p class="sec-sub">Marked steps are stored in your browser only - nothing uploaded.</p>
        <div id="tracker-widget-@@ID@@"></div>
      </div>
    </section>

    <footer>
      <p>JobSearchSF - @@ID@@ - @@COMPANY_ESC@@ - verification snapshot <span id="today"></span>. Apply through official employer portal only. No recruiters, no fees, no guesses. Pass 8 Easy Apply: One-Click = Kit ZIP download + official ATS open.</p>
      <p><a href="../index.html">&larr; Back to main list</a> | <a href="@@OFFICIAL@@" target="_blank" rel="noopener">Official careers page</a> | <a href="@@APPLY_URL@@" target="_blank" rel="noopener">Apply direct</a> | <a href="../assets/kits/@@ID@@_kit.zip" download>📦 Kit ZIP</a> | <a href="../assets/screening/@@ID@@_screening.txt" download>📋 Screening</a></p>
    </footer>
  </main>
  <script src="../assets/js/tracker.js"></script>
  <script>
    document.getElementById('today').textContent = new Date().toISOString().slice(0,10);
    JobTracker.mount('tracker-widget-@@ID@@', '@@ID@@');
  </script>
</body>
</html>
"""

def subpage_html(job, count):
    apply_url = url_of(job.get("applyLink") or job.get("officialLink"))
    st_label = esc(job.get("status", "monitor").replace("-", " "))
    st_note = esc(job.get("statusNote", ""))
    if job.get("status") == "flag":
        status_call = ("<div class=\"callout red\"><strong>Do not send an application to this row as it stands.</strong> "
                       "%s<br><br>%s</div>" % (esc(job.get("flag", "")), st_note))
    else:
        cls = "callout" if job.get("status")=="monitor" else "callout ok"
        status_call = "<div class=\"%s\"><strong>Status: %s.</strong> %s</div>" % (cls, st_label, st_note)
    meta = ("%s - %s. Verified SF lab job with official direct-apply link, step-by-step beginner guide, "
            "downloadable resume, cover letter and intro email. JobSearchSF."
            % (clean_company(job.get("company", "")), role_type(job)))
    transit = ("From: 21st Ave & Judah St, San Francisco, CA 94122 (Judah & 21st Ave, N Judah)\n"
               "To: %s\nRoute: %s\nEmployer: %s\nOfficial posting: %s\n"
               "Check live times on SFMTA (sfmta.com) or 511.org before an interview; night and weekend "
               "service is thinner, and Muni delays are common at Market Street transfers."
               % (job.get("location", ""), job.get("route",""), job.get("company",""), job.get("officialLink","")))
    html_out = TEMPLATE
    reps = {
        "@@ID@@": job["id"],
        "@@COUNT@@": str(count),
        "@@COMPANY@@": esc(clean_company(job.get("company", ""))),
        "@@COMPANY_ESC@@": esc(job.get("company", "")),
        "@@COMPANY_MAIL@@": esc(clean_company(job.get("company","")).replace("&","and")),
        "@@POSITION@@": esc(role_type(job)),
        "@@POSITION_ESC@@": esc(job.get("position", "")),
        "@@POSITION_MAIL@@": esc(role_type(job).replace("&","and")),
        "@@META@@": esc(meta),
        "@@SCORE@@": str(job.get("matchScore", 0)),
        "@@FIT_SHORT@@": esc((job.get("fit", "") or "")[:160]),
        "@@LOC_ESC@@": esc(job.get("location", "")),
        "@@ZONE_ESC@@": esc(job.get("commuteZone", "")),
        "@@ROUTE_ESC@@": esc(job.get("route", "")),
        "@@OFFICIAL@@": esc(job.get("officialLink", "#")),
        "@@APPLY_URL@@": esc(apply_url),
        "@@APPLY_CHANNEL_ESC@@": esc(job.get("applyChannel", "")),
        "@@VERIFIED_LABEL@@": ("Verified - official employer source" if job.get("verified") else "Not verified"),
        "@@STATUS_CALL@@": status_call,
        "@@AUTOFILL@@": esc(build_autofill(job)),
    }
    for k, v in reps.items():
        html_out = html_out.replace(k, v)
    html_out = html_out.replace("@@STEPS@@", build_steps(job))
    html_out = html_out.replace("@@VERIFY@@", build_verify(job))
    html_out = html_out.replace("@@TRANSIT@@", esc(transit))
    html_out = html_out.replace("@@RESUME@@", esc(resume_text(job)))
    html_out = html_out.replace("@@COVER@@", esc(cover_text(job)))
    html_out = html_out.replace("@@EMAIL@@", esc(email_text(job)))
    html_out = html_out.replace("@@FLAG_ESC@@", esc(job.get("flag") or "No irregularity found at audit; re-verify before applying, since postings rotate."))
    return html_out

def main():
    jobs = load_jobs()
    count = len(jobs)
    # hints
    try:
        spec = importlib.util.spec_from_file_location("pass6_rows", os.path.join(ROOT, "pass6_rows.py"))
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        hints = {r["id"]: r for r in mod.ROWS}
        for j in jobs:
            if j["id"] in hints:
                for k in ("_letter_to", "_dept_line", "_role_type", "_email_note"):
                    j[k] = hints[j["id"]].get(k, "")
    except Exception as e:
        print("pass6 hints unavailable:", e)
    try:
        spec2 = importlib.util.spec_from_file_location("fix_city_rows", os.path.join(ROOT, "fix_city_rows.py"))
        mod2 = importlib.util.module_from_spec(spec2)
        spec2.loader.exec_module(mod2)
        for jid, d in mod2.NEW.items():
            for j in jobs:
                if j["id"] == jid:
                    for k in ("_letter_to", "_dept_line", "_role_type", "_email_note"):
                        j[k] = d.get(k, "")
    except Exception as e:
        print("city-row hints unavailable:", e)

    os.makedirs(RESUME_DIR, exist_ok=True)
    os.makedirs(COVER_DIR, exist_ok=True)
    os.makedirs(JOBS_DIR, exist_ok=True)

    master = resume_text(None)
    open(os.path.join(RESUME_DIR, "Brian_Chemistry_Resume.txt"), "w", encoding="utf-8").write(master)
    make_pdf(master, os.path.join(RESUME_DIR, "Brian_Chemistry_Resume.pdf"))
    base = base_cover_text()
    open(os.path.join(COVER_DIR, "Brian_Cover_Letter_Base.txt"), "w", encoding="utf-8").write(base)
    make_pdf(base, os.path.join(COVER_DIR, "Brian_Cover_Letter_Base.pdf"))

    n = 0
    for j in jobs:
        tag_file = j["id"]
        rt = resume_text(j)
        ct = cover_text(j)
        et = email_text(j)
        open(os.path.join(RESUME_DIR, "%s_resume.txt" % tag_file), "w", encoding="utf-8").write(rt)
        make_pdf(rt, os.path.join(RESUME_DIR, "%s_resume.pdf" % tag_file))
        open(os.path.join(COVER_DIR, "%s_cover.txt" % tag_file), "w", encoding="utf-8").write(ct)
        make_pdf(ct, os.path.join(COVER_DIR, "%s_cover.pdf" % tag_file))
        open(os.path.join(COVER_DIR, "%s_email.txt" % tag_file), "w", encoding="utf-8").write(et)
        page = subpage_html(j, count)
        open(os.path.join(JOBS_DIR, "%s.html" % tag_file), "w", encoding="utf-8").write(page)
        n += 1
    print(f"regenerated {n} rows (resume/cover/email txt+pdf + subpages) Pass8")
    print("total jobs:", count)

if __name__ == "__main__":
    main()
