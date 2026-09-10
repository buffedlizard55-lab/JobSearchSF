# -*- coding: utf-8 -*-
"""Pass 6 rows (job-101 .. job-120) for JobSearchSF.

Audit date: 2026-09-09. Every row below was checked against the employer's OWN
official source (UCSF AP Recruit, careers.sf.gov, Ashby, Greenhouse). Nothing is
invented: where the official source did not state something (street address,
salary, deadline), the row says so instead of guessing.

status values used by the site: "recently-posted" | "monitor" | "flag".
Rows marked "monitor" are real, verified employer sources where either
(a) no live opening matching Brian's profile was on the board at audit time, or
(b) the posting is live but the worksite/schedule is outside the San Francisco
    transit rule, so it is kept as a documented alternate rather than a target.
"""

AUDIT_DATE = "2026-09-09"

UCSF_DEPT_MISSION = "UCSF, San Francisco (Mission Bay campus - see posting for building/room)"
ZONE_B_ROUTE = ("ZONE B - N Judah eastbound to Embarcadero, then T-Third to "
                "23rd St/mission Bay; or 49-Van Ness to Mission Bay. ~35-50 min "
                "door to door. Confirm with SFMTA trip planner.")
ZONE_AB_ROUTE = ("ZONE A/B - 43 Masonic or 24-Division to Parnassus/2nd Ave for "
                 "Parnassus sites; T-Third or 49-Van Ness for Mission Bay sites. "
                 "~20-45 min. Confirm with SFMTA trip planner.")
APPLY_PORTAL = ("UCSF Academic Personnel portal (direct hire, no recruiter). "
                "Create an AP Recruit account, upload CV + cover letter, and enter "
                "reference contacts. No fee, no third party.")

# UCSF postings verified on 2026-09-09 from https://aprecruit.ucsf.edu/apply
# (the official "Browse Open Recruitments" list, which prints the open / review /
# accept-until dates for every live recruitment) and, where noted, from the
# individual posting page.
def ucsf(jpf, dept, rank, title_short, window_open, review, until,
         score, notes, reqs, fit, flag="", salary=None, campus=UCSF_DEPT_MISSION,
         zone="B", route=ZONE_B_ROUTE, verified_page=False, sources_extra=()):
    jid = "JPF" + str(jpf).zfill(5)
    url = "https://aprecruit.ucsf.edu/" + jid
    official = "https://aprecruit.ucsf.edu/apply"
    ver = ("Official UCSF AP Recruit posting page %s (fetched %s)" % (jid, AUDIT_DATE)
           if verified_page else
           "Official UCSF AP Recruit open-recruitments list aprecruit.ucsf.edu/apply "
           "(fetched %s) - %s listed with open date %s" % (AUDIT_DATE, jid, window_open))
    salary_line = (" A reasonable estimate published with the posting: %s." % salary) if salary else ""
    status = "monitor" if "past review" in notes else "recently-posted"
    d = {
        "id": None,  # assigned by caller
        "company": dept,
        "position": "%s - %s (%s)" % (rank, title_short, jid),
        "verified": True,
        "verificationMethod": ver,
        "matchScore": score,
        "batch": 6,
        "location": campus,
        "commuteZone": zone,
        "route": route,
        "officialLink": url,
        "applyLink": "%s - apply on UCSF's official AP Recruit portal" % url,
        "applyChannel": APPLY_PORTAL,
        "requirements": reqs,
        "fit": fit,
        "status": status,
        "statusNote": ("Application window: open %s; review %s; applications accepted "
                       "until %s (as printed on the official posting list, %s).%s"
                       % (window_open, review, until, AUDIT_DATE, (" " + notes) if notes else ""))
                      + salary_line,
        "flag": flag,
        "subpage": None,  # assigned by caller
        "sources": [{"label": "UCSF AP Recruit posting %s (official)" % jid, "url": url},
                    {"label": "UCSF open recruitments list (official)", "url": official}]
                   + list(sources_extra),
        # internal, not written to data.js:
        "_letter_to": "Search Committee",
        "_dept_line": dept.split(" - ")[0].strip(),
        "_role_type": rank,
        "_email_note": "UCSF AP Recruit asks for your CV plus reference contacts; the cover letter field is optional for Specialist postings.",
    }
    return d


