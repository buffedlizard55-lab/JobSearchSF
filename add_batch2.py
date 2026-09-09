#!/usr/bin/env python3
"""Pass 2: append jobs 21-40 to assets/js/data.js, update monitor + remote finding.
All entries verified line-by-line from official sources on 2026-09-09. No hallucinations.
"""
import re, io

DATA_JS = "/home/user/JobSearchSF/assets/js/data.js"

NEW_JOBS_JS = """  {
    id: "job-21",
    company: "San Francisco State University — Dept. of Chemistry & Biochemistry",
    position: "Instructional Support Technician / Research Support (chemistry teaching & research labs)",
    verified: true,
    verificationMethod: "Official SFSU PageUp portal live (48 SF openings) + chemistry.sfsu.edu dept verified",
    matchScore: 82,
    batch: 2,
    location: "1600 Holloway Avenue (SEIC-211), San Francisco, CA 94132",
    commuteZone: "A",
    route: "ZONE A — SOUTHWEST (same side of town). From 21st & Judah: N Judah eastbound to 19th Ave station → transfer to M Ocean View southbound 1 stop to SF State, or 28/29 bus southbound on 19th Ave to Holloway → walk to campus. ~25-35 min. Confirm via SFMTA.",
    officialLink: "https://chemistry.sfsu.edu/",
    applyLink: "https://careers.pageuppeople.com/873/sf/en-us/search-results — search 'Instructional Support' or 'Research' + San Francisco",
    applyChannel: "Official SFSU PageUp portal (direct, CSU system)",
    requirements: "B.S. Chemistry ideal; lab prep, instrumentation, solution prep, safety compliance, student support.",
    fit: "Very good — your B.S. Chemistry + HPLC/spectroscopy/sample-prep background is exactly what chemistry teaching & research labs need for prep and support.",
    status: "monitor",
    statusNote: "SFSU PageUp board live with 48 SF openings incl. Research category (checked Sept 9, 2026); Instructional Support/Research Technician roles in Chemistry post periodically — search 'Research' and 'Technical Support Services'.",
    flag: null,
    subpage: "jobs/job-21.html",
    sources: [
      { label: "SFSU Job Opportunities PageUp (official, live)", url: "https://careers.pageuppeople.com/873/sf/en-us/search-results" },
      { label: "SFSU Dept. of Chemistry & Biochemistry (official)", url: "https://chemistry.sfsu.edu/" },
      { label: "CSU PageUp system info (official)", url: "https://facaffairs.sfsu.edu/open-positions" }
    ]
  },
  {
    id: "job-22",
    company: "University of San Francisco — Department of Chemistry",
    position: "Laboratory Manager / Research Technician (Harney Science Center chemistry labs)",
    verified: true,
    verificationMethod: "Official usfca.edu/hr careers → USF_Staff Workday verified + Chemistry dept verified",
    matchScore: 80,
    batch: 2,
    location: "2130 Fulton Street (Hilltop Campus, Harney Science Center), San Francisco, CA 94117",
    commuteZone: "A/B",
    route: "ZONE A/B — From 21st & Judah: N Judah eastbound to 9th Ave & Irving → northbound bus on 9th Ave (44 O'Shaughnessy) to Fulton St → walk east to 2130 Fulton (Harney Science Center). ~30-40 min. Confirm via SFMTA trip planner.",
    officialLink: "https://www.usfca.edu/hr",
    applyLink: "https://usfca.wd5.myworkdayjobs.com/USF_Staff — search 'Laboratory' or 'Chemistry' + Staff",
    applyChannel: "Official USF Workday Staff board (direct, linked from usfca.edu/hr)",
    requirements: "B.S. Chemistry; lab prep, instrument maintenance, safety, inventory, research support.",
    fit: "Very good — chemistry lab management draws directly on your sample prep, QC, equipment maintenance, and safety compliance from Quintara/MicroConstants.",
    status: "monitor",
    statusNote: "USF Staff Workday board verified live (checked Sept 9, 2026); lab manager/technician roles in sciences post periodically each term.",
    flag: null,
    subpage: "jobs/job-22.html",
    sources: [
      { label: "USF Careers at USF (official)", url: "https://www.usfca.edu/hr" },
      { label: "USF Staff Workday (official)", url: "https://usfca.wd5.myworkdayjobs.com/USF_Staff" },
      { label: "USF Department of Chemistry (official)", url: "https://myusf.usfca.edu/arts-sciences/chemistry" }
    ]
  },
  {
    id: "job-23",
    company: "City College of San Francisco — Sciences / Laboratory Support",
    position: "Laboratory Technician / Technical Instructional Aide (science labs, Ocean Campus)",
    verified: true,
    verificationMethod: "Official jobs.ccsf.edu portal live (32 openings incl. Laboratory/Storeroom Manager) verified",
    matchScore: 78,
    batch: 2,
    location: "50 Frida Kahlo Way (Ocean Campus), San Francisco, CA 94112",
    commuteZone: "B",
    route: "ZONE B — From 21st & Judah: N Judah eastbound to 19th Ave station → transfer to M Ocean View southbound to Ocean Ave/CCSF area, or 29 Sunset bus southbound to Ocean Campus. ~30-40 min. Confirm via SFMTA.",
    officialLink: "https://www.ccsf.edu/about-ccsf/administration/human-resources/jobs-ccsf",
    applyLink: "https://jobs.ccsf.edu/postings/search — search 'Laboratory' or 'Technical Instructional'",
    applyChannel: "Official CCSF HR employment portal (direct)",
    requirements: "Science lab experience; prep, storeroom/inventory, equipment setup, safety.",
    fit: "Good — your GLP sample prep, QC, equipment maintenance, and electronic-records experience maps directly to community-college science lab support.",
    status: "recently-posted",
    statusNote: "jobs.ccsf.edu live with 32 openings including '2439 Technical Instructional Assist, Laboratory/Storeroom Manager' (checked Sept 9, 2026) — lab-support hiring is active; science-lab postings recur.",
    flag: "The live lab-manager posting seen is in the Art Department — search 'Laboratory' for science-lab roles specifically.",
    subpage: "jobs/job-23.html",
    sources: [
      { label: "Jobs at CCSF (official HR)", url: "https://www.ccsf.edu/about-ccsf/administration/human-resources/jobs-ccsf" },
      { label: "CCSF employment portal (official, live)", url: "https://jobs.ccsf.edu/postings/search" }
    ]
  },
  {
    id: "job-24",
    company: "California Academy of Sciences — Institute for Biodiversity Science (IBSS)",
    position: "Research Lab / Collections Support (Center for Comparative Genomics, specimen prep)",
    verified: true,
    verificationMethod: "Official calacademy.org/careers → Greenhouse board live (10 jobs) + 55 Music Concourse verified",
    matchScore: 68,
    batch: 2,
    location: "55 Music Concourse Drive, Golden Gate Park, San Francisco, CA 94118",
    commuteZone: "A",
    route: "ZONE A — VERY CLOSE (Golden Gate Park). From 21st & Judah: N Judah eastbound to 9th Ave & Irving → walk north on 9th Ave into the park to Music Concourse (~15 min walk) or 44 bus north. ~20-30 min total. Confirm via SFMTA.",
    officialLink: "https://www.calacademy.org/careers",
    applyLink: "https://job-boards.greenhouse.io/californiaacademyofsciences — search lab, collections, research support",
    applyChannel: "Official Greenhouse board (direct, linked from calacademy.org)",
    requirements: "Lab experience; sample/specimen prep, DNA extraction awareness, meticulous records.",
    fit: "Moderate-good — your sample prep, extraction, and QC discipline transfer to genomics/collections lab support; more biology than chemistry.",
    status: "monitor",
    statusNote: "Greenhouse board live with 10 jobs (checked Sept 9, 2026) but currently senior-heavy (curators, managers); entry lab/collections support roles post periodically — set a job alert.",
    flag: "Current board is senior-heavy; entry roles are periodic — set Greenhouse job alert rather than expecting an immediate opening.",
    subpage: "jobs/job-24.html",
    sources: [
      { label: "Cal Academy Careers (official)", url: "https://www.calacademy.org/careers" },
      { label: "Cal Academy Greenhouse jobs (official, live)", url: "https://job-boards.greenhouse.io/californiaacademyofsciences" }
    ]
  },
  {
    id: "job-25",
    company: "UCSF Health Stanyan Hospital (formerly St. Mary's Medical Center)",
    position: "Laboratory Assistant — Clinical Lab Support (entry, non-licensed)",
    verified: true,
    verificationMethod: "Official sfcommunityhospitals.ucsfhealth.org confirms UCSF Health acquisition + 450 Stanyan address",
    matchScore: 66,
    batch: 2,
    location: "450 Stanyan Street, San Francisco, CA 94117 (Cole Valley / Haight)",
    commuteZone: "A/B",
    route: "ZONE A/B — From 21st & Judah: N Judah eastbound to 9th Ave & Irving → 7 Haight bus eastbound to Stanyan St → short walk north to 450 Stanyan. ~25-35 min. Confirm via SFMTA.",
    officialLink: "https://sfcommunityhospitals.ucsfhealth.org/st-marys",
    applyLink: "https://jobs.ucsfmedicalcenter.org — search 'Stanyan' or 'Laboratory Assistant' + San Francisco",
    applyChannel: "Official UCSF Health portal (direct) — hospital is now UCSF Health, not Dignity",
    requirements: "Entry lab support; specimen handling, data entry, equipment upkeep; CLS roles need CA license.",
    fit: "Moderate-good — entry lab assistant is accessible with your GLP/sample-prep background; licensed CLS track is not (flag).",
    status: "monitor",
    statusNote: "UCSF Health portal verified; Stanyan lab-support roles post periodically — search hospital name on the portal.",
    flag: "Hospital renamed: apply via UCSF Health portal (jobs.ucsfmedicalcenter.org), NOT Dignity/CommonSpirit boards. CLS/MLT roles require CA license — target Lab Assistant titles.",
    subpage: "jobs/job-25.html",
    sources: [
      { label: "UCSF Health community hospitals — Stanyan (official)", url: "https://sfcommunityhospitals.ucsfhealth.org/" },
      { label: "UCSF Health jobs portal (official)", url: "https://jobs.ucsfmedicalcenter.org" }
    ]
  },
  {
    id: "job-26",
    company: "Sutter Health — CPMC Davies Campus",
    position: "Pathology Laboratory Assistant II (specimen handling, chemicals, lab support)",
    verified: true,
    verificationMethod: "Official jobs.sutterhealth.org portal live + sutterhealth.org Davies Campus address verified",
    matchScore: 70,
    batch: 2,
    location: "Castro and Duboce Streets (45 Castro St MOB), San Francisco, CA 94114",
    commuteZone: "B",
    route: "ZONE B — From 21st & Judah: N Judah eastbound to Church & Duboce station → short walk or J Church/bus to Castro & Duboce (Davies Campus). ~20-30 min. Confirm via SFMTA.",
    officialLink: "https://www.sutterhealth.org/find-location/facility/cpmc-davies-campus",
    applyLink: "https://jobs.sutterhealth.org/us/en — search 'Pathology Lab Assistant' + San Francisco",
    applyChannel: "Official Sutter Health jobs portal (direct, Phenom)",
    requirements: "Lab support experience; handling chemicals/pathogens, specimens, records, MS Office.",
    fit: "Good — your sample prep, QC, safety compliance, and organizational skills fit pathology lab support; chemistry handling is a plus.",
    status: "recently-posted",
    statusNote: "Pathology Lab Assistant II in San Francisco $36.30–$50.82/hr seen live on Sutter postings ~Sept 2026 (discovery); Sutter SF lab-support roles recur — verify live on jobs.sutterhealth.org.",
    flag: null,
    subpage: "jobs/job-26.html",
    sources: [
      { label: "CPMC Davies Campus (official Sutter location)", url: "https://www.sutterhealth.org/find-location/facility/cpmc-davies-campus" },
      { label: "Sutter Health jobs portal (official, live)", url: "https://jobs.sutterhealth.org/us/en" }
    ]
  },
  {
    id: "job-27",
    company: "Sutter Health — CPMC Van Ness Campus",
    position: "Laboratory Assistant — Clinical Lab Support (entry)",
    verified: true,
    verificationMethod: "Official sutterhealth.org Van Ness Campus page (1101 Van Ness Ave) + jobs portal verified",
    matchScore: 66,
    batch: 2,
    location: "1101 Van Ness Avenue, San Francisco, CA 94109",
    commuteZone: "B",
    route: "ZONE B — From 21st & Judah: N Judah eastbound to Van Ness station → walk north on Van Ness ~10 min or 47/49 bus north to 1101 Van Ness. ~35-45 min. CPMC runs a Civic Center BART shuttle (B Line). Confirm via SFMTA.",
    officialLink: "https://www.sutterhealth.org/find-location/facility/cpmc-van-ness-campus-1043247265",
    applyLink: "https://jobs.sutterhealth.org/us/en — search 'Laboratory Assistant' + Van Ness / San Francisco",
    applyChannel: "Official Sutter Health jobs portal (direct)",
    requirements: "Entry lab support; specimen handling, data entry, safety; CLS roles need CA license.",
    fit: "Moderate-good — entry lab assistant fits your GLP/sample-prep background; licensed roles do not (flag).",
    status: "monitor",
    statusNote: "Sutter portal verified live; Van Ness lab-support roles post periodically — search location 'San Francisco'.",
    flag: "Clinical Lab Scientist roles require California CLS license — target Lab Assistant / support titles only.",
    subpage: "jobs/job-27.html",
    sources: [
      { label: "CPMC Van Ness Campus (official Sutter location)", url: "https://www.sutterhealth.org/find-location/facility/cpmc-van-ness-campus-1043247265" },
      { label: "Sutter Health jobs portal (official)", url: "https://jobs.sutterhealth.org/us/en" }
    ]
  },
  {
    id: "job-28",
    company: "Chinese Hospital — Clinical Laboratory (Chinatown main campus)",
    position: "Clinical Laboratory Technician (Non-Testing Personnel) — specimen collection & lab support",
    verified: true,
    verificationMethod: "Official chinesehospital-sf.org job board LIVE posting Req #12756 (Aug 25, 2026) + lab address verified",
    matchScore: 48,
    batch: 2,
    location: "845 Jackson Street, 1/F (Main Lab, 24/7), San Francisco, CA 94133",
    commuteZone: "C",
    route: "ZONE C — From 21st & Judah: N Judah eastbound to Powell station → 30 Stockton bus or cable car north to Chinatown (Jackson St) → walk to 845 Jackson. ~40-50 min. Note: Sunset Blood Draw Center at 1800 31st Ave (your 94122!) exists but main lab is Chinatown. Confirm via SFMTA.",
    officialLink: "https://chinesehospital-sf.org/job-opportunities/",
    applyLink: "https://chinesehospital-sf.org/job/clinicallabtech/ — apply directly on hospital site (Req #12756)",
    applyChannel: "Official hospital website application (direct, no recruiter)",
    requirements: "REQUIRED: CA Phlebotomy Technician cert (CPT-1 or CPT-2); nights/weekends/holidays availability.",
    fit: "Limited — live verified posting, but it REQUIRES CPT-1/CPT-2 phlebotomy certification you do not hold; chemistry degree alone does not qualify. Preferred: Chinese fluency, 1 yr phlebotomy.",
    status: "recently-posted",
    statusNote: "LIVE verified posting: Clinical Laboratory Technician, Full-Time, posted Aug 25, 2026, Req #12756 on chinesehospital-sf.org (checked Sept 9, 2026). Re-verify live before applying.",
    flag: "REQUIRES California CPT-1/CPT-2 phlebotomy license — do not apply without it (or while in a CPT program). Also requires nights/weekends/holiday availability. Sunset clinic (1800 31st Ave, 94122) is in your zip but main lab is Chinatown.",
    subpage: "jobs/job-28.html",
    sources: [
      { label: "Chinese Hospital job opportunities (official, live)", url: "https://chinesehospital-sf.org/job-opportunities/" },
      { label: "CLT posting Req #12756 (official)", url: "https://chinesehospital-sf.org/job/clinicallabtech/" },
      { label: "Chinese Hospital Laboratory locations (official)", url: "https://chinesehospital-sf.org/laboratory/" }
    ]
  },
  {
    id: "job-29",
    company: "UCSF at Zuckerberg San Francisco General (ZSFG) — Research",
    position: "Staff Research Associate I/II — Clinical & translational research support",
    verified: true,
    verificationMethod: "Official zsfg.ucsf.edu (UCSF partnership since 1873) + careers.ucsf.edu portal verified",
    matchScore: 76,
    batch: 2,
    location: "1001 Potrero Avenue, San Francisco, CA 94110 (Potrero / Mission)",
    commuteZone: "C",
    route: "ZONE C — From 21st & Judah: N Judah eastbound to downtown → transfer to 9/9R San Bruno or 22 Fillmore southbound to Potrero Ave; alt: BART to 24th St + free ZSFG shuttle (peak hours). ~50-65 min. Free UCSF shuttles link campuses. Confirm via SFMTA.",
    officialLink: "https://zsfg.ucsf.edu/about-ucsf-zsfg",
    applyLink: "https://careers.ucsf.edu — search 'Staff Research Associate' + 'ZSFG' or 'San Francisco General'",
    applyChannel: "Official UCSF careers portal (direct) — UCSF-employed research staff at ZSFG",
    requirements: "B.S. science; sample prep, data recording, lab support, regulatory awareness.",
    fit: "Good — your B.S. + GLP sample prep/QC/data recording fits UCSF research-support roles; hospital-based translational labs value organizational skills too.",
    status: "monitor",
    statusNote: "UCSF portal verified; ZSFG-based SRA roles post regularly across departments — search 'ZSFG' weekly.",
    flag: "Two employers share this campus: UCSF research staff apply via careers.ucsf.edu; City/DPH clinical staff via careers.sf.gov — use the right portal for the posting.",
    subpage: "jobs/job-29.html",
    sources: [
      { label: "UCSF at ZSFG partnership (official)", url: "https://zsfg.ucsf.edu/about-ucsf-zsfg" },
      { label: "ZSFG hospital address (official sf.gov)", url: "https://www.sf.gov/location--urgent-care-zuckerberg-san-francisco-general-hospital-zsfg" },
      { label: "UCSF Careers portal (official)", url: "https://careers.ucsf.edu" }
    ]
  },
  {
    id: "job-30",
    company: "SFVA Health Care System (federal) — Clinical & Research Labs",
    position: "Biological Science Technician / Medical Technician (federal direct-hire)",
    verified: true,
    verificationMethod: "Official va.gov SF jobs-and-careers page → USAJOBS verified + 4150 Clement federal site",
    matchScore: 68,
    batch: 2,
    location: "4150 Clement Street, San Francisco, CA 94121 (Richmond / Lincoln Park)",
    commuteZone: "B/C",
    route: "ZONE B/C — From 21st & Judah: N Judah east to 19th Ave → 38R Geary westbound to 32nd Ave & Geary → walk north ~8 min to Clement. ~45-60 min. Alt: 44 north from 9th & Irving → 38 west. Confirm via SFMTA.",
    officialLink: "https://www.va.gov/san-francisco-health-care/work-with-us/jobs-and-careers/",
    applyLink: "https://www.usajobs.gov/ — search 'San Francisco VA' + laboratory / biological science technician",
    applyChannel: "Official USAJOBS federal portal (direct federal hire, NOT NCIRE affiliate)",
    requirements: "Varies by series (0404 Bio Sci Tech, 0644 Medical Tech); lab experience; US citizenship.",
    fit: "Moderate-good — federal lab-tech series value hands-on sample prep/QC/equipment experience; distinct from NCIRE affiliate roles (jobs 11-12).",
    status: "monitor",
    statusNote: "SFVA jobs page verified (updated July 2026); federal lab-tech announcements post on USAJOBS as vacancies open — set a USAJOBS saved search.",
    flag: "Federal hiring: US citizenship generally required; background check, drug screening, vaccines; hiring process is slower (weeks-months). This is direct federal employment, separate from NCIRE (jobs 11-12).",
    subpage: "jobs/job-30.html",
    sources: [
      { label: "SFVA Jobs and careers (official va.gov)", url: "https://www.va.gov/san-francisco-health-care/work-with-us/jobs-and-careers/" },
      { label: "USAJOBS federal portal (official)", url: "https://www.usajobs.gov/" }
    ]
  },
  {
    id: "job-31",
    company: "Quest Diagnostics — San Francisco patient & lab services",
    position: "Specimen Processor / Laboratory Assistant (entry clinical support)",
    verified: true,
    verificationMethod: "Official careers.questdiagnostics.com live + official questdiagnostics.com SF locations verified",
    matchScore: 55,
    batch: 2,
    location: "2198 15th Street (at Noe) + multiple SF sites, San Francisco, CA 94114",
    commuteZone: "B",
    route: "ZONE B — From 21st & Judah: N Judah eastbound to Church & Duboce → J Church south 1-2 stops or short walk to 15th & Noe. ~20-30 min. Confirm site on posting + SFMTA.",
    officialLink: "https://careers.questdiagnostics.com/",
    applyLink: "https://careers.questdiagnostics.com/search-jobs — search 'Specimen' or 'Laboratory' + San Francisco",
    applyChannel: "Official Quest careers portal (direct)",
    requirements: "Entry: specimen handling, accessioning, data entry; phlebotomy cert for draw roles.",
    fit: "Moderate — specimen processing uses your sample handling/QC/data-entry skills; SF sites are largely patient centers, so verify the posting's work location is SF.",
    status: "monitor",
    statusNote: "Quest careers portal verified live with Laboratory + Specimen Processing career areas (checked Sept 9, 2026); SF postings appear periodically.",
    flag: "SF locations are mostly patient service centers (phlebotomy); major testing labs are outside SF — verify 'San Francisco, CA' in the location field of each posting. Beware fake-Quest-job scams (Quest posts a fraud warning on its careers page) — apply only via careers.questdiagnostics.com.",
    subpage: "jobs/job-31.html",
    sources: [
      { label: "Quest careers (official, live)", url: "https://careers.questdiagnostics.com/" },
      { label: "Quest SF 15th St location (official)", url: "https://www.questdiagnostics.com/locations/detail.html/DMT/94114/75/1" }
    ]
  },
  {
    id: "job-32",
    company: "Labcorp — San Francisco locations",
    position: "Laboratory Assistant / Patient Service Support (entry)",
    verified: true,
    verificationMethod: "Official careers.labcorp.com live + official locations.labcorp.com (6 SF sites) verified",
    matchScore: 55,
    batch: 2,
    location: "148 Noe Street (+ 490 Post, 2100/2233 Post, 2622 Ocean, 728 Pacific), San Francisco, CA",
    commuteZone: "B",
    route: "ZONE B — From 21st & Judah: N Judah eastbound to Church & Duboce → short walk/bus to Noe St sites (~20-30 min). For 2622 Ocean Ave site: N Judah → M/29 south (~30 min). Verify site on posting. Confirm via SFMTA.",
    officialLink: "https://careers.labcorp.com/global/en",
    applyLink: "https://careers.labcorp.com/global/search-results — search 'Laboratory' + San Francisco, CA",
    applyChannel: "Official Labcorp careers portal (direct)",
    requirements: "Entry: specimen handling, accessioning, customer intake; phlebotomy for draw roles.",
    fit: "Moderate — lab-assistant/specimen duties use your sample handling and data-entry skills; SF sites are patient centers, so verify SF work location per posting.",
    status: "monitor",
    statusNote: "Labcorp careers portal verified live (checked Sept 9, 2026); SF-area support postings appear periodically.",
    flag: "SF locations are patient service centers; major labs are outside SF — verify 'San Francisco, CA' location on each posting. Apply only via careers.labcorp.com.",
    subpage: "jobs/job-32.html",
    sources: [
      { label: "Labcorp careers (official, live)", url: "https://careers.labcorp.com/global/en" },
      { label: "Labcorp SF locations (official, 6 sites)", url: "https://locations.labcorp.com/ca/san-francisco/" }
    ]
  },
  {
    id: "job-33",
    company: "City & County of San Francisco — SFPUC (Water Quality)",
    position: "Water Quality Technician (Class 2481) — field & lab water/wastewater analyses",
    verified: true,
    verificationMethod: "Official careers.sf.gov classification 2481 verified (full job description + pay table)",
    matchScore: 87,
    batch: 2,
    location: "SFPUC Water Quality facilities, San Francisco (525 Golden Gate Ave admin + treatment-plant labs)",
    commuteZone: "C",
    route: "ZONE C — Downtown admin: N Judah eastbound direct to Civic Center ~25-30 min. Treatment-plant labs (e.g., Southeast): N Judah → T-Third south + bus, 45-75 min depending on site. Verify exact work site on the job ad.",
    officialLink: "https://careers.sf.gov/classifications/?classCode=2481",
    applyLink: "https://careers.sf.gov — search '2481' or 'Water Quality Technician'",
    applyChannel: "Official City & County of SF portal (direct civil service)",
    requirements: "AA with biology/chemistry/microbiology coursework (your B.S. Chemistry exceeds this) OR 18 mo water-utility tech experience; CA driver's license.",
    fit: "Excellent — entry-level class; your B.S. Chemistry + wet-chemistry/QC/field-sampling-adjacent skills exceed the AA minimum; chemical & microbiological analyses are core duties.",
    status: "monitor",
    statusNote: "Classification 2481 verified with 2026 pay table ($88K–$124K/yr); postings open periodically as exams — set a careers.sf.gov alert for '2481'.",
    flag: "Requires valid CA driver's license; some positions may require Water Distribution Operator D1 cert. Civil-service exam windows are time-limited.",
    subpage: "jobs/job-33.html",
    sources: [
      { label: "SF Careers — Water Quality Technician 2481 (official)", url: "https://careers.sf.gov/classifications/?classCode=2481" },
      { label: "SF Careers — City job search (official)", url: "https://careers.sf.gov" }
    ]
  },
  {
    id: "job-34",
    company: "SFPD Forensic Services Division — Crime Lab (Chemical Analysis)",
    position: "Criminalist I (Class 8259) — entry-level forensic chemistry (Chemical Analysis section)",
    verified: true,
    verificationMethod: "Official careers.sf.gov classification 8259 + live-structure postings (1995 Evans Ave) verified",
    matchScore: 84,
    batch: 2,
    location: "1995 Evans Avenue (Forensic Services Division Crime Lab), Bayview, San Francisco, CA 94124",
    commuteZone: "D",
    route: "ZONE D — LONGEST. From 21st & Judah: N Judah eastbound → T-Third southbound to Evans Ave area → short bus/walk to 1995 Evans. ~60-80 min. New $105M TC&FSD facility with controlled-substances & breath/blood-alcohol labs. Confirm via SFMTA.",
    officialLink: "https://careers.sf.gov/classifications/?classCode=8259",
    applyLink: "https://careers.sf.gov — search '8259' or 'Criminalist I'",
    applyChannel: "Official City & County of SF portal (direct civil service / exempt)",
    requirements: "B.S. with major in chemistry/biochemistry/molecular biology; Chemical Analysis posts need 8 sem units chemistry w/lab + 8 units organic w/lab (B.S. Chemistry covers); valid driver's license. No experience required.",
    fit: "Very good — entry-level Criminalist; your B.S. Chemistry + HPLC/spectroscopy/synthesis background fits the Chemical Analysis section directly.",
    status: "monitor",
    statusNote: "Classification 8259 verified ($104K–$127K/yr, entry-level, on-the-job training); Criminalist I/II/III recruitments posted Oct 2024 & Nov 2023 at 1995 Evans Ave — watch for next window.",
    flag: "Zone D long commute from Sunset. Law-enforcement hiring: background check/polygraph likely, on-call/standby + weekend shifts possible, court testimony duty. Exam windows close fast (days-weeks).",
    subpage: "jobs/job-34.html",
    sources: [
      { label: "SF Careers — Criminalist I 8259 (official)", url: "https://careers.sf.gov/classifications/?classCode=8259" },
      { label: "Criminalist I posting structure — 1995 Evans Ave (official)", url: "https://careers.sf.gov/role/?id=3743990005764126" },
      { label: "SFPD careers info (official)", url: "https://www.sanfranciscopolice.org/your-sfpd/careers" }
    ]
  },
  {
    id: "job-35",
    company: "Laguna Honda Hospital & Rehabilitation Center (City/DPH)",
    position: "Laboratory / Clinical Support (hospital lab assistant & aide roles)",
    verified: true,
    verificationMethod: "Official sf.gov location page (375 Laguna Honda Blvd) + City-run hospital → careers.sf.gov",
    matchScore: 64,
    batch: 2,
    location: "375 Laguna Honda Boulevard, San Francisco, CA 94116 (Forest Hill)",
    commuteZone: "A/B",
    route: "ZONE A/B — From 21st & Judah: N Judah eastbound to 9th Ave & Irving → 43 Masonic southbound toward Forest Hill → walk/bus to 375 Laguna Honda Blvd. ~30-45 min. Confirm via SFMTA (hilly area).",
    officialLink: "https://www.sf.gov/location--laguna-honda-hospital-and-rehabilitation-center",
    applyLink: "https://careers.sf.gov — search 'Laguna Honda' + laboratory / technician / assistant",
    applyChannel: "Official City & County of SF portal (direct civil service)",
    requirements: "Varies by class (2416 Lab Tech II, aides); lab coursework/experience; patient-area screening.",
    fit: "Moderate-good — City hospital lab-support roles use your GLP sample prep/QC/equipment skills; licensed CLS roles excluded (flag).",
    status: "monitor",
    statusNote: "City-run hospital verified; lab-support postings appear on careers.sf.gov periodically — search facility name weekly.",
    flag: "Clinical Lab Scientist roles require CA CLS license — target Lab Technician/Assistant/Aide titles. Hospital roles may require TB screening, N95 fit testing, vaccines.",
    subpage: "jobs/job-35.html",
    sources: [
      { label: "Laguna Honda Hospital location (official sf.gov)", url: "https://www.sf.gov/location--laguna-honda-hospital-and-rehabilitation-center" },
      { label: "SF Careers — City job search (official)", url: "https://careers.sf.gov" }
    ]
  },
  {
    id: "job-36",
    company: "UCSF Health Hyde Hospital (formerly Saint Francis Memorial)",
    position: "Laboratory Assistant — Clinical Lab Support (entry, non-licensed)",
    verified: true,
    verificationMethod: "Official sfcommunityhospitals.ucsfhealth.org confirms UCSF Health acquisition + 900 Hyde address",
    matchScore: 64,
    batch: 2,
    location: "900 Hyde Street (between Bush & Pine, Nob Hill), San Francisco, CA 94109",
    commuteZone: "C",
    route: "ZONE C — From 21st & Judah: N Judah eastbound to Civic Center station → 19 Polk northbound (or Powell-Mason cable car from Powell) toward Hyde/Bush → short walk to 900 Hyde. ~35-45 min. Confirm via SFMTA (hilly Nob Hill).",
    officialLink: "https://sfcommunityhospitals.ucsfhealth.org/saint-francis",
    applyLink: "https://jobs.ucsfmedicalcenter.org — search 'Hyde' or 'Laboratory Assistant' + San Francisco",
    applyChannel: "Official UCSF Health portal (direct) — hospital is now UCSF Health, not Dignity",
    requirements: "Entry lab support; specimen handling, data entry, upkeep; CLS roles need CA license.",
    fit: "Moderate-good — entry lab assistant fits your GLP/sample-prep background; licensed CLS track does not (flag).",
    status: "monitor",
    statusNote: "UCSF Health portal verified; Hyde lab-support roles post periodically — search hospital name on the portal.",
    flag: "Hospital renamed: apply via UCSF Health portal (jobs.ucsfmedicalcenter.org), NOT Dignity/CommonSpirit boards. CLS/MLT roles require CA license — target Lab Assistant titles.",
    subpage: "jobs/job-36.html",
    sources: [
      { label: "UCSF Health community hospitals — Hyde (official)", url: "https://sfcommunityhospitals.ucsfhealth.org/" },
      { label: "UCSF Health jobs portal (official)", url: "https://jobs.ucsfmedicalcenter.org" }
    ]
  },
  {
    id: "job-37",
    company: "San Francisco Unified School District (SFUSD)",
    position: "Science Laboratory / Classroom Support (classified staff, e.g., science prep technician)",
    verified: true,
    verificationMethod: "Official careers.sfusd.edu → Red Rover official ATS verified + 555 Franklin admin verified",
    matchScore: 58,
    batch: 2,
    location: "555 Franklin Street (admin) + school sites citywide, San Francisco, CA 94102",
    commuteZone: "C",
    route: "ZONE C — Admin: N Judah eastbound direct to Civic Center → short walk to 555 Franklin (~25-35 min). School sites vary — verify site on posting; most are N Judah/bus reachable. Confirm via SFMTA.",
    officialLink: "https://careers.sfusd.edu/",
    applyLink: "https://jobs.redroverk12.com/org/sfusd — SFUSD official applicant system; search science / laboratory / technician",
    applyChannel: "Official SFUSD applicant system Red Rover (direct district hiring, not a recruiter)",
    requirements: "Varies; science lab prep, inventory, safety; school-year schedule; background check.",
    fit: "Moderate — your chemistry lab skills fit science-prep/support duties; titles and sites vary by school (flag).",
    status: "monitor",
    statusNote: "SFUSD careers + Red Rover board verified live (checked Sept 9, 2026); classified science-support roles post with school-year hiring cycles.",
    flag: "Exact title varies by school ('Science Technician', 'Lab Assistant', aide roles) — read each posting's site + duties. Requires working with students + background clearance. Red Rover is SFUSD's official hiring system (like Workday), not a third-party recruiter.",
    subpage: "jobs/job-37.html",
    sources: [
      { label: "SFUSD careers (official)", url: "https://careers.sfusd.edu/" },
      { label: "SFUSD job board Red Rover (official ATS)", url: "https://jobs.redroverk12.com/org/sfusd" },
      { label: "SFUSD admin offices 555 Franklin (official)", url: "https://archive.sfusd.edu/en/schools/school-information/administration-facilities.html" }
    ]
  },
  {
    id: "job-38",
    company: "Exploratorium — Museum of Science, Art & Human Perception",
    position: "Exhibit / Science Technician (hands-on science support & maintenance)",
    verified: true,
    verificationMethod: "Official exploratorium.edu/about/jobs → current-openings verified + Piers 15/17 SF address",
    matchScore: 52,
    batch: 2,
    location: "Pier 15/17, Embarcadero, San Francisco, CA 94111",
    commuteZone: "B",
    route: "ZONE B — EASY DIRECT RIDE. From 21st & Judah: N Judah eastbound DIRECT to Embarcadero station (no transfer, ~24 min) → walk to Pier 15/17. ~30-40 min total. One of the simplest commutes on this list. Confirm via SFMTA.",
    officialLink: "https://www.exploratorium.edu/about/jobs",
    applyLink: "https://www.exploratorium.edu/about/jobs/current-openings — search technician / maintenance / exhibits",
    applyChannel: "Official Exploratorium website (direct)",
    requirements: "Hands-on technical aptitude; prototyping/maintenance; safety; public-floor support.",
    fit: "Science-adjacent bridge role, NOT bench chemistry — your lab discipline, equipment maintenance, and troubleshooting transfer; wet-chemistry skills underused (flag).",
    status: "monitor",
    statusNote: "Exploratorium jobs board verified live (checked Sept 9, 2026); technician/maintenance roles (e.g., Exhibit Maintenance Technician) post periodically.",
    flag: "Not bench chemistry — exhibit/prototype shop + public-floor science support. Consider as a science-adjacent bridge only if bench roles stall. Easiest commute on the list (direct N Judah).",
    subpage: "jobs/job-38.html",
    sources: [
      { label: "Exploratorium jobs (official)", url: "https://www.exploratorium.edu/about/jobs" },
      { label: "Exploratorium current openings (official)", url: "https://www.exploratorium.edu/about/jobs/current-openings" }
    ]
  },
  {
    id: "job-39",
    company: "SF Office of the Chief Medical Examiner — Forensic Laboratory Division",
    position: "Forensic Laboratory Analyst (Class 2403) — drug/poison screens, extractions, chromatography",
    verified: true,
    verificationMethod: "Official careers.sf.gov classification 2403 verified (full description, B.S. + no experience) + OCME lab address via data.sfgov.org",
    matchScore: 90,
    batch: 2,
    location: "1 Newhall Street (Forensic Laboratory facility), Bayview, San Francisco, CA 94124",
    commuteZone: "D",
    route: "ZONE D — LONGEST. From 21st & Judah: N Judah eastbound → T-Third southbound toward Bayview → bus/walk to 1 Newhall St (near Evans Ave). ~60-80 min. Same Bayview cluster as Anresco + SFPD lab. Confirm via SFMTA.",
    officialLink: "https://careers.sf.gov/classifications/?classCode=2403&setId=COMMN",
    applyLink: "https://careers.sf.gov — search '2403' or 'Forensic Laboratory Analyst'",
    applyChannel: "Official City & County of SF portal (direct civil service)",
    requirements: "B.S. in natural/physical/applied science + 1 lab course; EXPERIENCE: NONE required; valid CA driver's license. Duties: volatile/drug/poison screens, chemical extractions, immunoassays, chromatography, spectrophotometry.",
    fit: "Excellent — your B.S. Chemistry + extractions + chromatography + spectroscopy + QC is a near-exact match for forensic toxicology benchwork; no experience required.",
    status: "monitor",
    statusNote: "Classification 2403 verified ($102K–$124K/yr, no experience required); postings open as exams — set a careers.sf.gov alert for '2403'.",
    flag: "Zone D long commute. Requires CA driver's license. Forensic setting: background check, biohazard/decomposed-case exposure, unpleasant odors, possible court testimony. Exam windows are time-limited.",
    subpage: "jobs/job-39.html",
    sources: [
      { label: "SF Careers — Forensic Laboratory Analyst 2403 (official)", url: "https://careers.sf.gov/classifications/?classCode=2403&setId=COMMN" },
      { label: "OCME facility 1 Newhall St (official data.sfgov.org)", url: "https://data.sfgov.org/api/views/rwbr-kbhe/rows.rdf?accessType=DOWNLOAD" },
      { label: "SF Careers — City job search (official)", url: "https://careers.sf.gov" }
    ]
  },
  {
    id: "job-40",
    company: "American Red Cross — SF Blood & Platelet Donation Center (Biomedical Services)",
    position: "Blood Collection / Biomedical Support (entry, trained on the job)",
    verified: true,
    verificationMethod: "Official redcross.org SF location (1663 Market St) + official Workday careers verified",
    matchScore: 50,
    batch: 2,
    location: "1663 Market Street (at Gough), San Francisco, CA 94103",
    commuteZone: "B",
    route: "ZONE B — EASY DIRECT RIDE. From 21st & Judah: N Judah eastbound in the Market St subway to Church station → short walk to 1663 Market (Market & Gough). ~20-30 min, no transfer. Confirm via SFMTA.",
    officialLink: "https://www.redcross.org/local/california/northern-california-coastal.html",
    applyLink: "https://americanredcross.wd1.myworkdayjobs.com/American_Red_Cross_Careers — search Biomedical / Blood Collection + San Francisco",
    applyChannel: "Official Red Cross Workday (direct, linked from redcross.org careers)",
    requirements: "Entry collection roles train on the job (phlebotomy); lab testing at regional labs.",
    fit: "Healthcare-adjacent bridge — uses patient/specimen-handling discipline; NOT bench chemistry (flag). Good commute, mission-driven employer.",
    status: "monitor",
    statusNote: "Red Cross careers + Workday verified live (checked Sept 9, 2026); Biomedical/Blood Collection SF postings appear periodically.",
    flag: "Collection roles are phlebotomy/donor-facing (training provided), not bench chemistry. Lab testing happens at regional labs — verify 'San Francisco, CA' on each posting. Consider as bridge only.",
    subpage: "jobs/job-40.html",
    sources: [
      { label: "Red Cross Northern California Coastal region (official)", url: "https://www.redcross.org/local/california/northern-california-coastal.html" },
      { label: "Red Cross careers (official)", url: "https://www.redcross.org/about-us/careers.html" },
      { label: "Red Cross Workday jobs (official)", url: "https://americanredcross.wd1.myworkdayjobs.com/American_Red_Cross_Careers" }
    ]
  }
"""

