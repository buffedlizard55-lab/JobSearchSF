/* JobSearchSF — application tracker (localStorage, device-only, no account) */
(function () {
  var KEY = "jobsearchsf_tracker_v1";
  var CHECK_KEY = "jobsearchsf_checklist_v1";
  var STATUSES = ["not-started", "applied", "interview", "follow-up", "offer", "closed"];
  var LABELS = {
    "not-started": "Not started",
    "applied": "Applied",
    "interview": "Interview",
    "follow-up": "Follow-up sent",
    "offer": "Offer",
    "closed": "Closed / no fit"
  };
  var STEPS = [
    "Verified live posting on official site",
    "Created account on official portal",
    "Downloaded tailored resume + cover letter",
    "Submitted application directly (no recruiter)",
    "Saved confirmation number",
    "Prepared for interview",
    "Sent follow-up (7-10 days)"
  ];

  function load(key, fallback) {
    try {
      var raw = localStorage.getItem(key);
      return raw ? JSON.parse(raw) : fallback;
    } catch (e) { return fallback; }
  }
  function save(key, val) {
    try { localStorage.setItem(key, JSON.stringify(val)); } catch (e) {}
  }
  function esc(s) {
    return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
  }

  function getStatus(jobId) {
    var t = load(KEY, {});
    return t[jobId] || "not-started";
  }
  function setStatus(jobId, status) {
    var t = load(KEY, {});
    t[jobId] = status;
    save(KEY, t);
    // refresh any inline selects showing this job
    document.querySelectorAll('[data-tracker-for="' + jobId + '"]').forEach(function (el) {
      if (el.tagName === "SELECT") el.value = status;
    });
    renderSummary();
  }
  function getChecks(jobId) {
    var c = load(CHECK_KEY, {});
    return c[jobId] || [];
  }
  function setCheck(jobId, idx, on) {
    var c = load(CHECK_KEY, {});
    var arr = c[jobId] || [];
    arr[idx] = !!on;
    c[jobId] = arr;
    save(CHECK_KEY, c);
  }

  function statusBadge(status) {
    var map = {
      "not-started": "badge monitor",
      "applied": "badge zoneB",
      "interview": "badge score-mid",
      "follow-up": "badge score-mid",
      "offer": "badge verified",
      "closed": "badge flag"
    };
    return '<span class="' + (map[status] || "badge monitor") + '">' + esc(LABELS[status] || status) + "</span>";
  }

  /* Inline <select> for table rows */
  function selectHtml(jobId) {
    var cur = getStatus(jobId);
    var opts = STATUSES.map(function (s) {
      return '<option value="' + s + '"' + (s === cur ? " selected" : "") + ">" + esc(LABELS[s]) + "</option>";
    }).join("");
    return '<select class="tracker-select" data-tracker-for="' + esc(jobId) + '" aria-label="Application status for ' + esc(jobId) + '">' + opts + "</select>";
  }

  /* Full widget for subpages: status + checklist */
  function mount(elId, jobId) {
    var el = document.getElementById(elId);
    if (!el) return;
    var cur = getStatus(jobId);
    var checks = getChecks(jobId);
    var opts = STATUSES.map(function (s) {
      return '<option value="' + s + '"' + (s === cur ? " selected" : "") + ">" + esc(LABELS[s]) + "</option>";
    }).join("");
    var steps = STEPS.map(function (label, i) {
      var on = !!checks[i];
      return '<label class="check-item"><input type="checkbox" data-check-idx="' + i + '"' + (on ? " checked" : "") + "> " + esc(label) + "</label>";
    }).join("");
    el.innerHTML =
      '<div class="tracker-widget">' +
        '<div class="tracker-row"><strong>Status:</strong> <select class="tracker-select" data-tracker-for="' + esc(jobId) + '">' + opts + "</select> " + statusBadge(cur) + "</div>" +
        '<div class="tracker-steps">' + steps + "</div>" +
        '<p style="font-size:.8rem;color:var(--muted)">Saved automatically on this device. Nothing is uploaded anywhere.</p>' +
      "</div>";
    el.querySelector("select").addEventListener("change", function (e) {
      setStatus(jobId, e.target.value);
      mount(elId, jobId); // re-render badge
    });
    el.querySelectorAll("input[type=checkbox]").forEach(function (box) {
      box.addEventListener("change", function () {
        setCheck(jobId, parseInt(box.getAttribute("data-check-idx"), 10), box.checked);
      });
    });
  }

  /* Progress summary on index page */
  function renderSummary() {
    var el = document.getElementById("tracker-summary");
    if (!el) return;
    var t = load(KEY, {});
    var total = (window.JOBS_DATA || []).length;
    var counts = {};
    STATUSES.forEach(function (s) { counts[s] = 0; });
    (window.JOBS_DATA || []).forEach(function (j) {
      var s = t[j.id] || "not-started";
      counts[s] = (counts[s] || 0) + 1;
    });
    var done = (counts["applied"] || 0) + (counts["interview"] || 0) + (counts["follow-up"] || 0) + (counts["offer"] || 0);
    var pct = total ? Math.round((done / total) * 100) : 0;
    el.innerHTML =
      "<strong>My progress:</strong> " + done + " / " + total + " in motion (" + pct + "%) · " +
      statusBadge("applied") + " " + (counts["applied"] || 0) + " · " +
      statusBadge("interview") + " " + (counts["interview"] || 0) + " · " +
      statusBadge("follow-up") + " " + (counts["follow-up"] || 0) + " · " +
      statusBadge("offer") + " " + (counts["offer"] || 0) +
      ' <button class="btn btn-sm" id="tracker-reset" style="margin-left:8px">Reset</button>';
    var reset = document.getElementById("tracker-reset");
    if (reset) reset.addEventListener("click", function () {
      if (confirm("Reset all tracked statuses and checklists on this device?")) {
        save(KEY, {}); save(CHECK_KEY, {});
        document.querySelectorAll(".tracker-select").forEach(function (s) { s.value = "not-started"; });
        renderSummary();
      }
    });
  }

  window.JobTracker = {
    mount: mount,
    selectHtml: selectHtml,
    statusBadge: statusBadge,
    getStatus: getStatus,
    setStatus: setStatus,
    renderSummary: renderSummary
  };

  document.addEventListener("change", function (e) {
    var t = e.target;
    if (t && t.classList && t.classList.contains("tracker-select") && t.getAttribute("data-tracker-for")) {
      setStatus(t.getAttribute("data-tracker-for"), t.value);
    }
  });
})();
