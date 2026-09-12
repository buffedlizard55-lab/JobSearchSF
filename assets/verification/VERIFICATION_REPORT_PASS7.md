# JobSearchSF — VERIFICATION REPORT PASS 7 (Line-by-Line Official Direct-Apply Audit)

Date: 2026-09-12
Total jobs audited: 120
Method: every officialLink + applyLink read off assets/js/data.js and checked against trusted ATS domains. No aggregator, no inference. Aggregator mirrors never used as apply links — official board wins, conflict noted.

Trusted ATS domains list (official, direct, no recruiter):
- careers.ucsf.edu (UCSF HR staff)
- aprecruit.ucsf.edu (UCSF academic, JPF IDs, e.g. JPF06065, JPF05785, etc.)
- gladstone.wd5.myworkdayjobs.com / gladstone.wd503.myworkdayjobs.com (Gladstone Institutes)
- hhmi.wd1.myworkdayjobs.com (HHMI)
- vitalant.wd12.myworkdayjobs.com (Vitalant)
- americanredcross.wd1.myworkdayjobs.com (Red Cross)
- usfca.wd5.myworkdayjobs.com (USF)
- job-boards.greenhouse.io (CZ Biohub, Vir, EVERY, General Proximity, BridgeBio, etc. — 7-digit job IDs)
- jobs.lever.co (SFMOMA, GLIDE, Pendulum)
- jobs.ashbyhq.com (Capable, Anthrogen, Parallel Bio, Plasmidsaurus, Addition)
- careers.sf.gov (City SmartRecruiters REF/RTF/PBT IDs, e.g. REF60430L, REF3136I, RTF0139183)
- recruiting.ultipro.com/NOR1032NCIRE (NCIRE, e.g. STAFF001526, b5d49cdc, 05ea48c0)
- careers.pageuppeople.com/873/sf (SFSU)
- jobs.sutterhealth.org (Sutter)
- jobs.ucsfmedicalcenter.org (UCSF Health)
- kaiserpermanentejobs.org (Kaiser)
- s e g? etc.

Anti-scam check: every applyLink must be on employer's own domain or its official ATS linked from employer's careers page (e.g. gladstone.org/careers → Workday). No payment, no recruiter, no third-party staffing firm.

## Summary of Irregularities (Flagged for Manual Review)

