/* JobSearchSF — rendering & filtering (pure client-side) — 20 verified entries */
(function () {
  const STATUS_META = {
    "recently-posted": { cls: "badge recently-posted", label: "Recently posted" },
    "monitor":          { cls: "badge monitor", label: "Monitor" },
    "flag":             { cls: "badge flag", label: "Flagged" }
  };
  const ZONE_META = {
    A: { cls: "badge zoneA", label: "Zone A — Shortest (~Inner Sunset/Parnassus)" },
    B: { cls: "badge zoneB", label: "Zone B — Good (Mission Bay via N→T)" },
    C: { cls: "badge zoneC", label: "Zone C — Moderate" },
    D: { cls: "badge zoneD", label: "Zone D — Longest (Bayview)" },
    Flagged: { cls: "badge zoneFlagged", label: "Flagged" }
  };

  function esc(s) {
    return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
  }
  function linkify(url) { return '<a href="' + esc(url) + '" target="_blank" rel="noopener">' + esc(url) + '</a>'; }
  function scoreBadge(score) {
    if (score >= 85) return '<span class="badge score-high">' + esc(score) + '% match</span>';
    if (score >= 70) return '<span class="badge score-mid">' + esc(score) + '% match</span>';
    return '<span class="badge score-low">' + esc(score) + '% match</span>';
  }
  function sourcesHtml(arr) {
    if (!arr || !arr.length) return "";
    const items = arr.map(function (s) {
      const u = s.url || "#";
      return '<li>' + esc(s.label) + ' — <a href="' + esc(u) + '" target="_blank" rel="noopener">' + esc(u) + '</a></li>';
    }).join("");
    return '<div class="sources"><strong>Sources for manual review (official verified):</strong><ul>' + items + "</ul></div>";
  }

  function jobRow(j) {
    const st = STATUS_META[j.status] || STATUS_META.monitor;
    const zm = ZONE_META[j.commuteZone] || ZONE_META.C;
    const verifiedBadge = j.verified ? '<span class="badge verified">✓ Verified</span>' : '<span class="badge flag">Unverified</span>';
    return (
      '<tr data-id="' + esc(j.id) + '">' +
        '<td><div class="company">' + esc(j.company) + '</div><div class="role">' + esc(j.position) + '</div><div style="margin-top:6px"><span class="' + st.cls + '">' + esc(st.label) + '</span> <span class="' + zm.cls + '">' + esc(zm.label.split(" — ")[0]) + '</span></div></td>' +
        '<td>' + verifiedBadge + '<div style="margin-top:6px;font-size:.78rem;color:#5f6f81">' + esc(j.verificationMethod || "Official site + address") + '</div></td>' +
        '<td>' + scoreBadge(j.matchScore || 0) + '<div style="margin-top:6px;font-size:.80rem">' + esc(j.fit ? j.fit.slice(0,90) + "..." : "") + '</div></td>' +
        '<td><a href="' + esc(j.officialLink) + '" target="_blank" rel="noopener" class="btn btn-sm">Official site</a><div style="margin-top:6px;font-size:.78rem"><a href="' + esc(j.applyLink) + '" target="_blank" rel="noopener">' + esc(j.applyLink.slice(0,55)) + '...</a></div></td>' +
        '<td><a href="' + esc(j.subpage) + '" class="btn btn-sm btn-primary">Apply guide →</a><div style="margin-top:6px;font-size:.78rem">📍 ' + esc(j.location) + '</div></td>' +
      '</tr>'
    );
  }

  function jobCard(j) {
    const st = STATUS_META[j.status] || STATUS_META.monitor;
    const zm = ZONE_META[j.commuteZone] || ZONE_META.C;
    const verifiedBadge = j.verified ? '<span class="badge verified">✓ Verified — official site + SF address</span>' : '';
    let flag = "";
    if (j.flag) flag = '<div class="flag-note">⚠ ' + esc(j.flag) + "</div>";
    return (
      '<article class="job" data-id="' + esc(j.id) + '" id="' + esc(j.id) + '">' +
        "<div>" +
          '<h4>' + esc(j.company) + ' ' + verifiedBadge + '</h4>' +
          '<div class="role">' + esc(j.position) + "</div>" +
          '<div class="meta-row"><span><span class="' + st.cls + '">' + esc(st.label) + '</span> <span class="' + zm.cls + '">' + esc(zm.label) + '</span> ' + scoreBadge(j.matchScore) + '</span></div>' +
          '<div class="meta-row"><span>📍 ' + esc(j.location) + '</span><span>🏢 ' + esc(j.company) + '</span></div>' +
        "</div>" +
        '<div class="grid">' +
          '<div class="field"><div class="lbl">Status & verification</div><div class="val">' + esc(j.statusNote) + '<br><br><strong>Verified:</strong> ' + esc(j.verificationMethod) + '</div></div>' +
          '<div class="field"><div class="lbl">Transit from ~21st & Judah (N Judah + bus)</div><div class="val">' + esc(j.route) + '</div></div>' +
          '<div class="field"><div class="lbl">Fit & requirements</div><div class="val"><strong>Match:</strong> ' + esc(j.matchScore) + '% — ' + esc(j.fit) + '<br><br><strong>Req:</strong> ' + esc(j.requirements) + '</div></div>' +
          '<div class="field apply"><div class="lbl">Apply directly (official)</div><div class="val"><strong>' + esc(j.applyChannel) + '</strong><br><a href="' + esc(j.applyLink) + '" target="_blank" rel="noopener">' + esc(j.applyLink) + '</a><br><br><a href="' + esc(j.subpage) + '" class="btn btn-primary btn-sm">Open step-by-step apply guide →</a><br><br><a href="' + esc(j.officialLink) + '" target="_blank" rel="noopener">' + esc(j.officialLink) + '</a></div></div>' +
        "</div>" +
        flag +
        sourcesHtml(j.sources) +
      "</article>"
    );
  }

  function render(list) {
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
  }

  function filterBy(status, searchTerm) {
    let list = window.JOBS_DATA || [];
    if (status && status !== "all") {
      list = list.filter(function (j) { return j.status === status; });
    }
    if (searchTerm) {
      const q = searchTerm.toLowerCase();
      list = list.filter(function (j) {
        return (j.company + " " + j.position + " " + j.location + " " + j.fit + " " + j.requirements).toLowerCase().includes(q);
      });
    }
    render(list);
    const empty = document.getElementById("jobs-empty");
    if (empty) empty.classList.toggle("hidden", list.length > 0);
  }

  window.addEventListener("DOMContentLoaded", function () {
    const list = window.JOBS_DATA || [];
    render(list);
    // filters
    document.querySelectorAll(".f-status").forEach(function (b) {
      b.addEventListener("click", function () {
        document.querySelectorAll(".f-status").forEach(function (x) { x.classList.remove("active"); });
        b.classList.add("active");
        const term = document.getElementById("search-input") ? document.getElementById("search-input").value : "";
        filterBy(b.dataset.status, term);
      });
    });
    const searchInput = document.getElementById("search-input");
    if (searchInput) {
      searchInput.addEventListener("input", function () {
        const activeBtn = document.querySelector(".f-status.active");
        const status = activeBtn ? activeBtn.dataset.status : "all";
        filterBy(status, searchInput.value);
      });
    }
    const el = document.getElementById("today");
    if (el) el.textContent = new Date().toISOString().slice(0, 10);
  });
})();
