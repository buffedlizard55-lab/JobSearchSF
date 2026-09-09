#!/usr/bin/env python3
"""Pass 3: update index.html (counts, filters, CSV, Top-10, transit, links),
app.js (batch3 badge, CSV export, Top-10), style.css (.batch3), jobs 01-40
back-links, sitemap.xml, README.md, IMPROVEMENTS.md. Single sequential script
(never parallel-edit the same file). All edits asserted.
"""
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

# ---------------- index.html ----------------
p = BASE + "/index.html"
s = load(p)

s = rep_once(s, "<title>JobSearchSF — 40 Verified SF Chemistry & Lab Jobs (N Judah Commute)</title>",
             "<title>JobSearchSF — 60 Verified SF Chemistry & Lab Jobs (N Judah Commute)</title>", "title")
s = rep_once(s, '<meta name="description" content="40 verified San Francisco',
             '<meta name="description" content="60 verified San Francisco', "meta")
s = rep_once(s, "<h1>JobSearchSF 🧪 — 40 Verified SF Jobs</h1>",
             "<h1>JobSearchSF 🧪 — 60 Verified SF Jobs</h1>", "h1")
s = rep_once(s, '<span class="badge batch2">20 new in Pass 2</span>',
             '<span class="badge batch2">20 in Pass 2</span> <span class="badge batch3">20 new in Pass 3</span>', "hero badges")
s = rep_once(s, "Verified: <strong>40 entries + official sources</strong>",
             "Verified: <strong>60 entries + official sources</strong>", "hero count")
s = rep_once(s, "<strong>This page lists 40 verified, SF-located lab-science opportunities</strong> (20 from Pass 1 + 20 new in Pass 2, double-verified Sept 9, 2026)",
             "<strong>This page lists 60 verified, SF-located lab-science opportunities</strong> (20 Pass 1 + 20 Pass 2 + 20 new in Pass 3, triple-verified Sept 9, 2026)", "overview")
s = rep_once(s, "<h2 class=\"sec\">Verified opportunities — sortable table (40 jobs)</h2>",
             "<h2 class=\"sec\">Verified opportunities — sortable table (60 jobs)</h2>", "table h2")
s = rep_once(s, '<button class="f-status active" data-status="all">All 40</button>',
             '<button class="f-status active" data-status="all">All 60</button>', "all btn")
s = rep_once(s, '<button class="f-batch active" data-batch="all">Pass 1 + 2</button>',
             '<button class="f-batch active" data-batch="all">Pass 1+2+3</button>', "batch all")
s = rep_once(s, '<button class="f-batch" data-batch="2">New: Pass 2 (21-40)</button>',
             '<button class="f-batch" data-batch="2">Pass 2 (21-40)</button>\n        <button class="f-batch" data-batch="3">New: Pass 3 (41-60)</button>', "batch3 btn")
s = rep_once(s, '<input id="search-input" type="text" placeholder="Search company, role, HPLC, chemistry, etc.">',
             '<input id="search-input" type="text" placeholder="Search company, role, HPLC, chemistry, etc.">\n        <button id="export-csv" class="btn btn-sm" title="Download the currently filtered list as CSV">⬇ Export CSV</button>', "csv btn")

# Top-10 section before TABLE
top10_html = """    <!-- TOP 10 -->
    <section class="block" id="top10">
      <div class="card">
        <h2 class="sec">Top 10 by match score — start here</h2>
        <p class="sec-sub">Highest chemistry-fit across all 60 verified entries. Click any row to open its step-by-step apply guide.</p>
        <ol id="top10-list" style="line-height:1.9"></ol>
      </div>
    </section>

    <!-- TABLE -->"""
s = rep_once(s, "    <!-- TABLE -->", top10_html, "top10 section")

