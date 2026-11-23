/* The Vector — month-range picker.
   <div class="period" data-id="x" data-from="2027-01" data-to="2027-06" data-min="2027-01" data-max="2028-12" data-label="مدة المبادرة"></div>
   Click a start month, then an end month. Fires "period:change" {from, to} on the element.
   Window API: VPeriod(el) to build one added later; VPeriodText("2027-01","2027-06") for display. */
(function () {
  "use strict";
  const M = ["يناير", "فبراير", "مارس", "أبريل", "مايو", "يونيو", "يوليو", "أغسطس", "سبتمبر", "أكتوبر", "نوفمبر", "ديسمبر"];
  const parse = s => { const [y, m] = (s || "").split("-").map(Number); return y ? y * 12 + (m - 1) : null; };
  const fmt = n => `${Math.floor(n / 12)}-${String(n % 12 + 1).padStart(2, "0")}`;
  const name = n => `${M[n % 12]} ${Math.floor(n / 12)}`;
  const text = (a, b) => {
    if (a == null) return "";
    if (b == null || a === b) return name(a);
    const ya = Math.floor(a / 12), yb = Math.floor(b / 12);
    return ya === yb ? `${M[a % 12]} – ${M[b % 12]} ${ya}` : `${name(a)} – ${name(b)}`;
  };
  const months = (a, b) => b - a + 1;
  const dur = n => n === 12 ? "سنة كاملة" : n === 1 ? "شهر واحد" : n === 2 ? "شهران" : n <= 10 ? `${n} أشهر` : `${n} شهرًا`;
  window.VPeriodText = (a, b) => text(parse(a), parse(b));
  window.VPeriodMonths = (a, b) => months(parse(a), parse(b));

  const CAL = '<svg class="i" viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/></svg>';
  const PREV = '<svg class="i i--sm" viewBox="0 0 24 24" aria-hidden="true"><path d="M9 6l6 6-6 6"/></svg>';
  const NEXT = '<svg class="i i--sm" viewBox="0 0 24 24" aria-hidden="true"><path d="M15 6l-6 6 6 6"/></svg>';
  let openOne = null;

  window.VPeriod = function (root) {
    if (root.dataset.ready) return; root.dataset.ready = "1";
    const id = root.dataset.id;
    let from = parse(root.dataset.from), to = parse(root.dataset.to);
    const min = parse(root.dataset.min), max = parse(root.dataset.max);
    let year = Math.floor((from ?? min ?? parse("2027-01")) / 12), picking = "from", hover = null;

    root.innerHTML = `<button type="button" class="period__btn input" id="${id}" aria-haspopup="dialog" aria-expanded="false">${CAL}<span class="period__val"></span><span class="period__dur"></span></button>
      <div class="period__pop" role="dialog" aria-label="${root.dataset.label || "اختر الفترة"}" hidden>
        <div class="period__head"><button type="button" class="period__nav" data-y="-1" aria-label="السنة السابقة">${PREV}</button><b class="period__year"></b><button type="button" class="period__nav" data-y="1" aria-label="السنة التالية">${NEXT}</button></div>
        <p class="period__hint"></p>
        <div class="period__grid" role="group"></div>
        <div class="period__presets"><span>سريع:</span><button type="button" data-n="3">3 أشهر</button><button type="button" data-n="6">6 أشهر</button><button type="button" data-n="12">سنة</button></div>
        <div class="period__foot"><span class="period__sum"></span><button type="button" class="btn btn--primary btn--sm period__ok">تم</button></div>
      </div>
      <input type="hidden" name="${id}-from"><input type="hidden" name="${id}-to">`;
    const btn = root.querySelector(".period__btn"), pop = root.querySelector(".period__pop"), grid = root.querySelector(".period__grid");
    const hFrom = root.querySelector(`[name="${id}-from"]`), hTo = root.querySelector(`[name="${id}-to"]`);

    function paint() {
      root.querySelector(".period__val").textContent = text(from, to) || "اختر الفترة";
      root.querySelector(".period__dur").textContent = from != null && to != null ? dur(months(from, to)) : "";
      root.classList.toggle("is-empty", from == null);
      hFrom.value = from != null ? fmt(from) : ""; hTo.value = to != null ? fmt(to) : "";
      root.querySelector(".period__year").textContent = year;
      root.querySelector(".period__hint").textContent = picking === "from" ? "اختر شهر البداية" : "اختر شهر النهاية";
      root.querySelector(".period__sum").textContent = from != null && to != null ? `${text(from, to)} · ${dur(months(from, to))}` : "";
      const end = picking === "to" && hover != null ? hover : to;
      const lo = from != null && end != null ? Math.min(from, end) : from, hi = from != null && end != null ? Math.max(from, end) : from;
      if (+grid.dataset.year !== year) {
        grid.dataset.year = year;
        grid.innerHTML = M.map((m, i) => { const n = year * 12 + i, off = (min != null && n < min) || (max != null && n > max);
          return `<button type="button" class="period__m" data-n="${n}" ${off ? "disabled" : ""}>${m}</button>`; }).join("");
      }
      grid.querySelectorAll(".period__m").forEach(b => { const n = +b.dataset.n;
        b.classList.toggle("is-start", n === lo); b.classList.toggle("is-end", n === hi);
        b.classList.toggle("is-in", lo != null && n > lo && n < hi); b.setAttribute("aria-pressed", String(lo != null && n >= lo && n <= hi)); });
      root.querySelectorAll(".period__nav").forEach(b => {
        const y = year + +b.dataset.y;
        b.disabled = (min != null && y * 12 + 11 < min) || (max != null && y * 12 > max);
      });
    }
    function emit() { root.dispatchEvent(new CustomEvent("period:change", { bubbles: true, detail: { from: hFrom.value, to: hTo.value } })); }
    function show() {
      if (openOne && openOne !== close) openOne();
      pop.hidden = false; btn.setAttribute("aria-expanded", "true"); root.classList.add("is-open"); picking = "from"; paint();
      const r = pop.getBoundingClientRect(); root.classList.toggle("is-up", r.bottom > innerHeight - 8 && r.top > r.height + 80);
      (grid.querySelector(".is-start") || grid.querySelector("button:not(:disabled)"))?.focus();
      openOne = close;
    }
    function close() { pop.hidden = true; btn.setAttribute("aria-expanded", "false"); root.classList.remove("is-open", "is-up"); hover = null; if (openOne === close) openOne = null; }
    btn.addEventListener("click", () => pop.hidden ? show() : close());
    grid.addEventListener("mouseover", e => { const b = e.target.closest(".period__m"); if (b && picking === "to" && hover !== +b.dataset.n) { hover = +b.dataset.n; paint(); } });
    grid.addEventListener("click", e => {
      const b = e.target.closest(".period__m"); if (!b) return; const n = +b.dataset.n;
      if (picking === "from") { from = n; to = n; picking = "to"; paint(); }
      else { if (n < from) { to = from; from = n; } else to = n; picking = "from"; hover = null; paint(); emit(); root.classList.add("is-picked"); setTimeout(() => { root.classList.remove("is-picked"); close(); btn.focus(); }, 260); }
    });
    root.querySelector(".period__presets").addEventListener("click", e => {
      const b = e.target.closest("[data-n]"); if (!b) return;
      if (from == null) from = year * 12;
      to = from + +b.dataset.n - 1; if (max != null && to > max) to = max;
      picking = "from"; paint(); emit();
    });
    root.querySelectorAll(".period__nav").forEach(b => b.addEventListener("click", () => { year += +b.dataset.y; paint(); }));
    root.querySelector(".period__ok").addEventListener("click", () => { close(); btn.focus(); });
    root.addEventListener("keydown", e => {
      if (e.key === "Escape" && !pop.hidden) { e.stopPropagation(); close(); btn.focus(); }
      const b = e.target.closest(".period__m"); if (!b) return;
      const d = { ArrowLeft: 1, ArrowRight: -1, ArrowDown: 3, ArrowUp: -3 }[e.key];   // RTL grid
      if (d) { e.preventDefault(); const k = +b.dataset.n - year * 12 + d; if (k < 0) { year--; paint(); } else if (k > 11) { year++; paint(); } const t = grid.querySelector(`[data-n="${+b.dataset.n + d}"]`); t && !t.disabled && t.focus(); }
    });
    document.addEventListener("pointerdown", e => { if (!pop.hidden && !root.contains(e.target)) close(); });
    root.setValue = (a, b) => { from = parse(a); to = parse(b); if (from != null) year = Math.floor(from / 12); paint(); };
    root.getValue = () => ({ from: hFrom.value, to: hTo.value });
    paint();
  };
  document.querySelectorAll(".period").forEach(window.VPeriod);
})();
