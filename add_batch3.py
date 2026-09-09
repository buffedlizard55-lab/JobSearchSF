#!/usr/bin/env python3
"""Pass 3: append jobs 41-60 to assets/js/data.js, update monitor + remote finding.
All entries verified line-by-line from official sources on 2026-09-09. No hallucinations.
"""
import io

DATA_JS = "/home/user/JobSearchSF/assets/js/data.js"

NEW_JOBS_JS = """  {
    id: "job-41",
    company: "UCSF — Helen Diller Family Comprehensive Cancer Center",
    position: "Staff Research Associate I/II — Cancer biology & shared-resource labs (sample prep, assays)",
    verified: true,
    verificationMethod: "Official cancer.ucsf.edu Diller Building page (1450 3rd St) + shared-resource cores verified",
    matchScore: 78,
    batch: 3,
    location: "1450 3rd Street (Helen Diller Family Cancer Research Building, Mission Bay), San Francisco, CA 94158",
    commuteZone: "B",
    route: "ZONE B — From 21st & Judah: N Judah eastbound to Embarcadero → T-Third southbound 2-3 stops to UCSF/Chase Center (16th St) → walk to 1450 3rd St. ~40-50 min. Confirm via SFMTA.",
    officialLink: "https://cancer.ucsf.edu/",
    applyLink: "https://careers.ucsf.edu — search 'Staff Research Associate' + Helen Diller / Cancer Center",
    applyChannel: "Official UCSF careers portal (direct, UC system)",
    requirements: "B.S. in chemistry/biology; cell culture, molecular assays, sample prep; cancer-biology interest.",
    fit: "Good — your sample-prep, QC, and instrumentation background fits SRA I/II posts in cancer-center labs and shared resources (genomics, flow cytometry). More biology-facing than pure chemistry.",
    status: "monitor",
    statusNote: "UCSF careers portal verified live (checked Sept 9, 2026); Diller/Cancer Center SRA reqs post continuously — search 'Staff Research Associate' + 'Cancer'.",
    flag: null,
    subpage: "jobs/job-41.html",
    sources: [
      { label: "Helen Diller Building address (official cancer.ucsf.edu)", url: "https://cancer.ucsf.edu/insiders/facilities/mission-bay-diller-building" },
      { label: "Cancer Center shared resources (official)", url: "https://cancer.ucsf.edu/research/cores/lca/lca-info" },
      { label: "UCSF Careers (official)", url: "https://careers.ucsf.edu" }
    ]
  },
  {
    id: "job-42",
    company: "UCSF — Francis I. Proctor Foundation for Research in Ophthalmology",
    position: "Staff Research Associate I/II — Ocular infectious-disease / microbiology labs (assays, sample prep)",
    verified: true,
    verificationMethod: "Official proctor.ucsf.edu contact page (490 Illinois St Fl 2) verified",
    matchScore: 72,
    batch: 3,
    location: "490 Illinois Street, Floor 2, San Francisco, CA 94143 (Mission Bay / Potrero edge)",
    commuteZone: "B",
    route: "ZONE B — From 21st & Judah: N Judah eastbound to Embarcadero → T-Third southbound to UCSF/Chase Center (16th St) → walk east to 490 Illinois St. ~40-50 min. Confirm via SFMTA.",
    officialLink: "https://proctor.ucsf.edu/",
    applyLink: "https://careers.ucsf.edu — search 'Proctor' + 'Staff Research Associate'",
    applyChannel: "Official UCSF careers portal (direct, UC system)",
    requirements: "B.S. life science; sterile technique, sample prep, assays; ophthalmology/microbiology interest.",
    fit: "Good-minus — your analytical and sample-prep discipline transfers to ocular-microbiology assay support; heavier on microbiology than chemistry.",
    status: "monitor",
    statusNote: "Proctor Foundation address verified on proctor.ucsf.edu (checked Sept 9, 2026); SRA reqs post on UCSF careers periodically — search 'Proctor'.",
    flag: null,
    subpage: "jobs/job-42.html",
    sources: [
      { label: "Proctor Foundation official site + address", url: "https://proctor.ucsf.edu/cornea-external-disease-refractive-surgery-fellowship" },
      { label: "UCSF Careers (official)", url: "https://careers.ucsf.edu" }
    ]
  },
  {
    id: "job-43",
    company: "City & County of San Francisco — SFDPH / Citywide Labs",
    position: "Laboratory Technician I (Class 2402) — Entry lab support (glassware, media, inventory, records)",
    verified: true,
    verificationMethod: "Official careers.sf.gov classification 2402 spec verified ($72K-$88K/yr, no license, promotes to 2416)",
    matchScore: 80,
    batch: 3,
    location: "Citywide — SFDPH Public Health Laboratories & City clinics (duty station per posting; HQ 101 Grove St), San Francisco",
    commuteZone: "C",
    route: "ZONE C — Assignment varies; most SFDPH lab sites are near Civic Center: N Judah eastbound to Civic Center → short walk. Confirm duty station on posting. ~30-40 min typical.",
    officialLink: "https://careers.sf.gov/classifications/?classCode=2402",
    applyLink: "https://careers.sf.gov — search '2402' or 'Laboratory Technician I'",
    applyChannel: "Official City & County of SF portal (direct civil service)",
    requirements: "HS diploma + 6 mo lab experience OR 15 semester units incl. one chem/bio lab course (your B.S. far exceeds); no license required.",
    fit: "Very good as an on-ramp — you exceed every minimum and the rung promotes to 2416; duties are deliberately routine (glassware/media/inventory), a foot-in-the-door rather than a chemist role.",
    status: "monitor",
    statusNote: "Class 2402 spec verified live (checked Sept 9, 2026); entrance exams post as needed — watch careers.sf.gov for 2402 announcements.",
    flag: "Entry rung is routine by design (glassware, media, inventory) — a foot-in-the-door, not a chemist role; promotes to 2416 Laboratory Technician II.",
    subpage: "jobs/job-43.html",
    sources: [
      { label: "2402-Laboratory Technician I classification (official)", url: "https://careers.sf.gov/classifications/?classCode=2402" },
      { label: "City careers portal (official)", url: "https://careers.sf.gov" }
    ]
  },
  {
    id: "job-44",
    company: "City & County of San Francisco — SFDPH Public Health Laboratories",
    position: "Microbiologist I/II (Class 2463) — Diagnostic micro testing (LICENSED track — plan-ahead entry)",
    verified: true,
    verificationMethod: "Official careers.sf.gov classification 2463 + past Microbiologist I recruitments verified",
    matchScore: 45,
    batch: 3,
    location: "SF Public Health Laboratories (SFDPH), San Francisco (duty station per posting; HQ 101 Grove St)",
    commuteZone: "C",
    route: "ZONE C — Civic Center corridor: N Judah eastbound to Civic Center → short walk to SFDPH lab facilities. ~30-40 min.",
    officialLink: "https://careers.sf.gov/classifications/?classCode=2463",
    applyLink: "https://careers.sf.gov — search '2463' or 'Microbiologist'",
    applyChannel: "Official City & County of SF portal (direct civil service)",
    requirements: "B.S. with microbiology major AND valid CA Public Health Microbiologist certificate (state board).",
    fit: "Low until certified — this is the licensed ceiling above the 2402/2416 ladder; included so you can plan the certificate path, not to apply today.",
    status: "monitor",
    statusNote: "Class 2463 spec + past recruitments verified (checked Sept 9, 2026); monitor while pursuing the PHM certificate path.",
    flag: "HARD REQUIREMENT: valid CA Public Health Microbiologist certificate + microbiology major — you do not currently hold it; monitor-and-plan entry only.",
    subpage: "jobs/job-44.html",
    sources: [
      { label: "2463-Microbiologist I/II classification (official)", url: "https://careers.sf.gov/classifications/?classCode=2463" },
      { label: "City careers portal (official)", url: "https://careers.sf.gov" }
    ]
  },
  {
    id: "job-45",
    company: "Sutter Health — CPMC Mission Bernal Campus",
    position: "Laboratory Assistant / Pathology Lab Support — Clinical lab support (entry)",
    verified: true,
    verificationMethod: "Official sutterhealth.org Mission Bernal facility page (3555 Cesar Chavez St) + jobs portal verified",
    matchScore: 66,
    batch: 3,
    location: "3555 Cesar Chavez Street, San Francisco, CA 94110 (Mission Bernal Campus)",
    commuteZone: "C",
    route: "ZONE C — From 21st & Judah: N Judah eastbound to Civic Center → BART southbound 1 stop to 24th St/Mission → 14/49 bus east or ~15-min walk to 3555 Cesar Chavez. ~45-60 min.",
    officialLink: "https://www.sutterhealth.org/find-location/facility/cpmc-emergency-mission-bernal-campus",
    applyLink: "https://jobs.sutterhealth.org/us/en — search 'Laboratory Assistant' + Mission Bernal / San Francisco",
    applyChannel: "Official Sutter Health jobs portal (direct)",
    requirements: "Entry lab support; specimen handling, data entry; CPT/MLT a plus for some roles.",
    fit: "Good entry fit — your GLP/sample-prep background maps to hospital lab support; licensed CLS roles excluded.",
    status: "monitor",
    statusNote: "Sutter jobs portal + Mission Bernal address verified (checked Sept 9, 2026); lab-assistant reqs post per campus — filter San Francisco.",
    flag: null,
    subpage: "jobs/job-45.html",
    sources: [
      { label: "CPMC Mission Bernal Campus (official sutterhealth.org)", url: "https://www.sutterhealth.org/find-location/facility/cpmc-emergency-mission-bernal-campus" },
      { label: "Sutter Health jobs (official)", url: "https://jobs.sutterhealth.org/us/en" }
    ]
  },
  {
    id: "job-46",
    company: "Sutter Health — CPMC Research Institute (CPMCRI)",
    position: "Research Associate / Study Coordinator, lab track — Specimen processing, regulatory docs, QC records",
    verified: true,
    verificationMethod: "FDP federal clearinghouse record (475 Brannan St Ste 130) + official sutterhealth.org/research verified",
    matchScore: 70,
    batch: 3,
    location: "475 Brannan Street, Suite 130, San Francisco, CA 94107 (SoMa)",
    commuteZone: "B/C",
    route: "ZONE B/C — From 21st & Judah: N Judah eastbound to Embarcadero → walk south ~15 min or Muni bus to Brannan St. ~35-45 min.",
    officialLink: "https://www.sutterhealth.org/research/",
    applyLink: "https://jobs.sutterhealth.org/us/en — search 'Research' + San Francisco / CPMC Research Institute",
    applyChannel: "Official Sutter Health jobs portal (direct)",
    requirements: "B.S. life science; sample processing, regulatory documents, data entry; clinical-research interest.",
    fit: "Good — your specimen processing + QC documentation from Quintara/MicroConstants transfers to translational research support.",
    status: "monitor",
    statusNote: "CPMCRI address + research site verified (checked Sept 9, 2026); research associate/coordinator reqs post on Sutter jobs — search 'Research'.",
    flag: null,
    subpage: "jobs/job-46.html",
    sources: [
      { label: "CPMCRI federal clearinghouse record (475 Brannan St)", url: "https://fdpclearinghouse.org/organizations/533" },
      { label: "Sutter Health Research (official)", url: "https://www.sutterhealth.org/research/" },
      { label: "Sutter Health jobs (official)", url: "https://jobs.sutterhealth.org/us/en" }
    ]
  },
  {
    id: "job-47",
    company: "Fine Arts Museums of San Francisco — de Young Museum",
    position: "Museum / Conservation Technician track — Materials handling, documentation (via City portal)",
    verified: true,
    verificationMethod: "FAMSF confirmed as City department hiring via careers.sf.gov (live City postings cite de Young, 50 Hagiwara Tea Garden Dr)",
    matchScore: 58,
    batch: 3,
    location: "50 Hagiwara Tea Garden Drive, Golden Gate Park, San Francisco, CA 94118",
    commuteZone: "A",
    route: "ZONE A — VERY CLOSE. From 21st & Judah: N Judah eastbound to 9th Ave & Irving → walk north into Golden Gate Park to Hagiwara Tea Garden Dr (~15 min) or 44 bus. ~20-30 min total.",
    officialLink: "https://www.famsf.org/",
    applyLink: "https://careers.sf.gov — search 'Fine Arts Museum' / 'Museum' (FAMSF hires through the City)",
    applyChannel: "Official City & County of SF portal (FAMSF is a City department — direct)",
    requirements: "Varies by rung; conservation tech: hands-on materials aptitude, meticulous records; conservator: master's in art conservation.",
    fit: "Moderate — solvents/materials handling + documentation discipline is adjacent to conservation-tech work; art-conservation credential gap for the conservator rung.",
    status: "monitor",
    statusNote: "City-portal hiring chain verified (checked Sept 9, 2026); FAMSF tech/preparator reqs post on careers.sf.gov — search 'Fine Arts Museum'.",
    flag: "Conservator roles require a master's in art conservation; the technician/preparator rungs are the accessible track.",
    subpage: "jobs/job-47.html",
    sources: [
      { label: "FAMSF official site", url: "https://www.famsf.org/" },
      { label: "FAMSF City posting w/ de Young address (official careers.sf.gov)", url: "https://careers.sf.gov/role/?id=743999827405805" }
    ]
  },
  {
    id: "job-48",
    company: "San Francisco Museum of Modern Art (SFMOMA)",
    position: "Conservation Technician / Preparator track — Art handling, condition reporting (via official Lever board)",
    verified: true,
    verificationMethod: "Official sfmoma.org/join-the-team links to jobs.lever.co/sfmoma; 151 Third St address verified",
    matchScore: 60,
    batch: 3,
    location: "151 Third Street, San Francisco, CA 94103 (SoMa / Yerba Buena)",
    commuteZone: "C",
    route: "ZONE C — From 21st & Judah: N Judah eastbound to Powell or Montgomery → walk south to 151 Third St. ~30-40 min.",
    officialLink: "https://www.sfmoma.org/join-the-team/",
    applyLink: "https://jobs.lever.co/sfmoma — search Conservation / Preparator / Registration",
    applyChannel: "Official SFMOMA Lever board (direct, linked from sfmoma.org)",
    requirements: "Art handling, materials aptitude, condition reporting; conservation master's for the conservator rung.",
    fit: "Moderate — your chemistry/materials sense + meticulous documentation is adjacent to conservation support; credential gap above the tech rung.",
    status: "monitor",
    statusNote: "Official join-the-team → Lever chain verified live (checked Sept 9, 2026); conservation/preparator reqs post intermittently — set a Lever alert.",
    flag: "Conservator = master's track; target Preparator / Technician / Registration-support rungs.",
    subpage: "jobs/job-48.html",
    sources: [
      { label: "SFMOMA Join Our Team (official)", url: "https://www.sfmoma.org/join-the-team/" },
      { label: "SFMOMA official Lever board", url: "https://jobs.lever.co/sfmoma" }
    ]
  },
  {
    id: "job-49",
    company: "Aquarium of the Bay (Bay Ecotarium)",
    position: "Biologist I — Entry, water-quality laboratory + environmental parameters (ANIMAL-CARE role)",
    verified: true,
    verificationMethod: "Official aquariumofthebay.org/careers shows Biologist I entry posting with water-quality-lab duties; PIER 39 address verified",
    matchScore: 55,
    batch: 3,
    location: "PIER 39, Embarcadero & Beach Street, San Francisco, CA 94133",
    commuteZone: "C",
    route: "ZONE C — From 21st & Judah: N Judah eastbound to Embarcadero → F-line streetcar east to Pier 39 (or ~20-min walk). ~40-55 min.",
    officialLink: "https://www.aquariumofthebay.org/careers/",
    applyLink: "https://www.aquariumofthebay.org/careers/ — Biologist I posting live (checked Sept 9, 2026)",
    applyChannel: "Official Aquarium careers page (direct)",
    requirements: "Entry; water-quality testing, animal care, logs; SCUBA for exhibit diving.",
    fit: "Moderate — water-quality/environmental-parameter testing uses your analytical discipline; heavy animal-care and SCUBA component.",
    status: "recently-posted",
    statusNote: "Biologist I entry posting live on official careers page (checked Sept 9, 2026) — re-verify before applying; water-quality lab is one duty among husbandry tasks.",
    flag: "Role includes animal care + SCUBA + husbandry — the water-quality lab is one duty among many, not a pure chemistry post.",
    subpage: "jobs/job-49.html",
    sources: [
      { label: "Aquarium of the Bay Careers incl. Biologist I (official)", url: "https://www.aquariumofthebay.org/careers/" },
      { label: "Aquarium of the Bay official site + PIER 39 address", url: "https://www.aquariumofthebay.org/" }
    ]
  },
  {
    id: "job-50",
    company: "Dandelion Chocolate — 16th Street Factory",
    position: "Sanitation / Production QC track — Quality systems, chemical handling, food safety (Mission factory)",
    verified: true,
    verificationMethod: "Official dandelionchocolate.com visit page (2600 16th St) + official ApplyToJob board verified",
    matchScore: 60,
    batch: 3,
    location: "2600 16th Street (16th Street Factory), San Francisco, CA 94103 (Mission)",
    commuteZone: "C",
    route: "ZONE C — From 21st & Judah: N Judah eastbound to Church & Duboce → J Church southbound to 16th & Church → walk east on 16th to 2600 16th St (~15 min). ~40-50 min.",
    officialLink: "https://www.dandelionchocolate.com/pages/visit-us",
    applyLink: "https://dandelionchocolate.applytojob.com/apply — search San Francisco production / sanitation / quality",
    applyChannel: "Official Dandelion Chocolate career board (direct ATS)",
    requirements: "Food safety/quality procedures, chemical handling for sanitation, detail orientation; early shifts.",
    fit: "Moderate-good — quality systems + chemical handling + documentation map to your QC/GLP habits; production-floor setting.",
    status: "monitor",
    statusNote: "Official factory address + career board verified (checked Sept 9, 2026); sanitation/production reqs post per season — check board weekly.",
    flag: "Production environment: physical work, early shifts, food-safety pace — QC-adjacent, not a lab-chemistry post.",
    subpage: "jobs/job-50.html",
    sources: [
      { label: "16th Street Factory address (official)", url: "https://www.dandelionchocolate.com/pages/visit-us" },
      { label: "Dandelion Chocolate career board (official ATS)", url: "https://dandelionchocolate.applytojob.com/apply" }
    ]
  },
  {
    id: "job-51",
    company: "North East Medical Services (NEMS) — Chinatown Main Clinic",
    position: "Lab Assistant I — Clinic laboratory support (community health center)",
    verified: true,
    verificationMethod: "Official nems.org careers chain → nems.betterteam.com board; 1520 Stockton St main clinic corroborated by CDC directory",
    matchScore: 62,
    batch: 3,
    location: "1520 Stockton Street (Main Clinic, Chinatown), San Francisco, CA 94133",
    commuteZone: "C",
    route: "ZONE C — From 21st & Judah: N Judah eastbound to Powell → 30 Stockton bus north into Chinatown (or cable car) to 1520 Stockton. ~40-50 min.",
    officialLink: "https://www.nems.org/",
    applyLink: "https://nems.betterteam.com/ — Lab Assistant postings recur; check weekly",
    applyChannel: "Official NEMS BetterTeam board (direct, linked from nems.org)",
    requirements: "Lab assisting; phlebotomy/CPT often required; Cantonese/Mandarin strongly preferred.",
    fit: "Good-minus — specimen handling + clinical pace fit your background; CPT certification + Chinese language are gaps to plan around.",
    status: "monitor",
    statusNote: "BetterTeam board + main-clinic address verified (checked Sept 9, 2026); Lab Assistant I SF postings recur — check board weekly.",
    flag: "Phlebotomy/CPT certificate commonly required; Cantonese/Mandarin strongly preferred for patient-facing duties.",
    subpage: "jobs/job-51.html",
    sources: [
      { label: "NEMS official site", url: "https://www.nems.org/" },
      { label: "NEMS official job board (BetterTeam)", url: "https://nems.betterteam.com/" },
      { label: "NEMS Stockton Clinic listing (CDC directory)", url: "https://npin.cdc.gov/organization/north-east-medical-services-1" }
    ]
  },
  {
    id: "job-52",
    company: "Kaiser Permanente — SF Mission Bay Medical Offices",
    position: "Laboratory Assistant / Specimen Processor — MOB lab (entry, non-licensed rung only)",
    verified: true,
    verificationMethod: "Official healthy.kaiserpermanente.org facility page (1600 Owens St) verified",
    matchScore: 55,
    batch: 3,
    location: "1600 Owens Street, San Francisco, CA 94158 (Mission Bay)",
    commuteZone: "B",
    route: "ZONE B — From 21st & Judah: N Judah eastbound to Embarcadero → T-Third southbound to Mission Bay (UCSF/Chase Center) → walk to 1600 Owens St. ~40-50 min.",
    officialLink: "https://healthy.kaiserpermanente.org/northern-california/facilities/san-francisco-mission-bay-medical-offices-322881",
    applyLink: "https://kaiserpermanentejobs.org — search 'Laboratory Assistant' + Mission Bay / San Francisco",
    applyChannel: "Official Kaiser careers portal (direct)",
    requirements: "Entry specimen processing; CPT or MLT/CLS often required depending on req.",
    fit: "Moderate — accessible only at the explicitly non-licensed assistant rung; most Kaiser lab reqs are licensed (CPT/MLT/CLS).",
    status: "monitor",
    statusNote: "Mission Bay facility page verified (checked Sept 9, 2026); filter kaiserpermanentejobs.org by San Francisco + Laboratory Assistant, read license lines carefully.",
    flag: "Kaiser lab roles commonly require CPT/MLT/CLS state certification — target explicitly non-licensed 'Laboratory Assistant' reqs only.",
    subpage: "jobs/job-52.html",
    sources: [
      { label: "Mission Bay Medical Offices facility page (official)", url: "https://healthy.kaiserpermanente.org/northern-california/facilities/san-francisco-mission-bay-medical-offices-322881" },
      { label: "Kaiser careers portal (official)", url: "https://kaiserpermanentejobs.org" }
    ]
  },
  {
    id: "job-53",
    company: "SF City Clinic (SFDPH) — Municipal STI Clinic",
    position: "Laboratory / Phlebotomy Support — Specimen collection & processing (CPT track, via City portal)",
    verified: true,
    verificationMethod: "City-run clinic at 356 7th St corroborated (Wikipedia + Apple Maps place data incl. sf.gov clinic page); hiring via careers.sf.gov",
    matchScore: 55,
    batch: 3,
    location: "356 7th Street, San Francisco, CA 94103 (SoMa)",
    commuteZone: "C",
    route: "ZONE C — From 21st & Judah: N Judah eastbound to Civic Center → walk south to 356 7th St (~10 min). ~30-40 min.",
    officialLink: "https://sf.gov/cityclinic",
    applyLink: "https://careers.sf.gov — search 'City Clinic' / '2402' / '2416' (clinic lab classes)",
    applyChannel: "Official City & County of SF portal (clinic is SFDPH-run — direct)",
    requirements: "Specimen collection/processing; CPT-I phlebotomy certification commonly required.",
    fit: "Moderate — STI-clinic lab pace fits your sample-handling background once the CPT path is planned.",
    status: "monitor",
    statusNote: "Clinic identity + address corroborated (checked Sept 9, 2026); lab classes assigned here post on careers.sf.gov — search 'City Clinic'.",
    flag: "Patient-facing specimen collection typically requires CPT-I phlebotomy certification.",
    subpage: "jobs/job-53.html",
    sources: [
      { label: "SF City Clinic page (sf.gov)", url: "https://sf.gov/cityclinic" },
      { label: "San Francisco City Clinic (Wikipedia overview)", url: "https://en.wikipedia.org/wiki/San_Francisco_City_Clinic" },
      { label: "City careers portal (official)", url: "https://careers.sf.gov" }
    ]
  },
  {
    id: "job-54",
    company: "U.S. Customs and Border Protection — San Francisco Laboratory (federal)",
    position: "Chemist (1320 series) — Analytical chemistry, trade & commodity testing (via USAJOBS)",
    verified: true,
    verificationMethod: "Official cbp.gov Labs page lists SF Laboratory (630 Sansome St Rm 1450); ISO/IEC 17025 network corroborated by WCO doc",
    matchScore: 80,
    batch: 3,
    location: "630 Sansome Street, Room 1450, San Francisco, CA 94111 (Financial District)",
    commuteZone: "C",
    route: "ZONE C — From 21st & Judah: N Judah eastbound to Embarcadero or Montgomery → walk north to 630 Sansome St. ~30-40 min.",
    officialLink: "https://www.cbp.gov/about/labs-scientific-svcs/org-operations",
    applyLink: "https://www.usajobs.gov — search 'Chemist' + 'Customs and Border Protection' + San Francisco; set an alert",
    applyChannel: "Official USAJOBS federal portal (direct federal hiring)",
    requirements: "B.S. Chemistry (1320 series); analytical methods; U.S. citizenship + background investigation.",
    fit: "Excellent — a working analytical-chemistry federal lab; your HPLC/spectroscopy/chromatography profile is the bullseye for Chemist reqs.",
    status: "monitor",
    statusNote: "SF Laboratory verified on cbp.gov (checked Sept 9, 2026); Chemist reqs post on USAJOBS intermittently — set a saved search for CBP + San Francisco.",
    flag: "Federal hiring: U.S. citizenship, background investigation, slow USAJOBS process — but the chemistry fit is elite.",
    subpage: "jobs/job-54.html",
    sources: [
      { label: "CBP Labs org + SF Laboratory address (official cbp.gov)", url: "https://www.cbp.gov/about/labs-scientific-svcs/org-operations" },
      { label: "USAJOBS federal portal (official)", url: "https://www.usajobs.gov" }
    ]
  },
  {
    id: "job-55",
    company: "Wildtype Foods — Cultivated Seafood (Dogpatch pilot plant)",
    position: "Research Associate — Food chemistry / QC, physical & chemical testing (monitor — no openings now)",
    verified: true,
    verificationMethod: "Official wildtypefoods.com + official Greenhouse board (job-boards.greenhouse.io/Wildtype) verified; 953 Indiana St HQ corroborated",
    matchScore: 68,
    batch: 3,
    location: "953 Indiana Street, San Francisco, CA 94107 (Dogpatch)",
    commuteZone: "B",
    route: "ZONE B — From 21st & Judah: N Judah eastbound to Embarcadero → T-Third southbound to 22nd St station → walk east to Indiana St. ~45-60 min.",
    officialLink: "https://www.wildtypefoods.com/",
    applyLink: "https://job-boards.greenhouse.io/Wildtype — no openings now; monitor + speculative outreach via site contact page",
    applyChannel: "Official Wildtype Greenhouse board (direct)",
    requirements: "B.S. food/chem/bio; physical/chemical tests, formulation screening, QC; startup pace.",
    fit: "Good — past Research Associate reqs ($70-92K) centered on food chemistry, testing, and QC — close to your profile when hiring resumes.",
    status: "monitor",
    statusNote: "Greenhouse board shows no current openings (checked Sept 9, 2026) — monitor board + contact page; past RA reqs fit well.",
    flag: "No current openings on the official board (checked Sept 9, 2026) — monitor + network; do not apply via 3rd-party reposts.",
    subpage: "jobs/job-55.html",
    sources: [
      { label: "Wildtype official site", url: "https://www.wildtypefoods.com/" },
      { label: "Wildtype official Greenhouse board", url: "https://job-boards.greenhouse.io/Wildtype" }
    ]
  },
  {
    id: "job-56",
    company: "Asian Art Museum (City & County of San Francisco)",
    position: "Conservation / Collections track — XRF materials science, handling, records (via City portal)",
    verified: true,
    verificationMethod: "AAM confirmed as City department hiring via careers.sf.gov (live 2026 City posting cites 200 Larkin St + apply-directly-to-City chain)",
    matchScore: 55,
    batch: 3,
    location: "200 Larkin Street, San Francisco, CA 94102 (Civic Center)",
    commuteZone: "C",
    route: "ZONE C — From 21st & Judah: N Judah eastbound to Civic Center → walk to 200 Larkin St. ~30-40 min.",
    officialLink: "https://www.asianart.org/",
    applyLink: "https://careers.sf.gov — search 'Asian Art Museum' / 'Conservation' / 'Collections' (AAM hires through the City)",
    applyChannel: "Official City & County of SF portal (AAM is a City department — direct)",
    requirements: "Conservation (3518): master's in art conservation + materials/XRF experience; collections support: handling, records, preventive care.",
    fit: "Moderate — the XRF spectroscopy/materials-science angle is chemistry-adjacent; credential gap for the conservator rung.",
    status: "monitor",
    statusNote: "City-portal hiring chain verified via live 2026 AAM posting (checked Sept 9, 2026); conservation/collections reqs post on careers.sf.gov.",
    flag: "Associate Museum Conservator (3518) requires a conservation master's + museum experience; collections-assistant rungs are the accessible track.",
    subpage: "jobs/job-56.html",
    sources: [
      { label: "Asian Art Museum official site", url: "https://www.asianart.org/" },
      { label: "City careers portal (official)", url: "https://careers.sf.gov" }
    ]
  },
  {
    id: "job-57",
    company: "Chinese Hospital — Sunset Health Services / Blood Draw Center",
    position: "Laboratory / Blood-Draw Support — Specimen collection (WALKABLE from home)",
    verified: true,
    verificationMethod: "Official chinesehospital-sf.org/laboratory lists Blood Draw Center – Sunset at 1800 31st Ave (Mon/Wed/Fri)",
    matchScore: 65,
    batch: 3,
    location: "1800 31st Avenue (Sunset Health Services), San Francisco, CA 94122",
    commuteZone: "A",
    route: "ZONE A — WALKABLE. From 21st & Judah: 1800 31st Ave is ~1 mile — walk (~20 min) or 29 Sunset bus. Easiest commute on this list.",
    officialLink: "https://chinesehospital-sf.org/laboratory/",
    applyLink: "https://chinesehospital-sf.org — Careers / Job Opportunities → search Sunset / lab / blood draw",
    applyChannel: "Official hospital website application (direct, no recruiter)",
    requirements: "Specimen collection/support; CPT-I commonly required; Chinese language strongly preferred.",
    fit: "Good-minus — ~10 blocks from home; clinical specimen handling fits your background with CPT planning.",
    status: "monitor",
    statusNote: "Sunset Blood Draw Center verified on hospital lab page (checked Sept 9, 2026); lab/assistant reqs post under Careers / Job Opportunities.",
    flag: "Blood-draw duties typically require CPT-I certification; Chinese language strongly preferred.",
    subpage: "jobs/job-57.html",
    sources: [
      { label: "Laboratory + Sunset Blood Draw Center (official)", url: "https://chinesehospital-sf.org/laboratory/" },
      { label: "Clinic Locations incl. Sunset Health Services (official)", url: "https://chinesehospital-sf.org/clinics/" }
    ]
  },
  {
    id: "job-58",
    company: "U.S. Mint — San Francisco Mint (federal)",
    position: "Metal Forming Machine Operator / Production QC track — Precision coin inspection (via USAJOBS)",
    verified: true,
    verificationMethod: "Official usmint.gov SF branch page + 155 Hermann St corroborated; SF Mint production roles confirmed via USAJOBS/Indeed discovery",
    matchScore: 52,
    batch: 3,
    location: "155 Hermann Street, San Francisco, CA 94102 (Market / Hayes edge)",
    commuteZone: "C",
    route: "ZONE C — From 21st & Judah: N Judah eastbound to Van Ness → walk south to 155 Hermann St. ~30-40 min.",
    officialLink: "https://www.usmint.gov/about/tours-and-locations/san-francisco",
    applyLink: "https://www.usajobs.gov — search 'U.S. Mint' + San Francisco; set an alert",
    applyChannel: "Official USAJOBS federal portal (direct federal hiring)",
    requirements: "Federal eligibility; precision inspection, manufacturing aptitude; no chemistry degree needed.",
    fit: "Lower chemistry fit — exacting visual/QC inspection uses your QC discipline; production floor with shift work, a federal foot-in-the-door at best.",
    status: "monitor",
    statusNote: "SF Mint branch verified (checked Sept 9, 2026); production/operator reqs post on USAJOBS intermittently — set a saved search.",
    flag: "Manufacturing/production role (proof-coin QC inspection), not chemistry — federal foot-in-the-door only.",
    subpage: "jobs/job-58.html",
    sources: [
      { label: "U.S. Mint at San Francisco (official usmint.gov)", url: "https://www.usmint.gov/about/tours-and-locations/san-francisco" },
      { label: "USAJOBS federal portal (official)", url: "https://www.usajobs.gov" }
    ]
  },
  {
    id: "job-59",
    company: "Heluna Health — Research Associate, SFDPH Center for Public Health Research",
    position: "Research Associate — Public-health research support, CPHR/CSUH (employer of record: Heluna Health)",
    verified: true,
    verificationMethod: "Official helunahealth.org (nonprofit fiscal sponsor since 1969) verified live; SF Research Associate postings confirmed via discovery",
    matchScore: 62,
    batch: 3,
    location: "SFDPH research sites, San Francisco (e.g., 101 Grove St / Population Health Division — per posting)",
    commuteZone: "C",
    route: "ZONE C — Civic Center corridor: N Judah eastbound to Civic Center → short walk to SFDPH sites. ~30-40 min.",
    officialLink: "https://www.helunahealth.org/",
    applyLink: "https://www.helunahealth.org/ — Careers → search San Francisco Research Associate (CPHR/CSUH postings recur)",
    applyChannel: "Official Heluna Health portal (direct employer of record, not a staffing recruiter)",
    requirements: "B.A./B.S.; research support, protocols, community engagement; public-health interest.",
    fit: "Good-minus — public-health research support uses your records/QC discipline; epi/social-science leaning with community fieldwork.",
    status: "monitor",
    statusNote: "Heluna Health official site verified live (checked Sept 9, 2026); SF Research Associate postings ($27-34/hr) recur — check Careers weekly.",
    flag: "Grant-funded, temporary/benefitted roles with non-standard hours and community fieldwork — research support, not bench chemistry.",
    subpage: "jobs/job-59.html",
    sources: [
      { label: "Heluna Health official site", url: "https://www.helunahealth.org/" }
    ]
  },
  {
    id: "job-60",
    company: "Bridge HIV (SFDPH + UCSF) — HIV Prevention Research Unit",
    position: "Research Associate / Specimen Processing — Chain-of-custody, LIMS, human-sample handling (via Heluna)",
    verified: true,
    verificationMethod: "Official bridgehiv.org verified live + sf.gov page confirms 25 Van Ness Ste 100; hiring via Heluna Health confirmed",
    matchScore: 64,
    batch: 3,
    location: "25 Van Ness Avenue, Suite 100, San Francisco, CA 94102 (Civic Center)",
    commuteZone: "C",
    route: "ZONE C — From 21st & Judah: N Judah eastbound to Van Ness or Civic Center → walk to 25 Van Ness Ave. ~30-40 min.",
    officialLink: "https://www.bridgehiv.org/",
    applyLink: "https://www.helunahealth.org/ — Careers → search 'Bridge HIV' Research Associate (Heluna is employer of record)",
    applyChannel: "Official Heluna Health portal for Bridge HIV unit (direct, not a recruiter)",
    requirements: "B.A./B.S.; specimen processing, chain-of-custody, LIMS/ELN; HIV-community research setting.",
    fit: "Good-minus — biobanking/specimen-processing duties use your sample-handling + records discipline; grant-funded research setting.",
    status: "monitor",
    statusNote: "Bridge HIV site + address verified (checked Sept 9, 2026); RA postings flow through Heluna Health Careers — search 'Bridge HIV'.",
    flag: "Grant-funded, temporary/benefitted roles; clinical-community research setting, not bench chemistry.",
    subpage: "jobs/job-60.html",
    sources: [
      { label: "Bridge HIV official site", url: "https://www.bridgehiv.org/" },
      { label: "Bridge HIV address (official sf.gov page)", url: "https://www.sf.gov/public-health-pride-parade-contingent" },
      { label: "Heluna Health official site (hiring channel)", url: "https://www.helunahealth.org/" }
    ]
  },
"""

