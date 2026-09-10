# -*- coding: utf-8 -*-
"""Pass 6 self-audit correction: the three City & County of SF rows were rewritten
after fetching each careers.sf.gov role page in full (the search-snippet version of
the facts was incomplete/misleading).

Verified 2026-09-09 from the role pages:
  2416 Lab Tech II  id 3743990002599958  "Laboratory Technician II (2416) - DPH - 139184"
      Recruitment RTF0139183-01154737 / PBT-2416-139184, published Sep 22 2023,
      opening Sep 13 2023, final closing Sep 22 2023, class salary $81,692-$99,372
      (announcement text lists $73,398-$89,336 for that common range), 101 Grove Street,
      Mon-Fri 8am-5pm + some Saturdays, contact Hanz Pagao hanz.pagao@sfdph.org,
      HS diploma + 1 yr lab experience (15 semester units incl. one college chem/bio
      lab course substitutes for 6 months; 30 units / two lab courses for the full year).
  2402 Lab Tech I   id 743999809251111  "Laboratory Technician I - Access to City Employment (ACE) (2402)"
      Recruitment REF3136I, published Mar 3 2022, salary $72,332-$87,906, department
      "Access to City Employment" - an ACE posting, which requires a Certification of
      Disability from the CA Dept of Rehabilitation or a Veterans Preference Letter from
      the US Dept of Veterans Affairs. Minimum quals: HS diploma + 6 months lab work
      (or 15 semester units including one college chemistry/biology lab course).
  2463 Microbiologist I id 3743990001679838  REF26033Y / PBT-2463-134715, published
      Jun 8 2023, opened Apr 25 2023, deadline Jun 8 2023, class range $104,806-$182,936
      (announcement compensation $91,910-$129,402, steps 1-8), contact Diane Zhou
      diane.zhou@sfdph.org. MINIMUM QUALIFICATIONS: baccalaureate with major coursework in
      medical/public health bacteriology or microbiology AND a valid certificate as a public
      health microbiologist issued by the CA state board of health - no substitution listed.
"""
import os
import re

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(ROOT, "assets", "js", "data.js")


def js_str(s):
    return '"' + str(s).replace("\\", "\\\\").replace('"', '\\"').replace("\n", " ") + '"'


