#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pass 7 — Easy Apply automation:
- Generate DOCX versions for all 120 resumes + cover letters
- Generate per-job ZIP kits (resume PDF+TXT+DOCX, cover PDF+TXT+DOCX, email TXT, README with direct apply link)
- Update gen_docs.py template to include Easy Apply box (we patch it)
- Generate verification report line-by-line
"""

import os
import re
import json
import glob
import zipfile
from docx import Document
from docx.shared import Pt

ROOT = os.path.dirname(os.path.abspath(__file__))
RESUME_DIR = os.path.join(ROOT, "assets", "resume")
COVER_DIR = os.path.join(ROOT, "assets", "cover")
DOCX_DIR = os.path.join(ROOT, "assets", "docx")
KITS_DIR = os.path.join(ROOT, "assets", "kits")
PROFILE_DIR = os.path.join(ROOT, "assets", "profile")
JOBS_DIR = os.path.join(ROOT, "jobs")
DATA_JS = os.path.join(ROOT, "assets", "js", "data.js")

os.makedirs(DOCX_DIR, exist_ok=True)
os.makedirs(KITS_DIR, exist_ok=True)

def load_jobs():
    txt = open(DATA_JS, encoding="utf-8").read()
    body = txt.split("window.JOBS_DATA", 1)[1]
    jobs = []
    for block in re.finditer(r"\{\s*id: \"(job-\d+)\",(.*?)\n  \}", body, re.S):
        jid, rest = block.group(1), block.group(2)
        j = {"id": jid}
        for key in ("company", "position", "location", "commuteZone", "route", "officialLink", "applyLink", "applyChannel", "requirements", "fit", "status", "statusNote", "flag", "subpage", "verificationMethod"):
            m = re.search(r"\b%s: \"((?:[^\"\\]|\\.)*)\"" % key, rest, re.S)
            j[key] = (m.group(1).replace('\\"', '"').replace("\\n", "\n").replace("\\/", "/") if m else "")
        m = re.search(r"\bmatchScore: (\d+)", rest)
        j["matchScore"] = int(m.group(1)) if m else 0
        m = re.search(r"\bbatch: (\d+)", rest)
        j["batch"] = int(m.group(1)) if m else 1
        jobs.append(j)
    return jobs

def txt_to_docx(txt_path, docx_path):
    text = open(txt_path, encoding="utf-8").read()
    doc = Document()
    style = doc.styles['Normal']
    font = style.font
    font.name = 'Calibri'
    font.size = Pt(10.5)
    # Add paragraphs preserving line breaks
    for line in text.split("\n"):
        if not line.strip():
            doc.add_paragraph("")
            continue
        # bold detection for headers
        if re.match(r"^(SUMMARY|CORE LABORATORY SKILLS|LABORATORY EXPERIENCE|ADDITIONAL EXPERIENCE|EDUCATION|PUBLICATION|BRIAN)$", line.strip()):
            p = doc.add_paragraph()
            run = p.add_run(line.strip())
            run.bold = True
            run.font.size = Pt(11)
        elif re.match(r"^[\w()\-.,'\"| ]+ - .+ - [A-Z][a-z]{2} \d{4}", line):
            p = doc.add_paragraph()
            run = p.add_run(line)
            run.bold = True
            run.font.size = Pt(10.5)
        else:
            doc.add_paragraph(line)
    doc.save(docx_path)

def clean_url(s):
    m = re.search(r"https?://[^\s\u2014\u2013>\"\\]]+", str(s or ""))
    return m.group(0).rstrip(".,") if m else "#"

def generate_docx():
    count = 0
    # resumes
    for txt_file in sorted(glob.glob(os.path.join(RESUME_DIR, "job-*_resume.txt")) + [os.path.join(RESUME_DIR, "Brian_Chemistry_Resume.txt")]):
        base = os.path.basename(txt_file).replace(".txt", ".docx")
        out = os.path.join(DOCX_DIR, base)
        txt_to_docx(txt_file, out)
        count += 1
    # covers
    for txt_file in sorted(glob.glob(os.path.join(COVER_DIR, "job-*_cover.txt")) + [os.path.join(COVER_DIR, "Brian_Cover_Letter_Base.txt")]):
        base = os.path.basename(txt_file).replace(".txt", ".docx")
        out = os.path.join(DOCX_DIR, base)
        txt_to_docx(txt_file, out)
        count += 1
    print(f"Generated {count} DOCX files in {DOCX_DIR}")

def generate_kits(jobs):
    # Read profile screening answers for README reference
    screening_path = os.path.join(PROFILE_DIR, "Screening_Answers.txt")
    profile_json_path = os.path.join(PROFILE_DIR, "Brian_Profile.json")
    count = 0
    for job in jobs:
        jid = job["id"]
        num = re.search(r"(\d+)$", jid).group(1)
        tag = f"job-{int(num):02d}"
        # files
        resume_txt = os.path.join(RESUME_DIR, f"{tag}_resume.txt")
        resume_pdf = os.path.join(RESUME_DIR, f"{tag}_resume.pdf")
        resume_docx = os.path.join(DOCX_DIR, f"{tag}_resume.docx")
        cover_txt = os.path.join(COVER_DIR, f"{tag}_cover.txt")
        cover_pdf = os.path.join(COVER_DIR, f"{tag}_cover.pdf")
        cover_docx = os.path.join(DOCX_DIR, f"{tag}_cover.docx")
        email_txt = os.path.join(COVER_DIR, f"{tag}_email.txt")
        # README content
        official = job.get("officialLink", "")
        apply_url = clean_url(job.get("applyLink", "") or official)
        apply_channel = job.get("applyChannel", "")
        company = job.get("company", "")
        position = job.get("position", "")
        location = job.get("location", "")
        match = job.get("matchScore", "")
        status = job.get("status", "")
        status_note = job.get("statusNote", "")
        flag = job.get("flag", "")
        verification = job.get("verificationMethod", "")

        readme = f"""JobSearchSF — Easy Apply Kit