MONITOR_ADD = """  {
    employer: "DEA Western Laboratory (Pleasanton — NOT SF)",
    note: "Verified via official EPA release: the DEA Western Laboratory is in Pleasanton, CA — not SF, not N Judah commutable. Excluded Pass 3 so a 'Bay Area' search doesn't mislead; revisit only if seeking East Bay roles.",
    commute: "Pleasanton — not commutable",
    source: "https://www.epa.gov/newsreleases/epa-recognizes-drug-enforcement-administration-western-laboratory-pleasanton-calif"
  },
  {
    employer: "San Francisco Zoo — Veterinary Technician (licensed track)",
    note: "SF Zoo Vet Tech postings require graduation from an AVMA-accredited veterinary-technician program, and no standalone official Zoo lab board was confirmed (sfzoo.org/careers 404s). Licensed-track only — excluded Pass 3.",
    commute: "Licensed track — cert required",
    source: "https://www.sfzoo.org/"
  }
"""

with io.open(DATA_JS, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Append jobs 41-60 before the end of JOBS_DATA (anchor on job-40 tail).
old_tail = '    subpage: "jobs/job-40.html",'
assert old_tail in content, "job-40 tail not found"
# Find the closing of job-40 object: the "  },\n];" after job-40 sources block.
new_jobs_block = NEW_JOBS_JS.rstrip()
assert new_jobs_block.endswith("},"), "new jobs must end with },"
# job-40 entry currently ends with "  }\n];" — insert comma + new jobs.
# Robust approach: replace the exact end sequence of job-40 + array close.
# (Comment lines sit between "];" and window.REMOTE_FINDING, so anchor on the close itself.)
end_seq = '    ]\n  }\n];\n'
assert content.count(end_seq) == 1, "job-40 end sequence not unique/found"
content = content.replace(end_seq, '    ]\n  },\n' + new_jobs_block + '\n];\n', 1)

# 2. Update REMOTE_FINDING note for Pass 3 re-check.
remote_old = "Pass 1 + Pass 2 re-check (Sept 9, 2026) across official employer portals (UCSF, Gladstone, CZ Biohub, Vitalant, NCIRE, Vir, Twist, Anresco, City, SFSU, USF, CCSF, Cal Academy, Sutter, Chinese Hospital, SFVA/USAJOBS, Quest, Labcorp, SFUSD, Exploratorium, OCME, Red Cross)"
assert remote_old in content, "remote note not found"
remote_new = "Pass 1 + Pass 2 + Pass 3 re-check (Sept 9, 2026) across official employer portals (UCSF incl. Helen Diller/Proctor, Gladstone, CZ Biohub, Vitalant, NCIRE, Vir, Twist, Anresco, City incl. 2402/2463/FAMSF/AAM, SFSU, USF, CCSF, Cal Academy, Sutter incl. Mission Bernal/CPMCRI, Chinese Hospital incl. Sunset, SFVA/USAJOBS, CBP/USAJOBS, Mint/USAJOBS, Quest, Labcorp, SFUSD, Exploratorium, OCME, Red Cross, SFMOMA/Lever, Aquarium, Wildtype/Greenhouse, Dandelion, NEMS/BetterTeam, Kaiser, Heluna, Bridge HIV, City Clinic/SFDPH)"
content = content.replace(remote_old, remote_new, 1)
content = content.replace("Best path remains the 40 SF-transit-commutable roles above.",
                          "Best path remains the 60 SF-transit-commutable roles above.", 1)

# 3. Append Pass-3 exclusions to MONITOR_REFERENCE.
mon_tail = """    employer: "Nurix Therapeutics — HQ SF, labs in Brisbane","""
assert mon_tail in content, "monitor tail not found"
nurix_end = """    source: "https://job-boards.greenhouse.io/nurix"
  }
];"""
assert nurix_end in content, "nurix end not found"
content = content.replace(nurix_end,
    """    source: "https://job-boards.greenhouse.io/nurix"
  },
""" + MONITOR_ADD + "];", 1)

# 4. Fix stale header count.
assert "20 VERIFIED San Francisco opportunities" in content
content = content.replace("20 VERIFIED San Francisco opportunities", "60 VERIFIED San Francisco opportunities", 1)

with io.open(DATA_JS, "w", encoding="utf-8") as f:
    f.write(content)

print("data.js updated: +20 jobs (41-60), +2 exclusions, remote re-check note, header count")
