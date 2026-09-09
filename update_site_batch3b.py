#!/usr/bin/env python3
"""Pass 3 resume: README.md + IMPROVEMENTS.md only (index/app/css/jobs/sitemap
already saved by update_site_batch3.py before its README anchor assert)."""
import io, re

BASE = "/home/user/JobSearchSF"

def load(p):
    with io.open(p, encoding="utf-8") as f:
        return f.read()

def save(p, s):
    with io.open(p, "w", encoding="utf-8") as f:
        f.write(s)

def rep_once(s, old, new, label):
    assert s.count(old) == 1, f"anchor not unique/found: {label}"
    return s.replace(old, new, 1)

# ---------------- README.md ----------------
p = BASE + "/README.md"
s = load(p)
assert "60 Verified SF Chemistry" not in s, "README already updated?"
s = rep_once(s, "# JobSearchSF 🧪 — 40 Verified SF Chemistry & Lab Jobs (N Judah Commute)",
             "# JobSearchSF 🧪 — 60 Verified SF Chemistry & Lab Jobs (N Judah Commute)", "readme h1")
s = rep_once(s, "A clean, GitHub Pages site for **40 verified San Francisco chemistry / research / lab-science opportunities** (20 Pass 1 + 20 Pass 2, double-verified Sept 9, 2026)",
             "A clean, GitHub Pages site for **60 verified San Francisco chemistry / research / lab-science opportunities** (20 Pass 1 + 20 Pass 2 + 20 Pass 3, triple-verified Sept 9, 2026)", "readme intro")
s = rep_once(s, "- **20 verified entries** (not hallucinations)", "- **60 verified entries** (not hallucinations)", "readme feat")
# "through `job-40.html`" appears twice (lines ~12 and ~90): replace both, plus "40 subpages"
assert s.count("through `job-40.html`") == 2, "through-count changed"
s = s.replace("through `job-40.html`", "through `job-60.html`")
assert s.count("`job-60.html` — 40 subpages") == 1
s = s.replace("`job-60.html` — 40 subpages", "`job-60.html` — 60 subpages")
s = rep_once(s, "## 40 Verified Entries (SF, N Judah Commutable)", "## 60 Verified Entries (SF, N Judah Commutable)", "readme h2")
m = re.search(r"^40\. .+$", s, flags=re.M)
assert m, "readme entry 40 not found"
entries41_60 = """
41. UCSF Helen Diller Cancer Center — SRA I/II cancer biology — 1450 3rd St — Zone B — 78% — careers.ucsf.edu
42. UCSF Proctor Foundation (Ophthalmology) — SRA I/II ocular micro — 490 Illinois St Fl 2 — Zone B — 72% — careers.ucsf.edu
43. City — Lab Technician I 2402 (entry, promotes to 2416) — citywide/SFDPH — Zone C — 80% — careers.sf.gov
44. City — Microbiologist I/II 2463 (LICENSED, plan-ahead) — SF Public Health Lab — Zone C — 45% — careers.sf.gov
45. Sutter CPMC Mission Bernal — Lab Assistant — 3555 Cesar Chavez St — Zone C — 66% — jobs.sutterhealth.org
46. Sutter CPMC Research Institute — Research Associate — 475 Brannan St Ste 130 — Zone B/C — 70% — jobs.sutterhealth.org
47. FAMSF de Young Museum — Conservation Technician track — 50 Hagiwara Tea Garden Dr — Zone A — 58% — careers.sf.gov
48. SFMOMA — Conservation Technician/Preparator track — 151 Third St — Zone C — 60% — jobs.lever.co/sfmoma
49. Aquarium of the Bay — Biologist I water-quality lab (RECENTLY POSTED, animal-care+SCUBA) — PIER 39 — Zone C — 55% — aquariumofthebay.org/careers
50. Dandelion Chocolate 16th St Factory — Sanitation/Production QC — 2600 16th St — Zone C — 60% — ApplyToJob board
51. NEMS Chinatown — Lab Assistant I — 1520 Stockton St — Zone C — 62% — nems.betterteam.com
52. Kaiser Mission Bay MOB — Lab Assistant (non-licensed rung) — 1600 Owens St — Zone B — 55% — kaiserpermanentejobs.org
53. SF City Clinic (SFDPH) — Lab/Phlebotomy Support — 356 7th St — Zone C — 55% — careers.sf.gov
54. CBP San Francisco Laboratory (federal) — Chemist 1320 series — 630 Sansome St Rm 1450 — Zone C — 80% — USAJOBS
55. Wildtype Foods (Dogpatch) — RA food chemistry/QC (monitor, no openings now) — 953 Indiana St — Zone B — 68% — Greenhouse
56. Asian Art Museum — Conservation/Collections track — 200 Larkin St — Zone C — 55% — careers.sf.gov
57. Chinese Hospital Sunset — Lab/Blood-Draw Support (WALKABLE) — 1800 31st Ave — Zone A — 65% — chinesehospital-sf.org
58. US Mint San Francisco (federal) — Production QC track — 155 Hermann St — Zone C — 52% — USAJOBS
59. Heluna Health — RA, SFDPH Center for Public Health Research — SFDPH sites — Zone C — 62% — helunahealth.org
60. Bridge HIV (SFDPH+UCSF) — RA/Specimen Processing — 25 Van Ness Ste 100 — Zone C — 64% — via Heluna"""
s = s[:m.end()] + entries41_60 + s[m.end():]
city_line = "- City: https://careers.sf.gov, https://careers.sf.gov/classifications/?classCode=2486, https://careers.sf.gov/classifications/?classCode=2416"
assert s.count(city_line) == 1, "readme city line"
s = s.replace(city_line, city_line + ", https://careers.sf.gov/classifications/?classCode=2402, https://careers.sf.gov/classifications/?classCode=2463\n- Federal: https://www.usajobs.gov, https://www.cbp.gov/about/labs-scientific-svcs/org-operations, https://www.usmint.gov/about/tours-and-locations/san-francisco\n- Museums/aquarium: https://www.sfmoma.org/join-the-team/, https://jobs.lever.co/sfmoma, https://www.famsf.org/, https://www.asianart.org/, https://www.aquariumofthebay.org/careers/\n- Food/biotech: https://www.wildtypefoods.com/, https://job-boards.greenhouse.io/Wildtype, https://www.dandelionchocolate.com/pages/visit-us, https://dandelionchocolate.applytojob.com/apply\n- Clinics/research: https://www.nems.org/, https://nems.betterteam.com/, https://www.helunahealth.org/, https://www.bridgehiv.org/, https://sf.gov/cityclinic, https://chinesehospital-sf.org/laboratory/", 1)
save(p, s)
print("README.md updated")