NEW = {
    "job-115": {
        "company": "City & County of San Francisco - Department of Public Health (class 2416)",
        "position": "Laboratory Technician II (2416) - SFDPH Public Health Laboratory, 101 Grove St (position-based test)",
        "verified": True,
        "verificationMethod": ("careers.sf.gov role page 'Laboratory Technician II (2416) - DPH - 139184' "
                               "(id 3743990002599958) fetched in full on 2026-09-09 - duties, minimum quals, "
                               "location, shift, salary and department contact read off the City's own page"),
        "matchScore": 86,
        "batch": 6,
        "location": "101 Grove Street, San Francisco, CA 94102 (Public Health Laboratory, SFDPH)",
        "commuteZone": "C",
        "route": ("ZONE C - 43 Masonic from Judah & 21st Ave toward the Civic Center, or N Judah eastbound to "
                  "Powell + 5 Fulton to AFDC/Civic Center. ~30-40 min door to door."),
        "officialLink": "https://careers.sf.gov/classifications/?classCode=2416",
        "applyLink": ("https://careers.sf.gov/role/?id=3743990002599958 - City of SF SmartRecruiters portal "
                      "(recruitment RTF0139183-01154737 / PBT-2416-139184)"),
        "applyChannel": ("Official City & County of San Francisco portal - direct civil-service hire, position-based "
                         "test, never through a staffing firm"),
        "requirements": ("High school diploma or equivalent AND one (1) year of laboratory experience within the last "
                         "five years assisting with preparation of cultures, media, reagents and specimens for "
                         "microbiological exams (or equivalent to class 2402 work). Substitution per the City page: "
                         "15 semester units including one college lab course in chemistry or a biological science "
                         "covers 6 months; 30 semester units with two such lab courses covers the full year. Duties: "
                         "unpacking and centrifuging specimens, separating plasma/serum, preparing media and reagents, "
                         "stains for microscopy, incubator/refrigerator temperature logs, QC on equipment, entering "
                         "patient and specimen data into the lab information system, equipment maintenance, and "
                         "assisting research projects."),
        "fit": ("Closest City class to your record: the coursework substitution is chemistry-lab friendly, your paid "
                "lab terms are specimen/media/QC/records work, and the City prints this as an entry-to-journey "
                "assistant role rather than a licensed scientist post. Mon-Fri 8am-5pm with some Saturdays, per the "
                "announcement."),
        "status": "monitor",
        "statusNote": ("Last City announcement for this exact posting opened Sep 13, 2023 and finally closed "
                        "Sep 22, 2023, so there is no open filing window on 2026-09-09 - the role page stays "
                        "published and states the eligible list 'may be used to fill future vacancies in this class' "
                        "(Rule of 3). Salary shown on the class header: $81,692-$99,372; the 2023 announcement text "
                        "printed $73,398-$89,336 for the common range at that time. Watch the class page and apply "
                        "inside the first days of any new window."),
        "flag": ("Civil-service mechanics: this is a position-based test for a specific vacancy, so you compete for "
                 "the open seat rather than landing on a general list; the announcement also directs applicants to a "
                 "required supplemental questionnaire (the 2023 posting linked an MS Form). A department contact is "
                 "printed on the City page (Hanz Pagao, hanz.pagao@sfdph.org) - use it only to ask about the "
                 "qualification review, never to apply outside the portal."),
        "sources": [{"label": "SFDPH Lab Technician II 2416 role page (official, fetched 2026-09-09)",
                     "url": "https://careers.sf.gov/role/?id=3743990002599958"},
                    {"label": "City class 2416 classification page (official)",
                     "url": "https://careers.sf.gov/classifications/?classCode=2416"}],
        "_letter_to": "Hiring Manager",
        "_dept_line": "San Francisco Department of Public Health",
        "_role_type": "Laboratory Technician II",
        "_email_note": ("The City only accepts applications through careers.sf.gov; the printed contact exists for "
                        "questions about the recruitment, not for applying by email."),
    },
    "job-116": {
        "company": "City & County of San Francisco - class 2402 Laboratory Technician I",
        "position": "Laboratory Technician I (2402) - entry-level City lab class (general window - watch the class page)",
        "verified": True,
        "verificationMethod": ("careers.sf.gov class-2402 role page (id 743999809251111) fetched in full on "
                               "2026-09-09; class definition, minimum qualifications and the $72,332-$87,906 salary "
                               "range are quoted from the City's own page, alongside the classification page"),
        "matchScore": 80,
        "batch": 6,
        "location": "City departments that hire class 2402 (SFDPH Public Health Laboratory, 101 Grove St; other City labs as assigned)",
        "commuteZone": "C",
        "route": ("ZONE C - 43 Masonic or N Judah + 5 Fulton to the Civic Center / AFDC area; SFPUC labs at 525 "
                  "Golden Gate Ave are a short walk from Civic Center. ~25-40 min."),
        "officialLink": "https://careers.sf.gov/classifications/?classCode=2402",
        "applyLink": ("https://careers.sf.gov/classifications/?classCode=2402 - open exams for this class are listed "
                      "on the City's own careers site; apply only through careers.sf.gov"),
        "applyChannel": "Official City & County of San Francisco portal (direct; entry-level class)",
        "requirements": ("High school diploma or equivalent AND six (6) months of laboratory experience within the "
                         "last five years: cleaning and sterilizing lab equipment, packing/unpacking and labeling "
                         "supplies or specimens, preparing glassware for microbiological exams, keeping records of "
                         "testing or patient information. Substitution per the City page: 15 semester units "
                         "(or 22.5 quarter units) from an accredited college including one college laboratory course "
                         "in chemistry or a biological science replaces the six months entirely. Duties include "
                         "pipetting reagents, making up percentage reagents, autoclaving infectious waste, verifying "
                         "and date-stamping incoming supplies, maintaining lab inventory, and aliquoting research "
                         "specimens."),
        "fit": ("This is the easiest City minimum to clear honestly: a B.S. in Chemistry with college lab coursework "
                "meets the substitution outright, and the duty list is the same glassware, reagent-prep, labeling "
                "and record-keeping work you did at Quintara and MicroConstants. Pay is lower than the scientist "
                "classes; it is a door in, not a destination."),
        "status": "monitor",
        "statusNote": ("No open general filing window on 2026-09-09. The only live 2402 role page the City is "
                        "serving (id 743999809251111, published Mar 3, 2022, recruitment REF3136I, salary "
                        "$72,332-$87,906) is an Access to City Employment (ACE) exam - see the flag. Check the "
                        "class page weekly; the City re-posts 2402 exams periodically and the ACE channel recurs too."),
        "flag": ("IMPORTANT eligibility catch found while verifying: the 2402 page currently published is an ACE "
                 "recruitment, which hires people with a disability and requires either a Certification of Disability "
                 "from the California Department of Rehabilitation or a Veterans Preference Letter from the U.S. "
                 "Department of Veterans Affairs. If you do not have one of those, do not apply through that "
                 "announcement - wait for a general 2402 exam. Applying to the wrong channel wastes the window."),
        "sources": [{"label": "City 2402 role page incl. class definition + ACE eligibility text (official, fetched 2026-09-09)",
                     "url": "https://careers.sf.gov/role/?id=743999809251111"},
                    {"label": "City class 2402 classification page (official)",
                     "url": "https://careers.sf.gov/classifications/?classCode=2402"}],
        "_letter_to": "Hiring Manager",
        "_dept_line": "City and County of San Francisco",
        "_role_type": "Laboratory Technician I",
        "_email_note": ("For an ACE application the program contacts printed on the City page are Danielle Anderson, "
                        "Leorah Dang, Porsche Bunton and John Weber (@sfgov.org) - but only after you have "
                        "confirmed you meet the ACE eligibility requirement."),
    },
    "job-117": {
        "company": "City & County of San Francisco - Department of Public Health (class 2463)",
        "position": "Microbiologist I (2463) - SFDPH Public Health Laboratory - QUALIFICATION GAP, do not apply yet",
        "verified": True,
        "verificationMethod": ("careers.sf.gov role page 'Microbiologist I - 2463 - Department of Public Health' "
                               "(id 3743990001679838, REF26033Y / PBT-2463-134715) fetched in full on 2026-09-09; "
                               "minimum qualifications, compensation and dates quoted from the City's own page"),
        "matchScore": 34,
        "batch": 6,
        "location": "San Francisco Public Health Laboratories, Department of Public Health, San Francisco",
        "commuteZone": "C",
        "route": ("ZONE C - 43 Masonic from Judah & 21st Ave toward the Civic Center / AFDC campus; N Judah + 5 "
                  "Fulton as alternate. ~30-40 min."),
        "officialLink": "https://careers.sf.gov/classifications/?classCode=2463",
        "applyLink": ("https://careers.sf.gov/role/?id=3743990001679838 - City portal; read the minimum "
                      "qualifications before spending any time on it"),
        "applyChannel": "Official City & County of San Francisco portal (position-based test, Rule of 3)",
        "requirements": ("Baccalaureate with major course work in medical or public health bacteriology or "
                         "microbiology AND a valid certificate as a public health microbiologist issued by the "
                         "California state board of health. No experience substitution is listed for either. Duties: "
                         "qualitative/quantitative diagnostic analysis of human, food and environmental specimens by "
                         "serologic, molecular, agglutination and biochemical methods; smears/cultures and "
                         "acid-fast bacilli microscopy; TB drug-susceptibility testing; reagent and supply "
                         "inventory; equipment calibration, daily QC and troubleshooting; proficiency testing to "
                         "federal regulation."),
        "fit": ("The duties fit your QC and instrumentation habits, but the minimum qualifications do not: a "
                "chemistry degree without a microbiology major plus the California public health microbiologist "
                "certificate is a hard screen, and the City rejects on that basis rather than ranking you lower."),
        "status": "flag",
        "statusNote": ("Listed deliberately as a blocked row so the requirement is visible instead of rediscovered "
                        "in three months: the last City window for this posting ran Apr 25 - Jun 8, 2023 (class "
                        "range $104,806-$182,936; the 2023 announcement printed $91,910-$129,402, steps 1-8, "
                        "variable shifts), and the qualification screen would have excluded this application. "
                        "To make this real you would need microbiology course work and the state certificate; the "
                        "2416 Laboratory Technician II class (job-115) is the same building and same lab without "
                        "that gate."),
        "flag": ("Not eligible as the record stands - B.S. Chemistry (UCSC 2011) is not a microbiology major and no "
                 "CA public health microbiologist certificate is held. Do not apply to 2463 postings until that "
                 "changes; do not let an agent or a 'we can get you around the certificate' offer touch this - both "
                 "are disqualifiers and a scam tell."),
        "sources": [{"label": "SFDPH Microbiologist I 2463 role page (official, fetched 2026-09-09)",
                     "url": "https://careers.sf.gov/role/?id=3743990001679838"},
                    {"label": "City class 2463 classification page (official)",
                     "url": "https://careers.sf.gov/classifications/?classCode=2463"}],
        "_letter_to": "Hiring Manager",
        "_dept_line": "San Francisco Department of Public Health",
        "_role_type": "Microbiologist I",
        "_email_note": ("Do not email the department about this class - the qualification screen is published and "
                        "absolute. Redirect the effort to class 2416 (job-115) or class 2402 (job-116)."),
    },
}