# Transit rows before </tbody>
transit_rows = """            <tr>
              <td><strong>Mission Bay — Helen Diller (1450 3rd St)</strong> — SRA cancer labs <span class="badge batch3">New</span></td>
              <td>N Judah eastbound to Embarcadero → T-Third southbound to UCSF/Chase Center (16th St) → walk to 1450 3rd St.</td>
              <td><span class="badge zoneB">B</span></td>
              <td>40-50 min</td>
            </tr>
            <tr>
              <td><strong>Mission Bay/Potrero — Proctor Foundation (490 Illinois St)</strong> — SRA eye-research labs <span class="badge batch3">New</span></td>
              <td>N Judah eastbound to Embarcadero → T-Third southbound to UCSF/Chase Center → walk east to 490 Illinois St.</td>
              <td><span class="badge zoneB">B</span></td>
              <td>40-50 min</td>
            </tr>
            <tr>
              <td><strong>Mission Bay — Kaiser MOB (1600 Owens St)</strong> — Lab assistant <span class="badge batch3">New</span></td>
              <td>N Judah eastbound to Embarcadero → T-Third southbound to Mission Bay → walk to 1600 Owens St.</td>
              <td><span class="badge zoneB">B</span></td>
              <td>40-50 min</td>
            </tr>
            <tr>
              <td><strong>Dogpatch — Wildtype (953 Indiana St)</strong> — RA food chemistry <span class="badge batch3">New</span></td>
              <td>N Judah eastbound to Embarcadero → T-Third southbound to 22nd St station → walk east to Indiana St.</td>
              <td><span class="badge zoneB">B</span></td>
              <td>45-60 min</td>
            </tr>
            <tr>
              <td><strong>SoMa — CPMC Research Institute (475 Brannan St)</strong> — Research associate <span class="badge batch3">New</span></td>
              <td>N Judah eastbound to Embarcadero → walk south ~15 min or Muni bus to Brannan St.</td>
              <td><span class="badge zoneB">B/C</span></td>
              <td>35-45 min</td>
            </tr>
            <tr>
              <td><strong>GG Park — de Young Museum (50 Hagiwara Tea Garden Dr)</strong> — Conservation tech <span class="badge batch3">New</span></td>
              <td>N Judah eastbound to 9th Ave & Irving → walk north into the park (~15 min) or 44 bus.</td>
              <td><span class="badge zoneA">A</span></td>
              <td>20-30 min</td>
            </tr>
            <tr>
              <td><strong>Sunset — Chinese Hospital Sunset (1800 31st Ave)</strong> — Blood-draw support <span class="badge batch3">New</span></td>
              <td>WALKABLE: ~1 mile from 21st & Judah — walk (~20 min) or 29 Sunset bus. Easiest commute on this list.</td>
              <td><span class="badge zoneA">A</span></td>
              <td>15-20 min</td>
            </tr>
            <tr>
              <td><strong>FiDi — CBP Laboratory (630 Sansome St, Rm 1450)</strong> — Chemist (federal) <span class="badge batch3">New</span></td>
              <td>N Judah eastbound to Embarcadero or Montgomery → walk north to 630 Sansome St.</td>
              <td><span class="badge zoneC">C</span></td>
              <td>30-40 min</td>
            </tr>
            <tr>
              <td><strong>Civic Center — City lab postings (101 Grove St area)</strong> — 2402/2463 classes <span class="badge batch3">New</span></td>
              <td>N Judah eastbound to Civic Center → short walk. Duty station varies — confirm on posting.</td>
              <td><span class="badge zoneC">C</span></td>
              <td>30-40 min</td>
            </tr>
            <tr>
              <td><strong>Civic Center — Asian Art Museum (200 Larkin St)</strong> — Conservation/collections <span class="badge batch3">New</span></td>
              <td>N Judah eastbound to Civic Center → walk to 200 Larkin St.</td>
              <td><span class="badge zoneC">C</span></td>
              <td>30-40 min</td>
            </tr>
            <tr>
              <td><strong>Civic Center — Bridge HIV (25 Van Ness Ave)</strong> — RA specimen processing <span class="badge batch3">New</span></td>
              <td>N Judah eastbound to Van Ness or Civic Center → walk to 25 Van Ness Ave.</td>
              <td><span class="badge zoneC">C</span></td>
              <td>30-40 min</td>
            </tr>
            <tr>
              <td><strong>Market/Hayes — US Mint (155 Hermann St)</strong> — Production QC (federal) <span class="badge batch3">New</span></td>
              <td>N Judah eastbound to Van Ness → walk south to 155 Hermann St.</td>
              <td><span class="badge zoneC">C</span></td>
              <td>30-40 min</td>
            </tr>
            <tr>
              <td><strong>SoMa — City Clinic (356 7th St)</strong> — Lab/phlebotomy support <span class="badge batch3">New</span></td>
              <td>N Judah eastbound to Civic Center → walk south to 356 7th St (~10 min).</td>
              <td><span class="badge zoneC">C</span></td>
              <td>30-40 min</td>
            </tr>
            <tr>
              <td><strong>SoMa — SFMOMA (151 Third St)</strong> — Conservation tech <span class="badge batch3">New</span></td>
              <td>N Judah eastbound to Powell or Montgomery → walk south to 151 Third St.</td>
              <td><span class="badge zoneC">C</span></td>
              <td>30-40 min</td>
            </tr>
            <tr>
              <td><strong>Mission — Dandelion Chocolate (2600 16th St)</strong> — Production QC <span class="badge batch3">New</span></td>
              <td>N Judah eastbound to Church & Duboce → J Church southbound to 16th & Church → walk east on 16th (~15 min).</td>
              <td><span class="badge zoneC">C</span></td>
              <td>40-50 min</td>
            </tr>
            <tr>
              <td><strong>Mission/Bernal — CPMC Mission Bernal (3555 Cesar Chavez)</strong> — Lab assistant <span class="badge batch3">New</span></td>
              <td>N Judah eastbound to Civic Center → BART southbound 1 stop to 24th St/Mission → 14/49 bus east or ~15-min walk.</td>
              <td><span class="badge zoneC">C</span></td>
              <td>45-60 min</td>
            </tr>
            <tr>
              <td><strong>Chinatown — NEMS (1520 Stockton St)</strong> — Lab assistant <span class="badge batch3">New</span></td>
              <td>N Judah eastbound to Powell → 30 Stockton bus north into Chinatown (or cable car) to 1520 Stockton.</td>
              <td><span class="badge zoneC">C</span></td>
              <td>40-50 min</td>
            </tr>
            <tr>
              <td><strong>Fisherman's Wharf — Aquarium of the Bay (PIER 39)</strong> — Biologist I water quality <span class="badge batch3">New</span></td>
              <td>N Judah eastbound to Embarcadero → F-line streetcar east to Pier 39 (or ~20-min walk).</td>
              <td><span class="badge zoneC">C</span></td>
              <td>40-55 min</td>
            </tr>
          </tbody>"""
