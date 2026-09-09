# JobSearchSF — Improvements Implemented (Easy Apply)

Goal: Make applying as easy as click, copy, paste, with no manual input, organized, verified, self-apply only.

## List of Improvements & Implementation Status

### 1. Verified Table with Clear Labels (DONE)
- Table columns: Company, Position, Verified badge, Match Score, Official Source Link, Apply Guide subpage
- Each row shows real SF physical address, commute zone, status (recently-posted/monitor)
- Implemented in index.html table + assets/js/data.js + assets/js/app.js

### 2. Match Score (DONE)
- Each job has matchScore 58-92% based on B.S. Chemistry + HPLC/NMR/spectroscopy/chromatography/GLP/QC vs requirements
- High >=85% green, mid 70-84% yellow, low <70% red
- Visible in table and detailed cards

### 3. Verified Badge + Verification Method (DONE)
- Every job has verified=true, verificationMethod field (e.g., "Official UCSF HR + AP Recruit portal, physical campus verified")
- Sources array with official URLs for manual review (careers.ucsf.edu, gladstone.org, czbiohub.org, vitalant.org, ncire.org, vir.bio, twistbioscience.com, anresco.com, careers.sf.gov)
- Physical SF addresses verified via secondary trusted directories: YellowPages, LinkedIn, Bloomberg, SEC filing, GlobalData, OpenGov, CA SOS
- No hallucinations — documented in assets/verification/VERIFICATION_LOG.txt

### 4. Official Direct-Apply Only, No Recruiters (DONE)
- applyLink points to official employer portal only (Workday, Greenhouse, UltiPro, careers.sf.gov)
- Anresco exception: anresco.com/careers links to its own Indeed company page (employer-managed, not 3rd-party recruiter) — documented
- applyChannel field states "Official ... portal (direct)"
- Anti-scam checklist in verification section

### 5. Transit Routes Built Out from 21st Ave & Judah St (DONE)
- Detailed step-by-step N Judah Muni + SFMTA bus routes for each job
- Zone system A (shortest) to D (longest Bayview)
- Table in transit section with 11 area/employer routes, estimated times, official planners (SFMTA, 511.org)
- Each job card and subpage has copy-paste transit block
- Home stop: Judah & 21st Ave N Judah

### 6. Subpage per Job with Step-by-Step Beginner Guide (DONE — 20 pages)
- Location: jobs/job-01.html through job-20.html
- Each subpage includes:
  - Header with company, position, match score, verified badge
  - How to Apply — 10 steps for complete beginner (verify live, create account, download tailored docs, fill app, upload, screening questions, submit, track, interview prep, follow-up)
  - Tailored resume box with Copy button + Download PDF/TXT
  - Tailored cover letter box with Copy button + Download
  - Intro email box with Copy button + Download
  - Transit copy-paste box
  - Verification section with official links, anti-scam
  - Footer with today date, back to main list

### 7. Tailored Resume & Cover Letter per Job (DONE — 20 each)
- Base resume: assets/resume/Brian_Chemistry_Resume.txt + .pdf
- Base cover: assets/cover/Brian_Cover_Letter_Base.txt + .pdf
- Tailored: assets/resume/job-XX_resume.txt + .pdf (20)
- Tailored: assets/cover/job-XX_cover.txt + .pdf (20)
- Each emphasizes skills matching that job (e.g., HPLC for Anresco, synthesis for UCSF Pharma Chem, GLP/QC for Vitalant)
- Brief, polite, professional, easy to read for hiring manager quick approval

### 8. Intro Email Matching Job Posting Directly (DONE — 20)
- assets/cover/job-XX_email.txt
- Subject line includes position + match score
- Body includes 3 bullet points of relevant experience, requirements match, official apply link, transit, attachments mention
- Ready to copy-paste into portal message or email if official contact listed
- Self-apply only, no recruiter

### 9. Click, Copy, Paste UX (DONE)
- Each job subpage has Copy buttons (navigator.clipboard.writeText) for resume, cover, email, transit
- Buttons show "✓ Copied!" feedback
- Download buttons for PDF/TXT
- Official apply buttons open in new tab (target="_blank")
- No manual typing needed

### 10. Search & Filter (DONE)
- Filter by status: All 20, Recently posted, Monitor
- Search input: filters company, role, location, fit, requirements (e.g., type "HPLC" or "chemistry")
- Live count display

### 11. Clean UI, User-Friendly, Organized (DONE)
- Topbar with gradient (N Judah green), meta box with origin
- Sticky nav pills
- Cards with shadow, rounded corners, hover effects
- Table-wrap with sticky header, hover rows
- Badges for verified, zone, match score, status
- Responsive mobile (wrap padding, full-width search)
- GitHub Pages ready: .nojekyll exists, index.html root, assets relative paths

### 12. Remote Finding (DONE)
- Remote only if verified direct from employer, no staffing agencies
- After checking official portals, no verified fully-remote bench-chemistry entry-level role found that is direct-hire
- Documented in data.js REMOTE_FINDING + index.html remote section + sources checked
- Honest reporting rather than padding with recruiter ads

### 13. Reviewed but Excluded Log (DONE)
- MONITOR_REFERENCE array in data.js: Cytokinetics South SF, Biotium Fremont, Plasmidsaurus South SF overnight
- Shows why excluded (out-of-district, not N Judah commutable, DNA focus + overnight shift)
- Transparency

### 14. Verification Log (DONE)
- assets/verification/VERIFICATION_LOG.txt — line-by-line verification of 20 entries, official links, addresses, match scores, routes
- No hallucinations — every employer checked against official website + SF address

### 15. Easy Navigation & Links (DONE)
- Main index.html links to each job subpage via table and cards
- Each subpage links back to main list, official site, apply direct
- Resume/cover/email assets linked from both main and subpages
- All paths relative for GitHub Pages

### 16. Self-Apply Focus (DONE)
- No 3rd party site applying — all apply buttons go to official employer ATS
- Instructions explicitly say "Apply directly via official portal only"
- Anti-scam checklist warns about recruiter-only, payment requests, mismatched domains

### 17. Beginner-Friendly Language (DONE)
- Step-by-step uses simple verbs: Verify, Create account, Download, Fill, Upload, Submit, Track, Prepare, Follow up
- Time estimates per step (2 min, 3 min, etc.)
- Polite cover letters (3 short paragraphs) for quick hiring manager approval

### 18. GitHub Pages Deployment Ready (DONE)
- .nojekyll file exists (serves static site directly)
- index.html in root, assets/css, assets/js, jobs/ subfolder
- No build step needed — pure static HTML/CSS/JS
- To publish: push arena/01a087a8-jobsearchsf branch, Settings → Pages → Deploy from branch → root

## How to Use (Click-Copy-Paste Flow)

1. Open https://[owner].github.io/JobSearchSF/
2. Search/filter table (e.g., type "HPLC")
3. Click "Apply guide →" for a job (e.g., job-01)
4. On subpage, click "Open Official Careers →" to verify live posting
5. Download tailored resume PDF + cover PDF (or Copy buttons)
6. Follow 10-step guide, paste into official portal
7. Submit directly, no recruiter
8. Track via official portal

All official verified sources are linked for manual review. No hallucinations. Flag irregularities.
