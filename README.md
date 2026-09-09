# JobSearchSF 🧪

A clean, single-page job-search site for **verified San Francisco chemistry / research / lab-science
opportunities**, ranked by **SFMTA public transit from ~21st Ave & Judah St** (Inner Sunset), with
**official direct-apply links** and **sources for manual review**.

Live site (GitHub Pages): served from the repo root at `https://<owner>.github.io/JobSearchSF/`.

## What it does
- Lists verified, SF-located research/lab employers that fit a **B.S. Chemistry (UCSC 2011)** profile
  targeting **entry-level Research Associate / lab chemist** roles.
- Shows each opportunity's **real physical SF location** and a **public-transit plan from 21st & Judah**.
- Provides the **official employer careers portal / email** for each — **apply directly, no recruiters**.
- Includes a transit/reachability guide, a remote-work finding, and a verification/anti-scam checklist.
- Uses a two-state **status label** per row: `recently-posted` (re-verify live) vs `monitor` (posts periodically),
  plus `flagged` for entries reviewed but not recommended.

## Honesty / no-hallucination rules baked into the project
1. Every employer is verified against its **official website + verifiable SF address**; each card carries
   **source links for manual review**.
2. Live postings rotate daily, so the site documents the **verified employer + role type to search for** and
   the **official application channel**, rather than claiming any single job is open "today." **Re-verify on the
   employer's own careers page before applying.**
3. Aggregator sites (Indeed/ZipRecruiter/etc.) are used only for **discovery** — never as the application channel.
4. Anything with caveats (licensure, long commute, internal-only, out-of-district) is **explicitly flagged**.

## Files
- `index.html` — the site (clean, accessible, filterable)
- `assets/css/style.css` — styling
- `assets/js/data.js` — the curated, verified opportunity data + source links (edit here to add/update)
- `assets/js/app.js` — client-side rendering & status filtering
- `.nojekyll` — so GitHub Pages serves the static site directly

## Run locally
```bash
python3 -m http.server 8000
# open http://localhost:8000
```

## Publishing to GitHub Pages
1. Push the `arena/01a0879c-jobsearchsf` branch.
2. On GitHub → repo **Settings → Pages** → Source: **Deploy from a branch** → branch `main` (or the merged
   `arena/...` branch) → folder `/ (root)`.
3. The site appears at `https://<owner>.github.io/JobSearchSF/`.

## Maintenance
To keep the list accurate, re-run a search each cycle, confirm each employer still lists a fitting role on its
official portal, update the `status`/`statusNote`, and refresh the research date. Never leave a stale "recently-posted"
label on a role that has closed.