s = rep_once(s, "          </tbody>", transit_rows, "transit rows")

# Subpage links
s = rep_once(s, "<strong>All 40 subpages — Pass 1:</strong>", "<strong>All 60 subpages — Pass 1:</strong>", "subpage all")
s = rep_once(s, "<p><strong>Pass 2 (new):</strong>", "<p><strong>Pass 2:</strong>", "subpage p2")
p3_links = " · ".join(f'<a href="jobs/job-{i:02d}.html">job-{i:02d}</a>' for i in range(41, 61))
anchor_p2_line = "job-40</a></p>"
assert s.count(anchor_p2_line) == 1
s = s.replace(anchor_p2_line, anchor_p2_line + f'\n        <p><strong>Pass 3 (new):</strong> {p3_links}</p>', 1)

# Footer
s = rep_once(s, "(Pass 1 + Pass 2 double-verified Sept 9, 2026)", "(Pass 1 + Pass 2 + Pass 3 triple-verified Sept 9, 2026)", "footer passes")
s = rep_once(s, "40 verified SF entries, each with official sources", "60 verified SF entries, each with official sources", "footer count")
save(p, s)
print("index.html updated")

# ---------------- app.js ----------------
p = BASE + "/assets/js/app.js"
s = load(p)
s = rep_once(s, "/* JobSearchSF — rendering & filtering (pure client-side) — 40 verified entries */",
             "/* JobSearchSF — rendering & filtering (pure client-side) — 60 verified entries */", "app header")
s = rep_once(s, """  function batchBadge(j) {
    return (j.batch === 2) ? ' <span class="badge batch2">New in Pass 2</span>' : "";
  }""",
             """  var lastList = [];
  function batchBadge(j) {
    if (j.batch === 3) return ' <span class="badge batch3">New in Pass 3</span>';
    if (j.batch === 2) return ' <span class="badge batch2">Pass 2</span>';
    return "";
  }""", "batch badge")
s = rep_once(s, """  function render(list) {
    const tableBody = document.getElementById("jobs-table-body");""",
             """  function render(list) {
    lastList = list || [];
    const tableBody = document.getElementById("jobs-table-body");""", "lastList")
