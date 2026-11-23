/* The Vector — motion layer: reveal on scroll, count-up, growing bars,
   step swaps, ripple, success burst. Purely decorative; respects reduced motion. */
(function () {
  "use strict";
  const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (reduce) return;

  const REVEAL = [
    ".page-head > *", ".w-hero__in > *", ".hero__in > *",
    ".kpi", ".task", ".role", ".card", "tbody tr", ".steps__item", ".legend li", ".tasks > *"
  ].join(",");
  const GROW = ".meter__fill, .cycle-bar > span, .seg-s";

  const io = new IntersectionObserver(entries => {
    entries.forEach(e => {
      if (!e.isIntersecting) return;
      const el = e.target; io.unobserve(el);
      el.classList.add("mx-on");
      if (el.closest(".hero")) el.querySelectorAll(".kpi__value").forEach(countUp);
    });
  }, { threshold: 0.12, rootMargin: "0px 0px -6% 0px" });

  function prime(root) {
    const groups = new Map();
    root.querySelectorAll(REVEAL).forEach(el => {
      if (el.closest(".mx-in") && el.closest(".mx-in") !== el) return;   // don't nest reveals
      if (el.classList.contains("mx-in") || el.closest(".sidenav, .seal, .combo__list, [hidden]")) return;
      const p = el.parentElement; const i = groups.get(p) || 0; groups.set(p, i + 1);
      el.style.setProperty("--mx-d", Math.min(i * 70, 560) + "ms");
      el.classList.add("mx-in"); io.observe(el);
    });
    root.querySelectorAll(GROW).forEach((el, i) => {
      if (el.classList.contains("mx-grow")) return;
      el.style.setProperty("--mx-d", (200 + (i % 12) * 60) + "ms");
      el.classList.add("mx-grow"); io.observe(el);
    });
  }

  /* Count-up: animates the first number in the text, keeps everything else (%, ٪, commas) */
  function countUp(el) {
    if (el.dataset.mxCounted) return; el.dataset.mxCounted = "1";
    /* work on the first text node that holds a number, so child markup and spacing stay intact */
    const w = document.createTreeWalker(el, NodeFilter.SHOW_TEXT); let node, m;
    while ((node = w.nextNode())) { m = node.nodeValue.match(/\d[\d,]*(\.\d+)?/); if (m) break; }
    if (!node || !m) return;
    const txt = node.nodeValue;
    const target = parseFloat(m[0].replace(/,/g, "")); const dec = m[1] ? m[1].length - 1 : 0;
    if (!isFinite(target) || target === 0) return;
    const pre = txt.slice(0, m.index), post = txt.slice(m.index + m[0].length);
    const dur = 1200 + Math.min(target, 100) * 4; const t0 = performance.now();
    const fmt = v => (dec ? v.toFixed(dec) : Math.round(v).toLocaleString("en-US"));
    node.nodeValue = pre + fmt(0) + post;
    (function tick(t) {
      const k = Math.min(1, (t - t0) / dur); const e = 1 - Math.pow(1 - k, 4);
      node.nodeValue = pre + fmt(target * e) + post;
      if (k < 1) requestAnimationFrame(tick);
    })(t0);
  }

  /* Stage/panel swaps: replay an entrance whenever something becomes visible */
  const mo = new MutationObserver(list => {
    list.forEach(m => {
      const el = m.target;
      if (m.attributeName === "hidden" && !el.hidden && el.matches(".stage, .panel, [data-step]")) {
        el.classList.remove("mx-swap"); void el.offsetWidth; el.classList.add("mx-swap");
        prime(el);
        if (el.id === "stage-sent") celebrate(el);
      }
    });
  });
  document.querySelectorAll(".stage, .panel, [data-step]").forEach(el => mo.observe(el, { attributes: true, attributeFilter: ["hidden"] }));

  /* Success: draw the check, small gold/green burst */
  function celebrate(scope) {
    const ic = scope.querySelector("svg"); if (ic && !scope.closest("dialog")) { ic.classList.remove("mx-check"); void ic.getBoundingClientRect(); ic.classList.add("mx-check"); }
  }
  window.VCelebrate = celebrate;

  /* Ripple on every button press */
  document.addEventListener("pointerdown", e => {
    const b = e.target.closest(".btn"); if (!b || b.disabled || b.getAttribute("aria-disabled") === "true") return;
    const r = b.getBoundingClientRect(); const s = Math.max(r.width, r.height);
    const w = document.createElement("span"); w.className = "mx-ripple";
    w.style.cssText = `width:${s}px;height:${s}px;left:${e.clientX - r.left - s / 2}px;top:${e.clientY - r.top - s / 2}px`;
    b.appendChild(w); setTimeout(() => w.remove(), 650);
  });

  const start = () => prime(document);
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", () => requestAnimationFrame(start));
  else requestAnimationFrame(start);
  /* Pages that render content late (JS-built lists) */
  window.addEventListener("load", () => setTimeout(() => prime(document), 50));
})();
