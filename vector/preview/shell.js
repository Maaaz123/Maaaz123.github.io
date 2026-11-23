/* The Vector — shared shell for static previews.
   Builds: DGA seal strip, side nav (workspace switcher + 2-level nav), top bar,
   toast region; wires the searchable dropdown (combobox) and small helpers.
   Each page declares: <body data-ws="app|intel" data-page="…" data-roles="pmo head" data-crumb="…"> */
(function () {
  "use strict";

  /* ---------- Icons: one set, 24px grid, 1.75 stroke ---------- */
  const P = {
    home: '<path d="M3 10.5 12 3l9 7.5"/><path d="M5 9v11h14V9"/><path d="M10 20v-6h4v6"/>',
    inbox: '<path d="M3 13h5l1.5 3h5L16 13h5"/><path d="M5 5h14l2 8v6H3v-6z"/>',
    tasks: '<path d="M9 6h11M9 12h11M9 18h11"/><path d="m3.5 6 1.5 1.5L7.5 5M3.5 12l1.5 1.5L7.5 11M3.5 18l1.5 1.5L7.5 17"/>',
    review: '<rect x="5" y="4" width="14" height="17" rx="2"/><path d="M9 4V3h6v1"/><path d="m9 13 2 2 4-4"/>',
    folder: '<path d="M3 6a1 1 0 0 1 1-1h5l2 2h9a1 1 0 0 1 1 1v10a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1z"/>',
    settings: '<path d="M4 6h10M18 6h2M4 12h4M12 12h8M4 18h12M20 18h0"/><circle cx="16" cy="6" r="2"/><circle cx="10" cy="12" r="2"/><circle cx="18" cy="18" r="2"/>',
    brief: '<path d="M6 3h9l4 4v14H6z"/><path d="M14 3v5h5M9 12h7M9 16h5"/>',
    summary: '<path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/>',
    layers: '<path d="m12 3 9 5-9 5-9-5z"/><path d="m3 13 9 5 9-5"/>',
    decision: '<path d="M5 21V4"/><path d="M5 4h11l-2 4 2 4H5"/>',
    chat: '<path d="M4 5h16v11H9l-5 4z"/><path d="M8 9h8M8 12h5"/>',
    menu: '<path d="M4 7h16M4 12h16M4 17h16"/>',
    x: '<path d="M6 6l12 12M18 6 6 18"/>',
    chevDown: '<path d="m6 9 6 6 6-6"/>',
    next: '<path d="M19 12H5M11 6l-6 6 6 6"/>',          /* points left: "forward" in RTL */
    back: '<path d="M5 12h14M13 6l6 6-6 6"/>',
    check: '<path d="M5 12.5 10 17l9-10"/>',
    checkCircle: '<circle cx="12" cy="12" r="9"/><path d="m8 12.5 3 3 5-6"/>',
    alert: '<path d="M12 3 2 20h20z"/><path d="M12 10v4M12 17v.01"/>',
    alertCircle: '<circle cx="12" cy="12" r="9"/><path d="M12 8v5M12 16v.01"/>',
    info: '<circle cx="12" cy="12" r="9"/><path d="M12 11v5M12 8v.01"/>',
    clock: '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    shield: '<path d="M12 3 4 6v6c0 4.5 3.4 8 8 9 4.6-1 8-4.5 8-9V6z"/><path d="m8.5 12 2.5 2.5 4.5-5"/>',
    lock: '<rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/>',
    plus: '<path d="M12 5v14M5 12h14"/>',
    search: '<circle cx="11" cy="11" r="7"/><path d="m20 20-4-4"/>',
    calendar: '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>',
    user: '<circle cx="12" cy="8" r="4"/><path d="M4 21c1-4 4.5-6 8-6s7 2 8 6"/>',
    switch: '<path d="M7 7h13M16 3l4 4-4 4M17 17H4M8 13l-4 4 4 4"/>',
    send: '<path d="M21 3 3 10l7 3 3 7z"/><path d="m10 13 4-4"/>',
    edit: '<path d="M4 20h4L19 9l-4-4L4 16z"/><path d="m14 6 4 4"/>',
    link: '<path d="M10 14a4 4 0 0 0 6 0l3-3a4 4 0 0 0-6-6l-1 1"/><path d="M14 10a4 4 0 0 0-6 0l-3 3a4 4 0 0 0 6 6l1-1"/>',
    flag: '<path d="M5 21V4M5 4h11l-2 4 2 4H5"/>',
    pause: '<circle cx="12" cy="12" r="9"/><path d="M10 9v6M14 9v6"/>',
    minus: '<circle cx="12" cy="12" r="9"/><path d="M8 12h8"/>',
    dash: '<circle cx="12" cy="12" r="9" stroke-dasharray="3 3"/>',
    arrowDown: '<path d="M12 5v14M6 13l6 6 6-6"/>',
    trend: '<path d="M3 17l6-6 4 4 8-8"/><path d="M15 7h6v6"/>',
    globe: '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3.5 3 14.5 0 18M12 3c-3 3.5-3 14.5 0 18"/>'
  };
  const icon = (n, cls = "") => `<svg class="i ${cls}" viewBox="0 0 24 24" aria-hidden="true" focusable="false">${P[n] || ""}</svg>`;
  window.VIcon = icon;

  /* Status badge helper (colour + icon + words) */
  const STATUS = {
    ontrack:    ["على المسار", "checkCircle"],
    behind:     ["متأخر عن المسار", "clock"],
    wellbehind: ["متأخر جدًا", "alert"],
    complete:   ["مكتمل", "check"],
    planned:    ["مخطط", "calendar"],
    nofig:      ["تحديث بلا نسب", "minus"],
    noupd:      ["بلا تحديث", "dash"],
    published:  ["منشور", "checkCircle"],
    review:     ["بانتظار المراجعة", "clock"],
    returned:   ["أُعيد للتصحيح", "edit"],
    draft:      ["مسودة", "edit"],
    notstarted: ["لم يبدأ", "dash"],
    leader:     ["يحتاج قرار القيادة", "flag"]
  };
  window.VBadge = (k, label) => `<span class="badge badge--${k}">${icon(STATUS[k][1])}${label || STATUS[k][0]}</span>`;
  document.querySelectorAll("[data-badge]").forEach(el => { el.outerHTML = window.VBadge(el.dataset.badge, el.textContent.trim() || undefined); });

  /* ---------- Roles & navigation model ---------- */
  const ROLES = {
    pmo:     { name: "مكتب البرنامج", person: "إدارة البرامج والمشاريع", initial: "م", ws: ["app", "intel"], home: "app-home.html" },
    manager: { name: "مدير المبادرة", person: "حزمة رأس المال البشري", initial: "د", ws: ["app"], home: "my-tasks.html" },
    head:    { name: "رئيس الجهة", person: "القيادة", initial: "ر", ws: ["intel"], home: "leadership-brief.html" }
  };
  const NAV = {
    app: {
      pmo: [
        { id: "home", label: "الرئيسية", href: "app-home.html", icon: "inbox", count: 4, countLabel: "مهام" },
        { id: "review", label: "المراجعة والنشر", href: "review.html", icon: "review", count: 5, countLabel: "بانتظار المراجعة" },
        { id: "programs", label: "البرامج", href: "setup-wizard.html", icon: "folder",
          children: [{ id: "setup", label: "برنامج التحول الرقمي 2027", href: "setup-wizard.html" }] },
        { id: "settings", label: "الإعدادات", href: "#", icon: "settings", soon: true }
      ],
      manager: [
        { id: "tasks", label: "مهامي", href: "my-tasks.html", icon: "tasks", count: 3, countLabel: "تحديثات مطلوبة",
          children: [{ id: "update", label: "تحديث نوفمبر", href: "quick-update.html" }] }
      ]
    },
    intel: [
      { id: "brief", label: "خلاصة القيادة", href: "leadership-brief.html", icon: "brief" },
      { id: "exec", label: "الملخص التنفيذي", href: "#", icon: "summary", soon: true },
      { id: "packages", label: "الحزم والمبادرات", href: "leadership-brief.html#packages", icon: "layers" },
      { id: "decisions", label: "قرارات القيادة", href: "leadership-brief.html#decisions", icon: "decision", count: 3, countLabel: "قرارات" },
      { id: "assistant", label: "المساعد الذكي", href: "#", icon: "chat", soon: true }
    ]
  };

  const body = document.body;
  const ws = body.dataset.ws;
  const pageId = body.dataset.page;
  const allowed = (body.dataset.roles || "").split(" ").filter(Boolean);
  let stored = null; try { stored = localStorage.getItem("tv-role"); } catch (e) {}
  const roleKey = allowed.includes(stored) ? stored : allowed[0];
  const role = ROLES[roleKey];

  /* ---------- Seal strip ---------- */
  function sealHTML() {
    return `
    <div class="seal" role="region" aria-label="التحقق من الموقع الحكومي">
      <div class="seal__bar">
        <span class="seal__mark">${icon("shield")}موقع حكومي مسجل لدى هيئة الحكومة الرقمية</span>
        <button class="seal__toggle" type="button" aria-expanded="false" aria-controls="seal-panel">كيف تحقق؟ ${icon("chevDown", "i--sm")}</button>
        <span class="seal__reg">رقم التسجيل: <bdi class="num">20XXXXXXXXX</bdi> <span class="placeholder-tag">رقم توضيحي — نسخة عرض</span></span>
      </div>
      <div class="seal__panel" id="seal-panel" hidden>
        <div class="cluster" style="--gap:12px;align-items:flex-start">${icon("globe")}<p>المواقع الحكومية الرسمية تستخدم نطاق <bdi dir="ltr">.gov.sa</bdi>، ويظهر في أعلاها رقم تسجيل يمكن التحقق منه لدى هيئة الحكومة الرقمية.</p></div>
        <div class="cluster" style="--gap:12px;align-items:flex-start">${icon("lock")}<p>هذه نسخة عرض: الرقم الظاهر مثال، ويُستبدل برقم تسجيل الجهة الفعلي ورابط التحقق الرسمي عند الإطلاق.</p></div>
      </div>
    </div>`;
  }

  function navItem(it) {
    const isCur = it.id === pageId || (it.children || []).some(c => c.id === pageId);
    const exact = it.id === pageId;
    const count = it.count ? `<span class="count" aria-label="${it.count} ${it.countLabel}">${it.count}</span>` : "";
    const soon = it.soon ? ` data-soon="1"` : "";
    let kids = "";
    if (it.children && isCur) {
      kids = `<ul>${it.children.map(c => `<li><a href="${c.href}"${c.id === pageId ? ' aria-current="page"' : ""}>${c.label}</a></li>`).join("")}</ul>`;
    }
    return `<li><a href="${it.href}"${exact ? ' aria-current="page"' : (isCur ? ' aria-current="true"' : "")}${soon}>${icon(it.icon)}<span>${it.label}</span>${count}</a>${kids}</li>`;
  }

  function sidenavHTML() {
    const items = ws === "app" ? (NAV.app[roleKey] || NAV.app.pmo) : NAV.intel;
    const wsLink = (k, label, href) => {
      if (!role.ws.includes(k)) return `<span aria-disabled="true" title="ليست ضمن صلاحيات دور ${role.name}">${icon("lock", "i--sm")}${label}</span>`;
      return `<a href="${href}"${ws === k ? ' aria-current="page"' : ""}>${label}</a>`;
    };
    const appHref = roleKey === "manager" ? "my-tasks.html" : "app-home.html";
    const foot = ws === "app"
      ? `<div class="cycle-mini">
           <div class="cycle-mini__row"><b>دورة نوفمبر 2026</b><span class="t-muted">تُغلق بعد 7 أيام</span></div>
           <div class="cycle-mini__bar" role="img" aria-label="18 من 30 بطاقة منشورة"><span style="inline-size:60%"></span></div>
           <div class="t-xs t-muted"><span class="num">18</span> من <span class="num">30</span> بطاقة منشورة</div>
         </div>`
      : `<div class="alert alert--neutral" style="padding:12px">${icon("lock", "i--sm")}<div class="alert__body"><span class="t-sm"><b>للقراءة فقط</b></span><span class="t-xs t-muted">تعرض ما نشره مكتب البرنامج فقط. آخر نشر: 20 نوفمبر</span></div></div>`;
    return `
      <a class="brand" href="welcome.html" aria-label="The Vector — الصفحة الأولى">
        <span class="brand__mark">${logoSVG()}</span>
        <span><span class="brand__name">The Vector</span><br><span class="brand__entity">هيئة الرواد للتطوير <span class="demo-tag">اسم تجريبي</span></span></span>
      </a>
      <fieldset class="ws-switch">
        <legend>مساحة العمل</legend>
        ${wsLink("app", "التطبيق", appHref)}
        ${wsLink("intel", "الطبقة الذكية", "leadership-brief.html")}
      </fieldset>
      <p class="nav-label" id="nav-label">${ws === "app" ? "التطبيق" : "الطبقة الذكية"}</p>
      <ul class="nav" aria-labelledby="nav-label">${items.map(navItem).join("")}</ul>
      <div class="sidenav__foot">
        ${foot}
        <div class="role-chip">
          <span class="role-chip__avatar" aria-hidden="true">${role.initial}</span>
          <span class="role-chip__text"><span class="t-xs t-muted">الدور الحالي</span><b>${role.name}</b></span>
          <a class="btn btn--tertiary btn--sm" href="welcome.html">تبديل</a>
        </div>
      </div>`;
  }

  function logoSVG() {
    // Vector mark: a rising path ending in a gold point — the programme moving towards its target.
    return `<svg width="24" height="24" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 18 10 12l3 3 6-7" fill="none" stroke="var(--dga-gray-0)" stroke-width="2.25" stroke-linecap="round" stroke-linejoin="round"/><circle cx="19" cy="7" r="2.6" fill="var(--dga-gold-400)"/></svg>`;
  }
  window.VLogo = logoSVG;

  function topbarHTML() {
    const wsName = ws === "app" ? "التطبيق" : "الطبقة الذكية";
    return `
      <button class="btn icon-btn menu-btn" type="button" aria-controls="sidenav" aria-expanded="false" aria-label="فتح القائمة">${icon("menu")}</button>
      <nav class="breadcrumb" aria-label="مسار التنقل"><ol>
        <li><a href="${ws === "app" ? (roleKey === "manager" ? "my-tasks.html" : "app-home.html") : "leadership-brief.html"}">${wsName}</a></li>
        ${(body.dataset.crumb || "").split("|").map((c, i, a) => `<li${i === a.length - 1 ? ' aria-current="page"' : ""}>${c}</li>`).join("")}
      </ol></nav>
      <div class="topbar__end">
        <span class="demo-tag">${icon("info", "i--sm")}<span>بيانات توضيحية<span class="long"> لأغراض العرض</span></span></span>
        <div class="seg" role="group" aria-label="اللغة">
          <button type="button" aria-pressed="true" lang="ar">ع</button>
          <button type="button" aria-pressed="false" lang="en" data-soon="1">EN</button>
        </div>
      </div>`;
  }

  /* ---------- Build ---------- */
  const main = document.getElementById("main");
  document.body.insertAdjacentHTML("afterbegin", `<a class="skip-link" href="#main">تخطَّ إلى المحتوى</a>${sealHTML()}`);
  if (main && ws) {
    const shell = document.createElement("div");
    shell.className = "shell";
    shell.innerHTML = `<nav class="sidenav" id="sidenav" aria-label="القائمة الرئيسية"><div class="sidenav__in">${sidenavHTML()}</div></nav><div class="scrim"></div><div class="main"><header class="topbar">${topbarHTML()}</header></div>`;
    main.parentNode.insertBefore(shell, main);
    shell.querySelector(".main").appendChild(main);
    const btn = shell.querySelector(".menu-btn");
    const setOpen = (o) => { shell.classList.toggle("nav-open", o); btn.setAttribute("aria-expanded", String(o)); btn.setAttribute("aria-label", o ? "إغلاق القائمة" : "فتح القائمة"); if (o) shell.querySelector(".sidenav a").focus(); };
    btn.addEventListener("click", () => setOpen(!shell.classList.contains("nav-open")));
    shell.querySelector(".scrim").addEventListener("click", () => setOpen(false));
    document.addEventListener("keydown", e => { if (e.key === "Escape" && shell.classList.contains("nav-open")) { setOpen(false); btn.focus(); } });
  }
  const sealBtn = document.querySelector(".seal__toggle");
  sealBtn.addEventListener("click", () => {
    const o = sealBtn.getAttribute("aria-expanded") === "true";
    sealBtn.setAttribute("aria-expanded", String(!o));
    document.getElementById("seal-panel").hidden = o;
  });

  /* ---------- Notifications: toast + success sheet ----------
     notify({type:"success"|"info"|"warning"|"error", title, text, undo})
     successSheet({title, text, rows:[[k,v]], primary:{label,href}, secondary:{label,href}}) */
  const region = document.createElement("div");
  region.className = "toast-region"; region.setAttribute("role", "status"); region.setAttribute("aria-live", "polite");
  document.body.appendChild(region);
  const NICON = {
    success: '<svg class="ni" viewBox="0 0 40 40" aria-hidden="true"><circle class="ni__ring" cx="20" cy="20" r="17"/><path class="ni__mark" d="M12.5 20.5l5 5 10-11"/></svg>',
    info:    '<svg class="ni" viewBox="0 0 40 40" aria-hidden="true"><circle class="ni__ring" cx="20" cy="20" r="17"/><path class="ni__mark" d="M20 18v10M20 12.5v.5"/></svg>',
    warning: '<svg class="ni" viewBox="0 0 40 40" aria-hidden="true"><path class="ni__ring" d="M20 4 37 34H3z"/><path class="ni__mark" d="M20 15v9M20 28.5v.5"/></svg>',
    error:   '<svg class="ni" viewBox="0 0 40 40" aria-hidden="true"><circle class="ni__ring" cx="20" cy="20" r="17"/><path class="ni__mark" d="M14 14l12 12M26 14 14 26"/></svg>'
  };
  window.notify = function (o) {
    const type = o.type || "success", ms = o.ms || 5200;
    const t = document.createElement("div");
    t.className = `toast toast--${type}`;
    t.innerHTML = `<span class="toast__icon">${NICON[type]}</span><div class="toast__body"><p class="toast__title">${o.title || ""}</p>${o.text ? `<p class="toast__text">${o.text}</p>` : ""}</div>${o.undo ? '<button type="button" class="toast__undo">تراجع</button>' : ""}<button type="button" class="toast__close" aria-label="إغلاق">${icon("x", "i--sm")}</button><span class="toast__timer" style="animation-duration:${ms}ms"></span>`;
    let left = ms, t0 = Date.now(), timer;
    const close = () => { t.classList.add("is-leaving"); setTimeout(() => t.remove(), 320); };
    const arm = () => { t0 = Date.now(); timer = setTimeout(close, left); };
    t.addEventListener("mouseenter", () => { clearTimeout(timer); left -= Date.now() - t0; t.classList.add("is-paused"); });
    t.addEventListener("mouseleave", () => { t.classList.remove("is-paused"); arm(); });
    t.querySelector(".toast__close").onclick = close;
    if (o.undo) t.querySelector(".toast__undo").onclick = () => { o.undo(); close(); };
    region.prepend(t);
    while (region.children.length > 3) region.lastChild.remove();
    arm();
    return t;
  };
  /* Old signature still works: toast("text", "info") */
  window.toast = (msg, ic = "checkCircle") => window.notify({ type: ic === "info" ? "info" : "success", title: msg });

  /* Empty / error state block with the product mark */
  window.VState = function (o) {
    const mark = `<svg class="vmark" viewBox="0 0 24 24" aria-hidden="true"><path class="vmark__path" d="M4 18 10 12l3 3 6-7"/><circle class="vmark__dot" cx="19" cy="7" r="2.6"/></svg>`;
    const ic = o.type === "error" ? icon("alertCircle", "i--lg") : mark;
    return `<div class="state state--${o.type || "empty"}"><span class="state__art">${ic}</span><h2 class="state__title" tabindex="-1">${o.title}</h2>${o.text ? `<p class="state__text">${o.text}</p>` : ""}${o.action ? `<div class="state__actions">${o.action}</div>` : ""}</div>`;
  };
  window.successSheet = function (o) {
    let d = document.getElementById("success-sheet");
    if (!d) { d = document.createElement("dialog"); d.id = "success-sheet"; d.className = "sheet"; document.body.appendChild(d); }
    const rows = (o.rows || []).map(([k, v]) => `<li><span>${k}</span><b>${v}</b></li>`).join("");
    const btn = (b, cls) => b ? (b.href ? `<a class="btn ${cls}" href="${b.href}">${b.label}</a>` : `<button type="button" class="btn ${cls}" data-close>${b.label}</button>`) : "";
    d.setAttribute("aria-labelledby", "sheet-t");
    d.innerHTML = `<div class="sheet__in"><div class="sheet__badge"><i></i><i></i><svg class="vmark" viewBox="0 0 24 24" aria-hidden="true"><path class="vmark__path" d="M4 18 10 12l3 3 6-7"/><circle class="vmark__dot" cx="19" cy="7" r="2.6"/></svg></div><h2 id="sheet-t" class="sheet__title" tabindex="-1">${o.title}</h2>${o.text ? `<p class="sheet__text">${o.text}</p>` : ""}${rows ? `<ul class="sheet__rows">${rows}</ul>` : ""}<div class="sheet__actions">${btn(o.primary, "btn--primary")}${btn(o.secondary, "btn--secondary")}</div></div>`;
    d.querySelectorAll("[data-close]").forEach(x => x.onclick = () => d.close());
    d.onclick = e => { if (e.target === d) d.close(); };
    d.showModal(); d.querySelector(".sheet__title").focus();
    setTimeout(() => window.VCelebrate && window.VCelebrate(d.querySelector(".sheet__badge")), 250);
  };
  document.addEventListener("click", e => {
    const s = e.target.closest("[data-soon]");
    if (s) { e.preventDefault(); window.notify({ type: "info", title: "غير متاحة في المعاينة", text: "هذه الصفحة خارج نطاق النسخة التجريبية." }); }
  });

  /* ---------- Searchable dropdown (combobox) ---------- */
  // Arabic-aware search: unify letter forms, then drop the definite article / "لل" so
  // "الموارد" finds "للموارد" and "اداره" finds "إدارة".
  const fold = s => (s || "").toLowerCase().replace(/[أإآ]/g, "ا").replace(/ة/g, "ه").replace(/ى/g, "ي"); // length-preserving
  const norm = s => fold(s).replace(/[\u064B-\u0652\u0640]/g, "").split(/\s+/).filter(Boolean)
    .map(w => w.length > 3 ? w.replace(/^(وال|بال|كال|فال|لل|ال)/, "") : w);
  const matches = (label, q) => { const L = norm(label).join(" "); return norm(q).every(t => L.includes(t)); };
  window.VCombo = function initCombo(root) {
    const input = root.querySelector(".combo__input");
    const list = root.querySelector(".combo__list");
    const toggle = root.querySelector(".combo__toggle");
    const hidden = root.querySelector("input[type=hidden]");
    const opts = [...list.querySelectorAll("[role=option]")];
    opts.forEach(o => { o.dataset.label = o.dataset.label || o.firstChild.textContent.trim(); });
    let empty = list.querySelector(".combo__empty");
    if (!empty) { empty = document.createElement("li"); empty.className = "combo__empty"; empty.setAttribute("role", "presentation"); empty.textContent = "لا توجد نتيجة مطابقة. جرّب كلمة أخرى."; empty.hidden = true; list.appendChild(empty); }
    let active = -1;
    const visible = () => opts.filter(o => !o.hidden);
    const open = () => { list.hidden = false; root.classList.add("is-open"); input.setAttribute("aria-expanded", "true"); };
    const close = () => { list.hidden = true; root.classList.remove("is-open"); input.setAttribute("aria-expanded", "false"); setActive(-1); };
    const setActive = (i) => {
      opts.forEach(o => o.classList.remove("is-active"));
      const v = visible(); active = i;
      if (i >= 0 && v[i]) { v[i].classList.add("is-active"); input.setAttribute("aria-activedescendant", v[i].id); v[i].scrollIntoView({ block: "nearest" }); }
      else input.removeAttribute("aria-activedescendant");
    };
    const filter = (all) => {
      const q = all ? "" : input.value.trim();
      opts.forEach(o => {
        const label = o.dataset.label;
        o.hidden = !!q && !matches(label + " " + (o.dataset.keywords || ""), q);
        const span = o.querySelector(".opt-label");
        const idx = q ? fold(label).indexOf(fold(q)) : -1;
        if (span) span.innerHTML = idx >= 0 ? label.slice(0, idx) + "<mark>" + label.slice(idx, idx + q.length) + "</mark>" + label.slice(idx + q.length) : label;
      });
      empty.hidden = visible().length > 0;
      setActive(visible().length ? 0 : -1);
    };
    const choose = (o) => {
      opts.forEach(x => x.setAttribute("aria-selected", "false"));
      o.setAttribute("aria-selected", "true");
      input.value = o.dataset.label;
      if (hidden) hidden.value = o.dataset.value || o.dataset.label;
      root.closest(".field")?.classList.remove("is-invalid");
      input.removeAttribute("aria-invalid");
      close();
      root.dispatchEvent(new CustomEvent("combo:change", { detail: o.dataset, bubbles: true }));
    };
    opts.forEach(o => {
      if (!o.querySelector(".opt-label")) {
        const t = o.firstChild; const s = document.createElement("span"); s.className = "opt-label"; s.textContent = t.textContent.trim(); o.replaceChild(s, t);
      }
      o.addEventListener("mousedown", e => { e.preventDefault(); choose(o); });
    });
    input.addEventListener("input", () => { open(); filter(); });
    input.addEventListener("focus", () => { input.select(); });
    const openAll = () => { open(); filter(true); const sel = visible().findIndex(o => o.getAttribute("aria-selected") === "true"); if (sel >= 0) setActive(sel); };
    input.addEventListener("click", () => { if (list.hidden) openAll(); });
    toggle.addEventListener("click", () => { if (list.hidden) { input.focus(); openAll(); } else close(); });
    input.addEventListener("keydown", e => {
      const v = visible();
      if (e.key === "ArrowDown") { e.preventDefault(); if (list.hidden) { openAll(); } else setActive(Math.min(active + 1, v.length - 1)); }
      else if (e.key === "ArrowUp") { e.preventDefault(); setActive(Math.max(active - 1, 0)); }
      else if (e.key === "Enter") { e.preventDefault(); if (!list.hidden && v[active]) choose(v[active]); }
      else if (e.key === "Escape") { if (!list.hidden) { e.preventDefault(); const sel = opts.find(o => o.getAttribute("aria-selected") === "true"); input.value = sel ? sel.dataset.label : ""; close(); } }
    });
    input.addEventListener("blur", () => setTimeout(() => {
      if (!root.contains(document.activeElement)) {
        const sel = opts.find(o => o.getAttribute("aria-selected") === "true");
        input.value = sel ? sel.dataset.label : "";
        close();
      }
    }, 120));
  };
  /* Build combobox markup from data-options="Label::meta|Label2" (keeps page HTML short) */
  window.VBuildCombo = function (root) {
    if (root.querySelector(".combo__list")) return;
    const id = root.dataset.id;
    const sel = root.dataset.selected || "";
    const opts = (root.dataset.options || "").split("|").filter(Boolean).map((o, i) => {
      const [label, meta] = o.split("::");
      return `<li role="option" id="${id}-o${i}" data-value="${label}" aria-selected="${label === sel}">${label}${meta ? `<small>${meta}</small>` : ""}</li>`;
    }).join("");
    const desc = root.dataset.describedby ? ` aria-describedby="${root.dataset.describedby}"` : "";
    root.innerHTML = `<div class="combo__control"><input class="input combo__input" id="${id}" type="text" role="combobox" aria-autocomplete="list" aria-expanded="false" aria-controls="${id}-list" autocomplete="off" value="${sel}" placeholder="${root.dataset.placeholder || "اكتب للبحث أو اختر"}"${desc}${root.dataset.required ? ' aria-required="true"' : ""}><button type="button" class="combo__toggle" tabindex="-1" aria-label="عرض الخيارات">${icon("chevDown")}</button></div><ul class="combo__list" role="listbox" id="${id}-list" aria-label="${root.dataset.label || ""}" hidden>${opts}</ul><input type="hidden" name="${id}" value="${sel}">`;
  };
  document.querySelectorAll(".combo").forEach(c => { window.VBuildCombo(c); window.VCombo(c); });
})();
