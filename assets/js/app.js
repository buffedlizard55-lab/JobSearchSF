/* JobSearchSF — rendering & filtering (pure client-side) — 60 verified entries */
(function () {
  const STATUS_META = {
    "recently-posted": { cls: "badge recently-posted", label: "Recently posted" },
    "monitor":          { cls: "badge monitor", label: "Monitor" },
    "flag":             { cls: "badge flag", label: "Flagged" }
  };
  const ZONE_META = {
    A:   { cls: "badge zoneA", label: "Zone A — Shortest (~Inner Sunset/Parnassus)" },
    "A/B": { cls: "badge zoneA", label: "Zone A/B — Short (Inner Sunset + nearby)" },
    B:   { cls: "badge zoneB", label: "Zone B — Good (Mission Bay via N→T / direct N)" },
    "B/C": { cls: "badge zoneB", label: "Zone B/C — Good-Moderate" },
    C:   { cls: "badge zoneC", label: "Zone C — Moderate" },
    D:   { cls: "badge zoneD", label: "Zone D — Longest (Bayview)" },
    Flagged: { cls: "badge zoneFlagged", label: "Flagged" }
  };
  const ZONE_ORDER = { A: 0, "A/B": 1, B: 2, "B/C": 3, C: 4, D: 5 };

  function esc(s) {
    return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
  }
  // applyLink fields contain "URL — search instructions"; extract clean URL for href
  function cleanUrl(s) {
    const m = String(s || "").match(/https?:\/\/[^\s\u2014\u2013>\"\]]+/);
    return m ? m[0] : "#";
  }
  function scoreBadge(score) {
    if (score >= 85) return '<span class="badge score-high">' + esc(score) + '% match</span>';
    if (score >= 70) return '<span class="badge score-mid">' + esc(score) + '% match</span>';
    return '<span class="badge score-low">' + esc(score) + '% match</span>';
  }
  var lastList = [];
  function batchBadge(j) {
    if (j.batch === 3) return ' <span class="badge batch3">New in Pass 3</span>';
    if (j.batch === 2) return ' <span class="badge batch2">Pass 2</span>';
    return "";
  }
  function sourcesHtml(arr) {
    if (!arr || !arr.length) return "";
    const items = arr.map(function (s) {
      const u = s.url || "#";
      return '<li>' + esc(s.label) + ' — <a href="' + esc(u) + '" target="_blank" rel="noopener">' + esc(u) + '</a></li>';
    }).join("");
    return '<div class="sources"><strong>Sources for manual review (official verified):</strong><ul>' + items + "</ul></div>";
  }
  function trackerCell(j) {
    if (window.JobTracker) return window.JobTracker.selectHtml(j.id);
    return "";
  }

  function jobRow(j) {
    const st = STATUS_META[j.status] || STATUS_META.monitor;
    const zm = ZONE_META[j.commuteZone] || ZONE_META.C;
    const verifiedBadge = j.verified ? '<span class="badge verified">✓ Verified</span>' : '<span class="badge flag">Unverified</span>';
    const applyUrl = cleanUrl(j.applyLink);
    return (
      '<tr data-id="' + esc(j.id) + '">' +
        '<td><div class="company">' + esc(j.company) + '</div><div class="role">' + esc(j.position) + '</div><div style="margin-top:6px"><span class="' + st.cls + '">' + esc(st.label) + '</span> <span class="' + zm.cls + '">' + esc(zm.label.split(" — ")[0]) + '</span>' + batchBadge(j) + '</div></td>' +
        '<td>' + verifiedBadge + '<div style="margin-top:6px;font-size:.78rem;color:#5f6f81">' + esc(j.verificationMethod || "Official site + address") + '</div></td>' +
        '<td>' + scoreBadge(j.matchScore || 0) + '<div style="margin-top:6px;font-size:.80rem">' + esc(j.fit ? j.fit.slice(0,90) + "..." : "") + '</div></td>' +
        '<td><a href="' + esc(j.officialLink) + '" target="_blank" rel="noopener" class="btn btn-sm">Official site</a><div style="margin-top:6px;font-size:.78rem"><a href="' + esc(applyUrl) + '" target="_blank" rel="noopener">Apply direct →</a><br>' + esc(String(j.applyLink).slice(0,60)) + '...</div></td>' +
        '<td><a href="' + esc(j.subpage) + '" class="btn btn-sm btn-primary">Apply guide →</a><div style="margin-top:6px;font-size:.78rem">📍 ' + esc(j.location) + '</div></td>' +
        '<td>' + trackerCell(j) + '</td>' +
      '</tr>'
    );
  }

  function jobCard(j) {
    const st = STATUS_META[j.status] || STATUS_META.monitor;
    const zm = ZONE_META[j.commuteZone] || ZONE_META.C;
    const verifiedBadge = j.verified ? '<span class="badge verified">✓ Verified — official site + SF address</span>' : '';
    const applyUrl = cleanUrl(j.applyLink);
    let flag = "";
    if (j.flag) flag = '<div class="flag-note">⚠ ' + esc(j.flag) + "</div>";
    return (
      '<article class="job" data-id="' + esc(j.id) + '" id="' + esc(j.id) + '">' +
        "<div>" +
          '<h4>' + esc(j.company) + ' ' + verifiedBadge + batchBadge(j) + '</h4>' +
          '<div class="role">' + esc(j.position) + "</div>" +
          '<div class="meta-row"><span><span class="' + st.cls + '">' + esc(st.label) + '</span> <span class="' + zm.cls + '">' + esc(zm.label) + '</span> ' + scoreBadge(j.matchScore) + '</span></div>' +
          '<div class="meta-row"><span>📍 ' + esc(j.location) + '</span><span>🏢 ' + esc(j.company) + '</span></div>' +
        "</div>" +
        '<div class="grid">' +
          '<div class="field"><div class="lbl">Status & verification</div><div class="val">' + esc(j.statusNote) + '<br><br><strong>Verified:</strong> ' + esc(j.verificationMethod) + '</div></div>' +
          '<div class="field"><div class="lbl">Transit from ~21st & Judah (N Judah + bus)</div><div class="val">' + esc(j.route) + '</div></div>' +
          '<div class="field"><div class="lbl">Fit & requirements</div><div class="val"><strong>Match:</strong> ' + esc(j.matchScore) + '% — ' + esc(j.fit) + '<br><br><strong>Req:</strong> ' + esc(j.requirements) + '</div></div>' +
          '<div class="field apply"><div class="lbl">Apply directly (official)</div><div class="val"><strong>' + esc(j.applyChannel) + '</strong><br><a href="' + esc(applyUrl) + '" target="_blank" rel="noopener">Apply direct →</a><br>' + esc(j.applyLink) + '<br><br><a href="' + esc(j.subpage) + '" class="btn btn-primary btn-sm">Open step-by-step apply guide →</a><br><br><a href="' + esc(j.officialLink) + '" target="_blank" rel="noopener">' + esc(j.officialLink) + '</a></div></div>' +
        "</div>" +
        flag +
        sourcesHtml(j.sources) +
      "</article>"
    );
  }

  function render(list) {
    lastList = list || [];
    const tableBody = document.getElementById("jobs-table-body");
    const container = document.getElementById("jobs");
    const countEl = document.getElementById("count");
    const tableCountEl = document.getElementById("table-count");
    if (tableBody) {
      tableBody.innerHTML = list.map(jobRow).join("");
    }
    if (container) {
      container.innerHTML = list.map(jobCard).join("");
    }
    if (countEl) countEl.textContent = list.length + " verified rows (re-verify live postings before applying)";
    if (tableCountEl) tableCountEl.textContent = list.length + " jobs";
    if (window.JobTracker) window.JobTracker.renderSummary();

    const refContainer = document.getElementById("monitor-ref");
    if (refContainer && window.MONITOR_REFERENCE) {
      refContainer.innerHTML = window.MONITOR_REFERENCE.map(function (m) {
        const s = m.source ? "<br><span style='font-size:.8rem'><a href='" + esc(m.source) + "' target='_blank' rel='noopener'>" + esc(m.source) + "</a></span>" : "";
        return '<div class="field"><div class="lbl">' + esc(m.employer) + ' — ' + esc(m.commute) + '</div><div class="val">' + esc(m.note) + s + '</div></div>';
      }).join("");
    }

    const remoteContainer = document.getElementById("remote-finding");
    if (remoteContainer && window.REMOTE_FINDING) {
      const r = window.REMOTE_FINDING;
      const src = r.sources ? r.sources.map(function(s){ return '<li>' + esc(s.label) + ' — <a href="' + esc(s.url) + '" target="_blank" rel="noopener">' + esc(s.url) + '</a></li>'; }).join("") : "";
      remoteContainer.innerHTML = '<div class="callout red"><strong>Remote finding: ' + esc(r.status) + '</strong><br>' + esc(r.note) + '</div>' + (src ? '<div class="sources"><strong>Sources checked:</strong><ul>' + src + '</ul></div>' : '');
    }

    const top10 = document.getElementById("top10-list");
    if (top10 && window.JOBS_DATA) {
      const best = window.JOBS_DATA.slice().sort(function (a, b) { return (b.matchScore || 0) - (a.matchScore || 0); }).slice(0, 10);
      top10.innerHTML = best.map(function (j, i) {
        return '<li><a href="' + esc(j.subpage) + '"><strong>' + esc(j.company) + '</strong> — ' + esc(j.position.split(" — ")[0]) + '</a> <span class="badge score-high">' + esc(j.matchScore) + '%</span></li>';
      }).join("");
    }
  }

  function currentFilters() {
    const activeStatus = document.querySelector(".f-status.active");
    const activeZone = document.querySelector(".f-zone.active");
    const activeBatch = document.querySelector(".f-batch.active");
    const sortSel = document.getElementById("sort-select");
    const searchInput = document.getElementById("search-input");
    return {
      status: activeStatus ? activeStatus.dataset.status : "all",
      zone: activeZone ? activeZone.dataset.zone : "all",
      batch: activeBatch ? activeBatch.dataset.batch : "all",
      sort: sortSel ? sortSel.value : "match",
      term: searchInput ? searchInput.value : ""
    };
  }

  function applyFilters() {
    const f = currentFilters();
    let list = window.JOBS_DATA || [];
    if (f.status && f.status !== "all") {
      list = list.filter(function (j) { return j.status === f.status; });
    }
    if (f.zone && f.zone !== "all") {
      // Zone filter matches base letter: A matches A and A/B; B matches B, A/B, B/C; etc.
      list = list.filter(function (j) {
        return String(j.commuteZone || "").split("/").indexOf(f.zone) !== -1;
      });
    }
    if (f.batch && f.batch !== "all") {
      const b = parseInt(f.batch, 10);
      list = list.filter(function (j) { return (j.batch || 1) === b; });
    }
    if (f.term) {
      const q = f.term.toLowerCase();
      list = list.filter(function (j) {
        return (j.company + " " + j.position + " " + j.location + " " + j.fit + " " + j.requirements).toLowerCase().includes(q);
      });
    }
    // sort (copy first)
    list = list.slice();
    if (f.sort === "match") {
      list.sort(function (a, b) { return (b.matchScore || 0) - (a.matchScore || 0); });
    } else if (f.sort === "zone") {
      list.sort(function (a, b) { return (ZONE_ORDER[a.commuteZone] ?? 9) - (ZONE_ORDER[b.commuteZone] ?? 9) || (b.matchScore - a.matchScore); });
    } else if (f.sort === "company") {
      list.sort(function (a, b) { return String(a.company).localeCompare(String(b.company)); });
    }
    render(list);
    const empty = document.getElementById("jobs-empty");
    if (empty) empty.classList.toggle("hidden", list.length > 0);
  }

  window.addEventListener("DOMContentLoaded", function () {
    applyFilters();
    document.querySelectorAll(".f-status").forEach(function (b) {
      b.addEventListener("click", function () {
        document.querySelectorAll(".f-status").forEach(function (x) { x.classList.remove("active"); });
        b.classList.add("active");
        applyFilters();
      });
    });
    document.querySelectorAll(".f-zone").forEach(function (b) {
      b.addEventListener("click", function () {
        document.querySelectorAll(".f-zone").forEach(function (x) { x.classList.remove("active"); });
        b.classList.add("active");
        applyFilters();
      });
    });
    document.querySelectorAll(".f-batch").forEach(function (b) {
      b.addEventListener("click", function () {
        document.querySelectorAll(".f-batch").forEach(function (x) { x.classList.remove("active"); });
        b.classList.add("active");
        applyFilters();
      });
    });
    const searchInput = document.getElementById("search-input");
    if (searchInput) {
      searchInput.addEventListener("input", applyFilters);
    }
    const sortSel = document.getElementById("sort-select");
    if (sortSel) {
      sortSel.addEventListener("change", applyFilters);
    }
    const csvBtn = document.getElementById("export-csv");
    if (csvBtn) {
      csvBtn.addEventListener("click", function () {
        const rows = [["id", "company", "position", "matchScore", "zone", "status", "location", "officialLink", "applyLink", "subpage"]];
        (lastList || []).forEach(function (j) {
          rows.push([j.id, j.company, j.position, j.matchScore, j.commuteZone, j.status, j.location, j.officialLink, j.applyLink, j.subpage]);
        });
        const csv = "\uFEFF" + rows.map(function (r) {
          return r.map(function (c) { return '"' + String(c == null ? "" : c).replace(/"/g, '""') + '"'; }).join(",");
        }).join("\r\n");
        const blob = new Blob([csv], { type: "text/csv;charset=utf-8" });
        const a = document.createElement("a");
        a.href = URL.createObjectURL(blob);
        a.download = "jobsearchsf-export.csv";
        document.body.appendChild(a);
        a.click();
        setTimeout(function () { URL.revokeObjectURL(a.href); a.remove(); }, 500);
      });
    }
    const el = document.getElementById("today");
    if (el) el.textContent = new Date().toISOString().slice(0, 10);
  });
})();
