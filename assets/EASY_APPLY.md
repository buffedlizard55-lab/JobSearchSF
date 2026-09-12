# JobSearchSF — ⚡ Easy Apply (Pass 7) — Download & Submit

**Goal:** Applying for any job should be as easy as **Download Kit ZIP → Open Official Apply → Submit resume + cover + autofill copy-paste**. No typing, no research, no recruiter.

Date: 2026-09-12 (Pass 7 audit)
Total jobs: 120 verified SF (direct-hire, no recruiters)
Easy Apply assets: 120 Kit ZIPs + 242 DOCX + 360 PDF/TXT + autofill vault

## 3-Click Flow (Human Thinking Process Research Applied)

Research (careery.pro, flashfirejobs.com) shows the highest success + lowest friction is:
1. **Quality-first matching** over volume
2. **Prepare core materials library** (resume/cover/email/autofill)
3. **Assisted mode → semi-automated** (human opens official portal, pastes prepared data)

We implemented that as:

### Step 1 — Filter (5 seconds)
- Open `index.html`
- Type skill (e.g. "HPLC" or "LC-MS") in search, or filter by Zone A (shortest commute) / Recently posted / Pass 6
- Count updates live

### Step 2 — Download Kit ZIP (1 click)
- In table, click **📦 Kit ZIP** (or on subpage top Easy Apply box: **📦 Download Kit ZIP**)
- Each ZIP contains:
  - `job-XX_resume.pdf` + `.txt` + `.docx` (DOCX for Workday/SmartRecruiters that require .docx)
  - `job-XX_cover.pdf` + `.txt` + `.docx`
  - `job-XX_email.txt` (subject + 3-bullet intro matching posting)
  - `Screening_Answers.txt` (common ATS screening answers, honest No for GC-MS/ICP-MS/LIMS/cell culture/mouse/CPT)
  - `Brian_Profile.json` (machine-readable profile for autofill tools)
  - `README.txt` with officialLink + direct applyLink + channel + verification + 3-click how-to + anti-scam check

### Step 3 — Submit Official (1 click + paste)
- Click **🚀 Apply direct →** (official direct-apply only, no recruiters)
- Official domains verified line-by-line (see VERIFICATION_REPORT_PASS7.md):
  - `careers.ucsf.edu` (UCSF HR), `aprecruit.ucsf.edu` (UCSF academic JPF IDs)
  - `gladstone.wd5.myworkdayjobs.com` (Gladstone), `hhmi.wd1.myworkdayjobs.com` (HHMI)
  - `vitalant.wd12.myworkdayjobs.com` (Vitalant), `americanredcross.wd1.myworkdayjobs.com` (Red Cross)
  - `usfca.wd5.myworkdayjobs.com` (USF), `job-boards.greenhouse.io` (CZ Biohub, Vir, EVERY, General Proximity, BridgeBio, etc. — 7-digit job IDs verified)
  - `jobs.lever.co` (SFMOMA, GLIDE, Pendulum), `jobs.ashbyhq.com` (Capable, Anthrogen, Parallel Bio, Plasmidsaurus, Addition)
  - `careers.sf.gov` (City SmartRecruiters REF/RTF/PBT IDs), `recruiting.ultipro.com/NOR1032NCIRE` (NCIRE)
  - `careers.pageuppeople.com/873/sf` (SFSU), `jobs.sutterhealth.org`, `jobs.ucsfmedicalcenter.org`, `kaiserpermanentejobs.org`, etc.
- Upload resume PDF or DOCX (both provided), cover PDF/DOCX, paste autofill from copy-box
- Submit, track via official portal

**Total time per application:** ~2-3 minutes after first kit download.

## Autofill Vault (No Typing)

**Location:** `index.html` #autofill section + every subpage #easy box copy-box + `assets/kits/` + `assets/profile/`

**Common ATS fields pre-filled (copy button):**
- Full Name: Brian
- Email: Brian.j1274@gmail.com
- Phone: (707) 596-8503
- Location: San Francisco, CA 94122 (Inner Sunset, 21st & Judah)
- Work Authorization: US Citizen, no sponsorship required (per profile)
- Education: B.S. Chemistry, UC Santa Cruz 2007-2011, Lab: Yat Li Group GaN CVD, Publication: ACS J Med Chem Feb 2011
- Experience:
  - Quintara Biosciences Jan-May 2012: GLP, sample prep, QC, data analysis, equipment maintenance, electronic records
  - MicroConstants (now EAG) Aug-Dec 2011: extraction, chromatography, spectroscopy, sample prep, QC, e-records
  - Threshold Pharmaceuticals Jun-Aug 2011: organic synthesis, HPLC, NMR, purification
  - Property Management: operations, budget tracking, scheduling (transferable to lab ops)