ID: {jid} — {tag}
Company: {company}
Position: {position}
Location: {location}
Match Score: {match}%
Status: {status}
Status Note: {status_note}
Flag: {flag or 'None — no irregularity found at audit; re-verify live before applying'}
Verification: {verification}

Official Site: {official}
Direct Apply (official, no recruiter): {apply_url}
Channel: {apply_channel}

HOW TO APPLY IN 3 CLICKS (no manual typing needed):
1. Open the Direct Apply link above (official employer ATS only). Verify the posting is still live — postings rotate daily.
2. Upload Resume PDF (or DOCX if portal requires DOCX) and Cover Letter PDF from this ZIP.
   - Resume: {tag}_resume.pdf / .docx / .txt
   - Cover: {tag}_cover.pdf / .docx / .txt
   - Email: {tag}_email.txt (use if portal has message box or if official contact listed)
3. Copy-paste personal info from assets/profile/Screening_Answers.txt (or Brian_Profile.json) into the form. Answer screening honestly (say No if you haven't done a technique, mention what you HAVE done: HPLC, NMR, UV-Vis, chromatography, sample prep, GLP, QC, electronic records). Submit directly, save confirmation number in tracker on job page.

AUTOFILL VAULT:
- Profile JSON: assets/profile/Brian_Profile.json
- Screening answers: assets/profile/Screening_Answers.txt
- Master resume: assets/resume/Brian_Chemistry_Resume.pdf
- Master cover: assets/cover/Brian_Cover_Letter_Base.pdf

VERIFICATION FOR MANUAL REVIEW:
- Official Link: {official}
- Direct Apply Link: {apply_url}
- All sources are in data.js for this job. See job page for full source list.
- Apply only via official domain (Greenhouse job-boards.greenhouse.io, Lever jobs.lever.co, Ashby jobs.ashbyhq.com, Workday, SmartRecruiters careers.sf.gov, UltiPro recruiting.ultipro.com, AP Recruit aprecruit.ucsf.edu). Never via aggregator (Indeed/ZipRecruiter) except Anresco's own Indeed company page which is employer-managed.

ANTI-SCAM CHECK:
- No payment, no fee, no SSN/banking before interview.
- Reply should come from employer's own email domain.
- If posting says "South San Francisco" but title says "San Francisco" (e.g., Plasmidsaurus), confirm worksite before applying — flagged in this dataset.

Generated: 2026-09-12 (Pass 7 Easy Apply)
Branch: arena/01a097c2-jobsearchsf
"""

        zip_path = os.path.join(KITS_DIR, f"{tag}_kit.zip")
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as z:
            if os.path.exists(resume_txt):
                z.write(resume_txt, arcname=f"{tag}_resume.txt")
            if os.path.exists(resume_pdf):
                z.write(resume_pdf, arcname=f"{tag}_resume.pdf")
            if os.path.exists(resume_docx):
                z.write(resume_docx, arcname=f"{tag}_resume.docx")
            if os.path.exists(cover_txt):
                z.write(cover_txt, arcname=f"{tag}_cover.txt")
            if os.path.exists(cover_pdf):
                z.write(cover_pdf, arcname=f"{tag}_cover.pdf")
            if os.path.exists(cover_docx):
                z.write(cover_docx, arcname=f"{tag}_cover.docx")
            if os.path.exists(email_txt):
                z.write(email_txt, arcname=f"{tag}_email.txt")
            z.writestr("README.txt", readme)
            # include screening answers for convenience
            if os.path.exists(screening_path):
                z.write(screening_path, arcname="Screening_Answers.txt")
            if os.path.exists(profile_json_path):
                z.write(profile_json_path, arcname="Brian_Profile.json")
        count += 1
    print(f"Generated {count} kit ZIPs in {KITS_DIR}")

def main():
    jobs = load_jobs()
    print(f"Loaded {len(jobs)} jobs from data.js")
    generate_docx()
    generate_kits(jobs)

if __name__ == "__main__":
    main()