KEYS = ["company", "position", "verificationMethod", "matchScore", "batch", "location",
        "commuteZone", "route", "officialLink", "applyLink", "applyChannel", "requirements",
        "fit", "status", "statusNote", "flag", "subpage", "sources"]


def serialize_block(jid, d):
    out = ["  {", "    id: %s," % js_str(jid)]
    for k in KEYS:
        if k == "verified":
            continue
        if k == "batch":
            out.append("    batch: 6,")
        elif k == "subpage":
            num = int(jid.split("-")[1])
            out.append("    subpage: %s," % js_str("jobs/job-%d.html" % num))
        elif k == "sources":
            src = ",\n".join("      { label: %s, url: %s }" % (js_str(s["label"]), js_str(s["url"])) for s in d[k])
            out.append("    sources: [\n%s\n    ]" % src)
        elif k in ("matchScore",):
            out.append("    matchScore: %d," % int(d[k]))
        else:
            out.append("    %s: %s," % (k, js_str(d[k])))
    # verified flag right after position, matching the existing style
    out.insert(4, "    verified: true,")
    return "\n".join(out) + "\n  },"


def main():
    txt = open(DATA, encoding="utf-8").read()
    for jid, d in NEW.items():
        m = re.search(r"\n  \{\s*id: \"%s\",.*?\n  \}," % jid, txt, re.S)
        if not m:
            print("MISS block", jid)
            continue
        txt = txt[:m.start()] + "\n" + serialize_block(jid, d) + txt[m.end():]
        print("rewrote", jid)
    open(DATA, "w", encoding="utf-8").write(txt)


if __name__ == "__main__":
    main()