top10_js = """
    const top10 = document.getElementById("top10-list");
    if (top10 && window.JOBS_DATA) {
      const best = window.JOBS_DATA.slice().sort(function (a, b) { return (b.matchScore || 0) - (a.matchScore || 0); }).slice(0, 10);
      top10.innerHTML = best.map(function (j, i) {
        return '<li><a href="' + esc(j.subpage) + '"><strong>' + esc(j.company) + '</strong> — ' + esc(j.position.split(" — ")[0]) + '</a> <span class="badge score-high">' + esc(j.matchScore) + '%</span></li>';
      }).join("");
    }
"""
s = rep_once(s, """      remoteContainer.innerHTML = '<div class="callout red"><strong>Remote finding: ' + esc(r.status) + '</strong><br>' + esc(r.note) + '</div>' + (src ? '<div class="sources"><strong>Sources checked:</strong><ul>' + src + '</ul></div>' : '');
    }
  }""",
             """      remoteContainer.innerHTML = '<div class="callout red"><strong>Remote finding: ' + esc(r.status) + '</strong><br>' + esc(r.note) + '</div>' + (src ? '<div class="sources"><strong>Sources checked:</strong><ul>' + src + '</ul></div>' : '');
    }
""" + top10_js + "  }", "top10 render")
csv_js = """    const csvBtn = document.getElementById("export-csv");
    if (csvBtn) {
      csvBtn.addEventListener("click", function () {
        const rows = [["id", "company", "position", "matchScore", "zone", "status", "location", "officialLink", "applyLink", "subpage"]];
        (lastList || []).forEach(function (j) {
          rows.push([j.id, j.company, j.position, j.matchScore, j.commuteZone, j.status, j.location, j.officialLink, j.applyLink, j.subpage]);
        });
        const csv = "\\uFEFF" + rows.map(function (r) {
          return r.map(function (c) { return '"' + String(c == null ? "" : c).replace(/"/g, '""') + '"'; }).join(",");
        }).join("\\r\\n");
        const blob = new Blob([csv], { type: "text/csv;charset=utf-8" });
        const a = document.createElement("a");
        a.href = URL.createObjectURL(blob);
        a.download = "jobsearchsf-export.csv";
        document.body.appendChild(a);
        a.click();
        setTimeout(function () { URL.revokeObjectURL(a.href); a.remove(); }, 500);
      });
    }
    const el = document.getElementById("today");"""
s = rep_once(s, '    const el = document.getElementById("today");', csv_js, "csv handler")
save(p, s)
print("app.js updated")

# ---------------- style.css ----------------
p = BASE + "/assets/css/style.css"
s = load(p)
s = rep_once(s, ".badge.batch2 { background: #ede9fe; color: #5b21b6; border: 1px solid #c4b5fd; }",
             ".badge.batch2 { background: #ede9fe; color: #5b21b6; border: 1px solid #c4b5fd; }\n.badge.batch3 { background: #dcfce7; color: #166534; border: 1px solid #86efac; }", "batch3 css")
save(p, s)
print("style.css updated")

# ---------------- jobs/job-01..40 back-links ----------------
n = 0
for i in range(1, 41):
    p = f"{BASE}/jobs/job-{i:02d}.html"
    s = load(p)
    c = s.count("all 40 jobs")
    assert c >= 1, f"no back-link in job-{i:02d}"
    s = s.replace("all 40 jobs", "all 60 jobs")
    save(p, s)
    n += c
print(f"jobs 01-40 back-links updated ({n} replacements)")

# ---------------- sitemap.xml ----------------
p = BASE + "/sitemap.xml"
s = load(p)
anchor = "  <url><loc>./jobs/job-40.html</loc><changefreq>monthly</changefreq><priority>0.8</priority></url>\n</urlset>"
assert s.count(anchor) == 1, "sitemap anchor"
add = "".join(f"  <url><loc>./jobs/job-{i:02d}.html</loc><changefreq>monthly</changefreq><priority>0.8</priority></url>\n" for i in range(41, 61))
s = s.replace(anchor, anchor.replace("\n</urlset>", "\n" + add + "</urlset>"), 1)
save(p, s)
print("sitemap.xml updated")

# ---------------- README.md ----------------
p = BASE + "/README.md"
s = load(p)
s = rep_once(s, "# JobSearchSF 🧪 — 40 Verified SF Chemistry & Lab Jobs (N Judah Commute)",
             "# JobSearchSF 🧪 — 60 Verified SF Chemistry & Lab Jobs (N Judah Commute)", "readme h1")
s = rep_once(s, "A clean, GitHub Pages site for **40 verified San Francisco chemistry / research / lab-science opportunities** (20 Pass 1 + 20 Pass 2, double-verified Sept 9, 2026)",
             "A clean, GitHub Pages site for **60 verified San Francisco chemistry / research / lab-science opportunities** (20 Pass 1 + 20 Pass 2 + 20 Pass 3, triple-verified Sept 9, 2026)", "readme intro")
s = rep_once(s, "- **20 verified entries** (not hallucinations)", "- **60 verified entries** (not hallucinations)", "readme feat")
s = rep_once(s, "`jobs/job-01.html` through `job-40.html`", "`jobs/job-01.html` through `job-60.html`", "readme thru")
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
print("ALL SITE UPDATES DONE")