- Applying to: {company} {position} — officialLink + directLink included per job
- Screening honest No: GC-MS, ICP-MS, LIMS, cell culture, mouse work, CPT license (where required, flagged)

**Files for autofill tools (Simplify, Teal, Chrome Autofill):**
- `assets/profile/Brian_Profile.json` — structured profile
- `assets/profile/Screening_Answers.txt` — Q&A bank
- `assets/profile/AUTOFILL_GUIDE.md` — how to import into browser autofill

**Per-job autofill copy-box:** Each `jobs/job-XX.html` has a copy-box with ID `autofill-text` built by `build_autofill(job)` — includes job-specific applying-to line + officialLink + directLink.

## Kit ZIP Inventory

- Location: `assets/kits/job-01_kit.zip` through `job-120_kit.zip` (120 files)
- Size: ~5-15 KB each (text + PDFs)
- Contains README with:
  - Company, Position, Location, Match Score, Status, Flag, Verification
  - Official Site, Direct Apply (official, no recruiter), Channel
  - HOW TO APPLY 3-click
  - AUTOFILL VAULT paths
  - VERIFICATION FOR MANUAL REVIEW (sources array)
  - ANTI-SCAM CHECK (direct domain, no payment, no recruiter)

## DOCX Inventory (for Workday/SmartRecruiters requiring DOCX)

- Location: `assets/docx/` — 242 files
- `job-XX_resume.docx` + `job-XX_cover.docx` (120 each) + masters
- Generated via python-docx, Sept 12 2026, same content as PDF/TXT but DOCX format

## Official Direct-Apply Only (No Recruiters) — Verification

Every `applyLink` verified to be official employer ATS, not recruiter:
- See `assets/verification/VERIFICATION_REPORT_PASS7.md` — line-by-line audit of 120 officialLink + applyLink against trusted ATS domains
- Flagged irregularities documented:
  - job-73 Anthropic withdrawn 2026-09-09 (official Greenhouse serves "no longer open")
  - job-92 City Chemist REF60430L closed May 8 2026 (filing deadline passed)
  - job-118 Plasmidsaurus SF vs South SF mismatch (title says SF, body says South SF overnight)
  - job-116 2402 ACE cert (requires disability cert or veterans letter)

## Anti-Hallucination Measures

- All 120 jobs have `verified=true` + `verificationMethod` + `sources` array with official URLs
- No address guessed — if posting says campus not street, row says "see posting"
- Salary only where posting printed it
- No reference names fabricated
- Aggregator mirrors never used as apply links — official board wins, conflict noted
- Mechanical audit: `write_logs.py` scans all docs for transit words, zone labels, placeholders, tracker meta — 0 violations in Pass 6/7

## How to Use (For Manual Review)

1. Open `index.html` → #easy section explains flow
2. Click any **📦 Kit ZIP** → inspect README + resume + cover + screening answers
3. Click **Apply direct →** → verify it opens official domain (careers.ucsf.edu, aprecruit.ucsf.edu JPF ID, gladstone.wd5, etc.)
4. Compare `officialLink` vs `applyLink` — both official, no recruiter domain
5. Check `assets/verification/VERIFICATION_REPORT_PASS7.md` for line-by-line domain audit
6. If irregularity flagged, see job's `flag` field + subpage callout

## Improvements Over Previous Passes

- Pass 1-6: 20→120 jobs, table + cards + subpages + resume/cover/email PDF/TXT, search/filter/sort/batch/zone, tracker localStorage, print checklist, CSV export, sitemap, verification logs, resume cleaning (no transit in resume)
- Pass 7 (this): Kit ZIP (all formats in one download), DOCX for ATS requiring DOCX, autofill vault (profile JSON + screening answers + copy-box per job), Easy Apply hero with 3-click flow, Official Source + Direct Apply column separation, Kit ZIP column in table, Easy Apply box at top of every subpage, per-job autofill copy button, verification report with ATS domain audit

## Files to Check

- `index.html` — hero + #easy + #autofill + table (Kit ZIP column + Official Source + Direct Apply)
- `assets/js/app.js` — renders Kit ZIP + DOCX + direct apply buttons
- `assets/js/data.js` — 120 jobs, each with officialLink + applyLink + sources
- `jobs/job-*.html` — 120 subpages, each with Easy Apply box + autofill copy-box
- `assets/kits/` — 120 ZIPs
- `assets/docx/` — 242 DOCX
- `assets/resume/` + `assets/cover/` — PDF/TXT/DOCX per job
- `assets/profile/` — Brian_Profile.json + Screening_Answers.txt + AUTOFILL_GUIDE.md
- `assets/verification/VERIFICATION_REPORT_PASS7.md` — line-by-line official domain audit
- `assets/verification/IMPROVEMENTS.md` — full improvement list (Pass 1-7)
- `sitemap.xml` — index + 120 subpages

End of Easy Apply guide.