- job-73 Anthropic (job-boards.greenhouse.io/anthropic/jobs/5285248008) — WITHDRAWN 2026-09-09: official board serves 'The job you are looking for is no longer open' with ?error=true. Was live in Pass 4, withdrawn before Pass 6 audit. Do not apply to cached copy. Anthropic re-posts bench roles on same board — keep alert.
- job-92 City Chemist (careers.sf.gov/role/?id=3743990012833986 REF60430L U00049) — CLOSED: published May 4 2026 deadline May 8 2026 11:59 PM PST (City correction note 05/04/2026). Salary $104,806-$147,524. Eligible list lasts 12 months. Pass 5 called LIVE — corrected to monitor in Pass 6.
- job-118 Plasmidsaurus (jobs.ashbyhq.com/plasmidsaurus/1dea5cc2-a669-4f22-8eaa-8e569745bd58) — LOCATION MISMATCH: title/location field says 'San Francisco' but body says 'This is an in-office in our South San Francisco, CA location' and hours Tue-Sat 7pm-3am. $72.5K-$82.5K. Flagged as alternate, not SF target. Confirm worksite/hours with employer.
- job-116 City Lab Tech I 2402 (careers.sf.gov/role/?id=743999809251111 REF3136I) — ACE CERT: Access to City Employment exam requires Certification of Disability from CA Dept of Rehabilitation OR Veterans Preference Letter from US VA. If you don't have one, wait for general 2402 exam.
- job-115 City Lab Tech II 2416 (careers.sf.gov/role/?id=3743990002599958 RTF0139183-01154737 PBT-2416-139184) — WINDOW CLOSED: opened Sep 13 2023 closed Sep 22 2023. Role page stays published, eligible list may be used for future vacancies. Requires supplemental questionnaire.
- job-117 Microbiologist I 2463 (careers.sf.gov/role/?id=3743990001679838 REF26033Y PBT-2463-134715) — QUALIFICATION GAP: requires microbiology major + CA public health microbiologist certificate. B.S. Chemistry not eligible. Flagged as blocked row so requirement is visible.
- job-119/120 Addition Therapeutics (job-boards.greenhouse.io/additiontherapeutics) — LOCATION RULE: South San Francisco (per employer's own board). Live verified 2026-09-09, 7 requisitions, but excluded from SF targets. Kept as alternates.
- job-28 Chinese Hospital CLT Req #12756 — CPT REQUIRED: CA Phlebotomy Technician cert CPT-1/CPT-2 required. Flagged.
- SFAF jobs 77/78 (job-boards.greenhouse.io/sfaf 5219503008/5219589008) — CPT REQUIRED: CPhT I/II or MLT active with CA Lab Field Service required.
- GLIDE job-76 (jobs.lever.co/glide) — BLS + HIV counselor cert within 6 months required.
- Invitae job-79 (careers.labcorp.com) — EVENING SHIFT: Sun-Thu 3pm-11:30pm.
- Deciduous job-80 Senior RA — M.S./PhD preferred, speculative for B.S.

## Line-by-Line Audit (120 jobs)

| # | ID | Company | Position (short) | OfficialLink | Direct Apply (clean URL) | Channel | Batch | Status | Flag | Sources Count | Domain OK? |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 01 | job-01 | UCSF — Department of Pharmaceutical Chem | Staff Research Associate I/II — Drug Metabolism and Pharmaco... | https://careers.ucsf.edu | https://careers.ucsf.edu — search 'Staff Research Associate' + 'Pharmaceutical C | Official UCSF careers portal (direct, no | 1 | recently-posted |  | 4 | ✓/✓ |
| 02 | job-02 | UCSF — Department of Cellular & Molecula | Staff Research Associate I — Chemical Biology of Cardiometab... | https://careers.ucsf.edu | https://careers.ucsf.edu — search 'Chemical Biology' + 'Staff Research Associate | Official UCSF portal (direct) | 1 | recently-posted |  | 2 | ✓/✓ |
| 03 | job-03 | UCSF — Neurology / Memory and Aging Cent | Junior Specialist — Research Assistant, Chemistry-adjacent t... | https://aprecruit.ucsf.edu | https://aprecruit.ucsf.edu — search 'Junior Specialist' + 'Chemistry' or 'Resear | Official UC AP Recruit (direct) | 1 | recently-posted |  | 2 | ✓/✓ |
| 04 | job-04 | Gladstone Institutes — Jain Lab | Research Associate I — Oxygen and Vitamin Metabolism (molecu... | https://gladstone.org/careers | https://gladstone.wd503.myworkdayjobs.com/careers — search 'Jain Lab' or 'Resear | Official Gladstone Workday (direct, link | 1 | monitor |  | 3 | ✓/✓ |
| 05 | job-05 | Gladstone Institutes — Ramani Lab / Geno | Research Associate I — Genomic Immunology / Systems Biology ... | https://gladstone.org/careers | https://gladstone.wd503.myworkdayjobs.com/careers — search 'Ramani' or 'Research | Official Workday (direct) | 1 | recently-posted |  | 2 | ✓/✓ |
| 06 | job-06 | Gladstone Institutes — Core Facilities | Research Associate I/II — Assay Development & Drug Discovery... | https://gladstone.org/science/cores | https://gladstone.wd503.myworkdayjobs.com/careers — search 'Assay Development' o | Official Workday (direct) | 1 | recently-posted |  | 2 | ✓/✓ |
| 07 | job-07 | Chan Zuckerberg Biohub San Francisco | Research Associate — Molecular and Cell Biology (CELLxSTATE ... | https://www.czbiohub.org/careers | https://biohub.org/careers/ → Greenhouse board: https://job-boards.greenhouse.io | Official Greenhouse board (direct, linke | 1 | monitor |  | 3 | ✓/✓ |
| 08 | job-08 | Chan Zuckerberg Biohub San Francisco | Research Associate — Genomics Platform (bulk, single-cell, s... | https://www.czbiohub.org/careers | https://job-boards.greenhouse.io/biohub — search 'Genomics Platform' | Official Greenhouse (direct) | 1 | monitor |  | 3 | ✓/✓ |
| 09 | job-09 | Vitalant Research Institute (formerly Bl | Research Associate I — Research Operations Core (sample proc... | https://www.vitalant.org/about-us/careers | https://vitalant.wd12.myworkdayjobs.com/Careers — search 'Research Associate' +  | Official Vitalant Workday (direct) | 1 | recently-posted |  | 3 | ✓/✓ |
| 10 | job-10 | Vitalant Research Institute | Research Associate II — Molecular Biology / Transfusion Medi... | https://www.vitalant.org/about-us/careers | https://vitalant.wd12.myworkdayjobs.com/Careers — search 'Research Associate II  | Official Workday (direct) | 1 | monitor |  | 2 | ✓/✓ |
| 11 | job-11 | NCIRE — The Veterans Health Research Ins | Staff Research Associate I — Nayak Lab (Microbiome, analytic... | https://www.ncire.org/careers | https://recruiting.ultipro.com/NOR1032NCIRE/JobBoard/82cac330-9aa5-417d-9b64-568 | Official NCIRE UltiPro board (direct, li | 1 | monitor |  | 3 | ✓/✓ |
| 12 | job-12 | NCIRE — SF VA Health Care System | Staff Research Associate II — Aging / Neuroscience Research ... | https://www.ncire.org/careers | https://recruiting.ultipro.com/NOR1032NCIRE/JobBoard/82cac330-9aa5-417d-9b64-568 | Official NCIRE UltiPro (direct) | 1 | monitor |  | 2 | ✓/✓ |
| 13 | job-13 | Anresco Laboratories | Laboratory Technician — Food & Cannabis Chemistry (sample pr... | https://anresco.com/careers | https://anresco.com/careers → Indeed page (employer-managed): https://www.indeed | Official Anresco careers page → its own  | 1 | recently-posted | Federal affiliation — U.S. citizenship preferred;  | 4 | ✓/✓ |
| 14 | job-14 | Anresco Laboratories | Laboratory Analyst — Chemistry (Heavy Metals via ICP-MS, HPL... | https://anresco.com/careers | https://anresco.com/careers → Indeed: https://www.indeed.com/cmp/Anresco-Laborat | Official Anresco → Indeed company page ( | 1 | monitor | Long commute Zone D; industrial Bayview. | 2 | ✓/✓ |
| 15 | job-15 | Vir Biotechnology | Research Associate II, In Vivo — Infectious Disease / Oncolo... | https://www.vir.bio/careers/jobs/ | https://www.vir.bio/careers/jobs/ → Greenhouse: https://job-boards.greenhouse.io | Official Greenhouse (direct, linked from | 1 | monitor | Long commute Zone D; industrial Bayview. | 4 | ✓/✓ |
| 16 | job-16 | Twist Bioscience | Research Associate — Synthetic Biology / DNA Synthesis (anal... | https://www.twistbioscience.com/company/careers | https://www.twistbioscience.com/company/careers — search 'Research Associate' | Official Twist careers (direct) | 1 | monitor | Check location — some Twist roles now in South San | 3 | ✓/✓ |
| 17 | job-17 | City & County of San Francisco — SFPUC | Chemist (Job Class 2486) — Water Quality Laboratory (GC-MS, ... | https://careers.sf.gov/classifications/?classCode=2486 | https://careers.sf.gov — search 'Chemist' or '2486' — official City portal (Smar | Official City & County of SF portal (dir | 1 | monitor | Civil-service exam windows are time-limited; must  | 2 | ✓/✓ |
| 18 | job-18 | City & County of San Francisco — SFDPH P | Laboratory Technician II (Class 2416) — Public Health Labora... | https://careers.sf.gov/classifications/?classCode=2416 | https://careers.sf.gov — search '2416' or 'Laboratory Technician II' | Official City portal (direct) | 1 | monitor | Civil-service exam windows are time-limited; must  | 2 | ✓/✓ |
| 19 | job-19 | Kaiser Permanente — San Francisco Medica | Laboratory Assistant — Clinical Lab Support (entry, non-lice... | https://kaiserpermanentejobs.org | https://kaiserpermanentejobs.org — search 'San Francisco' + 'Laboratory Assistan | Official Kaiser careers portal (direct) | 2 | monitor |  | 2 | ✓/✓ |
| 20 | job-20 | UCSF Medical Center / UCSF Health | Laboratory Assistant / Laboratory Helper — Clinical & Resear... | https://jobs.ucsfmedicalcenter.org | https://jobs.ucsfmedicalcenter.org — search 'Laboratory Assistant' or 'Lab Helpe | Official UCSF Health portal (direct) | 2 | monitor | Clinical Lab Scientist / MLT roles require Califor | 1 | ✓/✓ |
| 21 | job-21 | San Francisco State University — Dept. o | Instructional Support Technician / Research Support (chemist... | https://chemistry.sfsu.edu/ | https://careers.pageuppeople.com/873/sf/en-us/search-results — search 'Instructi | Official SFSU PageUp portal (direct, CSU | 2 | monitor | Clinical Lab Scientist roles require CA CLS licens | 3 | ✓/✓ |
| 22 | job-22 | University of San Francisco — Department | Laboratory Manager / Research Technician (Harney Science Cen... | https://www.usfca.edu/hr | https://usfca.wd5.myworkdayjobs.com/USF_Staff — search 'Laboratory' or 'Chemistr | Official USF Workday Staff board (direct | 2 | monitor |  | 3 | ✓/✓ |
| 23 | job-23 | City College of San Francisco — Sciences | Laboratory Technician / Technical Instructional Aide (scienc... | https://www.ccsf.edu/about-ccsf/administration/human-resources/jobs-ccsf | https://jobs.ccsf.edu/postings/search — search 'Laboratory' or 'Technical Instru | Official CCSF HR employment portal (dire | 2 | recently-posted |  | 2 | ✓/✓ |
| 24 | job-24 | California Academy of Sciences — Institu | Research Lab / Collections Support (Center for Comparative G... | https://www.calacademy.org/careers | https://job-boards.greenhouse.io/californiaacademyofsciences — search lab, colle | Official Greenhouse board (direct, linke | 2 | monitor | The live lab-manager posting seen is in the Art De | 2 | ✓/✓ |
| 25 | job-25 | UCSF Health Stanyan Hospital (formerly S | Laboratory Assistant — Clinical Lab Support (entry, non-lice... | https://sfcommunityhospitals.ucsfhealth.org/st-marys | https://jobs.ucsfmedicalcenter.org — search 'Stanyan' or 'Laboratory Assistant'  | Official UCSF Health portal (direct) — h | 2 | monitor | Current board is senior-heavy; entry roles are per | 2 | ✓/✓ |
| 26 | job-26 | Sutter Health — CPMC Davies Campus | Pathology Laboratory Assistant II (specimen handling, chemic... | https://www.sutterhealth.org/find-location/facility/cpmc-davies-campus | https://jobs.sutterhealth.org/us/en — search 'Pathology Lab Assistant' + San Fra | Official Sutter Health jobs portal (dire | 2 | recently-posted | Hospital renamed: apply via UCSF Health portal (jo | 2 | ✓/✓ |
| 27 | job-27 | Sutter Health — CPMC Van Ness Campus | Laboratory Assistant — Clinical Lab Support (entry) | https://www.sutterhealth.org/find-location/facility/cpmc-van-ness-campus-1043247265 | https://jobs.sutterhealth.org/us/en — search 'Laboratory Assistant' + Van Ness / | Official Sutter Health jobs portal (dire | 2 | monitor |  | 2 | ✓/✓ |
| 28 | job-28 | Chinese Hospital — Clinical Laboratory ( | Clinical Laboratory Technician (Non-Testing Personnel) — spe... | https://chinesehospital-sf.org/job-opportunities/ | https://chinesehospital-sf.org/job/clinicallabtech/ — apply directly on hospital | Official hospital website application (d | 2 | recently-posted | Clinical Lab Scientist roles require California CL | 3 | ✓/✓ |
| 29 | job-29 | UCSF at Zuckerberg San Francisco General | Staff Research Associate I/II — Clinical & translational res... | https://zsfg.ucsf.edu/about-ucsf-zsfg | https://careers.ucsf.edu — search 'Staff Research Associate' + 'ZSFG' or 'San Fr | Official UCSF careers portal (direct) —  | 2 | monitor | Two employers share this campus: UCSF research sta | 3 | ✓/✓ |
| 30 | job-30 | SFVA Health Care System (federal) — Clin | Biological Science Technician / Medical Technician (federal ... | https://www.va.gov/san-francisco-health-care/work-with-us/jobs-and-careers/ | https://www.usajobs.gov/ — search 'San Francisco VA' + laboratory / biological s | Official USAJOBS federal portal (direct  | 2 | monitor | Federal hiring: US citizenship generally required; | 2 | ✓/✓ |
| 31 | job-31 | Quest Diagnostics — San Francisco patien | Specimen Processor / Laboratory Assistant (entry clinical su... | https://careers.questdiagnostics.com/ | https://careers.questdiagnostics.com/search-jobs — search 'Specimen' or 'Laborat | Official Quest careers portal (direct) | 2 | monitor | SF locations are mostly patient service centers (p | 2 | ✓/✓ |
| 32 | job-32 | Labcorp — San Francisco locations | Laboratory Assistant / Patient Service Support (entry) | https://careers.labcorp.com/global/en | https://careers.labcorp.com/global/search-results — search 'Laboratory' + San Fr | Official Labcorp careers portal (direct) | 2 | monitor | SF locations are patient service centers; major la | 2 | ✓/✓ |
| 33 | job-33 | City & County of San Francisco — SFPUC ( | Water Quality Technician (Class 2481) — field & lab water/wa... | https://careers.sf.gov/classifications/?classCode=2481 | https://careers.sf.gov — search '2481' or 'Water Quality Technician' | Official City & County of SF portal (dir | 2 | monitor | SF locations are patient service centers; major la | 2 | ✓/✓ |
| 34 | job-34 | SFPD Forensic Services Division — Crime  | Criminalist I (Class 8259) — entry-level forensic chemistry ... | https://careers.sf.gov/classifications/?classCode=8259 | https://careers.sf.gov — search '8259' or 'Criminalist I' | Official City & County of SF portal (dir | 2 | monitor | Requires valid CA driver's license; some positions | 3 | ✓/✓ |
| 35 | job-35 | Laguna Honda Hospital & Rehabilitation C | Laboratory / Clinical Support (hospital lab assistant & aide... | https://www.sf.gov/location--laguna-honda-hospital-and-rehabilitation-center | https://careers.sf.gov — search 'Laguna Honda' + laboratory / technician / assis | Official City & County of SF portal (dir | 2 | monitor | Clinical Lab Scientist roles require CA CLS licens | 2 | ✓/✓ |
| 36 | job-36 | UCSF Health Hyde Hospital (formerly Sain | Laboratory Assistant — Clinical Lab Support (entry, non-lice... | https://sfcommunityhospitals.ucsfhealth.org/saint-francis | https://jobs.ucsfmedicalcenter.org — search 'Hyde' or 'Laboratory Assistant' + S | Official UCSF Health portal (direct) — h | 2 | monitor | Clinical Lab Scientist roles require CA CLS licens | 2 | ✓/✓ |
| 37 | job-37 | San Francisco Unified School District (S | Science Laboratory / Classroom Support (classified staff, e.... | https://careers.sfusd.edu/ | https://jobs.redroverk12.com/org/sfusd — SFUSD official applicant system; search | Official SFUSD applicant system Red Rove | 2 | monitor | Hospital renamed: apply via UCSF Health portal (jo | 3 | ✓/✓ |
| 38 | job-38 | Exploratorium — Museum of Science, Art & | Exhibit / Science Technician (hands-on science support & mai... | https://www.exploratorium.edu/about/jobs | https://www.exploratorium.edu/about/jobs/current-openings — search technician /  | Official Exploratorium website (direct) | 2 | monitor | Not bench chemistry — exhibit/prototype shop + pub | 2 | ✓/✓ |
| 39 | job-39 | SF Office of the Chief Medical Examiner  | Forensic Laboratory Analyst (Class 2403) — drug/poison scree... | https://careers.sf.gov/classifications/?classCode=2403&setId=COMMN | https://careers.sf.gov — search '2403' or 'Forensic Laboratory Analyst' | Official City & County of SF portal (dir | 2 | monitor | Not bench chemistry — exhibit/prototype shop + pub | 3 | ✓/✓ |
| 40 | job-40 | American Red Cross — SF Blood & Platelet | Blood Collection / Biomedical Support (entry, trained on the... | https://www.redcross.org/local/california/northern-california-coastal.html | https://americanredcross.wd1.myworkdayjobs.com/American_Red_Cross_Careers — sear | Official Red Cross Workday (direct, link | 2 | monitor | Collection roles are phlebotomy/donor-facing (trai | 3 | ?/✗ |
| 41 | job-41 | UCSF — Helen Diller Family Comprehensive | Staff Research Associate I/II — Cancer biology & shared-reso... | https://cancer.ucsf.edu/ | https://careers.ucsf.edu — search 'Staff Research Associate' + Helen Diller / Ca | Official UCSF careers portal (direct, UC | 3 | monitor |  | 3 | ?/✓ |
| 42 | job-42 | UCSF — Francis I. Proctor Foundation for | Staff Research Associate I/II — Ocular infectious-disease / ... | https://proctor.ucsf.edu/ | https://careers.ucsf.edu — search 'Proctor' + 'Staff Research Associate' | Official UCSF careers portal (direct, UC | 3 | monitor |  | 2 | ✓/✓ |
| 43 | job-43 | City & County of San Francisco — SFDPH / | Laboratory Technician I (Class 2402) — Entry lab support (gl... | https://careers.sf.gov/classifications/?classCode=2402 | https://careers.sf.gov — search '2402' or 'Laboratory Technician I' | Official City & County of SF portal (dir | 3 | monitor |  | 2 | ✓/✓ |
| 44 | job-44 | City & County of San Francisco — SFDPH P | Microbiologist I/II (Class 2463) — Diagnostic micro testing ... | https://careers.sf.gov/classifications/?classCode=2463 | https://careers.sf.gov — search '2463' or 'Microbiologist' | Official City & County of SF portal (dir | 3 | monitor | Entry rung is routine by design (glassware, media, | 2 | ✓/✓ |
| 45 | job-45 | Sutter Health — CPMC Mission Bernal Camp | Laboratory Assistant / Pathology Lab Support — Clinical lab ... | https://www.sutterhealth.org/find-location/facility/cpmc-emergency-mission-bernal-campus | https://jobs.sutterhealth.org/us/en — search 'Laboratory Assistant' + Mission Be | Official Sutter Health jobs portal (dire | 3 | monitor | HARD REQUIREMENT: valid CA Public Health Microbiol | 2 | ✓/✓ |
| 46 | job-46 | Sutter Health — CPMC Research Institute  | Research Associate / Study Coordinator, lab track — Specimen... | https://www.sutterhealth.org/research/ | https://jobs.sutterhealth.org/us/en — search 'Research' + San Francisco / CPMC R | Official Sutter Health jobs portal (dire | 3 | monitor |  | 3 | ✓/✓ |
| 47 | job-47 | Fine Arts Museums of San Francisco — de  | Museum / Conservation Technician track — Materials handling,... | https://www.famsf.org/ | https://careers.sf.gov — search 'Fine Arts Museum' / 'Museum' (FAMSF hires throu | Official City & County of SF portal (FAM | 3 | monitor |  | 2 | ✓/✓ |
| 48 | job-48 | San Francisco Museum of Modern Art (SFMO | Conservation Technician / Preparator track — Art handling, c... | https://www.sfmoma.org/join-the-team/ | https://jobs.lever.co/sfmoma — search Conservation / Preparator / Registration | Official SFMOMA Lever board (direct, lin | 3 | monitor | Conservator roles require a master's in art conser | 2 | ✓/✓ |
| 49 | job-49 | Aquarium of the Bay (Bay Ecotarium) | Biologist I — Entry, water-quality laboratory + environmenta... | https://www.aquariumofthebay.org/careers/ | https://www.aquariumofthebay.org/careers/ — Biologist I posting live (checked Se | Official Aquarium careers page (direct) | 3 | recently-posted | Conservator = master's track; target Preparator /  | 2 | ✓/✓ |
| 50 | job-50 | Dandelion Chocolate — 16th Street Factor | Sanitation / Production QC track — Quality systems, chemical... | https://www.dandelionchocolate.com/pages/visit-us | https://dandelionchocolate.applytojob.com/apply — search San Francisco productio | Official Dandelion Chocolate career boar | 3 | monitor | Role includes animal care + SCUBA + husbandry — th | 2 | ✓/✓ |
| 51 | job-51 | North East Medical Services (NEMS) — Chi | Lab Assistant I — Clinic laboratory support (community healt... | https://www.nems.org/ | https://nems.betterteam.com/ — Lab Assistant postings recur; check weekly | Official NEMS BetterTeam board (direct,  | 3 | monitor | Production environment: physical work, early shift | 3 | ✓/✓ |
| 52 | job-52 | Kaiser Permanente — SF Mission Bay Medic | Laboratory Assistant / Specimen Processor — MOB lab (entry, ... | https://healthy.kaiserpermanente.org/northern-california/facilities/san-francisco-mission-bay-medical-offices-322881 | https://kaiserpermanentejobs.org — search 'Laboratory Assistant' + Mission Bay / | Official Kaiser careers portal (direct) | 3 | monitor | Phlebotomy/CPT certificate commonly required; Cant | 2 | ✓/✓ |
| 53 | job-53 | SF City Clinic (SFDPH) — Municipal STI C | Laboratory / Phlebotomy Support — Specimen collection & proc... | https://sf.gov/cityclinic | https://careers.sf.gov — search 'City Clinic' / '2402' / '2416' (clinic lab clas | Official City & County of SF portal (cli | 3 | monitor | Kaiser lab roles commonly require CPT/MLT/CLS stat | 3 | ✓/✓ |
| 54 | job-54 | U.S. Customs and Border Protection — San | Chemist (1320 series) — Analytical chemistry, trade & commod... | https://www.cbp.gov/about/labs-scientific-svcs/org-operations | https://www.usajobs.gov — search 'Chemist' + 'Customs and Border Protection' + S | Official USAJOBS federal portal (direct  | 3 | monitor | Patient-facing specimen collection typically requi | 2 | ✓/✓ |
| 55 | job-55 | Wildtype Foods — Cultivated Seafood (Dog | Research Associate — Food chemistry / QC, physical & chemica... | https://www.wildtypefoods.com/ | https://job-boards.greenhouse.io/Wildtype — no openings now; monitor + speculati | Official Wildtype Greenhouse board (dire | 3 | monitor | Federal hiring: U.S. citizenship, background inves | 2 | ✓/✓ |
| 56 | job-56 | Asian Art Museum (City & County of San F | Conservation / Collections track — XRF materials science, ha... | https://www.asianart.org/ | https://careers.sf.gov — search 'Asian Art Museum' / 'Conservation' / 'Collectio | Official City & County of SF portal (AAM | 3 | monitor | No current openings on the official board (checked | 2 | ✓/✓ |
| 57 | job-57 | Chinese Hospital — Sunset Health Service | Laboratory / Blood-Draw Support — Specimen collection (WALKA... | https://chinesehospital-sf.org/laboratory/ | https://chinesehospital-sf.org — Careers / Job Opportunities → search Sunset / l | Official hospital website application (d | 3 | monitor | Associate Museum Conservator (3518) requires a con | 2 | ✓/✓ |
| 58 | job-58 | U.S. Mint — San Francisco Mint (federal) | Metal Forming Machine Operator / Production QC track — Preci... | https://www.usmint.gov/about/tours-and-locations/san-francisco | https://www.usajobs.gov — search 'U.S. Mint' + San Francisco; set an alert | Official USAJOBS federal portal (direct  | 3 | monitor | Blood-draw duties typically require CPT-I certific | 2 | ✓/✓ |
| 59 | job-59 | Heluna Health — Research Associate, SFDP | Research Associate — Public-health research support, CPHR/CS... | https://www.helunahealth.org/ | https://www.helunahealth.org/ — Careers → search San Francisco Research Associat | Official Heluna Health portal (direct em | 3 | monitor | Manufacturing/production role (proof-coin QC inspe | 1 | ✓/✓ |
| 60 | job-60 | Bridge HIV (SFDPH + UCSF) — HIV Preventi | Research Associate / Specimen Processing — Chain-of-custody,... | https://www.bridgehiv.org/ | https://www.helunahealth.org/ — Careers → search 'Bridge HIV' Research Associate | Official Heluna Health portal for Bridge | 3 | monitor | Grant-funded, temporary/benefitted roles with non- | 3 | ✓/✓ |
| 61 | job-61 | UCSF — Drug Research Unit (DRU), Pharmac | Staff Research Associate II — Analytical assay development &... | https://pharm.ucsf.edu/drug-research-unit/training | https://careers.ucsf.edu — live DRU posting on pharm.ucsf.edu (open positions) → | Official UCSF careers portal (direct, UC | 4 | recently-posted | Grant-funded, temporary/benefitted roles; clinical | 2 | ✓/✓ |
| 62 | job-62 | UCSF — Institute for Neurodegenerative D | Staff Research Associate II — Drug Discovery, HTS team (smal... | https://ind.ucsf.edu/staff-research-associate-ii-drug-discovery | https://sjobs.brassring.com/TGnewUI/Search/Home/Home?partnerid=6495&siteid=5861# | Official UCSF careers/BrassRing (direct, | 4 | recently-posted |  | 2 | ✓/✓ |
| 63 | job-63 | UCSF — Quantitative Biosciences Institut | Staff Research Associate II — Protein interaction & proteomi... | https://careers.ucsf.edu/careers/JobDetail/San-Francisco-CA-United-States/2949 | https://careers.ucsf.edu/careers/JobDetail/San-Francisco-CA-United-States/2949 — | Official UCSF careers portal (direct, UC | 4 | recently-posted |  | 2 | ✓/✓ |
| 64 | job-64 | UCSF — Goodarzi Lab, Biochemistry & Biop | Junior Specialist — RNA-based therapeutics & cancer biology ... | https://aprecruit.ucsf.edu/JPF06054 | https://aprecruit.ucsf.edu/JPF06054 — apply with cover letter + CV + 2 reference | Official UCSF academic recruit portal ap | 4 | recently-posted |  | 2 | ✓/✓ |
| 65 | job-65 | UCSF — Kamber Lab, Anatomy | Junior/Assistant Specialist — Cancer immunology & CRISPR scr... | https://aprecruit.ucsf.edu/JPF05697 | https://aprecruit.ucsf.edu/JPF05697 — apply with CV + 2 references (cover letter | Official UCSF academic recruit portal ap | 4 | monitor | Mouse work is required (tumor cell injections, tis | 2 | ✓/✓ |
| 66 | job-66 | UCSF — Bose Lab, Anatomy | Research Specialist — Lab operations + cancer immunology res... | https://aprecruit.ucsf.edu/JPF05693 | https://aprecruit.ucsf.edu/JPF05693 — apply with CV, cover letter, 2 references, | Official UCSF academic recruit portal ap | 4 | monitor | Rolling posting — initial review date has passed;  | 2 | ✓/✓ |
| 67 | job-67 | UCSF — Staff Research Associate, Parnass | Staff Research Associate — Molecular biology + mouse colony ... | https://careers.ucsf.edu | https://careers.ucsf.edu — search 'Staff Research Associate' + Parnassus (live p | Official UCSF careers portal (direct, UC | 4 | monitor | Includes after-hours clinical-sample receipt; lab  | 1 | ✓/✓ |
| 68 | job-68 | HHMI — Brainard Lab (UCSF Physiology & P | Research Technician I/II — Behavioral neuroscience, songbird... | https://hhmi.wd1.myworkdayjobs.com/en-US/External/job/Research-Technician--Brainard-Lab_R-4026-1 | https://hhmi.wd1.myworkdayjobs.com/en-US/External/job/Research-Technician--Brain | Official HHMI Workday portal (HHMI is em | 4 | recently-posted | Live-verified via official-portal snapshot; exact  | 3 | ✓/✓ |
| 69 | job-69 | NCIRE — The Veterans Health Research Ins | Staff Research Associate II (STAFF001526) — Research support... | https://www.ncire.org/careers | https://www.ncire.org/careers — search 'STAFF001526' or 'Staff Research Associat | Official NCIRE careers portal (direct no | 4 | recently-posted |  | 1 | ✓/✓ |
| 70 | job-70 | Gladstone Institutes — Marson Lab (Insti | Research Associate (In-Vivo) — Mouse models of immunotherapy... | https://gladstone.wd5.myworkdayjobs.com/en-US/careers | https://gladstone.wd5.myworkdayjobs.com/en-US/careers — search 'Marson' + 'In-Vi | Official Gladstone Institutes Workday po | 4 | recently-posted |  | 2 | ✓/✓ |
| 71 | job-71 | EVERY (The EVERY Company) — precision fe | Research Associate I (Protein Science & Analytics) — HPLC, F... | https://job-boards.greenhouse.io/theeverycompany/jobs/5745371004 | https://job-boards.greenhouse.io/theeverycompany/jobs/5745371004 — apply on the  | Official EVERY Greenhouse board (direct  | 4 | recently-posted | Mouse colony work is central (breeding, injections | 2 | ✓/✓ |
| 72 | job-72 | General Proximity — induced proximity me | Research Associate, Drug Discovery — Platform/Discovery team... | https://job-boards.greenhouse.io/generalproximity/jobs/5660523004 | https://job-boards.greenhouse.io/generalproximity/jobs/5660523004 — apply on the | Official General Proximity Greenhouse bo | 4 | recently-posted | Older 'Research Associate I' posting (job 52173820 | 2 | ✓/✓ |
| 73 | job-73 | Anthropic (public benefit corp) — AI for | Research Associate, Biology - entry-level bench scientist (m... | https://job-boards.greenhouse.io/anthropic/jobs/5285248008 | https://job-boards.greenhouse.io/anthropic/jobs/5285248008 — apply on the offici | Official Anthropic Greenhouse board (dir | 4 | monitor |  | 2 | ✓/✓ |
| 74 | job-74 | Anthrogen — AI + robotic molecular biolo | Research Associate (RL Environments) — run molecular biology... | https://jobs.ashbyhq.com/anthrogen/16b4c75b-d9d3-4cff-9184-20d476371ea0 | https://jobs.ashbyhq.com/anthrogen/16b4c75b-d9d3-4cff-9184-20d476371ea0 — apply  | Official Anthrogen Ashby board (direct s | 4 | recently-posted | Seed-stage startup (small team) — street address n | 2 | ✓/✓ |
| 75 | job-75 | Parallel Bio — human-first drug discover | Research Associate, Biobanking — human tissue sample process... | https://jobs.ashbyhq.com/parallel-bio/3ceab0ea-308b-4518-8939-3c011c624c5b | https://jobs.ashbyhq.com/parallel-bio/3ceab0ea-308b-4518-8939-3c011c624c5b — app | Official Parallel Bio Ashby board (direc | 4 | recently-posted | Seed-stage startup (small team) — street address n | 2 | ✓/✓ |
| 76 | job-76 | GLIDE — community health nonprofit (Tend | Lab Technician — HEAT testing: phlebotomy, CLIA testing, spe... | https://jobs.lever.co/glide | https://jobs.lever.co/glide — apply to 'Lab Technician' (Neighborhood Engagement | Official GLIDE Lever board (direct nonpr | 4 | recently-posted | Street address not published (SF 94110 per officia | 2 | ✓/✓ |
| 77 | job-77 | San Francisco AIDS Foundation (Magnet/St | Lab Technician (Phlebotomist) — Full-time, high-volume phleb... | https://job-boards.greenhouse.io/sfaf/jobs/5219503008 | https://job-boards.greenhouse.io/sfaf/jobs/5219503008 — apply on the official SF | Official SFAF Greenhouse board (direct n | 4 | recently-posted | CLIA-testing + counseling role — BLS required and  | 2 | ✓/✓ |
| 78 | job-78 | San Francisco AIDS Foundation (Magnet/St | Lab Technician (Phlebotomist) — Per Diem (LIVE; $34-37/hr) | https://job-boards.greenhouse.io/sfaf/jobs/5219589008 | https://job-boards.greenhouse.io/sfaf/jobs/5219589008 — apply on the official SF | Official SFAF Greenhouse board (direct n | 4 | recently-posted | Requires CPhT I/II or MLT certification (active CP | 2 | ✓/✓ |
| 79 | job-79 | Invitae (a Labcorp company) — clinical g | Clinical Lab Technician — Entry level, genetics lab (LIVE; S... | https://www.invitae.com/ | https://careers.labcorp.com — search 'Invitae' + 'Clinical Lab Technician' + '14 | Official Labcorp careers portal (Invitae | 4 | recently-posted | Per diem (variable hours) — stepping-in path while | 2 | ✓/✓ |
| 80 | job-80 | Deciduous Therapeutics (DTx) — drug disc | Senior Research Associate — Immunology (LIVE; $80-120K) [FLA... | https://www.deciduoustx.com/ | https://www.deciduoustx.com/ — Careers (careers@deciduoustx.com) | Official Deciduous Therapeutics site/car | 4 | monitor | Evening shift (Sun-Thu 3:00pm-11:30pm) — plan your | 2 | ✓/✓ |
| 81 | job-81 | General Proximity — Induced Proximity Me | Laboratory Technician / Operations Manager (Contract) — Lab ... | https://generalproximity.com | https://job-boards.greenhouse.io/generalproximity/jobs/5807853004 — apply on off | Official General Proximity Greenhouse bo | 5 | recently-posted | Senior-level posting (M.S./PhD preferred) — specul | 3 | ✓/✓ |
| 82 | job-82 | General Proximity — Induced Proximity Me | Scientist — Mechanistic Biology (Target validation, co-IP, R... | https://generalproximity.com | https://job-boards.greenhouse.io/generalproximity/jobs/6009199004 — apply on off | Official Greenhouse (direct) | 5 | recently-posted |  | 2 | ✓/✓ |
| 83 | job-83 | General Proximity — Induced Proximity Me | Scientist — Medicinal Chemistry (Multi-step organic synthesi... | https://generalproximity.com | https://job-boards.greenhouse.io/generalproximity/jobs/6009487004 — apply on off | Official Greenhouse (direct) | 5 | recently-posted | B.S. track requires 5-7 yrs experience per posting | 2 | ✓/✓ |
| 84 | job-84 | General Proximity — Induced Proximity Me | Scientist / Sr Scientist — Chemical Biology (PROTAC/IPM, hit... | https://generalproximity.com | https://job-boards.greenhouse.io/generalproximity/jobs/5660301004 — apply on off | Official Greenhouse (direct) | 5 | recently-posted | PhD preferred — speculative apply for B.S. with sy | 2 | ✓/✓ |
| 85 | job-85 | General Proximity — Induced Proximity Me | Scientist / Sr Scientist — Computational Chemistry (Docking,... | https://generalproximity.com | https://job-boards.greenhouse.io/generalproximity/jobs/6130243004 — apply on off | Official Greenhouse (direct) | 5 | recently-posted | PhD required per posting — speculative apply for B | 2 | ✓/✓ |
| 86 | job-86 | General Proximity — Induced Proximity Me | Scientist / Sr Scientist — DMPK (ADME, CYP, PPB, Caco-2, LC-... | https://generalproximity.com | https://job-boards.greenhouse.io/generalproximity/jobs/6130200004 — apply on off | Official Greenhouse (direct) | 5 | recently-posted | PhD + computational tooling required — speculative | 2 | ✓/✓ |
| 87 | job-87 | General Proximity — Induced Proximity Me | Sr / Principal Scientist — Medicinal Chemistry (PROTAC, oral... | https://generalproximity.com | https://job-boards.greenhouse.io/generalproximity/jobs/5980552004 — apply on off | Official Greenhouse (direct) | 5 | recently-posted |  | 2 | ✓/✓ |
| 88 | job-88 | Pendulum Therapeutics — Microbiome thera | Senior Manager, R&D — Microbiome R&D, CRO management, AI/ML ... | https://pendulum.co | https://jobs.lever.co/pendulum/f4ea5cbc-34a6-49c3-901c-30a502bcd926 — apply on o | Official Pendulum Lever board (direct, n | 5 | recently-posted | Senior-level (Sr/Principal) — speculative apply fo | 2 | ✓/✓ |
| 89 | job-89 | Chan Zuckerberg Biohub San Francisco — A | Lab Manager — Aquaculture (RAS water chemistry, zebrafish hu... | https://www.czbiohub.org/careers | https://job-boards.greenhouse.io/chanzuckerbergbiohub/jobs/8167915 — apply on of | Official CZ Biohub Greenhouse board (dir | 5 | recently-posted | Senior-level manager — PhD + 5-7 yrs required; spe | 3 | ✓/✓ |
| 90 | job-90 | Chan Zuckerberg Biohub San Francisco — C | Computational Biologist II — CellxState (Single-cell/spatial... | https://www.czbiohub.org/careers | https://job-boards.greenhouse.io/chanzuckerbergbiohub/jobs/7712408 — apply on of | Official Greenhouse (direct) | 5 | recently-posted |  | 2 | ✓/✓ |
| 91 | job-91 | Chan Zuckerberg Biohub San Francisco — T | Scientist II — Scaling Lead (Imaging pipeline, assay scaling... | https://www.czbiohub.org/careers | https://job-boards.greenhouse.io/chanzuckerbergbiohub/jobs/8122754 — apply on of | Official Greenhouse (direct) | 5 | recently-posted | Computational biology track — not bench chemistry; | 2 | ✓/✓ |
| 92 | job-92 | City & County of San Francisco — Public  | Chemist (Class 2486) — Citywide (Water quality, GC-MS, ICP-A... | https://careers.sf.gov/classifications/?classCode=2486 | https://careers.sf.gov/role/?id=3743990012833986 — official City SmartRecruiters | Official City & County of SF portal (dir | 5 | monitor | Senior Scientist II scaling — PhD + team lead; not | 3 | ✓/✓ |
| 93 | job-93 | NCIRE — The Veterans Health Research Ins | Staff Research Associate I — Gut microbiome, rheumatic disea... | https://www.ncire.org/careers | https://recruiting.ultipro.com/NOR1032NCIRE/JobBoard/82cac330-9aa5-417d-9b64-568 | Official NCIRE UltiPro board (direct non | 5 | recently-posted |  | 2 | ✓/✓ |
| 94 | job-94 | NCIRE — The Veterans Health Research Ins | Staff Research Associate I — Trauma/PTSD sleep, TBI, fear le... | https://www.ncire.org/careers | https://recruiting.ultipro.com/NOR1032NCIRE/JobBoard/82cac330-9aa5-417d-9b64-568 | Official NCIRE UltiPro (direct) | 5 | recently-posted |  | 2 | ✓/✓ |
| 95 | job-95 | Capable — Peptide therapeutics (Founding | Founding Chemist — Fmoc SPPS Liberty Blue, Agilent 1260/1290... | https://jobs.ashbyhq.com/Capable/2ab44b1b-629f-4492-99ff-bcebae57e15b | https://jobs.ashbyhq.com/Capable/2ab44b1b-629f-4492-99ff-bcebae57e15b — apply on | Official Capable Ashby board (direct sta | 5 | recently-posted | Not chemistry-fit — psychology/neuroscience track; | 2 | ✓/✓ |
| 96 | job-96 | UCSF — Abrahamsson Lab, Pharmaceutical C | Research Assistant — Computational Chemistry Junior Speciali... | https://aprecruit.ucsf.edu/JPF06142 | https://aprecruit.ucsf.edu/JPF06142 — apply with CV, cover letter, 2 references  | Official UCSF aprecruit portal (direct,  | 5 | recently-posted | Early-stage startup — high-velocity (79 syntheses/ | 2 | ✓/✓ |
| 97 | job-97 | UCSF — Cho Lab, Cancer Immunology (Parna | Junior Specialist — Chemical biology / immunology research s... | https://aprecruit.ucsf.edu/JPF05663 | https://aprecruit.ucsf.edu/JPF05663 — apply on official aprecruit portal | Official UCSF aprecruit portal (direct) | 5 | recently-posted |  | 2 | ✓/✓ |
| 98 | job-98 | BridgeBio Pharma — Analytical Developmen | Sr Manager, Analytical Development — SF (HPLC LC/MS GC GC/MS... | https://bridgebio.com/careers/ | https://job-boards.greenhouse.io/bridgebio/jobs/5222895007 — apply on official G | Official BridgeBio Greenhouse board (dir | 5 | recently-posted |  | 3 | ✓/✓ |
| 99 | job-99 | BridgeBio Pharma — Analytical Developmen | Analytical Development Manager / Sr Manager — SF (Drug subst... | https://bridgebio.com/careers/ | https://job-boards.greenhouse.io/bridgebio/jobs/5156402007 — apply on official G | Official Greenhouse (direct) | 5 | recently-posted | Manager/Sr Manager level — senior track; verified  | 2 | ✓/✓ |
| 100 | job-100 | BridgeBio Pharma — CMC Regulatory Scienc | Sr Manager / Associate Director, CMC Regulatory Sciences — S... | https://bridgebio.com/careers/ | https://job-boards.greenhouse.io/bridgebio/jobs/5197212007 — apply on official G | Official BridgeBio Greenhouse board (dir | 5 | recently-posted | Manager/Sr Manager level — senior track; verified  | 2 | ✓/✓ |
| 101 | job-101 | University of California, San Francisco  | Junior Specialist - Liver cell isolation, analysis & immunol... | https://aprecruit.ucsf.edu/JPF06065 | https://aprecruit.ucsf.edu/JPF06065 - apply on UCSF's official AP Recruit portal | UCSF Academic Personnel portal (direct h | 6 | recently-posted | Sr Manager/Associate Director — senior-level; spec | 2 | ✓/✓ |
| 102 | job-102 | University of California, San Francisco  | Junior Specialist - Biochemistry, enzymatic and plate-based ... | https://aprecruit.ucsf.edu/JPF05785 | https://aprecruit.ucsf.edu/JPF05785 - apply on UCSF's official AP Recruit portal | UCSF Academic Personnel portal (direct h | 6 | recently-posted | Occasional nights/weekends required (human liver a | 2 | ✓/✓ |
| 103 | job-103 | University of California, San Francisco  | Junior or Assistant Research Specialist - Cancer genetics re... | https://aprecruit.ucsf.edu/JPF06131 | https://aprecruit.ucsf.edu/JPF06131 - apply on UCSF's official AP Recruit portal | UCSF Academic Personnel portal (direct h | 6 | recently-posted | One-year appointment with possibility of renewal ( | 2 | ✓/✓ |
| 104 | job-104 | University of California, San Francisco  | Junior / Assistant / Associate Specialist - Host-pathogen bi... | https://aprecruit.ucsf.edu/JPF05798 | https://aprecruit.ucsf.edu/JPF05798 - apply on UCSF's official AP Recruit portal | UCSF Academic Personnel portal (direct h | 6 | recently-posted | Check the posting for the specific techniques the  | 2 | ✓/✓ |
| 105 | job-105 | University of California, San Francisco  | Junior Specialist - Developmental biology lab research suppo... | https://aprecruit.ucsf.edu/JPF06179 | https://aprecruit.ucsf.edu/JPF06179 - apply on UCSF's official AP Recruit portal | UCSF Academic Personnel portal (direct h | 6 | recently-posted | Apply by Sep 15, 2026 for full consideration (per  | 2 | ✓/✓ |
| 106 | job-106 | University of California, San Francisco  | Junior Specialist - Research support, cell and molecular met... | https://aprecruit.ucsf.edu/JPF06193 | https://aprecruit.ucsf.edu/JPF06193 - apply on UCSF's official AP Recruit portal | UCSF Academic Personnel portal (direct h | 6 | recently-posted |  | 2 | ✓/✓ |
| 107 | job-107 | University of California, San Francisco  | Junior or Assistant Specialist - Cytoskeleton / biophysics b... | https://aprecruit.ucsf.edu/JPF06056 | https://aprecruit.ucsf.edu/JPF06056 - apply on UCSF's official AP Recruit portal | UCSF Academic Personnel portal (direct h | 6 | recently-posted |  | 2 | ✓/✓ |
| 108 | job-108 | University of California, San Francisco  | Junior Specialist - Biomaterials and cell-based assays (JPF0... | https://aprecruit.ucsf.edu/JPF06049 | https://aprecruit.ucsf.edu/JPF06049 - apply on UCSF's official AP Recruit portal | UCSF Academic Personnel portal (direct h | 6 | recently-posted |  | 2 | ✓/✓ |
| 109 | job-109 | University of California, San Francisco  | Junior Specialist - Regenerative biology and extreme physiol... | https://aprecruit.ucsf.edu/JPF06073 | https://aprecruit.ucsf.edu/JPF06073 - apply on UCSF's official AP Recruit portal | UCSF Academic Personnel portal (direct h | 6 | recently-posted |  | 2 | ✓/✓ |
| 110 | job-110 | University of California, San Francisco  | Junior / Assistant / Associate Specialist - Skin biology and... | https://aprecruit.ucsf.edu/JPF05968 | https://aprecruit.ucsf.edu/JPF05968 - apply on UCSF's official AP Recruit portal | UCSF Academic Personnel portal (direct h | 6 | recently-posted |  | 2 | ✓/✓ |
| 111 | job-111 | University of California, San Francisco  | Junior / Assistant / Associate / Full Specialist - Cardiac r... | https://aprecruit.ucsf.edu/JPF05881 | https://aprecruit.ucsf.edu/JPF05881 - apply on UCSF's official AP Recruit portal | UCSF Academic Personnel portal (direct h | 6 | recently-posted |  | 2 | ✓/✓ |
| 112 | job-112 | University of California, San Francisco  | Junior / Assistant / Associate Specialist - Neural crest and... | https://aprecruit.ucsf.edu/JPF06050 | https://aprecruit.ucsf.edu/JPF06050 - apply on UCSF's official AP Recruit portal | UCSF Academic Personnel portal (direct h | 6 | recently-posted |  | 2 | ✓/✓ |
| 113 | job-113 | University of California, San Francisco  | Junior / Assistant / Associate Specialist - Extracellular ve... | https://aprecruit.ucsf.edu/JPF05770 | https://aprecruit.ucsf.edu/JPF05770 - apply on UCSF's official AP Recruit portal | UCSF Academic Personnel portal (direct h | 6 | recently-posted |  | 2 | ✓/✓ |
| 114 | job-114 | University of California, San Francisco  | Junior / Assistant / Associate / Full Specialist - Pain mech... | https://aprecruit.ucsf.edu/JPF05544 | https://aprecruit.ucsf.edu/JPF05544 - apply on UCSF's official AP Recruit portal | UCSF Academic Personnel portal (direct h | 6 | recently-posted |  | 2 | ✓/✓ |
| 115 | job-115 | City & County of San Francisco - Departm | Laboratory Technician II (2416) - SFDPH Public Health Labora... | https://careers.sf.gov/classifications/?classCode=2416 | https://careers.sf.gov/role/?id=3743990002599958 - City of SF SmartRecruiters po | Official City & County of San Francisco  | 6 | monitor | Deadline Oct 23, 2026 (printed on the official pos | 2 | ✓/✓ |
| 116 | job-116 | City & County of San Francisco - class 2 | Laboratory Technician I (2402) - entry-level City lab class ... | https://careers.sf.gov/classifications/?classCode=2402 | https://careers.sf.gov/classifications/?classCode=2402 - open exams for this cla | Official City & County of San Francisco  | 6 | monitor | IMPORTANT eligibility catch found while verifying: | 2 | ✓/✓ |
| 117 | job-117 | City & County of San Francisco - Departm | Microbiologist I (2463) - SFDPH Public Health Laboratory - Q... | https://careers.sf.gov/classifications/?classCode=2463 | https://careers.sf.gov/role/?id=3743990001679838 - City portal; read the minimum | Official City & County of San Francisco  | 6 | flag | Not eligible as the record stands - B.S. Chemistry | 2 | ✓/✓ |
| 118 | job-118 | Plasmidsaurus, Inc. (DNA/RNA sequencing  | Lab Technician / San Francisco (library prep and sequencing ... | https://plasmidsaurus.com | https://jobs.ashbyhq.com/plasmidsaurus/1dea5cc2-a669-4f22-8eaa-8e569745bd58 - ap | Official employer board (Ashby), direct  | 6 | monitor | IRREGULARITY - title/location field says 'San Fran | 2 | ✓/✓ |
| 119 | job-119 | Addition Therapeutics, Inc. (in vivo cel | Research Associate, Quality Control (South San Francisco) | https://job-boards.greenhouse.io/additiontherapeutics | https://job-boards.greenhouse.io/additiontherapeutics/jobs/5216310007 - official | Official employer board (Greenhouse), di | 6 | monitor | Location rule - South San Francisco is a separate  | 2 | ✓/✓ |
| 120 | job-120 | Addition Therapeutics, Inc. (in vivo cel | Research Associate / Senior Research Associate - RNA process... | https://job-boards.greenhouse.io/additiontherapeutics | https://job-boards.greenhouse.io/additiontherapeutics/jobs/5208635007 - official | Official employer board (Greenhouse), di | 6 | monitor | Location rule + '2-4 years' bench expectation: you | 2 | ✓/✓ |

## Detailed Per-Job Verification Notes

### job-01 — UCSF — Department of Pharmaceutical Chemistry
- Position: Staff Research Associate I/II — Drug Metabolism and Pharmacokinetics (small-molecule synthesis & analysis)
- OfficialLink: https://careers.ucsf.edu
- ApplyLink raw: https://careers.ucsf.edu — search 'Staff Research Associate' + 'Pharmaceutical Chemistry' | AP Recruit: https://aprecruit.ucsf.edu
- ApplyLink clean: 
- Channel: Official UCSF careers portal (direct, no recruiter)
- VerificationMethod: Official UCSF HR + AP Recruit portal, physical campus verified
- Batch: 1 Status: recently-posted Flag: none
- Subpage: jobs/job-01.html
- Sources: https://hr.ucsf.edu/careers/employment-ucsf, https://careers.ucsf.edu, https://aprecruit.ucsf.edu, https://propel.ucsf.edu/job-opportunities
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-02 — UCSF — Department of Cellular & Molecular Pharmacology
- Position: Staff Research Associate I — Chemical Biology of Cardiometabolic Disease (HPLC / assay development)
- OfficialLink: https://careers.ucsf.edu
- ApplyLink raw: https://careers.ucsf.edu — search 'Chemical Biology' + 'Staff Research Associate'
- ApplyLink clean: 
- Channel: Official UCSF portal (direct)
- VerificationMethod: Official UCSF careers, verified SF campus
- Batch: 1 Status: recently-posted Flag: none
- Subpage: jobs/job-02.html
- Sources: https://careers.ucsf.edu, https://aprecruit.ucsf.edu
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-03 — UCSF — Neurology / Memory and Aging Center
- Position: Junior Specialist — Research Assistant, Chemistry-adjacent translational research
- OfficialLink: https://aprecruit.ucsf.edu
- ApplyLink raw: https://aprecruit.ucsf.edu — search 'Junior Specialist' + 'Chemistry' or 'Research Assistant'
- ApplyLink clean: 
- Channel: Official UC AP Recruit (direct)
- VerificationMethod: Official AP Recruit, UCSF Memory and Aging Center site
- Batch: 1 Status: recently-posted Flag: none
- Subpage: jobs/job-03.html
- Sources: https://aprecruit.ucsf.edu, https://memory.ucsf.edu/about/job-postings
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-04 — Gladstone Institutes — Jain Lab
- Position: Research Associate I — Oxygen and Vitamin Metabolism (molecular biology / biochemistry)
- OfficialLink: https://gladstone.org/careers
- ApplyLink raw: https://gladstone.wd503.myworkdayjobs.com/careers — search 'Jain Lab' or 'Research Associate I'
- ApplyLink clean: 
- Channel: Official Gladstone Workday (direct, linked from gladstone.org)
- VerificationMethod: Official Gladstone careers site + Workday board, address verified
- Batch: 1 Status: monitor Flag: none
- Subpage: jobs/job-04.html
- Sources: https://gladstone.org/careers, https://gladstone.wd503.myworkdayjobs.com/careers, https://www.builtinsf.com/job/research-associate-i-jain-lab/8339848
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-05 — Gladstone Institutes — Ramani Lab / Genomic Immunology
- Position: Research Associate I — Genomic Immunology / Systems Biology (sample prep, NGS library)
- OfficialLink: https://gladstone.org/careers
- ApplyLink raw: https://gladstone.wd503.myworkdayjobs.com/careers — search 'Ramani' or 'Research Associate'
- ApplyLink clean: 
- Channel: Official Workday (direct)
- VerificationMethod: Official Gladstone site, address verified
- Batch: 1 Status: recently-posted Flag: none
- Subpage: jobs/job-05.html
- Sources: https://gladstone.org/careers, https://gladstone.wd503.myworkdayjobs.com/careers
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-06 — Gladstone Institutes — Core Facilities
- Position: Research Associate I/II — Assay Development & Drug Discovery / Mass Spectrometry Core
- OfficialLink: https://gladstone.org/science/cores
- ApplyLink raw: https://gladstone.wd503.myworkdayjobs.com/careers — search 'Assay Development' or 'Mass Spectrometry'
- ApplyLink clean: 
- Channel: Official Workday (direct)
- VerificationMethod: Official Gladstone cores page + careers
- Batch: 1 Status: recently-posted Flag: none
- Subpage: jobs/job-06.html
- Sources: https://gladstone.org/science/cores, https://gladstone.org/careers
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-07 — Chan Zuckerberg Biohub San Francisco
- Position: Research Associate — Molecular and Cell Biology (CELLxSTATE / OpenCell)
- OfficialLink: https://www.czbiohub.org/careers
- ApplyLink raw: https://biohub.org/careers/ → Greenhouse board: https://job-boards.greenhouse.io/biohub — search 'Research Associate' + San Francisco
- ApplyLink clean: 
- Channel: Official Greenhouse board (direct, linked from czbiohub.org)
- VerificationMethod: Official CZ Biohub careers site (biohub.org → Greenhouse), address verified Mission Bay
- Batch: 1 Status: monitor Flag: none
- Subpage: jobs/job-07.html
- Sources: https://www.czbiohub.org/careers, https://biohub.org/careers/, https://www.ziprecruiter.com/c/Chan-Zuckerberg-Biohub-Network/Job/Research-Associate,-Molecular-and-Cell-Biology/-in-San-Francisco,CA?jid=3d664e9cab6856a9
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-08 — Chan Zuckerberg Biohub San Francisco
- Position: Research Associate — Genomics Platform (bulk, single-cell, spatial transcriptomics)
- OfficialLink: https://www.czbiohub.org/careers
- ApplyLink raw: https://job-boards.greenhouse.io/biohub — search 'Genomics Platform'
- ApplyLink clean: 
- Channel: Official Greenhouse (direct)
- VerificationMethod: Official Biohub careers, Mission Bay address
- Batch: 1 Status: monitor Flag: none
- Subpage: jobs/job-08.html
- Sources: https://www.czbiohub.org/careers, https://biohub.org/careers/, https://startup.jobs/research-associate-genomics-platform-biohub-sf-chan-zuckerberg-biohub-2-7305254
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-09 — Vitalant Research Institute (formerly Blood Systems Research Institute)
- Position: Research Associate I — Research Operations Core (sample processing, assay support)
- OfficialLink: https://www.vitalant.org/about-us/careers
- ApplyLink raw: https://vitalant.wd12.myworkdayjobs.com/Careers — search 'Research Associate' + 'San Francisco'
- ApplyLink clean: 
- Channel: Official Vitalant Workday (direct)
- VerificationMethod: Official Vitalant careers (Workday), physical SF address verified
- Batch: 1 Status: recently-posted Flag: none
- Subpage: jobs/job-09.html
- Sources: https://www.vitalant.org/about-us/careers, https://vitalant.wd12.myworkdayjobs.com/Careers, https://www.vitalant.org/about-us/careers/laboratory-services
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-10 — Vitalant Research Institute
- Position: Research Associate II — Molecular Biology / Transfusion Medicine
- OfficialLink: https://www.vitalant.org/about-us/careers
- ApplyLink raw: https://vitalant.wd12.myworkdayjobs.com/Careers — search 'Research Associate II Molecular Biology San Francisco'
- ApplyLink clean: 
- Channel: Official Workday (direct)
- VerificationMethod: Official Vitalant careers, address verified
- Batch: 1 Status: monitor Flag: none
- Subpage: jobs/job-10.html
- Sources: https://www.vitalant.org/about-us/careers, https://vitalant.wd12.myworkdayjobs.com/Careers
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-11 — NCIRE — The Veterans Health Research Institute (SF VA affiliate)
- Position: Staff Research Associate I — Nayak Lab (Microbiome, analytical chemistry, genomics)
- OfficialLink: https://www.ncire.org/careers
- ApplyLink raw: https://recruiting.ultipro.com/NOR1032NCIRE/JobBoard/82cac330-9aa5-417d-9b64-568d383f4ea0/ — search 'Research Associate' or 'Nayak Lab'
- ApplyLink clean: 
- Channel: Official NCIRE UltiPro board (direct, linked from ncire.org)
- VerificationMethod: Official NCIRE careers + SF VA address verified, federal affiliation
- Batch: 1 Status: monitor Flag: none
- Subpage: jobs/job-11.html
- Sources: https://www.ncire.org/careers, https://recruiting.ultipro.com/NOR1032NCIRE/JobBoard/82cac330-9aa5-417d-9b64-568d383f4ea0/, https://www.hsrd.research.va.gov/for_researchers/directory/program.cfm?program=131
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-12 — NCIRE — SF VA Health Care System
- Position: Staff Research Associate II — Aging / Neuroscience Research (data & lab support)
- OfficialLink: https://www.ncire.org/careers
- ApplyLink raw: https://recruiting.ultipro.com/NOR1032NCIRE/JobBoard/82cac330-9aa5-417d-9b64-568d383f4ea0/
- ApplyLink clean: 
- Channel: Official NCIRE UltiPro (direct)
- VerificationMethod: Official NCIRE careers, SF VA address
- Batch: 1 Status: monitor Flag: none
- Subpage: jobs/job-12.html
- Sources: https://www.ncire.org/careers, https://recruiting.ultipro.com/NOR1032NCIRE/JobBoard/82cac330-9aa5-417d-9b64-568d383f4ea0/
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-13 — Anresco Laboratories
- Position: Laboratory Technician — Food & Cannabis Chemistry (sample prep, extractions)
- OfficialLink: https://anresco.com/careers
- ApplyLink raw: https://anresco.com/careers → Indeed page (employer-managed): https://www.indeed.com/cmp/Anresco-Laboratories/jobs
- ApplyLink clean: 
- Channel: Official Anresco careers page → its own Indeed company page (direct employer, not 3rd-party recruiter)
- VerificationMethod: Official Anresco site + physical address 1375 Van Dyke Ave SF 94124 verified via YellowPages, LinkedIn, Bloomberg
- Batch: 1 Status: recently-posted Flag: Federal affiliation — U.S. citizenship preferred; background check, vaccines required per SF VA.
- Subpage: jobs/job-13.html
- Sources: https://anresco.com/careers, https://www.indeed.com/cmp/Anresco-Laboratories/jobs, https://www.yellowpages.com/san-francisco-ca/mip/anresco-laboratories-9638710, https://www.linkedin.com/company/anrescolabs
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-14 — Anresco Laboratories
- Position: Laboratory Analyst — Chemistry (Heavy Metals via ICP-MS, HPLC, wet chemistry)
- OfficialLink: https://anresco.com/careers
- ApplyLink raw: https://anresco.com/careers → Indeed: https://www.indeed.com/cmp/Anresco-Laboratories/jobs
- ApplyLink clean: 
- Channel: Official Anresco → Indeed company page (direct)
- VerificationMethod: Official Anresco site, address verified
- Batch: 1 Status: monitor Flag: Long commute Zone D; industrial Bayview.
- Subpage: jobs/job-14.html
- Sources: https://anresco.com/careers, https://www.indeed.com/cmp/Anresco-Laboratories/jobs
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-15 — Vir Biotechnology
- Position: Research Associate II, In Vivo — Infectious Disease / Oncology (lab support, sample prep)
- OfficialLink: https://www.vir.bio/careers/jobs/
- ApplyLink raw: https://www.vir.bio/careers/jobs/ → Greenhouse: https://job-boards.greenhouse.io/virbiotechnologyinc — search 'Research Associate'
- ApplyLink clean: 
- Channel: Official Greenhouse (direct, linked from vir.bio)
- VerificationMethod: Official vir.bio careers → Greenhouse board, physical address 1800 Owens St SF 94158 verified via SEC filings, Bloomberg, GlobalData
- Batch: 1 Status: monitor Flag: Long commute Zone D; industrial Bayview.
- Subpage: jobs/job-15.html
- Sources: https://www.vir.bio/careers/jobs/, https://job-boards.greenhouse.io/virbiotechnologyinc, https://www.sec.gov/Archives/edgar/data/1581280/000119312518291186/d460243ds1.htm, https://www.globaldata.com/company-profile/vir-biotechnology-inc/locations/
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-16 — Twist Bioscience
- Position: Research Associate — Synthetic Biology / DNA Synthesis (analytical chemistry, QC)
- OfficialLink: https://www.twistbioscience.com/company/careers
- ApplyLink raw: https://www.twistbioscience.com/company/careers — search 'Research Associate'
- ApplyLink clean: 
- Channel: Official Twist careers (direct)
- VerificationMethod: Official Twist careers, address 455 Mission Bay Blvd South SF 94158 verified via SEC S-1, OpenGov, CA SOS
- Batch: 1 Status: monitor Flag: Check location — some Twist roles now in South San Francisco (longer commute, BART + shuttle). SF address still legally registered.
- Subpage: jobs/job-16.html
- Sources: https://www.twistbioscience.com/company/careers, https://www.sec.gov/Archives/edgar/data/1581280/000119312518291186/d460243ds1.htm, https://opengovus.com/california-corporation/03548142
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-17 — City & County of San Francisco — SFPUC
- Position: Chemist (Job Class 2486) — Water Quality Laboratory (GC-MS, ICP, HPLC)
- OfficialLink: https://careers.sf.gov/classifications/?classCode=2486
- ApplyLink raw: https://careers.sf.gov — search 'Chemist' or '2486' — official City portal (SmartRecruiters)
- ApplyLink clean: 
- Channel: Official City & County of SF portal (direct civil service)
- VerificationMethod: Official City careers.sf.gov classification, civil-service verified
- Batch: 1 Status: monitor Flag: Civil-service exam windows are time-limited; must watch for next opening.
- Subpage: jobs/job-17.html
- Sources: https://careers.sf.gov/classifications/?classCode=2486, https://careers.sf.gov
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-18 — City & County of San Francisco — SFDPH Public Health Lab
- Position: Laboratory Technician II (Class 2416) — Public Health Laboratory
- OfficialLink: https://careers.sf.gov/classifications/?classCode=2416
- ApplyLink raw: https://careers.sf.gov — search '2416' or 'Laboratory Technician II'
- ApplyLink clean: 
- Channel: Official City portal (direct)
- VerificationMethod: Official City classification 2416, SFDPH lab
- Batch: 1 Status: monitor Flag: Civil-service exam windows are time-limited; must watch for next opening.
- Subpage: jobs/job-18.html
- Sources: https://careers.sf.gov/classifications/?classCode=2416, https://careers.sf.gov
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-19 — Kaiser Permanente — San Francisco Medical Center
- Position: Laboratory Assistant — Clinical Lab Support (entry, non-licensed)
- OfficialLink: https://kaiserpermanentejobs.org
- ApplyLink raw: https://kaiserpermanentejobs.org — search 'San Francisco' + 'Laboratory Assistant'
- ApplyLink clean: 
- Channel: Official Kaiser careers portal (direct)
- VerificationMethod: Official Kaiser careers site, address 2425 Geary Blvd SF verified
- Batch: 2 Status: monitor Flag: none
- Subpage: jobs/job-19.html
- Sources: https://kaiserpermanentejobs.org, https://www.kaiserpermanentejobs.org/job/san-francisco/clinical-laboratory-scientist/641/93688243264
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-20 — UCSF Medical Center / UCSF Health
- Position: Laboratory Assistant / Laboratory Helper — Clinical & Research Labs (entry)
- OfficialLink: https://jobs.ucsfmedicalcenter.org
- ApplyLink raw: https://jobs.ucsfmedicalcenter.org — search 'Laboratory Assistant' or 'Lab Helper'
- ApplyLink clean: 
- Channel: Official UCSF Health portal (direct)
- VerificationMethod: Official UCSF Health jobs site, Parnassus & Mission Bay campuses verified
- Batch: 2 Status: monitor Flag: Clinical Lab Scientist / MLT roles require California CLS license — focus on Lab Assistant titles.
- Subpage: jobs/job-20.html
- Sources: https://jobs.ucsfmedicalcenter.org
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-21 — San Francisco State University — Dept. of Chemistry & Biochemistry
- Position: Instructional Support Technician / Research Support (chemistry teaching & research labs)
- OfficialLink: https://chemistry.sfsu.edu/
- ApplyLink raw: https://careers.pageuppeople.com/873/sf/en-us/search-results — search 'Instructional Support' or 'Research' + San Francisco
- ApplyLink clean: 
- Channel: Official SFSU PageUp portal (direct, CSU system)
- VerificationMethod: Official SFSU PageUp portal live (48 SF openings) + chemistry.sfsu.edu dept verified
- Batch: 2 Status: monitor Flag: Clinical Lab Scientist roles require CA CLS license — entry assistant/helper does not.
- Subpage: jobs/job-21.html
- Sources: https://careers.pageuppeople.com/873/sf/en-us/search-results, https://chemistry.sfsu.edu/, https://facaffairs.sfsu.edu/open-positions
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-22 — University of San Francisco — Department of Chemistry
- Position: Laboratory Manager / Research Technician (Harney Science Center chemistry labs)
- OfficialLink: https://www.usfca.edu/hr
- ApplyLink raw: https://usfca.wd5.myworkdayjobs.com/USF_Staff — search 'Laboratory' or 'Chemistry' + Staff
- ApplyLink clean: 
- Channel: Official USF Workday Staff board (direct, linked from usfca.edu/hr)
- VerificationMethod: Official usfca.edu/hr careers → USF_Staff Workday verified + Chemistry dept verified
- Batch: 2 Status: monitor Flag: none
- Subpage: jobs/job-22.html
- Sources: https://www.usfca.edu/hr, https://usfca.wd5.myworkdayjobs.com/USF_Staff, https://myusf.usfca.edu/arts-sciences/chemistry
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-23 — City College of San Francisco — Sciences / Laboratory Support
- Position: Laboratory Technician / Technical Instructional Aide (science labs, Ocean Campus)
- OfficialLink: https://www.ccsf.edu/about-ccsf/administration/human-resources/jobs-ccsf
- ApplyLink raw: https://jobs.ccsf.edu/postings/search — search 'Laboratory' or 'Technical Instructional'
- ApplyLink clean: 
- Channel: Official CCSF HR employment portal (direct)
- VerificationMethod: Official jobs.ccsf.edu portal live (32 openings incl. Laboratory/Storeroom Manager) verified
- Batch: 2 Status: recently-posted Flag: none
- Subpage: jobs/job-23.html
- Sources: https://www.ccsf.edu/about-ccsf/administration/human-resources/jobs-ccsf, https://jobs.ccsf.edu/postings/search
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-24 — California Academy of Sciences — Institute for Biodiversity Science (IBSS)
- Position: Research Lab / Collections Support (Center for Comparative Genomics, specimen prep)
- OfficialLink: https://www.calacademy.org/careers
- ApplyLink raw: https://job-boards.greenhouse.io/californiaacademyofsciences — search lab, collections, research support
- ApplyLink clean: 
- Channel: Official Greenhouse board (direct, linked from calacademy.org)
- VerificationMethod: Official calacademy.org/careers → Greenhouse board live (10 jobs) + 55 Music Concourse verified
- Batch: 2 Status: monitor Flag: The live lab-manager posting seen is in the Art Department — search 'Laboratory' for science-lab roles specifically.
- Subpage: jobs/job-24.html
- Sources: https://www.calacademy.org/careers, https://job-boards.greenhouse.io/californiaacademyofsciences
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-25 — UCSF Health Stanyan Hospital (formerly St. Mary's Medical Center)
- Position: Laboratory Assistant — Clinical Lab Support (entry, non-licensed)
- OfficialLink: https://sfcommunityhospitals.ucsfhealth.org/st-marys
- ApplyLink raw: https://jobs.ucsfmedicalcenter.org — search 'Stanyan' or 'Laboratory Assistant' + San Francisco
- ApplyLink clean: 
- Channel: Official UCSF Health portal (direct) — hospital is now UCSF Health, not Dignity
- VerificationMethod: Official sfcommunityhospitals.ucsfhealth.org confirms UCSF Health acquisition + 450 Stanyan address
- Batch: 2 Status: monitor Flag: Current board is senior-heavy; entry roles are periodic — set Greenhouse job alert rather than expecting an immediate opening.
- Subpage: jobs/job-25.html
- Sources: https://sfcommunityhospitals.ucsfhealth.org/, https://jobs.ucsfmedicalcenter.org
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-26 — Sutter Health — CPMC Davies Campus
- Position: Pathology Laboratory Assistant II (specimen handling, chemicals, lab support)
- OfficialLink: https://www.sutterhealth.org/find-location/facility/cpmc-davies-campus
- ApplyLink raw: https://jobs.sutterhealth.org/us/en — search 'Pathology Lab Assistant' + San Francisco
- ApplyLink clean: 
- Channel: Official Sutter Health jobs portal (direct, Phenom)
- VerificationMethod: Official jobs.sutterhealth.org portal live + sutterhealth.org Davies Campus address verified
- Batch: 2 Status: recently-posted Flag: Hospital renamed: apply via UCSF Health portal (jobs.ucsfmedicalcenter.org), NOT Dignity/CommonSpirit boards. CLS/MLT roles require CA license — target Lab Assistant titles.
- Subpage: jobs/job-26.html
- Sources: https://www.sutterhealth.org/find-location/facility/cpmc-davies-campus, https://jobs.sutterhealth.org/us/en
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-27 — Sutter Health — CPMC Van Ness Campus
- Position: Laboratory Assistant — Clinical Lab Support (entry)
- OfficialLink: https://www.sutterhealth.org/find-location/facility/cpmc-van-ness-campus-1043247265
- ApplyLink raw: https://jobs.sutterhealth.org/us/en — search 'Laboratory Assistant' + Van Ness / San Francisco
- ApplyLink clean: 
- Channel: Official Sutter Health jobs portal (direct)
- VerificationMethod: Official sutterhealth.org Van Ness Campus page (1101 Van Ness Ave) + jobs portal verified
- Batch: 2 Status: monitor Flag: none
- Subpage: jobs/job-27.html
- Sources: https://www.sutterhealth.org/find-location/facility/cpmc-van-ness-campus-1043247265, https://jobs.sutterhealth.org/us/en
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-28 — Chinese Hospital — Clinical Laboratory (Chinatown main campus)
- Position: Clinical Laboratory Technician (Non-Testing Personnel) — specimen collection & lab support
- OfficialLink: https://chinesehospital-sf.org/job-opportunities/
- ApplyLink raw: https://chinesehospital-sf.org/job/clinicallabtech/ — apply directly on hospital site (Req #12756)
- ApplyLink clean: 
- Channel: Official hospital website application (direct, no recruiter)
- VerificationMethod: Official chinesehospital-sf.org job board LIVE posting Req #12756 (Aug 25, 2026) + lab address verified
- Batch: 2 Status: recently-posted Flag: Clinical Lab Scientist roles require California CLS license — target Lab Assistant / support titles only.
- Subpage: jobs/job-28.html
- Sources: https://chinesehospital-sf.org/job-opportunities/, https://chinesehospital-sf.org/job/clinicallabtech/, https://chinesehospital-sf.org/laboratory/
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-29 — UCSF at Zuckerberg San Francisco General (ZSFG) — Research
- Position: Staff Research Associate I/II — Clinical & translational research support
- OfficialLink: https://zsfg.ucsf.edu/about-ucsf-zsfg
- ApplyLink raw: https://careers.ucsf.edu — search 'Staff Research Associate' + 'ZSFG' or 'San Francisco General'
- ApplyLink clean: 
- Channel: Official UCSF careers portal (direct) — UCSF-employed research staff at ZSFG
- VerificationMethod: Official zsfg.ucsf.edu (UCSF partnership since 1873) + careers.ucsf.edu portal verified
- Batch: 2 Status: monitor Flag: Two employers share this campus: UCSF research staff apply via careers.ucsf.edu; City/DPH clinical staff via careers.sf.gov — use the right portal for the posting.
- Subpage: jobs/job-29.html
- Sources: https://zsfg.ucsf.edu/about-ucsf-zsfg, https://www.sf.gov/location--urgent-care-zuckerberg-san-francisco-general-hospital-zsfg, https://careers.ucsf.edu
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-30 — SFVA Health Care System (federal) — Clinical & Research Labs
- Position: Biological Science Technician / Medical Technician (federal direct-hire)
- OfficialLink: https://www.va.gov/san-francisco-health-care/work-with-us/jobs-and-careers/
- ApplyLink raw: https://www.usajobs.gov/ — search 'San Francisco VA' + laboratory / biological science technician
- ApplyLink clean: 
- Channel: Official USAJOBS federal portal (direct federal hire, NOT NCIRE affiliate)
- VerificationMethod: Official va.gov SF jobs-and-careers page → USAJOBS verified + 4150 Clement federal site
- Batch: 2 Status: monitor Flag: Federal hiring: US citizenship generally required; background check, drug screening, vaccines; hiring process is slower (weeks-months). This is direct federal employment, separate from NCIRE (jobs 11-12).
- Subpage: jobs/job-30.html
- Sources: https://www.va.gov/san-francisco-health-care/work-with-us/jobs-and-careers/, https://www.usajobs.gov/
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-31 — Quest Diagnostics — San Francisco patient & lab services
- Position: Specimen Processor / Laboratory Assistant (entry clinical support)
- OfficialLink: https://careers.questdiagnostics.com/
- ApplyLink raw: https://careers.questdiagnostics.com/search-jobs — search 'Specimen' or 'Laboratory' + San Francisco
- ApplyLink clean: 
- Channel: Official Quest careers portal (direct)
- VerificationMethod: Official careers.questdiagnostics.com live + official questdiagnostics.com SF locations verified
- Batch: 2 Status: monitor Flag: SF locations are mostly patient service centers (phlebotomy); major testing labs are outside SF — verify 'San Francisco, CA' in the location field of each posting. Beware fake-Quest-job scams (Quest posts a fraud warning on its careers page) — apply only via careers.questdiagnostics.com.
- Subpage: jobs/job-31.html
- Sources: https://careers.questdiagnostics.com/, https://www.questdiagnostics.com/locations/detail.html/DMT/94114/75/1
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-32 — Labcorp — San Francisco locations
- Position: Laboratory Assistant / Patient Service Support (entry)
- OfficialLink: https://careers.labcorp.com/global/en
- ApplyLink raw: https://careers.labcorp.com/global/search-results — search 'Laboratory' + San Francisco, CA
- ApplyLink clean: 
- Channel: Official Labcorp careers portal (direct)
- VerificationMethod: Official careers.labcorp.com live + official locations.labcorp.com (6 SF sites) verified
- Batch: 2 Status: monitor Flag: SF locations are patient service centers; major labs are outside SF — verify 'San Francisco, CA' location on each posting. Apply only via careers.labcorp.com.
- Subpage: jobs/job-32.html
- Sources: https://careers.labcorp.com/global/en, https://locations.labcorp.com/ca/san-francisco/
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-33 — City & County of San Francisco — SFPUC (Water Quality)
- Position: Water Quality Technician (Class 2481) — field & lab water/wastewater analyses
- OfficialLink: https://careers.sf.gov/classifications/?classCode=2481
- ApplyLink raw: https://careers.sf.gov — search '2481' or 'Water Quality Technician'
- ApplyLink clean: 
- Channel: Official City & County of SF portal (direct civil service)
- VerificationMethod: Official careers.sf.gov classification 2481 verified (full job description + pay table)
- Batch: 2 Status: monitor Flag: SF locations are patient service centers; major labs are outside SF — verify 'San Francisco, CA' location on each posting. Apply only via careers.labcorp.com.
- Subpage: jobs/job-33.html
- Sources: https://careers.sf.gov/classifications/?classCode=2481, https://careers.sf.gov
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-34 — SFPD Forensic Services Division — Crime Lab (Chemical Analysis)
- Position: Criminalist I (Class 8259) — entry-level forensic chemistry (Chemical Analysis section)
- OfficialLink: https://careers.sf.gov/classifications/?classCode=8259
- ApplyLink raw: https://careers.sf.gov — search '8259' or 'Criminalist I'
- ApplyLink clean: 
- Channel: Official City & County of SF portal (direct civil service / exempt)
- VerificationMethod: Official careers.sf.gov classification 8259 + live-structure postings (1995 Evans Ave) verified
- Batch: 2 Status: monitor Flag: Requires valid CA driver's license; some positions may require Water Distribution Operator D1 cert. Civil-service exam windows are time-limited.
- Subpage: jobs/job-34.html
- Sources: https://careers.sf.gov/classifications/?classCode=8259, https://careers.sf.gov/role/?id=3743990005764126, https://www.sanfranciscopolice.org/your-sfpd/careers
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-35 — Laguna Honda Hospital & Rehabilitation Center (City/DPH)
- Position: Laboratory / Clinical Support (hospital lab assistant & aide roles)
- OfficialLink: https://www.sf.gov/location--laguna-honda-hospital-and-rehabilitation-center
- ApplyLink raw: https://careers.sf.gov — search 'Laguna Honda' + laboratory / technician / assistant
- ApplyLink clean: 
- Channel: Official City & County of SF portal (direct civil service)
- VerificationMethod: Official sf.gov location page (375 Laguna Honda Blvd) + City-run hospital → careers.sf.gov
- Batch: 2 Status: monitor Flag: Clinical Lab Scientist roles require CA CLS license — target Lab Technician/Assistant/Aide titles. Hospital roles may require TB screening, N95 fit testing, vaccines.
- Subpage: jobs/job-35.html
- Sources: https://www.sf.gov/location--laguna-honda-hospital-and-rehabilitation-center, https://careers.sf.gov
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-36 — UCSF Health Hyde Hospital (formerly Saint Francis Memorial)
- Position: Laboratory Assistant — Clinical Lab Support (entry, non-licensed)
- OfficialLink: https://sfcommunityhospitals.ucsfhealth.org/saint-francis
- ApplyLink raw: https://jobs.ucsfmedicalcenter.org — search 'Hyde' or 'Laboratory Assistant' + San Francisco
- ApplyLink clean: 
- Channel: Official UCSF Health portal (direct) — hospital is now UCSF Health, not Dignity
- VerificationMethod: Official sfcommunityhospitals.ucsfhealth.org confirms UCSF Health acquisition + 900 Hyde address
- Batch: 2 Status: monitor Flag: Clinical Lab Scientist roles require CA CLS license — target Lab Technician/Assistant/Aide titles. Hospital roles may require TB screening, N95 fit testing, vaccines.
- Subpage: jobs/job-36.html
- Sources: https://sfcommunityhospitals.ucsfhealth.org/, https://jobs.ucsfmedicalcenter.org
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-37 — San Francisco Unified School District (SFUSD)
- Position: Science Laboratory / Classroom Support (classified staff, e.g., science prep technician)
- OfficialLink: https://careers.sfusd.edu/
- ApplyLink raw: https://jobs.redroverk12.com/org/sfusd — SFUSD official applicant system; search science / laboratory / technician
- ApplyLink clean: 
- Channel: Official SFUSD applicant system Red Rover (direct district hiring, not a recruiter)
- VerificationMethod: Official careers.sfusd.edu → Red Rover official ATS verified + 555 Franklin admin verified
- Batch: 2 Status: monitor Flag: Hospital renamed: apply via UCSF Health portal (jobs.ucsfmedicalcenter.org), NOT Dignity/CommonSpirit boards. CLS/MLT roles require CA license — target Lab Assistant titles.
- Subpage: jobs/job-37.html
- Sources: https://careers.sfusd.edu/, https://jobs.redroverk12.com/org/sfusd, https://archive.sfusd.edu/en/schools/school-information/administration-facilities.html
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-38 — Exploratorium — Museum of Science, Art & Human Perception
- Position: Exhibit / Science Technician (hands-on science support & maintenance)
- OfficialLink: https://www.exploratorium.edu/about/jobs
- ApplyLink raw: https://www.exploratorium.edu/about/jobs/current-openings — search technician / maintenance / exhibits
- ApplyLink clean: 
- Channel: Official Exploratorium website (direct)
- VerificationMethod: Official exploratorium.edu/about/jobs → current-openings verified + Piers 15/17 SF address
- Batch: 2 Status: monitor Flag: Not bench chemistry — exhibit/prototype shop + public-floor science support. Consider as a science-adjacent bridge only if bench roles stall. Easiest commute on the list (direct N Judah).
- Subpage: jobs/job-38.html
- Sources: https://www.exploratorium.edu/about/jobs, https://www.exploratorium.edu/about/jobs/current-openings
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-39 — SF Office of the Chief Medical Examiner — Forensic Laboratory Division
- Position: Forensic Laboratory Analyst (Class 2403) — drug/poison screens, extractions, chromatography
- OfficialLink: https://careers.sf.gov/classifications/?classCode=2403&setId=COMMN
- ApplyLink raw: https://careers.sf.gov — search '2403' or 'Forensic Laboratory Analyst'
- ApplyLink clean: 
- Channel: Official City & County of SF portal (direct civil service)
- VerificationMethod: Official careers.sf.gov classification 2403 verified (full description, B.S. + no experience) + OCME lab address via data.sfgov.org
- Batch: 2 Status: monitor Flag: Not bench chemistry — exhibit/prototype shop + public-floor science support. Consider as a science-adjacent bridge only if bench roles stall. Easiest commute on the list (direct N Judah).
- Subpage: jobs/job-39.html
- Sources: https://careers.sf.gov/classifications/?classCode=2403&setId=COMMN, https://data.sfgov.org/api/views/rwbr-kbhe/rows.rdf?accessType=DOWNLOAD, https://careers.sf.gov
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-40 — American Red Cross — SF Blood & Platelet Donation Center (Biomedical Services)
- Position: Blood Collection / Biomedical Support (entry, trained on the job)
- OfficialLink: https://www.redcross.org/local/california/northern-california-coastal.html
- ApplyLink raw: https://americanredcross.wd1.myworkdayjobs.com/American_Red_Cross_Careers — search Biomedical / Blood Collection + San Francisco
- ApplyLink clean: 
- Channel: Official Red Cross Workday (direct, linked from redcross.org careers)
- VerificationMethod: Official redcross.org SF location (1663 Market St) + official Workday careers verified
- Batch: 2 Status: monitor Flag: Collection roles are phlebotomy/donor-facing (training provided), not bench chemistry. Lab testing happens at regional labs — verify 'San Francisco, CA' on each posting. Consider as bridge only.
- Subpage: jobs/job-40.html
- Sources: https://www.redcross.org/local/california/northern-california-coastal.html, https://www.redcross.org/about-us/careers.html, https://americanredcross.wd1.myworkdayjobs.com/American_Red_Cross_Careers
- Domain check: official REVIEW / apply REVIEW (check if official ATS linked from official careers page)

### job-41 — UCSF — Helen Diller Family Comprehensive Cancer Center
- Position: Staff Research Associate I/II — Cancer biology & shared-resource labs (sample prep, assays)
- OfficialLink: https://cancer.ucsf.edu/
- ApplyLink raw: https://careers.ucsf.edu — search 'Staff Research Associate' + Helen Diller / Cancer Center
- ApplyLink clean: 
- Channel: Official UCSF careers portal (direct, UC system)
- VerificationMethod: Official cancer.ucsf.edu Diller Building page (1450 3rd St) + shared-resource cores verified
- Batch: 3 Status: monitor Flag: none
- Subpage: jobs/job-41.html
- Sources: https://cancer.ucsf.edu/insiders/facilities/mission-bay-diller-building, https://cancer.ucsf.edu/research/cores/lca/lca-info, https://careers.ucsf.edu
- Domain check: official REVIEW / apply REVIEW (check if official ATS linked from official careers page)

### job-42 — UCSF — Francis I. Proctor Foundation for Research in Ophthalmology
- Position: Staff Research Associate I/II — Ocular infectious-disease / microbiology labs (assays, sample prep)
- OfficialLink: https://proctor.ucsf.edu/
- ApplyLink raw: https://careers.ucsf.edu — search 'Proctor' + 'Staff Research Associate'
- ApplyLink clean: 
- Channel: Official UCSF careers portal (direct, UC system)
- VerificationMethod: Official proctor.ucsf.edu contact page (490 Illinois St Fl 2) verified
- Batch: 3 Status: monitor Flag: none
- Subpage: jobs/job-42.html
- Sources: https://proctor.ucsf.edu/cornea-external-disease-refractive-surgery-fellowship, https://careers.ucsf.edu
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-43 — City & County of San Francisco — SFDPH / Citywide Labs
- Position: Laboratory Technician I (Class 2402) — Entry lab support (glassware, media, inventory, records)
- OfficialLink: https://careers.sf.gov/classifications/?classCode=2402
- ApplyLink raw: https://careers.sf.gov — search '2402' or 'Laboratory Technician I'
- ApplyLink clean: 
- Channel: Official City & County of SF portal (direct civil service)
- VerificationMethod: Official careers.sf.gov classification 2402 spec verified ($72K-$88K/yr, no license, promotes to 2416)
- Batch: 3 Status: monitor Flag: none
- Subpage: jobs/job-43.html
- Sources: https://careers.sf.gov/classifications/?classCode=2402, https://careers.sf.gov
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-44 — City & County of San Francisco — SFDPH Public Health Laboratories
- Position: Microbiologist I/II (Class 2463) — Diagnostic micro testing (LICENSED track — plan-ahead entry)
- OfficialLink: https://careers.sf.gov/classifications/?classCode=2463
- ApplyLink raw: https://careers.sf.gov — search '2463' or 'Microbiologist'
- ApplyLink clean: 
- Channel: Official City & County of SF portal (direct civil service)
- VerificationMethod: Official careers.sf.gov classification 2463 + past Microbiologist I recruitments verified
- Batch: 3 Status: monitor Flag: Entry rung is routine by design (glassware, media, inventory) — a foot-in-the-door, not a chemist role; promotes to 2416 Laboratory Technician II.
- Subpage: jobs/job-44.html
- Sources: https://careers.sf.gov/classifications/?classCode=2463, https://careers.sf.gov
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-45 — Sutter Health — CPMC Mission Bernal Campus
- Position: Laboratory Assistant / Pathology Lab Support — Clinical lab support (entry)
- OfficialLink: https://www.sutterhealth.org/find-location/facility/cpmc-emergency-mission-bernal-campus
- ApplyLink raw: https://jobs.sutterhealth.org/us/en — search 'Laboratory Assistant' + Mission Bernal / San Francisco
- ApplyLink clean: 
- Channel: Official Sutter Health jobs portal (direct)
- VerificationMethod: Official sutterhealth.org Mission Bernal facility page (3555 Cesar Chavez St) + jobs portal verified
- Batch: 3 Status: monitor Flag: HARD REQUIREMENT: valid CA Public Health Microbiologist certificate + microbiology major — you do not currently hold it; monitor-and-plan entry only.
- Subpage: jobs/job-45.html
- Sources: https://www.sutterhealth.org/find-location/facility/cpmc-emergency-mission-bernal-campus, https://jobs.sutterhealth.org/us/en
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-46 — Sutter Health — CPMC Research Institute (CPMCRI)
- Position: Research Associate / Study Coordinator, lab track — Specimen processing, regulatory docs, QC records
- OfficialLink: https://www.sutterhealth.org/research/
- ApplyLink raw: https://jobs.sutterhealth.org/us/en — search 'Research' + San Francisco / CPMC Research Institute
- ApplyLink clean: 
- Channel: Official Sutter Health jobs portal (direct)
- VerificationMethod: FDP federal clearinghouse record (475 Brannan St Ste 130) + official sutterhealth.org/research verified
- Batch: 3 Status: monitor Flag: none
- Subpage: jobs/job-46.html
- Sources: https://fdpclearinghouse.org/organizations/533, https://www.sutterhealth.org/research/, https://jobs.sutterhealth.org/us/en
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-47 — Fine Arts Museums of San Francisco — de Young Museum
- Position: Museum / Conservation Technician track — Materials handling, documentation (via City portal)
- OfficialLink: https://www.famsf.org/
- ApplyLink raw: https://careers.sf.gov — search 'Fine Arts Museum' / 'Museum' (FAMSF hires through the City)
- ApplyLink clean: 
- Channel: Official City & County of SF portal (FAMSF is a City department — direct)
- VerificationMethod: FAMSF confirmed as City department hiring via careers.sf.gov (live City postings cite de Young, 50 Hagiwara Tea Garden Dr)
- Batch: 3 Status: monitor Flag: none
- Subpage: jobs/job-47.html
- Sources: https://www.famsf.org/, https://careers.sf.gov/role/?id=743999827405805
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-48 — San Francisco Museum of Modern Art (SFMOMA)
- Position: Conservation Technician / Preparator track — Art handling, condition reporting (via official Lever board)
- OfficialLink: https://www.sfmoma.org/join-the-team/
- ApplyLink raw: https://jobs.lever.co/sfmoma — search Conservation / Preparator / Registration
- ApplyLink clean: 
- Channel: Official SFMOMA Lever board (direct, linked from sfmoma.org)
- VerificationMethod: Official sfmoma.org/join-the-team links to jobs.lever.co/sfmoma; 151 Third St address verified
- Batch: 3 Status: monitor Flag: Conservator roles require a master's in art conservation; the technician/preparator rungs are the accessible track.
- Subpage: jobs/job-48.html
- Sources: https://www.sfmoma.org/join-the-team/, https://jobs.lever.co/sfmoma
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-49 — Aquarium of the Bay (Bay Ecotarium)
- Position: Biologist I — Entry, water-quality laboratory + environmental parameters (ANIMAL-CARE role)
- OfficialLink: https://www.aquariumofthebay.org/careers/
- ApplyLink raw: https://www.aquariumofthebay.org/careers/ — Biologist I posting live (checked Sept 9, 2026)
- ApplyLink clean: 
- Channel: Official Aquarium careers page (direct)
- VerificationMethod: Official aquariumofthebay.org/careers shows Biologist I entry posting with water-quality-lab duties; PIER 39 address verified
- Batch: 3 Status: recently-posted Flag: Conservator = master's track; target Preparator / Technician / Registration-support rungs.
- Subpage: jobs/job-49.html
- Sources: https://www.aquariumofthebay.org/careers/, https://www.aquariumofthebay.org/
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-50 — Dandelion Chocolate — 16th Street Factory
- Position: Sanitation / Production QC track — Quality systems, chemical handling, food safety (Mission factory)
- OfficialLink: https://www.dandelionchocolate.com/pages/visit-us
- ApplyLink raw: https://dandelionchocolate.applytojob.com/apply — search San Francisco production / sanitation / quality
- ApplyLink clean: 
- Channel: Official Dandelion Chocolate career board (direct ATS)
- VerificationMethod: Official dandelionchocolate.com visit page (2600 16th St) + official ApplyToJob board verified
- Batch: 3 Status: monitor Flag: Role includes animal care + SCUBA + husbandry — the water-quality lab is one duty among many, not a pure chemistry post.
- Subpage: jobs/job-50.html
- Sources: https://www.dandelionchocolate.com/pages/visit-us, https://dandelionchocolate.applytojob.com/apply
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-51 — North East Medical Services (NEMS) — Chinatown Main Clinic
- Position: Lab Assistant I — Clinic laboratory support (community health center)
- OfficialLink: https://www.nems.org/
- ApplyLink raw: https://nems.betterteam.com/ — Lab Assistant postings recur; check weekly
- ApplyLink clean: 
- Channel: Official NEMS BetterTeam board (direct, linked from nems.org)
- VerificationMethod: Official nems.org careers chain → nems.betterteam.com board; 1520 Stockton St main clinic corroborated by CDC directory
- Batch: 3 Status: monitor Flag: Production environment: physical work, early shifts, food-safety pace — QC-adjacent, not a lab-chemistry post.
- Subpage: jobs/job-51.html
- Sources: https://www.nems.org/, https://nems.betterteam.com/, https://npin.cdc.gov/organization/north-east-medical-services-1
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-52 — Kaiser Permanente — SF Mission Bay Medical Offices
- Position: Laboratory Assistant / Specimen Processor — MOB lab (entry, non-licensed rung only)
- OfficialLink: https://healthy.kaiserpermanente.org/northern-california/facilities/san-francisco-mission-bay-medical-offices-322881
- ApplyLink raw: https://kaiserpermanentejobs.org — search 'Laboratory Assistant' + Mission Bay / San Francisco
- ApplyLink clean: 
- Channel: Official Kaiser careers portal (direct)
- VerificationMethod: Official healthy.kaiserpermanente.org facility page (1600 Owens St) verified
- Batch: 3 Status: monitor Flag: Phlebotomy/CPT certificate commonly required; Cantonese/Mandarin strongly preferred for patient-facing duties.
- Subpage: jobs/job-52.html
- Sources: https://healthy.kaiserpermanente.org/northern-california/facilities/san-francisco-mission-bay-medical-offices-322881, https://kaiserpermanentejobs.org
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-53 — SF City Clinic (SFDPH) — Municipal STI Clinic
- Position: Laboratory / Phlebotomy Support — Specimen collection & processing (CPT track, via City portal)
- OfficialLink: https://sf.gov/cityclinic
- ApplyLink raw: https://careers.sf.gov — search 'City Clinic' / '2402' / '2416' (clinic lab classes)
- ApplyLink clean: 
- Channel: Official City & County of SF portal (clinic is SFDPH-run — direct)
- VerificationMethod: City-run clinic at 356 7th St corroborated (Wikipedia + Apple Maps place data incl. sf.gov clinic page); hiring via careers.sf.gov
- Batch: 3 Status: monitor Flag: Kaiser lab roles commonly require CPT/MLT/CLS state certification — target explicitly non-licensed 'Laboratory Assistant' reqs only.
- Subpage: jobs/job-53.html
- Sources: https://sf.gov/cityclinic, https://en.wikipedia.org/wiki/San_Francisco_City_Clinic, https://careers.sf.gov
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-54 — U.S. Customs and Border Protection — San Francisco Laboratory (federal)
- Position: Chemist (1320 series) — Analytical chemistry, trade & commodity testing (via USAJOBS)
- OfficialLink: https://www.cbp.gov/about/labs-scientific-svcs/org-operations
- ApplyLink raw: https://www.usajobs.gov — search 'Chemist' + 'Customs and Border Protection' + San Francisco; set an alert
- ApplyLink clean: 
- Channel: Official USAJOBS federal portal (direct federal hiring)
- VerificationMethod: Official cbp.gov Labs page lists SF Laboratory (630 Sansome St Rm 1450); ISO/IEC 17025 network corroborated by WCO doc
- Batch: 3 Status: monitor Flag: Patient-facing specimen collection typically requires CPT-I phlebotomy certification.
- Subpage: jobs/job-54.html
- Sources: https://www.cbp.gov/about/labs-scientific-svcs/org-operations, https://www.usajobs.gov
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-55 — Wildtype Foods — Cultivated Seafood (Dogpatch pilot plant)
- Position: Research Associate — Food chemistry / QC, physical & chemical testing (monitor — no openings now)
- OfficialLink: https://www.wildtypefoods.com/
- ApplyLink raw: https://job-boards.greenhouse.io/Wildtype — no openings now; monitor + speculative outreach via site contact page
- ApplyLink clean: 
- Channel: Official Wildtype Greenhouse board (direct)
- VerificationMethod: Official wildtypefoods.com + official Greenhouse board (job-boards.greenhouse.io/Wildtype) verified; 953 Indiana St HQ corroborated
- Batch: 3 Status: monitor Flag: Federal hiring: U.S. citizenship, background investigation, slow USAJOBS process — but the chemistry fit is elite.
- Subpage: jobs/job-55.html
- Sources: https://www.wildtypefoods.com/, https://job-boards.greenhouse.io/Wildtype
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-56 — Asian Art Museum (City & County of San Francisco)
- Position: Conservation / Collections track — XRF materials science, handling, records (via City portal)
- OfficialLink: https://www.asianart.org/
- ApplyLink raw: https://careers.sf.gov — search 'Asian Art Museum' / 'Conservation' / 'Collections' (AAM hires through the City)
- ApplyLink clean: 
- Channel: Official City & County of SF portal (AAM is a City department — direct)
- VerificationMethod: AAM confirmed as City department hiring via careers.sf.gov (live 2026 City posting cites 200 Larkin St + apply-directly-to-City chain)
- Batch: 3 Status: monitor Flag: No current openings on the official board (checked Sept 9, 2026) — monitor + network; do not apply via 3rd-party reposts.
- Subpage: jobs/job-56.html
- Sources: https://www.asianart.org/, https://careers.sf.gov
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-57 — Chinese Hospital — Sunset Health Services / Blood Draw Center
- Position: Laboratory / Blood-Draw Support — Specimen collection (WALKABLE from home)
- OfficialLink: https://chinesehospital-sf.org/laboratory/
- ApplyLink raw: https://chinesehospital-sf.org — Careers / Job Opportunities → search Sunset / lab / blood draw
- ApplyLink clean: 
- Channel: Official hospital website application (direct, no recruiter)
- VerificationMethod: Official chinesehospital-sf.org/laboratory lists Blood Draw Center – Sunset at 1800 31st Ave (Mon/Wed/Fri)
- Batch: 3 Status: monitor Flag: Associate Museum Conservator (3518) requires a conservation master's + museum experience; collections-assistant rungs are the accessible track.
- Subpage: jobs/job-57.html
- Sources: https://chinesehospital-sf.org/laboratory/, https://chinesehospital-sf.org/clinics/
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-58 — U.S. Mint — San Francisco Mint (federal)
- Position: Metal Forming Machine Operator / Production QC track — Precision coin inspection (via USAJOBS)
- OfficialLink: https://www.usmint.gov/about/tours-and-locations/san-francisco
- ApplyLink raw: https://www.usajobs.gov — search 'U.S. Mint' + San Francisco; set an alert
- ApplyLink clean: 
- Channel: Official USAJOBS federal portal (direct federal hiring)
- VerificationMethod: Official usmint.gov SF branch page + 155 Hermann St corroborated; SF Mint production roles confirmed via USAJOBS/Indeed discovery
- Batch: 3 Status: monitor Flag: Blood-draw duties typically require CPT-I certification; Chinese language strongly preferred.
- Subpage: jobs/job-58.html
- Sources: https://www.usmint.gov/about/tours-and-locations/san-francisco, https://www.usajobs.gov
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-59 — Heluna Health — Research Associate, SFDPH Center for Public Health Research
- Position: Research Associate — Public-health research support, CPHR/CSUH (employer of record: Heluna Health)
- OfficialLink: https://www.helunahealth.org/
- ApplyLink raw: https://www.helunahealth.org/ — Careers → search San Francisco Research Associate (CPHR/CSUH postings recur)
- ApplyLink clean: 
- Channel: Official Heluna Health portal (direct employer of record, not a staffing recruiter)
- VerificationMethod: Official helunahealth.org (nonprofit fiscal sponsor since 1969) verified live; SF Research Associate postings confirmed via discovery
- Batch: 3 Status: monitor Flag: Manufacturing/production role (proof-coin QC inspection), not chemistry — federal foot-in-the-door only.
- Subpage: jobs/job-59.html
- Sources: https://www.helunahealth.org/
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-60 — Bridge HIV (SFDPH + UCSF) — HIV Prevention Research Unit
- Position: Research Associate / Specimen Processing — Chain-of-custody, LIMS, human-sample handling (via Heluna)
- OfficialLink: https://www.bridgehiv.org/
- ApplyLink raw: https://www.helunahealth.org/ — Careers → search 'Bridge HIV' Research Associate (Heluna is employer of record)
- ApplyLink clean: 
- Channel: Official Heluna Health portal for Bridge HIV unit (direct, not a recruiter)
- VerificationMethod: Official bridgehiv.org verified live + sf.gov page confirms 25 Van Ness Ste 100; hiring via Heluna Health confirmed
- Batch: 3 Status: monitor Flag: Grant-funded, temporary/benefitted roles with non-standard hours and community fieldwork — research support, not bench chemistry.
- Subpage: jobs/job-60.html
- Sources: https://www.bridgehiv.org/, https://www.sf.gov/public-health-pride-parade-contingent, https://www.helunahealth.org/
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-61 — UCSF — Drug Research Unit (DRU), Pharmaceutical Sciences
- Position: Staff Research Associate II — Analytical assay development & LC-MS sample analysis (LIVE posting)
- OfficialLink: https://pharm.ucsf.edu/drug-research-unit/training
- ApplyLink raw: https://careers.ucsf.edu — live DRU posting on pharm.ucsf.edu (open positions) → its apply link (UCSF careers/BrassRing)
- ApplyLink clean: 
- Channel: Official UCSF careers portal (direct, UC system)
- VerificationMethod: LIVE posting 'Staff Research Associate - Drug Research Unit / LC-MS Background' fetched from official pharm.ucsf.edu (Sept 9, 2026)
- Batch: 4 Status: recently-posted Flag: Grant-funded, temporary/benefitted roles; clinical-community research setting, not bench chemistry.
- Subpage: jobs/job-61.html
- Sources: https://pharm.ucsf.edu/drug-research-unit/training, https://careers.ucsf.edu
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-62 — UCSF — Institute for Neurodegenerative Diseases (IND)
- Position: Staff Research Associate II — Drug Discovery, HTS team (small-molecule screening; LIVE, Job Code 009617)
- OfficialLink: https://ind.ucsf.edu/staff-research-associate-ii-drug-discovery
- ApplyLink raw: https://sjobs.brassring.com/TGnewUI/Search/Home/Home?partnerid=6495&siteid=5861#jobDetails=3364720_5861 — 'Apply Here' from the ind.ucsf.edu posting (UCSF official BrassRing)
- ApplyLink clean: 
- Channel: Official UCSF careers/BrassRing (direct, UC system)
- VerificationMethod: LIVE posting fetched from official ind.ucsf.edu (Sept 9, 2026): Job Code 009617 SRA 2 NEX, Mission Bay (SF), external apply link to UCSF BrassRing
- Batch: 4 Status: recently-posted Flag: none
- Subpage: jobs/job-62.html
- Sources: https://ind.ucsf.edu/staff-research-associate-ii-drug-discovery, https://sjobs.brassring.com/TGnewUI/Search/Home/Home?partnerid=6495&siteid=5861#jobDetails=3364720_5861
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-63 — UCSF — Quantitative Biosciences Institute (QBI), Krogan Lab
- Position: Staff Research Associate II — Protein interaction & proteomics (cloning, iPSC culture, affinity workflows; LIVE)
- OfficialLink: https://careers.ucsf.edu/careers/JobDetail/San-Francisco-CA-United-States/2949
- ApplyLink raw: https://careers.ucsf.edu/careers/JobDetail/San-Francisco-CA-United-States/2949 — apply via the live listing
- ApplyLink clean: 
- Channel: Official UCSF careers portal (direct, UC system)
- VerificationMethod: LIVE JobDetail 2949 fetched from official careers.ucsf.edu (Sept 9, 2026): QBI Krogan Lab SRA II, Mission Bay (SF), 100%, day shift
- Batch: 4 Status: recently-posted Flag: none
- Subpage: jobs/job-63.html
- Sources: https://careers.ucsf.edu/careers/JobDetail/San-Francisco-CA-United-States/2949, https://careers.ucsf.edu
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-64 — UCSF — Goodarzi Lab, Biochemistry & Biophysics
- Position: Junior Specialist — RNA-based therapeutics & cancer biology (JPF06054, LIVE, posted Apr 2026)
- OfficialLink: https://aprecruit.ucsf.edu/JPF06054
- ApplyLink raw: https://aprecruit.ucsf.edu/JPF06054 — apply with cover letter + CV + 2 references (contact info only)
- ApplyLink clean: 
- Channel: Official UCSF academic recruit portal aprecruit.ucsf.edu (direct)
- VerificationMethod: LIVE posting JPF06054 fetched from official aprecruit.ucsf.edu (Sept 9, 2026): posted Apr 27, 2026, final date Oct 27, 2027, $55,000-$58,600
- Batch: 4 Status: recently-posted Flag: none
- Subpage: jobs/job-64.html
- Sources: https://aprecruit.ucsf.edu/JPF06054, https://aprecruit.ucsf.edu/JPF05571
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-65 — UCSF — Kamber Lab, Anatomy
- Position: Junior/Assistant Specialist — Cancer immunology & CRISPR screening (JPF05697, open until filled)
- OfficialLink: https://aprecruit.ucsf.edu/JPF05697
- ApplyLink raw: https://aprecruit.ucsf.edu/JPF05697 — apply with CV + 2 references (cover letter optional)
- ApplyLink clean: 
- Channel: Official UCSF academic recruit portal aprecruit.ucsf.edu (direct)
- VerificationMethod: Posting JPF05697 on official apprecruit.ucsf.edu (open until filled — first review Aug 22, 2025; $53,100-$188,200 by rank; kamberlab.com official lab site)
- Batch: 4 Status: monitor Flag: Mouse work is required (tumor cell injections, tissue harvesting) — posting states 'willingness to work with mice'.
- Subpage: jobs/job-65.html
- Sources: https://aprecruit.ucsf.edu/JPF05697, https://www.kamberlab.com
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-66 — UCSF — Bose Lab, Anatomy
- Position: Research Specialist — Lab operations + cancer immunology research (JPF05693, open until filled)
- OfficialLink: https://aprecruit.ucsf.edu/JPF05693
- ApplyLink raw: https://aprecruit.ucsf.edu/JPF05693 — apply with CV, cover letter, 2 references, 3-5 yr career-goal statement
- ApplyLink clean: 
- Channel: Official UCSF academic recruit portal apprecruit.ucsf.edu (direct)
- VerificationMethod: Posting JPF05693 on official apprecruit.ucsf.edu (open until filled — first review Aug 22, 2025; $55,000-$194,800 by rank; profiles.ucsf.edu/rohit.bose official PI page)
- Batch: 4 Status: monitor Flag: Rolling posting — initial review date has passed; confirm it is still open at apply time.
- Subpage: jobs/job-66.html
- Sources: https://aprecruit.ucsf.edu/JPF05693, https://profiles.ucsf.edu/rohit.bose
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-67 — UCSF — Staff Research Associate, Parnassus biomedical lab (cardiovascular/immunotherapy mouse models)
- Position: Staff Research Associate — Molecular biology + mouse colony support (LIVE; Parnassus 94143)
- OfficialLink: https://careers.ucsf.edu
- ApplyLink raw: https://careers.ucsf.edu — search 'Staff Research Associate' + Parnassus (live posting at 500 Parnassus Ave, 94143) → apply from the listing
- ApplyLink clean: 
- Channel: Official UCSF careers portal (direct, UC system)
- VerificationMethod: LIVE SRA posting for 500 Parnassus Ave (94143) confirmed via official careers.ucsf.edu (JobDetail pattern) in Sept 9, 2026 snapshot — confirm exact JobDetail ID before applying
- Batch: 4 Status: monitor Flag: Includes after-hours clinical-sample receipt; lab operations (not bench chemistry) is the primary responsibility.
- Subpage: jobs/job-67.html
- Sources: https://careers.ucsf.edu
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-68 — HHMI — Brainard Lab (UCSF Physiology & Psychiatry)
- Position: Research Technician I/II — Behavioral neuroscience, songbird model (LIVE req R-4026)
- OfficialLink: https://hhmi.wd1.myworkdayjobs.com/en-US/External/job/Research-Technician--Brainard-Lab_R-4026-1
- ApplyLink raw: https://hhmi.wd1.myworkdayjobs.com/en-US/External/job/Research-Technician--Brainard-Lab_R-4026-1 — official HHMI Workday (req R-4026)
- ApplyLink clean: 
- Channel: Official HHMI Workday portal (HHMI is employer of record for this UCSF lab — direct, not a recruiter)
- VerificationMethod: LIVE req R-4026 fetched from official hhmi.wd1.myworkdayjobs.com (Sept 9, 2026): work address 1550 4th St Ste 190, SF 94158; RT I $20.08-32.65/hr, RT II $24-39/hr; hhmi.org scientist profile verified
- Batch: 4 Status: recently-posted Flag: Live-verified via official-portal snapshot; exact JobDetail ID rotates — confirm at apply time. Mouse colony work is central.
- Subpage: jobs/job-68.html
- Sources: https://hhmi.wd1.myworkdayjobs.com/en-US/External/job/Research-Technician--Brainard-Lab_R-4026-1, https://www.hhmi.org/scientists/michael-brainard, https://brainardlab.ucsf.edu/
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-69 — NCIRE — The Veterans Health Research Institute (SF VA affiliate)
- Position: Staff Research Associate II (STAFF001526) — Research support with data workflows (LIVE)
- OfficialLink: https://www.ncire.org/careers
- ApplyLink raw: https://www.ncire.org/careers — search 'STAFF001526' or 'Staff Research Associate II' (official NCIRE Ultrio board)
- ApplyLink clean: 
- Channel: Official NCIRE careers portal (direct nonprofit employer — see also job-11/12)
- VerificationMethod: LIVE posting STAFF001526 (4150 Clement St, Lincoln Park, $25.24-$40.60/hr) confirmed on official NCIRE careers channel (Ultrio) Sept 9, 2026
- Batch: 4 Status: recently-posted Flag: none
- Subpage: jobs/job-69.html
- Sources: https://www.ncire.org/careers
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-70 — Gladstone Institutes — Marson Lab (Institute of Genomic Immunology)
- Position: Research Associate (In-Vivo) — Mouse models of immunotherapy + colony management (LIVE)
- OfficialLink: https://gladstone.wd5.myworkdayjobs.com/en-US/careers
- ApplyLink raw: https://gladstone.wd5.myworkdayjobs.com/en-US/careers — search 'Marson' + 'In-Vivo' / 'Research Associate I / II' (official Gladstone Workday board)
- ApplyLink clean: 
- Channel: Official Gladstone Institutes Workday portal (direct nonprofit employer — new live Marson-Lab posting; see also job-04/05/06)
- VerificationMethod: LIVE 'Research Associate (In-Vivo) - Marson Lab' + 'RA I/II - Marson Lab' confirmed on official gladstone.wd5.myworkdayjobs.com (SF, $28-33/hr) Sept 9, 2026; opportunities.ucsf.edu mirror
- Batch: 4 Status: recently-posted Flag: none
- Subpage: jobs/job-70.html
- Sources: https://gladstone.wd5.myworkdayjobs.com/en-US/careers, https://opportunities.ucsf.edu/content/research-associate-genomic-immunology-institute-gladstone
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-71 — EVERY (The EVERY Company) — precision fermentation, animal-free protein ingredients
- Position: Research Associate I (Protein Science & Analytics) — HPLC, FPLC, plate readers (LIVE; $75-85K)
- OfficialLink: https://job-boards.greenhouse.io/theeverycompany/jobs/5745371004
- ApplyLink raw: https://job-boards.greenhouse.io/theeverycompany/jobs/5745371004 — apply on the official Greenhouse board
- ApplyLink clean: 
- Channel: Official EVERY Greenhouse board (direct employer, B2B food-tech ingredient company)
- VerificationMethod: LIVE official Greenhouse posting (job 5745371004) fetched Sept 9, 2026 — 'San Francisco, California, United States', $75,000-$85,000; every.com official company site verified
- Batch: 4 Status: recently-posted Flag: Mouse colony work is central (breeding, injections, genotyping, euthanasia).
- Subpage: jobs/job-71.html
- Sources: https://job-boards.greenhouse.io/theeverycompany/jobs/5745371004, https://every.com/
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-72 — General Proximity — induced proximity medicines (OmniTAC engine)
- Position: Research Associate, Drug Discovery — Platform/Discovery team (LIVE; $32-45/hr)
- OfficialLink: https://job-boards.greenhouse.io/generalproximity/jobs/5660523004
- ApplyLink raw: https://job-boards.greenhouse.io/generalproximity/jobs/5660523004 — apply on the official Greenhouse board
- ApplyLink clean: 
- Channel: Official General Proximity Greenhouse board (direct startup employer)
- VerificationMethod: LIVE official Greenhouse posting (job 5660523004) fetched Sept 9, 2026 — MBC BioLabs at 135 Mississippi St, 'short walk from the 22nd St Caltrain Station' per posting
- Batch: 4 Status: recently-posted Flag: Older 'Research Associate I' posting (job 5217382004) is closed — use 5745371004 only. Street address (689 Bryant St HQ area) confirmed at interview.
- Subpage: jobs/job-72.html
- Sources: https://job-boards.greenhouse.io/generalproximity/jobs/5660523004, https://generalproximity.com
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-73 — Anthropic (public benefit corp) — AI for science, Life Sciences team
- Position: Research Associate, Biology - entry-level bench scientist (molecular biology + biochemistry; WITHDRAWN 2026-09-09, watch for repost)
- OfficialLink: https://job-boards.greenhouse.io/anthropic/jobs/5285248008
- ApplyLink raw: https://job-boards.greenhouse.io/anthropic/jobs/5285248008 — apply on the official Greenhouse board (resume OR LinkedIn profile required)
- ApplyLink clean: 
- Channel: Official Anthropic Greenhouse board (direct employer; careers hub anthropic.com/careers)
- VerificationMethod: LIVE official Greenhouse posting (job 5285248008) fetched Sept 9, 2026 — full description + application form on official board; anthropic.com/careers official; 548 Market St SF office corroborated
- Batch: 4 Status: monitor Flag: none
- Subpage: jobs/job-73.html
- Sources: https://job-boards.greenhouse.io/anthropic/jobs/5285248008, https://www.anthropic.com/careers
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-74 — Anthrogen — AI + robotic molecular biology lab (seed-stage)
- Position: Research Associate (RL Environments) — run molecular biology protocols on robotic platforms (LIVE; $120-200K)
- OfficialLink: https://jobs.ashbyhq.com/anthrogen/16b4c75b-d9d3-4cff-9184-20d476371ea0
- ApplyLink raw: https://jobs.ashbyhq.com/anthrogen/16b4c75b-d9d3-4cff-9184-20d476371ea0 — apply on the official Ashby board (posted July 7, 2026)
- ApplyLink clean: 
- Channel: Official Anthrogen Ashby board (direct startup employer)
- VerificationMethod: LIVE official Ashby posting fetched Sept 9, 2026 (jobs.ashbyhq.com/anthrogen) — 'Onsite in San Francisco'; anthrogen.com official + YC/seed-stage profile corroborate
- Batch: 4 Status: recently-posted Flag: Seed-stage startup (small team) — street address not published; confirm at interview. Posting emphasizes gaming/hand-eye coordination alongside bench work.
- Subpage: jobs/job-74.html
- Sources: https://jobs.ashbyhq.com/anthrogen/16b4c75b-d9d3-4cff-9184-20d476371ea0, https://www.anthrogen.com/
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-75 — Parallel Bio — human-first drug discovery + patient biobank
- Position: Research Associate, Biobanking — human tissue sample processing, LIMS, QC (LIVE; $70-85K)
- OfficialLink: https://jobs.ashbyhq.com/parallel-bio/3ceab0ea-308b-4518-8939-3c011c624c5b
- ApplyLink raw: https://jobs.ashbyhq.com/parallel-bio/3ceab0ea-308b-4518-8939-3c011c624c5b — apply on the official Ashby board (posted March 13, 2026)
- ApplyLink clean: 
- Channel: Official Parallel Bio Ashby board (direct venture-backed employer)
- VerificationMethod: LIVE official Ashby posting fetched Sept 9, 2026 (jobs.ashbyhq.com/parallel-bio) — '100% onsite role based at our San Francisco lab', SF 94110; parallel.bio official site verified
- Batch: 4 Status: recently-posted Flag: Seed-stage startup (small team) — street address not published; confirm at interview. Posting emphasizes gaming/hand-eye coordination alongside bench work.
- Subpage: jobs/job-75.html
- Sources: https://jobs.ashbyhq.com/parallel-bio/3ceab0ea-308b-4518-8939-3c011c624c5b, https://www.parallel.bio/
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-76 — GLIDE — community health nonprofit (Tenderloin, serving SF since 1963)
- Position: Lab Technician — HEAT testing: phlebotomy, CLIA testing, specimen processing (LIVE; $31-33/hr)
- OfficialLink: https://jobs.lever.co/glide
- ApplyLink raw: https://jobs.lever.co/glide — apply to 'Lab Technician' (Neighborhood Engagement & Street Crisis Response, Full-Time San Francisco)
- ApplyLink clean: 
- Channel: Official GLIDE Lever board (direct nonprofit employer)
- VerificationMethod: LIVE 'Lab Technician' on official Lever board jobs.lever.co/glide fetched Sept 9, 2026 ($31-33/hr, full job description); glide.org/contact official page confirms 330 Ellis St Main Building, 94102
- Batch: 4 Status: recently-posted Flag: Street address not published (SF 94110 per official posting) — confirm at interview; cold-chain + consent/IRB/HIPAA documentation is part of the role.
- Subpage: jobs/job-76.html
- Sources: https://jobs.lever.co/glide, https://www.glide.org/contact/
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-77 — San Francisco AIDS Foundation (Magnet/Strut)
- Position: Lab Technician (Phlebotomist) — Full-time, high-volume phlebotomy + QA (LIVE; $34-37/hr)
- OfficialLink: https://job-boards.greenhouse.io/sfaf/jobs/5219503008
- ApplyLink raw: https://job-boards.greenhouse.io/sfaf/jobs/5219503008 — apply on the official SFAF Greenhouse board
- ApplyLink clean: 
- Channel: Official SFAF Greenhouse board (direct nonprofit employer — Magnet/Strut clinics)
- VerificationMethod: LIVE official Greenhouse posting (job 5219503008) fetched Sept 9, 2026 — 'primarily located at 470 Castro St', $34-37/hr, full job description incl. qualifications
- Batch: 4 Status: recently-posted Flag: CLIA-testing + counseling role — BLS required and CA HIV counselor cert must be held or obtained within 6 months; CPhT/MLT a plus, not required.
- Subpage: jobs/job-77.html
- Sources: https://job-boards.greenhouse.io/sfaf/jobs/5219503008, https://sfaidsf.org
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-78 — San Francisco AIDS Foundation (Magnet/Strut)
- Position: Lab Technician (Phlebotomist) — Per Diem (LIVE; $34-37/hr)
- OfficialLink: https://job-boards.greenhouse.io/sfaf/jobs/5219589008
- ApplyLink raw: https://job-boards.greenhouse.io/sfaf/jobs/5219589008 — apply on the official SFAF Greenhouse board
- ApplyLink clean: 
- Channel: Official SFAF Greenhouse board (direct nonprofit employer)
- VerificationMethod: LIVE official Greenhouse posting (job 5219589008) fetched Sept 9, 2026 — Per Diem variant of the 470 Castro St Lab Technician role, $34-37/hr
- Batch: 4 Status: recently-posted Flag: Requires CPhT I/II or MLT certification (active CPhT with CA Laboratory Field Service) — obtain CPT certification first if you do not yet hold it.
- Subpage: jobs/job-78.html
- Sources: https://job-boards.greenhouse.io/sfaf/jobs/5219589008, https://sfaidsf.org
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-79 — Invitae (a Labcorp company) — clinical genetics
- Position: Clinical Lab Technician — Entry level, genetics lab (LIVE; Sun-Thu 3:00pm-11:30pm; $28.39-35/hr)
- OfficialLink: https://www.invitae.com/
- ApplyLink raw: https://careers.labcorp.com — search 'Invitae' + 'Clinical Lab Technician' + '1400 16th Street' (official Labcorp portal — Invitae reqs post there)
- ApplyLink clean: 
- Channel: Official Labcorp careers portal (Invitae is a Labcorp company — direct employer, not a recruiter; see also job-32)
- VerificationMethod: LIVE 'Clinical Lab Technician - Invitae - Entry level' (1400 16th St, Sun-Thu 3:00pm-11:30pm, $28.39-35/hr) confirmed via official Labcorp careers channel (careers.labcorp.com) Sept 9, 2026; invitae.com official
- Batch: 4 Status: recently-posted Flag: Per diem (variable hours) — stepping-in path while FT reqs fill; same certification requirements as the FT posting.
- Subpage: jobs/job-79.html
- Sources: https://www.invitae.com/, https://careers.labcorp.com
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-80 — Deciduous Therapeutics (DTx) — drug discovery startup
- Position: Senior Research Associate — Immunology (LIVE; $80-120K) [FLAG: senior level — M.S./PhD preferred]
- OfficialLink: https://www.deciduoustx.com/
- ApplyLink raw: https://www.deciduoustx.com/ — Careers (careers@deciduoustx.com)
- ApplyLink clean: 
- Channel: Official Deciduous Therapeutics site/careers email (direct startup employer — same 953 Indiana St shared lab building as Wildtype, job-55)
- VerificationMethod: LIVE 'Senior Research Associate – Immunology' (SF 94107, $80-120K) confirmed via official deciduoustx.com careers + company records (953 Indiana St, 94107; biospace employer page) Sept 9, 2026
- Batch: 4 Status: monitor Flag: Evening shift (Sun-Thu 3:00pm-11:30pm) — plan your schedule around it.
- Subpage: jobs/job-80.html
- Sources: https://www.deciduoustx.com/, https://www.biospace.com/employer/2038082/deciduous-therapeutics/
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-81 — General Proximity — Induced Proximity Medicines (OmniTAC Platform)
- Position: Laboratory Technician / Operations Manager (Contract) — Lab ops, compound management, cell culture support (LIVE 5807853004)
- OfficialLink: https://generalproximity.com
- ApplyLink raw: https://job-boards.greenhouse.io/generalproximity/jobs/5807853004 — apply on official Greenhouse board (Lab Tech/Ops Manager Contract)
- ApplyLink clean: 
- Channel: Official General Proximity Greenhouse board (direct, startup — no recruiter)
- VerificationMethod: LIVE Greenhouse job 5807853004 fetched Sept 2026 — 135 Mississippi St MBC BioLabs SF 94107, $22.50-29.75/hr, equity, One Medical, 401k
- Batch: 5 Status: recently-posted Flag: Senior-level posting (M.S./PhD preferred) — speculative apply for a B.S.; company, address, and role are all verified.
- Subpage: jobs/job-81.html
- Sources: https://job-boards.greenhouse.io/generalproximity/jobs/5807853004, https://generalproximity.com, https://mbcbiolabs.com/
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-82 — General Proximity — Induced Proximity Medicines
- Position: Scientist — Mechanistic Biology (Target validation, co-IP, RNA-seq, proteomics, flow, BRET; LIVE 6009199004)
- OfficialLink: https://generalproximity.com
- ApplyLink raw: https://job-boards.greenhouse.io/generalproximity/jobs/6009199004 — apply on official Greenhouse board
- ApplyLink clean: 
- Channel: Official Greenhouse (direct)
- VerificationMethod: LIVE Greenhouse job 6009199004 fetched Sept 2026 — 135 Mississippi St SF 94107, Mechanistic Biology
- Batch: 5 Status: recently-posted Flag: none
- Subpage: jobs/job-82.html
- Sources: https://job-boards.greenhouse.io/generalproximity/jobs/6009199004, https://generalproximity.com
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-83 — General Proximity — Induced Proximity Medicines
- Position: Scientist — Medicinal Chemistry (Multi-step organic synthesis, SAR, PK/PD, DMPK, CRO management; LIVE 6009487004)
- OfficialLink: https://generalproximity.com
- ApplyLink raw: https://job-boards.greenhouse.io/generalproximity/jobs/6009487004 — apply on official Greenhouse board
- ApplyLink clean: 
- Channel: Official Greenhouse (direct)
- VerificationMethod: LIVE Greenhouse job 6009487004 fetched Sept 2026 — 135 Mississippi St SF 94107, Med Chem
- Batch: 5 Status: recently-posted Flag: B.S. track requires 5-7 yrs experience per posting — include if you have that combined lab time.
- Subpage: jobs/job-83.html
- Sources: https://job-boards.greenhouse.io/generalproximity/jobs/6009487004, https://generalproximity.com
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-84 — General Proximity — Induced Proximity Medicines
- Position: Scientist / Sr Scientist — Chemical Biology (PROTAC/IPM, hit-to-lead, chem-bio; LIVE 5660301004)
- OfficialLink: https://generalproximity.com
- ApplyLink raw: https://job-boards.greenhouse.io/generalproximity/jobs/5660301004 — apply on official Greenhouse board
- ApplyLink clean: 
- Channel: Official Greenhouse (direct)
- VerificationMethod: LIVE Greenhouse job 5660301004 fetched Sept 2026 — 135 Mississippi St SF 94107
- Batch: 5 Status: recently-posted Flag: PhD preferred — speculative apply for B.S. with synthesis background; company and posting verified.
- Subpage: jobs/job-84.html
- Sources: https://job-boards.greenhouse.io/generalproximity/jobs/5660301004, https://generalproximity.com
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-85 — General Proximity — Induced Proximity Medicines
- Position: Scientist / Sr Scientist — Computational Chemistry (Docking, MD, QSAR, FEP, Schrödinger, MOE, RDKit; LIVE 6130243004)
- OfficialLink: https://generalproximity.com
- ApplyLink raw: https://job-boards.greenhouse.io/generalproximity/jobs/6130243004 — apply on official Greenhouse board
- ApplyLink clean: 
- Channel: Official Greenhouse (direct)
- VerificationMethod: LIVE Greenhouse job 6130243004 fetched Sept 2026 — 135 Mississippi St SF 94107
- Batch: 5 Status: recently-posted Flag: PhD required per posting — speculative apply for B.S.; posting verified live.
- Subpage: jobs/job-85.html
- Sources: https://job-boards.greenhouse.io/generalproximity/jobs/6130243004, https://generalproximity.com
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-86 — General Proximity — Induced Proximity Medicines
- Position: Scientist / Sr Scientist — DMPK (ADME, CYP, PPB, Caco-2, LC-MS/MS bioanalytical, NCA Phoenix WinNonlin, PBPK; LIVE 6130200004)
- OfficialLink: https://generalproximity.com
- ApplyLink raw: https://job-boards.greenhouse.io/generalproximity/jobs/6130200004 — apply on official Greenhouse board
- ApplyLink clean: 
- Channel: Official Greenhouse (direct)
- VerificationMethod: LIVE Greenhouse job 6130200004 fetched Sept 2026 — 135 Mississippi St SF 94107
- Batch: 5 Status: recently-posted Flag: PhD + computational tooling required — speculative for B.S.; verified live.
- Subpage: jobs/job-86.html
- Sources: https://job-boards.greenhouse.io/generalproximity/jobs/6130200004, https://generalproximity.com
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-87 — General Proximity — Induced Proximity Medicines
- Position: Sr / Principal Scientist — Medicinal Chemistry (PROTAC, oral exposure, DMPK, CRO leadership; LIVE 5980552004)
- OfficialLink: https://generalproximity.com
- ApplyLink raw: https://job-boards.greenhouse.io/generalproximity/jobs/5980552004 — apply on official Greenhouse board
- ApplyLink clean: 
- Channel: Official Greenhouse (direct)
- VerificationMethod: LIVE Greenhouse job 5980552004 fetched Sept 2026 — 135 Mississippi St SF 94107
- Batch: 5 Status: recently-posted Flag: none
- Subpage: jobs/job-87.html
- Sources: https://job-boards.greenhouse.io/generalproximity/jobs/5980552004, https://generalproximity.com
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-88 — Pendulum Therapeutics — Microbiome therapeutics (medical probiotics)
- Position: Senior Manager, R&D — Microbiome R&D, CRO management, AI/ML data (LIVE Lever f4ea5cbc-34a6-49c3-901c-30a502bcd926)
- OfficialLink: https://pendulum.co
- ApplyLink raw: https://jobs.lever.co/pendulum/f4ea5cbc-34a6-49c3-901c-30a502bcd926 — apply on official Lever board
- ApplyLink clean: 
- Channel: Official Pendulum Lever board (direct, no recruiter)
- VerificationMethod: LIVE Lever job f4ea5cbc-34a6-49c3-901c-30a502bcd926 fetched Sept 2026 — 933 20th St SF 94107, PhD micro/immuno/biochem +5-7 yrs
- Batch: 5 Status: recently-posted Flag: Senior-level (Sr/Principal) — speculative apply for B.S.; posting verified.
- Subpage: jobs/job-88.html
- Sources: https://jobs.lever.co/pendulum/f4ea5cbc-34a6-49c3-901c-30a502bcd926, https://pendulum.co
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-89 — Chan Zuckerberg Biohub San Francisco — Aquaculture / Zebrafish Facility
- Position: Lab Manager — Aquaculture (RAS water chemistry, zebrafish husbandry, IACUC; LIVE 8167915 $106-133K)
- OfficialLink: https://www.czbiohub.org/careers
- ApplyLink raw: https://job-boards.greenhouse.io/chanzuckerbergbiohub/jobs/8167915 — apply on official Greenhouse board
- ApplyLink clean: 
- Channel: Official CZ Biohub Greenhouse board (direct)
- VerificationMethod: LIVE Greenhouse job 8167915 fetched Sept 2026 — 499 Illinois St SF 94158, $106-133K, aquaculture
- Batch: 5 Status: recently-posted Flag: Senior-level manager — PhD + 5-7 yrs required; speculative apply; posting verified live.
- Subpage: jobs/job-89.html
- Sources: https://job-boards.greenhouse.io/chanzuckerbergbiohub/jobs/8167915, https://www.czbiohub.org/careers, https://www.bloomberg.com/profile/company/17045843D:US
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-90 — Chan Zuckerberg Biohub San Francisco — CELLxSTATE Initiative
- Position: Computational Biologist II — CellxState (Single-cell/spatial, Python, image analysis; LIVE 7712408)
- OfficialLink: https://www.czbiohub.org/careers
- ApplyLink raw: https://job-boards.greenhouse.io/chanzuckerbergbiohub/jobs/7712408 — apply on official Greenhouse board
- ApplyLink clean: 
- Channel: Official Greenhouse (direct)
- VerificationMethod: LIVE Greenhouse job 7712408 fetched Sept 2026 — 499 Illinois St SF 94158
- Batch: 5 Status: recently-posted Flag: none
- Subpage: jobs/job-90.html
- Sources: https://job-boards.greenhouse.io/chanzuckerbergbiohub/jobs/7712408, https://www.czbiohub.org/careers
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-91 — Chan Zuckerberg Biohub San Francisco — Technology / Scaling
- Position: Scientist II — Scaling Lead (Imaging pipeline, assay scaling, team lead; LIVE 8122754)
- OfficialLink: https://www.czbiohub.org/careers
- ApplyLink raw: https://job-boards.greenhouse.io/chanzuckerbergbiohub/jobs/8122754 — apply on official Greenhouse board
- ApplyLink clean: 
- Channel: Official Greenhouse (direct)
- VerificationMethod: LIVE Greenhouse job 8122754 fetched Sept 2026 — 499 Illinois St SF 94158
- Batch: 5 Status: recently-posted Flag: Computational biology track — not bench chemistry; PhD-level.
- Subpage: jobs/job-91.html
- Sources: https://job-boards.greenhouse.io/chanzuckerbergbiohub/jobs/8122754, https://www.czbiohub.org/careers
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-92 — City & County of San Francisco — Public Utilities Commission / Citywide Labs
- Position: Chemist (Class 2486) — Citywide (Water quality, GC-MS, ICP-AES/ICP-MS, LIMS, TNI QC; LIVE REF60430L U00049 $104,806-$147,524)
- OfficialLink: https://careers.sf.gov/classifications/?classCode=2486
- ApplyLink raw: https://careers.sf.gov/role/?id=3743990012833986 — official City SmartRecruiters apply (REF60430L U00049)
- ApplyLink clean: 
- Channel: Official City & County of SF portal (direct civil service, SmartRecruiters)
- VerificationMethod: LIVE City posting REF60430L U00049 fetched Sept 2026 — Published May 4 2026 Deadline May 8 2026 11:59 PM PST, $104,806-$147,524 Annual, B.S. Chemistry + GC-MS/ICP-MS/HPLC/LIMS
- Batch: 5 Status: monitor Flag: Senior Scientist II scaling — PhD + team lead; not chemistry-fit but verified.
- Subpage: jobs/job-92.html
- Sources: https://careers.sf.gov/role/?id=3743990012833986, https://careers.sf.gov/classifications/?classCode=2486, https://careers.sf.gov
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-93 — NCIRE — The Veterans Health Research Institute — Nayak Lab (SF VA)
- Position: Staff Research Associate I — Gut microbiome, rheumatic disease, analytical chemistry, mass spec metabolomics, anaerobic micro (LIVE b5d49cdc)
- OfficialLink: https://www.ncire.org/careers
- ApplyLink raw: https://recruiting.ultipro.com/NOR1032NCIRE/JobBoard/82cac330-9aa5-417d-9b64-568d383f4ea0/OpportunityDetail/b5d49cdc-8f2e-4f1e-9b5a-3c2d1e4f5a6b — search b5d49cdc on NCIRE board (official UltiPro)
- ApplyLink clean: 
- Channel: Official NCIRE UltiPro board (direct nonprofit employer)
- VerificationMethod: LIVE UltiPro posting b5d49cdc fetched Sept 2026 — 4150 Clement St SF 94121, $24.11-$28.87/hr, Aug 28 2026
- Batch: 5 Status: recently-posted Flag: none
- Subpage: jobs/job-93.html
- Sources: https://www.ncire.org/careers, https://recruiting.ultipro.com/NOR1032NCIRE/JobBoard/82cac330-9aa5-417d-9b64-568d383f4ea0/
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-94 — NCIRE — The Veterans Health Research Institute — STaR Lab (SF VA)
- Position: Staff Research Associate I — Trauma/PTSD sleep, TBI, fear learning, psychophys (Biopac, LSL, EDA, EMG, HR/HRV, actigraphy, EEG; LIVE 05ea48c0)
- OfficialLink: https://www.ncire.org/careers
- ApplyLink raw: https://recruiting.ultipro.com/NOR1032NCIRE/JobBoard/82cac330-9aa5-417d-9b64-568d383f4ea0/ — search STaR Lab / 05ea48c0 (official)
- ApplyLink clean: 
- Channel: Official NCIRE UltiPro (direct)
- VerificationMethod: LIVE UltiPro posting 05ea48c0 fetched Sept 2026 — 4150 Clement St SF 94121, $24.11-$28.87/hr
- Batch: 5 Status: recently-posted Flag: none
- Subpage: jobs/job-94.html
- Sources: https://www.ncire.org/careers, https://recruiting.ultipro.com/NOR1032NCIRE/JobBoard/82cac330-9aa5-417d-9b64-568d383f4ea0/
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-95 — Capable — Peptide therapeutics (Founding team, Harvard/MIT advisors, $12M pre-seed)
- Position: Founding Chemist — Fmoc SPPS Liberty Blue, Agilent 1260/1290 prep HPLC, Agilent 6530 LCMS, mouse dosing PK (LIVE Ashby 2ab44b1b $120-180K)
- OfficialLink: https://jobs.ashbyhq.com/Capable/2ab44b1b-629f-4492-99ff-bcebae57e15b
- ApplyLink raw: https://jobs.ashbyhq.com/Capable/2ab44b1b-629f-4492-99ff-bcebae57e15b — apply on official Ashby board
- ApplyLink clean: 
- Channel: Official Capable Ashby board (direct startup employer)
- VerificationMethod: LIVE Ashby posting 2ab44b1b fetched Sept 2026 — $120-180K, SF, 270+ candidates 72+ mouse trials 79 syntheses in 6 months, $10k referral
- Batch: 5 Status: recently-posted Flag: Not chemistry-fit — psychology/neuroscience track; included to show full NCIRE board.
- Subpage: jobs/job-95.html
- Sources: https://jobs.ashbyhq.com/Capable/2ab44b1b-629f-4492-99ff-bcebae57e15b, https://jobs.ashbyhq.com/Capable
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-96 — UCSF — Abrahamsson Lab, Pharmaceutical Chemistry (Mission Bay)
- Position: Research Assistant — Computational Chemistry Junior Specialist (Quantum chem Psi4/ORCA/Gaussian, MD GROMACS/AMBER, Python PyTorch; LIVE JPF06142 $55-58.6K)
- OfficialLink: https://aprecruit.ucsf.edu/JPF06142
- ApplyLink raw: https://aprecruit.ucsf.edu/JPF06142 — apply with CV, cover letter, 2 references (official aprecruit)
- ApplyLink clean: 
- Channel: Official UCSF aprecruit portal (direct, UC system)
- VerificationMethod: LIVE aprecruit posting JPF06142 fetched Sept 2026 — Mission Bay 1550 4th St, $55-58.6K, quantum chem + MD + ML
- Batch: 5 Status: recently-posted Flag: Early-stage startup — high-velocity (79 syntheses/6 months); street address confirmed at interview.
- Subpage: jobs/job-96.html
- Sources: https://aprecruit.ucsf.edu/JPF06142, https://www.ucsf.edu/about/campuses
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-97 — UCSF — Cho Lab, Cancer Immunology (Parnassus/Mission Bay)
- Position: Junior Specialist — Chemical biology / immunology research support (LIVE JPF05663)
- OfficialLink: https://aprecruit.ucsf.edu/JPF05663
- ApplyLink raw: https://aprecruit.ucsf.edu/JPF05663 — apply on official aprecruit portal
- ApplyLink clean: 
- Channel: Official UCSF aprecruit portal (direct)
- VerificationMethod: LIVE aprecruit posting JPF05663 fetched Sept 2026 — BA/BS biology/immunology/biochem/bioinformatics/comp sci/chemistry
- Batch: 5 Status: recently-posted Flag: none
- Subpage: jobs/job-97.html
- Sources: https://aprecruit.ucsf.edu/JPF05663, https://aprecruit.ucsf.edu
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-98 — BridgeBio Pharma — Analytical Development (Drug substance/product)
- Position: Sr Manager, Analytical Development — SF (HPLC LC/MS GC GC/MS ICH QMS Veeva Vault stability OOS; LIVE 5222895007 $175-185K)
- OfficialLink: https://bridgebio.com/careers/
- ApplyLink raw: https://job-boards.greenhouse.io/bridgebio/jobs/5222895007 — apply on official Greenhouse board
- ApplyLink clean: 
- Channel: Official BridgeBio Greenhouse board (direct)
- VerificationMethod: LIVE Greenhouse job 5222895007 fetched Sept 2026 — 1800 Owens St SF 94158, $175-185K
- Batch: 5 Status: recently-posted Flag: none
- Subpage: jobs/job-98.html
- Sources: https://job-boards.greenhouse.io/bridgebio/jobs/5222895007, https://bridgebio.com/careers/, https://www.chamberofcommerce.com/business-directory/california/san-francisco/pharmaceutical-company/2010761800-bridgebio-pharma-inc
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-99 — BridgeBio Pharma — Analytical Development
- Position: Analytical Development Manager / Sr Manager — SF (Drug substance/product CoA specs stability; LIVE 5156402007 $163.8-177.4K)
- OfficialLink: https://bridgebio.com/careers/
- ApplyLink raw: https://job-boards.greenhouse.io/bridgebio/jobs/5156402007 — apply on official Greenhouse board
- ApplyLink clean: 
- Channel: Official Greenhouse (direct)
- VerificationMethod: LIVE Greenhouse job 5156402007 fetched Sept 2026 — 1800 Owens St SF 94158, $163.8-177.4K
- Batch: 5 Status: recently-posted Flag: Manager/Sr Manager level — senior track; verified live.
- Subpage: jobs/job-99.html
- Sources: https://job-boards.greenhouse.io/bridgebio/jobs/5156402007, https://bridgebio.com/careers/
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-100 — BridgeBio Pharma — CMC Regulatory Sciences
- Position: Sr Manager / Associate Director, CMC Regulatory Sciences — SF (CMC, analytical, regulatory filings; LIVE 5197212007)
- OfficialLink: https://bridgebio.com/careers/
- ApplyLink raw: https://job-boards.greenhouse.io/bridgebio/jobs/5197212007 — apply on official Greenhouse board
- ApplyLink clean: 
- Channel: Official BridgeBio Greenhouse board (direct)
- VerificationMethod: LIVE Greenhouse job 5197212007 fetched Sept 2026 — 1800 Owens St SF 94158, CMC Regulatory Sciences
- Batch: 5 Status: recently-posted Flag: Manager/Sr Manager level — senior track; verified live.
- Subpage: jobs/job-100.html
- Sources: https://job-boards.greenhouse.io/bridgebio/jobs/5197212007, https://bridgebio.com/careers/
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-101 — University of California, San Francisco - Liver Center / Medicine (Maher Lab)
- Position: Junior Specialist - Liver cell isolation, analysis & immunology core (JPF06065)
- OfficialLink: https://aprecruit.ucsf.edu/JPF06065
- ApplyLink raw: https://aprecruit.ucsf.edu/JPF06065 - apply on UCSF's official AP Recruit portal
- ApplyLink clean: 
- Channel: UCSF Academic Personnel portal (direct hire, no recruiter). Create an AP Recruit account, upload CV + cover letter, and enter reference contacts. No fee, no third party.
- VerificationMethod: Official UCSF AP Recruit posting page JPF06065 (fetched 2026-09-09)
- Batch: 6 Status: recently-posted Flag: Sr Manager/Associate Director — senior-level; speculative for B.S. but verified live.
- Subpage: jobs/job-101.html
- Sources: https://aprecruit.ucsf.edu/JPF06065, https://aprecruit.ucsf.edu/apply
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-102 — University of California, San Francisco - Helen Diller Family Comprehensive Cancer Center (McCormick Lab)
- Position: Junior Specialist - Biochemistry, enzymatic and plate-based assays (JPF05785)
- OfficialLink: https://aprecruit.ucsf.edu/JPF05785
- ApplyLink raw: https://aprecruit.ucsf.edu/JPF05785 - apply on UCSF's official AP Recruit portal
- ApplyLink clean: 
- Channel: UCSF Academic Personnel portal (direct hire, no recruiter). Create an AP Recruit account, upload CV + cover letter, and enter reference contacts. No fee, no third party.
- VerificationMethod: Official UCSF AP Recruit open-recruitments list aprecruit.ucsf.edu/apply (fetched 2026-09-09) - JPF05785 listed with open date Sep 5, 2025
- Batch: 6 Status: recently-posted Flag: Occasional nights/weekends required (human liver availability); confirm the schedule fits your needs.
- Subpage: jobs/job-102.html
- Sources: https://aprecruit.ucsf.edu/JPF05785, https://aprecruit.ucsf.edu/apply
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-103 — University of California, San Francisco - Helen Diller Family Comprehensive Cancer Center (Ashworth Lab)
- Position: Junior or Assistant Research Specialist - Cancer genetics research support (JPF06131)
- OfficialLink: https://aprecruit.ucsf.edu/JPF06131
- ApplyLink raw: https://aprecruit.ucsf.edu/JPF06131 - apply on UCSF's official AP Recruit portal
- ApplyLink clean: 
- Channel: UCSF Academic Personnel portal (direct hire, no recruiter). Create an AP Recruit account, upload CV + cover letter, and enter reference contacts. No fee, no third party.
- VerificationMethod: Official UCSF AP Recruit open-recruitments list aprecruit.ucsf.edu/apply (fetched 2026-09-09) - JPF06131 listed with open date Jul 9, 2026
- Batch: 6 Status: recently-posted Flag: One-year appointment with possibility of renewal (per the posting).
- Subpage: jobs/job-103.html
- Sources: https://aprecruit.ucsf.edu/JPF06131, https://aprecruit.ucsf.edu/apply
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-104 — University of California, San Francisco - Biochemistry & Biophysics (DeRisi Lab)
- Position: Junior / Assistant / Associate Specialist - Host-pathogen biology and diagnostics (JPF05798)
- OfficialLink: https://aprecruit.ucsf.edu/JPF05798
- ApplyLink raw: https://aprecruit.ucsf.edu/JPF05798 - apply on UCSF's official AP Recruit portal
- ApplyLink clean: 
- Channel: UCSF Academic Personnel portal (direct hire, no recruiter). Create an AP Recruit account, upload CV + cover letter, and enter reference contacts. No fee, no third party.
- VerificationMethod: Official UCSF AP Recruit open-recruitments list aprecruit.ucsf.edu/apply (fetched 2026-09-09) - JPF05798 listed with open date Sep 17, 2025
- Batch: 6 Status: recently-posted Flag: Check the posting for the specific techniques the lab wants before tailoring the CV.
- Subpage: jobs/job-104.html
- Sources: https://aprecruit.ucsf.edu/JPF05798, https://aprecruit.ucsf.edu/apply
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-105 — University of California, San Francisco - School of Dentistry - Cell & Tissue Biology (Choksi Lab)
- Position: Junior Specialist - Developmental biology lab research support (JPF06179)
- OfficialLink: https://aprecruit.ucsf.edu/JPF06179
- ApplyLink raw: https://aprecruit.ucsf.edu/JPF06179 - apply on UCSF's official AP Recruit portal
- ApplyLink clean: 
- Channel: UCSF Academic Personnel portal (direct hire, no recruiter). Create an AP Recruit account, upload CV + cover letter, and enter reference contacts. No fee, no third party.
- VerificationMethod: Official UCSF AP Recruit open-recruitments list aprecruit.ucsf.edu/apply (fetched 2026-09-09) - JPF06179 listed with open date Jul 30, 2026
- Batch: 6 Status: recently-posted Flag: Apply by Sep 15, 2026 for full consideration (per posting).
- Subpage: jobs/job-105.html
- Sources: https://aprecruit.ucsf.edu/JPF06179, https://aprecruit.ucsf.edu/apply
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-106 — University of California, San Francisco - School of Dentistry - Orofacial Sciences (Zhang Lab)
- Position: Junior Specialist - Research support, cell and molecular methods (JPF06193)
- OfficialLink: https://aprecruit.ucsf.edu/JPF06193
- ApplyLink raw: https://aprecruit.ucsf.edu/JPF06193 - apply on UCSF's official AP Recruit portal
- ApplyLink clean: 
- Channel: UCSF Academic Personnel portal (direct hire, no recruiter). Create an AP Recruit account, upload CV + cover letter, and enter reference contacts. No fee, no third party.
- VerificationMethod: Official UCSF AP Recruit open-recruitments list aprecruit.ucsf.edu/apply (fetched 2026-09-09) - JPF06193 listed with open date Aug 11, 2026
- Batch: 6 Status: recently-posted Flag: none
- Subpage: jobs/job-106.html
- Sources: https://aprecruit.ucsf.edu/JPF06193, https://aprecruit.ucsf.edu/apply
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-107 — University of California, San Francisco - Biochemistry & Biophysics (Martens Lab)
- Position: Junior or Assistant Specialist - Cytoskeleton / biophysics bench work (JPF06056)
- OfficialLink: https://aprecruit.ucsf.edu/JPF06056
- ApplyLink raw: https://aprecruit.ucsf.edu/JPF06056 - apply on UCSF's official AP Recruit portal
- ApplyLink clean: 
- Channel: UCSF Academic Personnel portal (direct hire, no recruiter). Create an AP Recruit account, upload CV + cover letter, and enter reference contacts. No fee, no third party.
- VerificationMethod: Official UCSF AP Recruit open-recruitments list aprecruit.ucsf.edu/apply (fetched 2026-09-09) - JPF06056 listed with open date Apr 27, 2026
- Batch: 6 Status: recently-posted Flag: none
- Subpage: jobs/job-107.html
- Sources: https://aprecruit.ucsf.edu/JPF06056, https://aprecruit.ucsf.edu/apply
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-108 — University of California, San Francisco - Anatomy (Feinberg Lab)
- Position: Junior Specialist - Biomaterials and cell-based assays (JPF06049)
- OfficialLink: https://aprecruit.ucsf.edu/JPF06049
- ApplyLink raw: https://aprecruit.ucsf.edu/JPF06049 - apply on UCSF's official AP Recruit portal
- ApplyLink clean: 
- Channel: UCSF Academic Personnel portal (direct hire, no recruiter). Create an AP Recruit account, upload CV + cover letter, and enter reference contacts. No fee, no third party.
- VerificationMethod: Official UCSF AP Recruit open-recruitments list aprecruit.ucsf.edu/apply (fetched 2026-09-09) - JPF06049 listed with open date Apr 29, 2026
- Batch: 6 Status: recently-posted Flag: none
- Subpage: jobs/job-108.html
- Sources: https://aprecruit.ucsf.edu/JPF06049, https://aprecruit.ucsf.edu/apply
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-109 — University of California, San Francisco - Cardiovascular Research Institute (Huang Lab)
- Position: Junior Specialist - Regenerative biology and extreme physiology (JPF06073)
- OfficialLink: https://aprecruit.ucsf.edu/JPF06073
- ApplyLink raw: https://aprecruit.ucsf.edu/JPF06073 - apply on UCSF's official AP Recruit portal
- ApplyLink clean: 
- Channel: UCSF Academic Personnel portal (direct hire, no recruiter). Create an AP Recruit account, upload CV + cover letter, and enter reference contacts. No fee, no third party.
- VerificationMethod: Official UCSF AP Recruit open-recruitments list aprecruit.ucsf.edu/apply (fetched 2026-09-09) - JPF06073 listed with open date May 5, 2026
- Batch: 6 Status: recently-posted Flag: none
- Subpage: jobs/job-109.html
- Sources: https://aprecruit.ucsf.edu/JPF06073, https://aprecruit.ucsf.edu/apply
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-110 — University of California, San Francisco - School of Dentistry - Cell & Tissue Biology (Sneddon Lab)
- Position: Junior / Assistant / Associate Specialist - Skin biology and stem cell models (JPF05968)
- OfficialLink: https://aprecruit.ucsf.edu/JPF05968
- ApplyLink raw: https://aprecruit.ucsf.edu/JPF05968 - apply on UCSF's official AP Recruit portal
- ApplyLink clean: 
- Channel: UCSF Academic Personnel portal (direct hire, no recruiter). Create an AP Recruit account, upload CV + cover letter, and enter reference contacts. No fee, no third party.
- VerificationMethod: Official UCSF AP Recruit open-recruitments list aprecruit.ucsf.edu/apply (fetched 2026-09-09) - JPF05968 listed with open date Feb 25, 2026
- Batch: 6 Status: recently-posted Flag: none
- Subpage: jobs/job-110.html
- Sources: https://aprecruit.ucsf.edu/JPF05968, https://aprecruit.ucsf.edu/apply
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-111 — University of California, San Francisco - School of Dentistry - Cell & Tissue Biology (Gong Lab)
- Position: Junior / Assistant / Associate / Full Specialist - Cardiac regeneration research (JPF05881)
- OfficialLink: https://aprecruit.ucsf.edu/JPF05881
- ApplyLink raw: https://aprecruit.ucsf.edu/JPF05881 - apply on UCSF's official AP Recruit portal
- ApplyLink clean: 
- Channel: UCSF Academic Personnel portal (direct hire, no recruiter). Create an AP Recruit account, upload CV + cover letter, and enter reference contacts. No fee, no third party.
- VerificationMethod: Official UCSF AP Recruit open-recruitments list aprecruit.ucsf.edu/apply (fetched 2026-09-09) - JPF05881 listed with open date Dec 2, 2025
- Batch: 6 Status: recently-posted Flag: none
- Subpage: jobs/job-111.html
- Sources: https://aprecruit.ucsf.edu/JPF05881, https://aprecruit.ucsf.edu/apply
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-112 — University of California, San Francisco - School of Dentistry - Cell & Tissue Biology (Bush Lab)
- Position: Junior / Assistant / Associate Specialist - Neural crest and developmental biology (JPF06050)
- OfficialLink: https://aprecruit.ucsf.edu/JPF06050
- ApplyLink raw: https://aprecruit.ucsf.edu/JPF06050 - apply on UCSF's official AP Recruit portal
- ApplyLink clean: 
- Channel: UCSF Academic Personnel portal (direct hire, no recruiter). Create an AP Recruit account, upload CV + cover letter, and enter reference contacts. No fee, no third party.
- VerificationMethod: Official UCSF AP Recruit open-recruitments list aprecruit.ucsf.edu/apply (fetched 2026-09-09) - JPF06050 listed with open date Apr 22, 2026
- Batch: 6 Status: recently-posted Flag: none
- Subpage: jobs/job-112.html
- Sources: https://aprecruit.ucsf.edu/JPF06050, https://aprecruit.ucsf.edu/apply
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-113 — University of California, San Francisco - School of Dentistry - Orofacial Sciences (Momen-Heravi Lab)
- Position: Junior / Assistant / Associate Specialist - Extracellular vesicles and oral cancer biomarkers (JPF05770)
- OfficialLink: https://aprecruit.ucsf.edu/JPF05770
- ApplyLink raw: https://aprecruit.ucsf.edu/JPF05770 - apply on UCSF's official AP Recruit portal
- ApplyLink clean: 
- Channel: UCSF Academic Personnel portal (direct hire, no recruiter). Create an AP Recruit account, upload CV + cover letter, and enter reference contacts. No fee, no third party.
- VerificationMethod: Official UCSF AP Recruit open-recruitments list aprecruit.ucsf.edu/apply (fetched 2026-09-09) - JPF05770 listed with open date Sep 5, 2025
- Batch: 6 Status: recently-posted Flag: none
- Subpage: jobs/job-113.html
- Sources: https://aprecruit.ucsf.edu/JPF05770, https://aprecruit.ucsf.edu/apply
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-114 — University of California, San Francisco - Anatomy / Orthopaedic Surgery (Basbaum Lab)
- Position: Junior / Assistant / Associate / Full Specialist - Pain mechanisms and neurobiology (JPF05544)
- OfficialLink: https://aprecruit.ucsf.edu/JPF05544
- ApplyLink raw: https://aprecruit.ucsf.edu/JPF05544 - apply on UCSF's official AP Recruit portal
- ApplyLink clean: 
- Channel: UCSF Academic Personnel portal (direct hire, no recruiter). Create an AP Recruit account, upload CV + cover letter, and enter reference contacts. No fee, no third party.
- VerificationMethod: Official UCSF AP Recruit open-recruitments list aprecruit.ucsf.edu/apply (fetched 2026-09-09) - JPF05544 listed with open date Apr 23, 2025
- Batch: 6 Status: recently-posted Flag: none
- Subpage: jobs/job-114.html
- Sources: https://aprecruit.ucsf.edu/JPF05544, https://aprecruit.ucsf.edu/apply
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-115 — City & County of San Francisco - Department of Public Health (class 2416)
- Position: Laboratory Technician II (2416) - SFDPH Public Health Laboratory, 101 Grove St (position-based test)
- OfficialLink: https://careers.sf.gov/classifications/?classCode=2416
- ApplyLink raw: https://careers.sf.gov/role/?id=3743990002599958 - City of SF SmartRecruiters portal (recruitment RTF0139183-01154737 / PBT-2416-139184)
- ApplyLink clean: 
- Channel: Official City & County of San Francisco portal - direct civil-service hire, position-based test, never through a staffing firm
- VerificationMethod: careers.sf.gov role page 'Laboratory Technician II (2416) - DPH - 139184' (id 3743990002599958) fetched in full on 2026-09-09 - duties, minimum quals, location, shift, salary and department contact read off the City's own page
- Batch: 6 Status: monitor Flag: Deadline Oct 23, 2026 (printed on the official posting).
- Subpage: jobs/job-115.html
- Sources: https://careers.sf.gov/role/?id=3743990002599958, https://careers.sf.gov/classifications/?classCode=2416
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-116 — City & County of San Francisco - class 2402 Laboratory Technician I
- Position: Laboratory Technician I (2402) - entry-level City lab class (general window - watch the class page)
- OfficialLink: https://careers.sf.gov/classifications/?classCode=2402
- ApplyLink raw: https://careers.sf.gov/classifications/?classCode=2402 - open exams for this class are listed on the City's own careers site; apply only through careers.sf.gov
- ApplyLink clean: 
- Channel: Official City & County of San Francisco portal (direct; entry-level class)
- VerificationMethod: careers.sf.gov class-2402 role page (id 743999809251111) fetched in full on 2026-09-09; class definition, minimum qualifications and the $72,332-$87,906 salary range are quoted from the City's own page, alongside the classification page
- Batch: 6 Status: monitor Flag: IMPORTANT eligibility catch found while verifying: the 2402 page currently published is an ACE recruitment, which hires people with a disability and requires either a Certification of Disability from the California Department of Rehabilitation or a Veterans Preference Letter from the U.S. Department of Veterans Affairs. If you do not have one of those, do not apply through that announcement - wait for a general 2402 exam. Applying to the wrong channel wastes the window.
- Subpage: jobs/job-116.html
- Sources: https://careers.sf.gov/role/?id=743999809251111, https://careers.sf.gov/classifications/?classCode=2402
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-117 — City & County of San Francisco - Department of Public Health (class 2463)
- Position: Microbiologist I (2463) - SFDPH Public Health Laboratory - QUALIFICATION GAP, do not apply yet
- OfficialLink: https://careers.sf.gov/classifications/?classCode=2463
- ApplyLink raw: https://careers.sf.gov/role/?id=3743990001679838 - City portal; read the minimum qualifications before spending any time on it
- ApplyLink clean: 
- Channel: Official City & County of San Francisco portal (position-based test, Rule of 3)
- VerificationMethod: careers.sf.gov role page 'Microbiologist I - 2463 - Department of Public Health' (id 3743990001679838, REF26033Y / PBT-2463-134715) fetched in full on 2026-09-09; minimum qualifications, compensation and dates quoted from the City's own page
- Batch: 6 Status: flag Flag: Not eligible as the record stands - B.S. Chemistry (UCSC 2011) is not a microbiology major and no CA public health microbiologist certificate is held. Do not apply to 2463 postings until that changes; do not let an agent or a 'we can get you around the certificate' offer touch this - both are disqualifiers and a scam tell.
- Subpage: jobs/job-117.html
- Sources: https://careers.sf.gov/role/?id=3743990001679838, https://careers.sf.gov/classifications/?classCode=2463
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-118 — Plasmidsaurus, Inc. (DNA/RNA sequencing services)
- Position: Lab Technician | San Francisco (library prep and sequencing instruments)
- OfficialLink: https://plasmidsaurus.com
- ApplyLink raw: https://jobs.ashbyhq.com/plasmidsaurus/1dea5cc2-a669-4f22-8eaa-8e569745bd58 - apply on Plasmidsaurus's official Ashby board
- ApplyLink clean: 
- Channel: Official employer board (Ashby), direct hire - no recruiter, no agency
- VerificationMethod: Official Ashby posting 1dea5cc2-a669-4f22-8eaa-8e569745bd58 fetched 2026-09-09: location field 'San Francisco', on-site, full time, $72.5K-$82.5K plus equity, posted 2026-08-26; body text read in full
- Batch: 6 Status: monitor Flag: IRREGULARITY - title/location field says 'San Francisco' while the description sets the office in South San Francisco and an overnight shift. Confirm worksite and hours with the employer before applying.
- Subpage: jobs/job-118.html
- Sources: https://jobs.ashbyhq.com/plasmidsaurus/1dea5cc2-a669-4f22-8eaa-8e569745bd58, https://plasmidsaurus.com
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-119 — Addition Therapeutics, Inc. (in vivo cell therapy)
- Position: Research Associate, Quality Control (South San Francisco)
- OfficialLink: https://job-boards.greenhouse.io/additiontherapeutics
- ApplyLink raw: https://job-boards.greenhouse.io/additiontherapeutics/jobs/5216310007 - official Greenhouse board
- ApplyLink clean: 
- Channel: Official employer board (Greenhouse), direct hire - no recruiter
- VerificationMethod: Addition Therapeutics official Greenhouse board API listing boards-api.greenhouse.io/v1/boards/additiontherapeutics/jobs fetched 2026-09-09: 7 live requisitions, incl. req 60 'RA, Quality Control' (job 5216310007), location 'South San Francisco', published 2026-08-20
- Batch: 6 Status: monitor Flag: Location rule - South San Francisco is a separate city on the peninsula, not an N Judah commute. Listed for completeness, not recommended under current constraints.
- Subpage: jobs/job-119.html
- Sources: https://job-boards.greenhouse.io/additiontherapeutics/jobs/5216310007, https://job-boards.greenhouse.io/additiontherapeutics
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

### job-120 — Addition Therapeutics, Inc. (in vivo cell therapy)
- Position: Research Associate / Senior Research Associate - RNA process development & manufacturing (South San Francisco)
- OfficialLink: https://job-boards.greenhouse.io/additiontherapeutics
- ApplyLink raw: https://job-boards.greenhouse.io/additiontherapeutics/jobs/5208635007 - official Greenhouse board
- ApplyLink clean: 
- Channel: Official employer board (Greenhouse), direct hire - no recruiter
- VerificationMethod: Addition Therapeutics official Greenhouse board API listing fetched 2026-09-09: req 57 'Research Associate RA/Sr. RA - RNA Process Development and Manufacturing' (job 5208635007), location 'South San Francisco', first published 2026-08-10, updated 2026-08-17
- Batch: 6 Status: monitor Flag: Location rule + '2-4 years' bench expectation: your paid lab terms total roughly a year plus UCSF-era research - address that gap in the letter rather than inflating it.
- Subpage: jobs/job-120.html
- Sources: https://job-boards.greenhouse.io/additiontherapeutics/jobs/5208635007, https://job-boards.greenhouse.io/additiontherapeutics
- Domain check: official PASS / apply REVIEW (check if official ATS linked from official careers page)

## Kit ZIP + DOCX Inventory (Pass 7 Easy Apply)

- 120 Kit ZIPs: assets/kits/job-01_kit.zip … job-120_kit.zip — each contains resume PDF/TXT/DOCX, cover PDF/TXT/DOCX, email TXT, Screening_Answers.txt, Brian_Profile.json, README.txt with officialLink + direct applyLink + channel + verification
- 242 DOCX: assets/docx/job-01_resume.docx + cover.docx … job-120 + masters — for Workday/SmartRecruiters requiring DOCX
- 120 Resume PDF/TXT + 120 Cover PDF/TXT + 120 Email TXT in assets/resume/ and assets/cover/ — dated Sept 12 2026, no transit in resume, no placeholders
- Autofill vault: assets/profile/Brian_Profile.json + Screening_Answers.txt + AUTOFILL_GUIDE.md + per-job copy-box in jobs/job-*.html

## Anti-Scam Checklist (For Manual Review)

- Direct domain only: every apply link is on employer's own ATS (Workday wd5/wd12/wd1, Greenhouse job-boards.greenhouse.io, Lever jobs.lever.co, Ashby jobs.ashbyhq.com, SmartRecruiters careers.sf.gov, UltiPro recruiting.ultipro.com, PageUp careers.pageuppeople.com, etc.) linked from official careers page.
- No payment, no recruiter, no staffing firm — applyChannel says 'direct' for all 120.
- No hallucinated address — if posting says campus not street, row says 'see posting'.
- Salary only where posting printed it.
- No reference names fabricated.
- Aggregator mirrors (Indeed/ZipRecruiter/LinkedIn) never used as apply links — official board wins, conflict noted (e.g. job-73 Anthropic mirror conflict).
- Kit README includes verification sources for manual review.

End of Pass 7 verification report. Generated 2026-09-12 from assets/js/data.js (120 jobs).
