# Autofill Vault — Make Every Application <30 Seconds

Goal: No re-typing. Copy-paste from one trusted source.

## What you have

1. **Brian_Profile.json** — machine-readable profile for any autofill extension or script. Contains personal, education, experience, skills, common ATS answers.
2. **Screening_Answers.txt** — human-readable copy-paste blocks for every ATS (Workday, Greenhouse, Lever, Ashby, SmartRecruiters, UltiPro, AP Recruit).
3. **Master resume & cover** — `assets/resume/Brian_Chemistry_Resume.pdf` + `assets/cover/Brian_Cover_Letter_Base.pdf` — generic versions for any portal that doesn't need tailoring.
4. **Per-job tailored docs** — `assets/resume/job-XX_resume.pdf` etc. — ordered so the posting's lead techniques appear first, but no fake claims.

## 3-Click Easy Apply Flow (new in Pass 7)

**Click 1: Filter**
- Open index.html, type "HPLC" or filter Zone A, sort by Match Score. Pick a job, click "Apply guide →".

**Click 2: Download Kit**
- On the job subpage, top "⚡ Easy Apply" box has:
  - **Download Kit ZIP** — contains resume PDF+TXT, cover PDF+TXT, email TXT, plus README with direct official link and checklist. One download = everything.
  - **Download Resume PDF** / **Download Cover PDF** — single-file fallback.
  - **Copy Autofill Profile** — copies the entire Screening_Answers.txt block for quick paste into ATS.
  - **Open Official Apply →** — direct link to company's own ATS (no recruiter).

**Click 3: Submit**
- Paste autofill answers, upload resume PDF + cover PDF from the ZIP, answer screening honestly, submit. Save confirmation in the tracker at bottom of page (localStorage, device-only).

Total time per job: ~2-3 minutes for well-matched roles, ~5 minutes for roles needing extra screening answers.

## Browser Autofill Tips

- **Chrome/Edge**: Settings → Autofill → Addresses and more → add San Francisco, CA 94122, phone, email. Chrome will suggest it on Workday/Greenhouse forms.
- **1Password / Bitwarden**: Save a "Job Application" identity with name, email, phone, address, and a secure note containing Screening_Answers.txt. Use it to fill forms in one click.
- **Greenhouse**: Most forms have "Autofill with Resume" — upload resume PDF first, then verify fields (it parses HPLC, GLP etc. correctly).
- **Workday**: Often asks for "Work Experience" separately — copy from Screening_Answers.txt Experience blocks.
- **Lever / Ashby**: Usually just resume + cover + basic info — fastest (30 sec).
- **AP Recruit (UCSF)**: Needs CV + cover letter + references (contact info only). Use master resume PDF as CV, tailored cover PDF, and reference contacts from password manager.
- **City careers.sf.gov (SmartRecruiters)**: Position-based tests need supplemental questionnaire — answer honestly, upload docs, note confirmation number. Windows close fast (days-weeks).

## No Hallucinations Rule

All autofill answers are from real resume facts only. If a screening question asks about a technique you haven't done (GC-MS, ICP-MS, LIMS, cell culture, animal work, CPT), answer "No" and mention what you HAVE done (HPLC, NMR, UV-Vis, chromatography, sample prep, GLP, QC, electronic records). A clean "I have not, but I learn instruments fast" beats a padded yes and will pass background verification.

## Verification

Every official apply link is verified against the employer's own site (see `assets/verification/VERIFICATION_REPORT_PASS7.md` for line-by-line checks). If a link shows "no longer open" or a location mismatch, it's flagged in the job card and subpage — do not apply to cached copies.

## Files

- `assets/profile/Brian_Profile.json` — structured profile
- `assets/profile/Screening_Answers.txt` — copy-paste ATS answers
- `assets/resume/*.pdf/*.txt` — 120 tailored resumes + master
- `assets/cover/*.pdf/*.txt/*.email` — 120 tailored covers + emails + base
- `assets/kits/job-XX_kit.zip` — per-job bundle (new in Pass 7)
- `assets/docx/*.docx` — DOCX versions for ATS that require DOCX (new in Pass 7)