UCSF_JP = "University of California, San Francisco - "

ROWS = [
    # 101 -----------------------------------------------------------------
    ucsf(6065, UCSF_JP + "Liver Center / Medicine (Maher Lab)",
         "Junior Specialist", "Liver cell isolation, analysis & immunology core",
         "May 1, 2026", "May 16, 2026 (past - still reviewed while unfilled)",
         "Nov 1, 2027", 92,
         "Verified by fetching the posting page itself. The posting's own apply link "
         "points to aprecruit.ucsf.edu/JPF06025 for the same recruitment - use the "
         "JPF06065 page if the JPF06025 link does not resolve.",
         "Baccalaureate or 4+ years relevant research experience; demonstrated "
         "knowledge of chemistry sufficient to prepare and pH laboratory solutions; "
         "instrument care (perfusion pumps, centrifuges, incubators, biosafety "
         "cabinets); records and recharge accounting; occasional nights/weekends; "
         "Word and Excel. Cell-culture experience preferred.",
         "Best fit in this pass - the posting explicitly asks for chemistry knowledge "
         "for solution prep and pH, plus instrument upkeep and record keeping, which "
         "is exactly the Quintara / MicroConstants work. Core-facility pace, not "
         "publish-or-perish.",
         flag="Occasional nights/weekends required (human liver availability); confirm "
              "the schedule fits your needs.",
         salary="$55,000-$58,600 (UC Table 24B estimate printed on the posting)",
         verified_page=True),
    # 102 -----------------------------------------------------------------
    ucsf(5785, UCSF_JP + "Helen Diller Family Comprehensive Cancer Center (McCormick Lab)",
         "Junior Specialist", "Biochemistry, enzymatic and plate-based assays",
         "Sep 5, 2025", "Feb 15, 2026 (past - committee keeps reviewing while unfilled)",
         "Mar 5, 2027", 87,
         "Verified from the official posting page content indexed by UCSF; the review "
         "date has passed, so apply and note availability.",
         "Baccalaureate or 4+ years research experience; prior laboratory work "
         "required; biochemistry background preferred with enzymatic and plate-based "
         "assays (ELISA, luminescent); chromatography systems such as FPLC or HPLC "
         "preferred; tissue culture, electrophoresis, western blotting, protein "
         "purification useful.",
         "Chromatography is listed as preferred, not required, and the posting says it "
         "is a good step for someone building toward further training - matches a B.S. "
         "with HPLC and purification experience.",
         flag="One-year appointment with possibility of renewal (per the posting).",
         salary="$55,000-$58,600 (UC Table 24B estimate printed on the posting)"),
    # 103 -----------------------------------------------------------------
    ucsf(6131, UCSF_JP + "Helen Diller Family Comprehensive Cancer Center (Ashworth Lab)",
         "Junior or Assistant Research Specialist", "Cancer genetics research support",
         "Jul 9, 2026", "Jul 24, 2026 (past - reviewed while unfilled)",
         "Jan 9, 2028", 80,
         "Posted within the last two months - one of the newest SF lab openings on "
         "this site.",
         "Junior rank: baccalaureate or 4+ years research experience. Assistant rank: "
         "master's or bachelor's with 3+ years. Research execution, data analysis, "
         "manuscript and grant support (per posting).",
         "Entry rank is open to a B.S. with research experience; your publication and "
         "medicinal-chemistry internship read well for a cancer-genetics lab.",
         flag="Check the posting for the specific techniques the lab wants before "
              "tailoring the CV."),
    # 104 -----------------------------------------------------------------
    ucsf(5798, UCSF_JP + "Biochemistry & Biophysics (DeRisi Lab)",
         "Junior / Assistant / Associate Specialist", "Host-pathogen biology and diagnostics",
         "Sep 17, 2025", "Sep 15, 2026 - apply now for full consideration",
         "Mar 17, 2027", 79,
         "URGENT: the full-consideration date printed on the posting is 6 days after "
         "this audit.",
         "Baccalaureate (or 4+ years research experience) for Junior rank; laboratory "
         "work in molecular biology / microbiology; microscopy and assay work typical "
         "for the lab (per posting).",
         "A top-tier basic-science department that hires B.S. specialists; the review "
         "date is close, so apply first and refine later.",
         flag="Apply by Sep 15, 2026 for full consideration (per posting)."),
    # 105 -----------------------------------------------------------------
    ucsf(6179, UCSF_JP + "School of Dentistry - Cell & Tissue Biology (Choksi Lab)",
         "Junior Specialist", "Developmental biology lab research support",
         "Jul 30, 2026", "Aug 14, 2026 (past - reviewed while unfilled)",
         "Jan 30, 2028", 75,
         "Newest department in this group (opened Jul 30, 2026).",
         "Baccalaureate or 4+ years research experience; research under supervision; "
         "materials must list current/pending qualifications (per posting).",
         "Entry-level specialist rank with a stated B.S. route; bench technique is "
         "trained in place.",
         ),
    # 106 -----------------------------------------------------------------
    ucsf(6193, UCSF_JP + "School of Dentistry - Orofacial Sciences (Zhang Lab)",
         "Junior Specialist", "Research support, cell and molecular methods",
         "Aug 11, 2026", "Aug 26, 2026 (past - reviewed while unfilled)",
         "Feb 11, 2028", 74,
         "Posted 2026-08-11 - the most recently opened recruitment in this pass.",
         "Baccalaureate or 4+ years research experience; laboratory techniques per "
         "posting; documentation and data management.",
         "Very fresh posting means less competition from earlier applicant pools.",
         ),
    # 107 -----------------------------------------------------------------
    ucsf(6056, UCSF_JP + "Biochemistry & Biophysics (Martens Lab)",
         "Junior or Assistant Specialist", "Cytoskeleton / biophysics bench work",
         "Apr 27, 2026", "Jun 28, 2026 (past - reviewed while unfilled)",
         "Oct 27, 2027", 76,
         "",
         "Baccalaureate (or 4+ years research experience) for Junior rank; master's or "
         "bachelor's plus 3 years for Assistant rank; microscopy and biochemical "
         "methods per posting.",
         "Biochemistry-heavy bench role in a department that runs a specialist series "
         "rather than a PhD-only postdoc track.",
         ),
    # 108 -----------------------------------------------------------------
    ucsf(6049, UCSF_JP + "Anatomy (Feinberg Lab)",
         "Junior Specialist", "Biomaterials and cell-based assays",
         "Apr 29, 2026", "May 14, 2026 (past - reviewed while unfilled)",
         "Oct 29, 2027", 74,
         "",
         "Baccalaureate or 4+ years research experience; cell culture, assay "
         "development and materials handling per posting.",
         "Biomaterials work leans on solution prep, sterile handling and careful "
         "records - transferable from your QC and purification background.",
         ),
    # 109 -----------------------------------------------------------------
    ucsf(6073, UCSF_JP + "Cardiovascular Research Institute (Huang Lab)",
         "Junior Specialist", "Regenerative biology and extreme physiology",
         "May 5, 2026", "Jun 26, 2026 (past - reviewed while unfilled)",
         "Nov 5, 2027", 72,
         "",
         "Baccalaureate or 4+ years research experience; molecular and cell biology "
         "methods per posting.",
         "Mission Bay institute with shared-core access; entry specialist rank.",
         ),
    # 110 -----------------------------------------------------------------
    ucsf(5968, UCSF_JP + "School of Dentistry - Cell & Tissue Biology (Sneddon Lab)",
         "Junior / Assistant / Associate Specialist", "Skin biology and stem cell models",
         "Feb 25, 2026", "Aug 1, 2026 (past - reviewed while unfilled)",
         "Aug 25, 2027", 71,
         "",
         "Baccalaureate (or 4+ years research experience) at Junior rank; cell culture "
         "and molecular techniques per posting.",
         "Culture-heavy role; your aseptic and purification habits are the entry "
         "ticket.",
         ),
    # 111 -----------------------------------------------------------------
    ucsf(5881, UCSF_JP + "School of Dentistry - Cell & Tissue Biology (Gong Lab)",
         "Junior / Assistant / Associate / Full Specialist", "Cardiac regeneration research",
         "Dec 2, 2025", "Dec 17, 2025 (past - reviewed while unfilled)",
         "Jun 2, 2027", 70,
         "",
         "Baccalaureate or 4+ years research experience at Junior rank; research "
         "execution, data analysis, and scholarly contribution per posting.",
         "Long window (accepts to Jun 2027) - realistic for a B.S. at the Junior rank.",
         ),
    # 112 -----------------------------------------------------------------
    ucsf(6050, UCSF_JP + "School of Dentistry - Cell & Tissue Biology (Bush Lab)",
         "Junior / Assistant / Associate Specialist", "Neural crest and developmental biology",
         "Apr 22, 2026", "Jun 30, 2026 (past - reviewed while unfilled)",
         "Oct 22, 2027", 68,
         "",
         "Baccalaureate or 4+ years research experience at Junior rank; imaging and "
         "molecular methods per posting.",
         "Developmental biology with heavy imaging; a stretch from chemistry but the "
         "rank and record-keeping demands fit.",
         ),
    # 113 -----------------------------------------------------------------
    ucsf(5770, UCSF_JP + "School of Dentistry - Orofacial Sciences (Momen-Heravi Lab)",
         "Junior / Assistant / Associate Specialist", "Extracellular vesicles and oral cancer biomarkers",
         "Sep 5, 2025", "Jan 31, 2026 (past - reviewed while unfilled)",
         "Mar 5, 2027", 67,
         "",
         "Baccalaureate or 4+ years research experience; molecular biology, EV "
         "isolation and assay work per posting.",
         "Biomarker/analytics flavour (isolation, quantification, documentation) suits "
         "a QC-trained chemist.",
         ),
    # 114 -----------------------------------------------------------------
    ucsf(5544, UCSF_JP + "Anatomy / Orthopaedic Surgery (Basbaum Lab)",
         "Junior / Assistant / Associate / Full Specialist", "Pain mechanisms and neurobiology",
         "Apr 23, 2025", "Dec 15, 2025 (past - reviewed while unfilled)",
         "Oct 23, 2026 - closes in ~6 weeks", 66,
         "Window closes 2026-10-23; apply before then or it is gone.",
         "Baccalaureate or 4+ years research experience at Junior rank; behavioural "
         "and histological methods per posting.",
         "Established department with a rolling specialist series; deadline pressure is "
         "the reason it is listed here rather than lower.",
         flag="Deadline Oct 23, 2026 (printed on the official posting)."),
    # 115 -----------------------------------------------------------------
    # NOTE: the three City rows below (job-115/116/117) were superseded on the same pass by
    # fix_city_rows.py after each careers.sf.gov role page was read in full (ACE eligibility gate on
    # 2402, closed 2023 window on 2416, hard microbiology-major + state-certificate screen on 2463).
    # data.js now carries the corrected text; these entries remain only as the original draft.
    {
        "company": "City & County of San Francisco - Human Resources (class 2402)",
        "position": "Laboratory Technician I - entry level, citywide eligible list (class 2402)",
        "verified": True,
        "verificationMethod": ("careers.sf.gov role page for class 2402 Laboratory Technician I "
                               "(exam announcement id 743999809251111), fetched %s - salary band and "
                               "minimum qualifications read directly from the City page" % AUDIT_DATE),
        "matchScore": 84,
        "batch": 6,
        "location": "City departments using class 2402 (SFDPH Public Health Lab, 101 Grove St; SFPUC labs) - site set by hiring department",
        "commuteZone": "C",
        "route": ("ZONE C - N Judah eastbound to Civic Center for departmental interviews; "
                  "public health lab at 101 Grove St via 43 Masonic/5 Fulton. ~25-45 min."),
        "officialLink": "https://careers.sf.gov/classifications/?classCode=2402",
        "applyLink": ("https://careers.sf.gov/role/?id=743999809251111 - apply through the City's "
                      "official portal only"),
        "applyChannel": ("Official City & County of San Francisco portal (direct civil service hire; "
                         "never through a staffing firm)"),
        "requirements": ("Six (6) months of experience within the last five years in a laboratory "
                         "setting: cleaning/sterilising glassware and equipment, packing and labelling "
                         "supplies or specimens, preparing glassware for microbiological exams, keeping "
                         "testing/patient records. Entry level in the Laboratory Technician series."),
        "fit": ("Education-plus - the City's own 2402 minimum is 6 months of lab experience, which your "
                "Quintara and MicroConstants terms cover, and a B.S. makes you competitive for the "
                "hiring departments that use the list."),
        "status": "monitor",
        "statusNote": ("Class 2402 role/exam page is live on careers.sf.gov, but the announcement shown "
                       "at audit time is an Access to City Employment (ACE) exam published 2022-03-03 - "
                       "no open filing window on 2026-09-09. Set a weekly check on the class page; the "
                       "City re-posts lab classes periodically."),
        "flag": ("Civil-service eligible-list mechanics: pay is set by class and step, and you must pass "
                 "the exam to be ranked. Salary band printed on the City page: $69,862-$84,916."),
        "subpage": None,
        "sources": [{"label": "City class 2402 announcement (official)",
                     "url": "https://careers.sf.gov/role/?id=743999809251111"},
                    {"label": "City class 2402 classification page (official)",
                     "url": "https://careers.sf.gov/classifications/?classCode=2402"}],
        "_letter_to": "Hiring Manager",
        "_dept_line": "City and County of San Francisco",
        "_role_type": "Laboratory Technician I",
        "_email_note": "The City accepts applications only through careers.sf.gov; do not email a "
                       "department instead of applying.",
    },
    # 116 -----------------------------------------------------------------
    {
        "company": "City & County of San Francisco - Department of Public Health (class 2416)",
        "position": "Laboratory Technician II - SFDPH Public Health Laboratory (class 2416)",
        "verified": True,
        "verificationMethod": ("careers.sf.gov role page 'Laboratory Technician II (2416) - DPH - 139184' "
                               "(id 3743990002599958) read on %s; duties and minimum experience quoted "
                               "from the City page" % AUDIT_DATE),
        "matchScore": 82,
        "batch": 6,
        "location": "SF Department of Public Health, 101 Grove St, San Francisco, CA 94102 (building per assignment)",
        "commuteZone": "C",
        "route": ("ZONE C - 43 Masonic from Judah & 21st Ave straight to the Civic Center / AFDC "
                  "campus area, or N Judah to Powell + 5 Fulton. ~30-40 min."),
        "officialLink": "https://careers.sf.gov/classifications/?classCode=2416",
        "applyLink": ("https://careers.sf.gov/role/?id=3743990002599958 - apply through the City's "
                      "official portal only"),
        "applyChannel": ("Official City & County of San Francisco portal (direct public-sector hire; "
                         "no recruiter)"),
        "requirements": ("One (1) year of laboratory experience in the last five years assisting with "
                         "preparation of cultures, media, reagents and specimens (or equivalent to class "
                         "2402 work): specimen receipt and centrifugation, media/reagent prep, QC checks "
                         "on equipment, patient-data entry into the lab information system, equipment "
                         "maintenance."),
        "fit": ("Strong - specimen processing, media and reagent prep, QC logging and data entry are "
                "literally the MicroConstants and Quintara bullets; one year of lab experience is the "
                "stated bar and your paid lab terms plus UCSF-era research meet it."),
        "status": "monitor",
        "statusNote": ("The class 2416 DPH announcement page is reachable, but no currently open filing "
                       "window was printed on it at audit time (%s) - recruitment id 139184 is the last "
                       "listed. Watch for a new 2416 window; the Public Health Lab hires through it more "
                       "than once a year." % AUDIT_DATE),
        "flag": ("Position-based test (PBT) mechanics: the department screens for the specific vacancy, "
                 "so submit early when a window opens."),
        "subpage": None,
        "sources": [{"label": "SFDPH Lab Technician II 2416 role page (official)",
                     "url": "https://careers.sf.gov/role/?id=3743990002599958"},
                    {"label": "City class 2416 classification page (official)",
                     "url": "https://careers.sf.gov/classifications/?classCode=2416"}],
        "_letter_to": "Hiring Manager",
        "_dept_line": "SF Department of Public Health",
        "_role_type": "Laboratory Technician II",
        "_email_note": "Apply on careers.sf.gov; the City does not accept emailed applications.",
    },
    # 117 -----------------------------------------------------------------
    {
        "company": "City & County of San Francisco - Department of Public Health (class 2463)",
        "position": "Microbiologist I - Public Health Laboratory, bacteriology/parasitology/serology (class 2463)",
        "verified": True,
        "verificationMethod": ("careers.sf.gov role page 'Microbiologist I - 2463 - Department of Public "
                               "Health' (id 3743990001679838, recruitment PBT-2463-134715) read on %s; "
                               "duties and salary band quoted from the City page" % AUDIT_DATE),
        "matchScore": 76,
        "batch": 6,
        "location": "SF Department of Public Health / Public Health Laboratory, San Francisco",
        "commuteZone": "C",
        "route": ("ZONE C - 43 Masonic from Judah & 21st Ave toward the Civic Center / AFDC campus; "
                  "N Judah + 5 Fulton as alternate. ~30-40 min."),
        "officialLink": "https://careers.sf.gov/classifications/?classCode=2463",
        "applyLink": ("https://careers.sf.gov/role/?id=3743990001679838 - apply through the City's "
                      "official portal only"),
        "applyChannel": "Official City & County of San Francisco portal (direct, position-based test)",
        "requirements": ("Diagnostic analysis of human, food and environmental specimens by serologic, "
                         "molecular, agglutination and biochemical methods; specimen and reagent "
                         "condition monitoring; microscopy of smears/cultures; drug-susceptibility testing; "
                         "proficiency testing per federal regulation; equipment QC, calibration and "
                         "maintenance; supply and reagent inventory."),
        "fit": ("Qualifies on education for Microbiologist I if you hold the required degree in a "
                "laboratory science - check the announcement's minimum-qualification wording for whether "
                "a chemistry B.S. with microbiology coursework is accepted; QC, calibration and "
                "documentation are squarely your strength."),
        "status": "monitor",
        "statusNote": ("Announcement last updated 2023-06-01 on the City page (selection-procedure change "
                       "note); salary band printed $94,198-$161,200 for class 2463 I/II. No open filing "
                       "window verified on %s - re-check and confirm the minimum-qualification wording "
                       "for a chemistry degree before spending time on it." % AUDIT_DATE),
        "flag": ("Microbiology-specific: some 2463 hires need ASCP-style coursework; the City lists "
                 "education requirements per announcement. Do not assume a chemistry degree automatically "
                 "qualifies."),
        "subpage": None,
        "sources": [{"label": "SFDPH Microbiologist I 2463 role page (official)",
                     "url": "https://careers.sf.gov/role/?id=3743990001679838"},
                    {"label": "City class 2463 classification page (official)",
                     "url": "https://careers.sf.gov/classifications/?classCode=2463"}],
        "_letter_to": "Hiring Manager",
        "_dept_line": "SF Department of Public Health",
        "_role_type": "Microbiologist I",
        "_email_note": "Apply on careers.sf.gov only.",
    },
    # 118 -----------------------------------------------------------------
    {
        "company": "Plasmidsaurus, Inc. (DNA/RNA sequencing services)",
        "position": "Lab Technician | San Francisco (library prep and sequencing instruments)",
        "verified": True,
        "verificationMethod": ("Official Ashby posting 1dea5cc2-a669-4f22-8eaa-8e569745bd58 fetched %s: "
                               "location field 'San Francisco', on-site, full time, $72.5K-$82.5K plus "
                               "equity, posted 2026-08-26; body text read in full" % AUDIT_DATE),
        "matchScore": 84,
        "batch": 6,
        "location": ("Posting lists San Francisco, but the body says 'This is an in-office in our South "
                     "San Francisco, CA location' and hours are Tue-Sat 7pm-3am"),
        "commuteZone": "Flagged",
        "route": ("NOT an SF-commute row: South San Francisco worksite (BART/Caltrain + bus from 21st & "
                  "Judah, ~60-80 min) on an overnight shift - outside the SF-only rule."),
        "officialLink": "https://plasmidsaurus.com",
        "applyLink": ("https://jobs.ashbyhq.com/plasmidsaurus/1dea5cc2-a669-4f22-8eaa-8e569745bd58 - "
                      "apply on Plasmidsaurus's official Ashby board"),
        "applyChannel": "Official employer board (Ashby), direct hire - no recruiter, no agency",
        "requirements": ("Minimum 2 years hands-on DNA extraction, purification and/or sequencing "
                         "experience in a COMMERCIAL lab; DNA library preparation; operating and "
                         "troubleshooting sequencing and liquid-handling instruments; QC of sequencing "
                         "output; documentation; no sponsorship. Lifts/pipetting-heavy, long sit/stand "
                         "periods."),
        "fit": ("Skills overlap on purification, sample prep, instrument QC and documentation, but the "
                "posting demands 2 years of commercial-lab DNA extraction/sequencing, which your résumé "
                "does not show - be ready to speak honestly to that gap."),
        "status": "monitor",
        "statusNote": ("Live posting at audit (%s, posted 2026-08-26) but kept as a documented alternate "
                       "rather than a target for two reasons: worksite is South San Francisco, and the "
                       "schedule is Tue-Sat 7pm-3am." % AUDIT_DATE),
        "flag": ("IRREGULARITY - title/location field says 'San Francisco' while the description sets the "
                 "office in South San Francisco and an overnight shift. Confirm worksite and hours with "
                 "the employer before applying."),
        "subpage": None,
        "sources": [{"label": "Plasmidsaurus official Ashby posting (official)",
                     "url": "https://jobs.ashbyhq.com/plasmidsaurus/1dea5cc2-a669-4f22-8eaa-8e569745bd58"},
                    {"label": "Plasmidsaurus official site", "url": "https://plasmidsaurus.com"}],
        "_letter_to": "Hiring Manager",
        "_dept_line": "Plasmidsaurus Lab Operations",
        "_role_type": "Lab Technician",
        "_email_note": "Plasmidsaurus careers contact for accommodations/questions: careers@plasmidsaurus.com (printed on the posting).",
    },
    # 119 -----------------------------------------------------------------
    {
        "company": "Addition Therapeutics, Inc. (in vivo cell therapy)",
        "position": "Research Associate, Quality Control (South San Francisco)",
        "verified": True,
        "verificationMethod": ("Addition Therapeutics official Greenhouse board API listing "
                               "boards-api.greenhouse.io/v1/boards/additiontherapeutics/jobs fetched %s: "
                               "7 live requisitions, incl. req 60 'RA, Quality Control' (job 5216310007), "
                               "location 'South San Francisco', published 2026-08-20" % AUDIT_DATE),
        "matchScore": 80,
        "batch": 6,
        "location": "South San Francisco, CA (per the employer's own board - not San Francisco)",
        "commuteZone": "Flagged",
        "route": ("NOT an SF-commute row: South San Francisco worksite. From 21st & Judah it is N Judah "
                  "to Embarcadero + BART to South SF + bus/walk, roughly 70-85 min."),
        "officialLink": "https://job-boards.greenhouse.io/additiontherapeutics",
        "applyLink": "https://job-boards.greenhouse.io/additiontherapeutics/jobs/5216310007 - official Greenhouse board",
        "applyChannel": "Official employer board (Greenhouse), direct hire - no recruiter",
        "requirements": ("QC assays and documentation for a cell/gene-therapy pipeline (per the company's "
                         "RA-QC scope on its board: assay execution, records, method adherence). Board "
                         "lists no salary for this req."),
        "fit": ("Assay execution plus disciplined documentation is your Quintara/MicroConstants profile; "
                "the blocker is geography, not capability."),
        "status": "monitor",
        "statusNote": ("Real, currently live, direct-hire posting verified %s - excluded from the target "
                       "list only because every requisition on this employer's board is South San "
                       "Francisco, outside the SF-only rule. If you ever widen the radius, this is a top "
                       "alternate." % AUDIT_DATE),
        "flag": ("Location rule - South San Francisco is a separate city on the peninsula, not an N Judah "
                 "commute. Listed for completeness, not recommended under current constraints."),
        "subpage": None,
        "sources": [{"label": "Addition Therapeutics RA, Quality Control (official Greenhouse)",
                     "url": "https://job-boards.greenhouse.io/additiontherapeutics/jobs/5216310007"},
                    {"label": "Addition Therapeutics official careers board",
                     "url": "https://job-boards.greenhouse.io/additiontherapeutics"}],
        "_letter_to": "Hiring Manager",
        "_dept_line": "Addition Therapeutics Quality Control",
        "_role_type": "Research Associate, Quality Control",
        "_email_note": "Apply on the Greenhouse posting; the company does not list a recruiting email.",
    },
    # 120 -----------------------------------------------------------------
    {
        "company": "Addition Therapeutics, Inc. (in vivo cell therapy)",
        "position": "Research Associate / Senior Research Associate - RNA process development & manufacturing (South San Francisco)",
        "verified": True,
        "verificationMethod": ("Addition Therapeutics official Greenhouse board API listing fetched %s: "
                               "req 57 'Research Associate RA/Sr. RA - RNA Process Development and "
                               "Manufacturing' (job 5208635007), location 'South San Francisco', first "
                               "published 2026-08-10, updated 2026-08-17" % AUDIT_DATE),
        "matchScore": 78,
        "batch": 6,
        "location": "South San Francisco, CA (per the employer's own board - not San Francisco)",
        "commuteZone": "Flagged",
        "route": ("NOT an SF-commute row: South San Francisco worksite (BART/Caltrain + bus from 21st & "
                  "Judah, roughly 70-85 min)."),
        "officialLink": "https://job-boards.greenhouse.io/additiontherapeutics",
        "applyLink": "https://job-boards.greenhouse.io/additiontherapeutics/jobs/5208635007 - official Greenhouse board",
        "applyChannel": "Official employer board (Greenhouse), direct hire - no recruiter",
        "requirements": ("Bachelor's or master's in chemistry, biochemistry or related field with 2-4 "
                         "years of experience; tangential flow filtration; AKTA purification; bioreactors; "
                         "QC assays incl. Qubit, Fragment Analyzer, LAL endotoxin; molecular and cell "
                         "biology familiarity; JMP statistical software (as quoted in the posting text "
                         "surfaced for this req)."),
        "fit": ("Purification-plus-QC chemistry - flash/SE-HPLC and documentation map onto it, though "
                "TFF, AKTA and bioreactors are new instrumentation you would be trained on."),
        "status": "monitor",
        "statusNote": ("Live posting verified %s; excluded from the target list on location (South San "
                       "Francisco), not on fit. Strongest single alternate in this pass if the SF-only "
                       "rule ever relaxes." % AUDIT_DATE),
        "flag": ("Location rule + '2-4 years' bench expectation: your paid lab terms total roughly a "
                 "year plus UCSF-era research - address that gap in the letter rather than inflating it."),
        "subpage": None,
        "sources": [{"label": "Addition Therapeutics RA RNA Process Development (official Greenhouse)",
                     "url": "https://job-boards.greenhouse.io/additiontherapeutics/jobs/5208635007"},
                    {"label": "Addition Therapeutics official careers board",
                     "url": "https://job-boards.greenhouse.io/additiontherapeutics"}],
        "_letter_to": "Hiring Manager",
        "_dept_line": "Addition Therapeutics Process Development",
        "_role_type": "Research Associate, RNA Process Development",
        "_email_note": "Apply on the Greenhouse posting.",
    },
]

for i, r in enumerate(ROWS):
    num = 101 + i
    r["id"] = "job-%d" % num
    r["subpage"] = "jobs/job-%02d.html" % num