with io.open(DATA_JS, "r", encoding="utf-8") as f:
    content = f.read()

# Insert new jobs before the closing of JOBS_DATA array: find "];\n\n// Remote verification"
marker = "];\n\n// Remote verification"
assert marker in content, "JOBS_DATA end marker not found"
# The last job entry ends with "  }\n];" — replace "  }\n];" of job-20 with "  },\n" + new jobs
old_tail = """    sources: [
      { label: "UCSF Medical Center careers (official)", url: "https://jobs.ucsfmedicalcenter.org" }
    ]
  }
];"""
assert old_tail in content, "job-20 tail not found"
new_tail = """    sources: [
      { label: "UCSF Medical Center careers (official)", url: "https://jobs.ucsfmedicalcenter.org" }
    ]
  },
""" + NEW_JOBS_JS + "];"
content = content.replace(old_tail, new_tail)

# Update MONITOR_REFERENCE: append Kyntra + Nurix exclusions
monitor_old = """  {
    employer: "Plasmidsaurus (South SF, overnight shift)",
    note: "Real verified company (plasmidsaurus.com) with Lab Technician (DNA sequencing) posting on Ashby board, but shift ~7pm-3am Tue-Sat, South SF location, DNA focus not chemistry — flagged as not recommended.",
    commute: "South SF + overnight shift",
    source: "https://plasmidsaurus.com"
  }
];"""
monitor_new = """  {
    employer: "Plasmidsaurus (South SF, overnight shift)",
    note: "Real verified company (plasmidsaurus.com) with Lab Technician (DNA sequencing) posting on Ashby board, but shift ~7pm-3am Tue-Sat, South SF location, DNA focus not chemistry — flagged as not recommended.",
    commute: "South SF + overnight shift",
    source: "https://plasmidsaurus.com"
  },
  {
    employer: "Kyntra Bio, Inc. (formerly FibroGen) — SF HQ, corporate only",
    note: "Verified SF HQ at 350 Bay St #6009, SF 94133 (official contact page + GlobalData), but only ~34 employees and no SF wet-lab verified — corporate office, not a bench-chemistry employer. Excluded Pass 2 rather than padding the list.",
    commute: "SF HQ but no verified SF bench lab",
    source: "https://www.kyntrabio.com/contact-us/"
  },
  {
    employer: "Nurix Therapeutics — HQ SF, labs in Brisbane",
    note: "Verified HQ 1700 Owens St Ste 205, SF 94158, but ALL 30 current openings on official Greenhouse board (job-boards.greenhouse.io/nurix, checked Sept 9, 2026) are Brisbane, CA — including 'Research Associate II, Bioanalytical'. Brisbane is not N Judah commutable. Excluded Pass 2; revisit only if SF-based bench roles appear.",
    commute: "Brisbane — not N Judah commutable",
    source: "https://job-boards.greenhouse.io/nurix"
  }
];"""
assert monitor_old in content, "monitor tail not found"
content = content.replace(monitor_old, monitor_new)

