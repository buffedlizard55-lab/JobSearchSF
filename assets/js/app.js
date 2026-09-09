/* JobSearchSF — rendering & filtering (pure client-side) */
(function () {
  const STATUS_META = {
    "recently-posted": { cls: "badge recently-posted", label: "Recently posted (re-verify live)" },
    "monitor":          { cls: "badge monitor", label: "Monitor — posts periodically" },
    "flag":             { cls: "badge flag", label: "Flagged / review" }
  };
  const ZONE_META = {
    A: { cls: "badge zoneA", label: "Zone A — Shortest commute (~inner Sunset / Parnassus)" },
    B: { cls: "badge zoneB", label: "Zone B — Good (downtown/Mission Bay via N-Metro)" },
    C: { cls: "badge zoneC", label: "Zone C — Moderate/long (cross-town)" },
    D: { cls: "badge zoneD", label: "Zone D — Longest SFMTA trip" },
    Flagged: { cls: "badge zoneFlagged", label: "Flagged — not commute-friendly" }
  };

  function esc(s) {
    return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
  }
  function linkify(url) { return '<a href="' + esc(url) + '" target="_blank" rel="noopener">' + esc(url) + "</a>"; }
  function sourcesHtml(arr) {
    if (!arr || !arr.length) return "";
    const items = arr.map(function (s) {
      const u = s.url || "#";
      return '<li>' + esc(s.label) + " — " + linkify(u) + "</li>";
    }).join("");
    return '<div class="sources"><strong>Sources for manual review:</strong><ul>' + items + "</ul></div>";
  }

  function jobCard(j) {
    const st = STATUS_META[j.status] || STATUS_META.monitor;
    const zm = ZONE_META[j.commuteZone] || ZONE_META.C;
    const badgeRow =
      '<span class="' + st.cls + '">' + esc(st.label) + "</span> " +
      '<span class="' + zm.cls + '">' + esc(zm.label.split(" — ")[0]) + "</span>";
    let flag = "";
    if (j.flag) flag = '<div class="flag-note">&#9888; ' + esc(j.flag) + "</div>";
    return (
      '<article class="job" data-id="' + esc(j.id) + '">' +
        "<div>" +
          '<h4>' + esc(j.employer) + "</h4>" +
          '<div class="role">' + esc(j.role) + "</div>" +
          '<div class="meta-row"><span>' + badgeRow + "</span></div>" +
          '<div class="meta-row"><span>📍 ' + esc(j.location) + "</span><span>🏢 " + esc(j.orgType) + "</span></div>" +
        "</div>" +
        '<div class="grid">' +
          '<div class="field"><div class="lbl">Status</div><div class="val">' + esc(j.statusNote) + "</div></div>" +
          '<div class="field"><div class="lbl">Transit from ~21st &amp; Judah</div><div class="val">' + esc(j.route) + "</div></div>" +
          '<div class="field"><div class="lbl">Fit &amp; notes</div><div class="val"><strong>Fit:</strong> ' + esc(j.fit) + "<br><br><strong>Req:</strong> " + esc(j.requirements) + "</div></div>" +
          '<div class="field apply"><div class="lbl">Apply directly with employer</div><div class="val">' + esc(j.applyChannel) + "<br>" + esc(j.apply) + "</div></div>" +
        "</div>" +
        flag +
        sourcesHtml(j.sources) +
      "</article>"
    );
  }

  function render() {
    const list = window.JOBS_DATA || [];
    const container = document.getElementById("jobs");
    const refContainer = document.getElementById("monitor-ref");
    container.innerHTML = list.map(jobCard).join("");
    if (refContainer && window.MONITOR_REFERENCE) {
      refContainer.innerHTML = window.MONITOR_REFERENCE.map(function (m) {
        const s = m.source ? "<br><span style='font-size:.8rem'>" + linkify(m.source) + "</span>" : "";
        return '<div class="field"><div class="lbl">' + esc(m.employer) + "</div><div class='val'>" + esc(m.note) + s + "</div></div>";
      }).join("");
    }
    updateCount(list);
  }

  function updateCount(list) {
    const el = document.getElementById("count");
    if (el) el.textContent = list.length + " verified opportunity rows (re-verify live postings)";
  }

  function filterBy(status) {
    const list = window.JOBS_DATA || [];
    const btns = document.querySelectorAll(".filters .f-status");
    btns.forEach(function (b) { b.classList.toggle("active", b.dataset.status === status); });
    const filtered = status === "all" ? list : list.filter(function (j) { return j.status === status; });
    const container = document.getElementById("jobs");
    container.innerHTML = filtered.map(jobCard).join("");
    updateCount(filtered);
    document.getElementById("jobs-empty").classList.toggle("hidden", filtered.length > 0);
  }

  window.addEventListener("DOMContentLoaded", function () {
    render();
    // wire filter buttons
    document.querySelectorAll(".f-status").forEach(function (b) {
      b.addEventListener("click", function () { filterBy(b.dataset.status); });
    });
    // today's date footer
    const el = document.getElementById("today");
    if (el) el.textContent = new Date().toISOString().slice(0, 10);
  });
})();