# ---------------- IMPROVEMENTS.md ----------------
p = BASE + "/assets/verification/IMPROVEMENTS.md"
s = load(p)
assert "Pass 3 — 20 new entries" not in s, "IMPROVEMENTS already updated?"
addition = """
## Pass 3 — 20 new entries (jobs 41-60), triple-verified Sept 9, 2026

New this pass: UCSF Helen Diller SRA (41), UCSF Proctor SRA (42), City 2402 Lab Tech I (43),
City 2463 Microbiologist plan-ahead (44), Sutter Mission Bernal lab (45), CPMC Research Institute (46),
FAMSF de Young conservation-tech (47), SFMOMA conservation-tech (48), Aquarium Biologist I water-quality (49),
Dandelion Chocolate production QC (50), NEMS lab assistant (51), Kaiser Mission Bay lab (52),
SF City Clinic lab/CPT (53), CBP SF Laboratory Chemist federal (54), Wildtype RA (55),
Asian Art Museum conservation (56), Chinese Hospital Sunset walkable (57), US Mint production QC (58),
Heluna Health RA (59), Bridge HIV RA/specimen (60).

Bugs/process fixed in Pass 3:
- Parallel edit_file calls to the SAME file race (read-modify-write): only the last write
  fully persists and tails can corrupt. Rule: same-file edits go in ONE sequential script
  with asserts (add_batch3.py / update_site_batch3.py pattern). Never parallelize same-file edits.
- Proctor Foundation is 490 Illinois St Fl 2 (verified), not 95 Kirkham as first assumed.
- FAMSF + Asian Art Museum hire through careers.sf.gov (City departments), not standalone boards.
- DEA Western Laboratory is Pleasanton CA (excluded); SF Zoo vet-tech is licensed-track (excluded).

## Features added in Pass 3
15. **Batch filter extended:** Pass 3 (41-60) + "New in Pass 3" green badges on rows, cards, subpages, transit table.
16. **Top-10-by-match box** on the homepage (auto-rendered from data.js) — start-here shortlist.
17. **CSV export button** — downloads the currently filtered/sorted list (id, company, role, score, zone, links) with UTF-8 BOM for Excel.
18. **Transit table expanded:** +18 destination rows (Helen Diller, Proctor, Kaiser Mission Bay, Dogpatch,
    Brannan, de Young, Sunset 31st Ave, Sansome/CBP, Civic Center City labs, Larkin/AAM, 25 Van Ness,
    Mint/Hermann, City Clinic, SFMOMA, Dandelion 16th, Mission Bernal, NEMS/Stockton, PIER 39).
19. **Remote finding re-checked #3** across all Pass-3 portals — still none-verified (documented).
20. **Verification logs:** VERIFICATION_LOG_PASS3.txt added; data.js schema-validated
    (60 jobs × required fields × http URLs) + internal link-integrity check script.
21. **sitemap.xml** extended (index + 60 subpages). README entries 41-60 + new official sources.

## Pass-3 verification method (three passes, no hallucinations)
- Pass 1: official site + careers portal + SF address fetched per employer.
- Pass 2: every official URL re-checked live; assumptions corrected (see above).
- Pass 3 (build): automated schema + link + file-existence checks before publish.
"""
if not s.endswith("\n"):
    s += "\n"
s += addition
save(p, s)
print("IMPROVEMENTS.md updated")
print("RESUME SCRIPT DONE")