# Update REMOTE_FINDING note — pass 2 re-check
remote_old = '  note: "After checking official employer portals (UCSF, Gladstone, CZ Biohub, Vitalant, NCIRE, Vir, Twist, Anresco, City), no genuine entry-level bench-chemistry role was found that is (a) fully remote, (b) direct-hire by verified employer (not staffing agency), and (c) fits B.S. Chemistry profile. Most \'remote chemist\' ads route through staffing agencies, which violates your \'no recruiters\' rule. Best path remains SF-transit-commutable bench roles above. Re-check periodically; remote science roles that are direct occasionally appear at large pharma.",'
remote_new = '  note: "Pass 1 + Pass 2 re-check (Sept 9, 2026) across official employer portals (UCSF, Gladstone, CZ Biohub, Vitalant, NCIRE, Vir, Twist, Anresco, City, SFSU, USF, CCSF, Cal Academy, Sutter, Chinese Hospital, SFVA/USAJOBS, Quest, Labcorp, SFUSD, Exploratorium, OCME, Red Cross): no genuine entry-level bench-chemistry role was found that is (a) fully remote, (b) direct-hire by verified employer (not staffing agency), and (c) fits a B.S. Chemistry profile. Most remote chemist ads route through staffing agencies, violating the no-recruiters rule. Best path remains the 40 SF-transit-commutable roles above. Re-check monthly.",'
assert remote_old in content, "remote note not found"
content = content.replace(remote_old, remote_new)

with io.open(DATA_JS, "w", encoding="utf-8") as f:
    f.write(content)

print("data.js updated: +20 jobs, +2 exclusions, remote re-check note")
