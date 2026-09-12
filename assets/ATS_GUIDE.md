# ATS Guide — Pass 8 True 1-Click Easy Apply

Goal: Make applying as easy as download + submit. This guide gives 60-sec flow per ATS platform.

## Human Thinking Research Applied
- Visibility of system status: progress indicator (1-2-3 steps)
- Recognition > recall: copy-paste blocks, no re-typing
- Match real world: "Open Official Apply →" matches mental model
- Flexibility/efficiency: accelerators — One-Click button, bulk ZIPs, bookmarklet, extension draft

## Platform Cheat Sheets (verified from official docs + community)

### Workday (HHMI, Gladstone, Vitalant, Red Cross)
- Heavy autofill burden
- Upload resume DOCX first (<5MB, single-column, standard headers) — triggers "Autofill with Resume"
- Parse is DRAFT — review ALL fields, cannot edit after submit
- Fill optional fields (helps ranking)
- Mirror JD language
- Candidate Home tracking
- Files: use DOCX from kit (assets/docx/job-XX_resume.docx)

### Greenhouse (CZ Biohub, Vir, Cal Academy, EVERY, BridgeBio, Addition Tx)
- Light burden
- Recruiter sees PDF inline — prefers text-based PDF, single-column, name top line body not header, Skills comma-separated, Month YYYY, first bullet strongest
- Upload resume PDF
- Files: assets/resume/job-XX_resume.pdf

### Lever (SFMOMA, Pendulum)
- Moderate burden
- Longer custom Qs — concise free-text
- More forgiving PDF, keep one base layout, adapt form responses
- Files: PDF + tailored screening

### Ashby (Capable, Plasmidsaurus)
- Light burden, modern UI
- Files: PDF

### SmartRecruiters (City & County SF — careers.sf.gov)
- City postings: REF60430L, RTF014, PBT-etc
- Deadline 11:59 PM PST, eligible 12 months
- Requires DOCX often
- Files: DOCX + PDF

### UltiPro / UKG (NCIRE — recruiting.ultipro.com/NOR1032NCIRE)
- b5d49cdc site
- Prefers DOCX
- Files: DOCX

### AP Recruit (UCSF — aprecruit.ucsf.edu JPFxxxxx)
- Academic postings JPFxxxxx
- Upload PDF + cover + CV
- Files: PDF

### USAJOBS (SF VA, CBP Lab, US Mint)
- Federal resume — longer, include hours/week
- Upload PDF + transcripts if asked
- Files: PDF

## One-Click Flow (Pass 8)
1. Click ⚡ One-Click: Download Kit + Open Official Apply — kit ZIP downloads, official ATS opens in new tab
2. In ATS: Upload resume DOCX (Workday/SmartRecruiters/UltiPro) or PDF (Greenhouse/Lever/Ashby/AP Recruit) + cover from ZIP
3. Copy-paste from assets/screening/job-XX_screening.txt for screening Qs — honest No where needed + what you HAVE done (HPLC, NMR, UV-Vis, chromatography, sample prep, GLP, QC, electronic records)
4. Submit + save confirmation in tracker (localStorage, device-only)

## Automation (Power Users)
- Master JSON: assets/profile/All_Jobs_Easy_Apply.json — each entry has applyLinkClean (official ATS URL with job ID), kitZip, resume/cover paths, screening, matchScore, flag
- Bookmarklet: assets/bookmarklet.js — drag to bookmarks bar, click on any ATS page to autofill from Brian_Profile.json (local)
- Extension draft: assets/extension/ — manifest.json + content.js + popup.html + Brian_Profile.json — load unpacked in Chrome for one-click autofill (draft, manual review required)
- Bulk ZIPs: assets/kits/all_kits.zip (120 kits), top10_kits.zip, top20_kits.zip, all_resumes_pdfs.zip, all_covers_pdfs.zip

## Screening Honesty
If posting asks about GC-MS/ICP-MS/LIMS/cell culture/mouse/CPT you haven't done:
- Answer No
- Immediately add: "but have HPLC/NMR/UV-Vis/chromatography/sample prep/GLP/QC/electronic records; willing to train fast"
- See tailored screening file per job: assets/screening/job-XX_screening.txt

## No Hallucinations
All docs use real resume facts only (UCSC B.S. Chemistry 2011, Threshold, MicroConstants, Quintara, property manager contract). No fake techniques.

## Verification
Every job has:
- Official site (company careers)
- Direct apply link (official ATS URL with job ID where available: Greenhouse 7-digit, Lever ID, Ashby ID, JPF ID, REF ID)
- Kit ZIP with README containing direct links for manual review
- Flag field for irregularities (South SF location, withdrawn, ACE eligibility, cert gaps, Zone D)

Re-verify live posting before applying — postings rotate daily. Aggregators (Indeed, ZipRecruiter, LinkedIn) discovery only, never apply through them.

## Links for Manual Review
- Verification report: assets/verification/VERIFICATION_REPORT_PASS7.md
- ATS Guide: this file
- Master JSON: assets/profile/All_Jobs_Easy_Apply.json
- Bulk kits: assets/kits/
