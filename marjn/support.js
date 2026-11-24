// Marjn demo runtime: renders the .dc.html screens as a static site.
(function () {
  const faces = [];

  window.DCLogic = class DCLogic {
    constructor(props) { this.props = props || {}; this.state = {}; }
    setState(p) {
      const patch = typeof p === 'function' ? p(this.state) : p;
      this.state = Object.assign({}, this.state, patch);
      window.__dcRender();
    }
    forceUpdate() { window.__dcRender(); }
  };

  function lookup(path, scope) {
    path = path.trim();
    if (path === 'true') return true;
    if (path === 'false') return false;
    if (/^-?\d+(\.\d+)?$/.test(path)) return Number(path);
    let cur = scope;
    for (const part of path.split('.')) {
      if (cur == null) { window.__dcWarnings.push('unresolved hole: ' + path); return undefined; }
      cur = cur[part];
    }
    if (cur === undefined) window.__dcWarnings.push('undefined hole: ' + path);
    return cur;
  }
  const WHOLE = /^\s*\{\{\s*([^}]+?)\s*\}\}\s*$/;
  const interp = (s, scope) => s.replace(/\{\{\s*([^}]+?)\s*\}\}/g, (_, p) => { const v = lookup(p, scope); return v == null ? '' : String(v); });

  function renderNode(node, scope, out) {
    if (node.nodeType === 3) { out.push(document.createTextNode(interp(node.nodeValue, scope))); return; }
    if (node.nodeType !== 1) return;
    const tag = node.localName;
    if (tag === 'helmet') return;
    if (tag === 'template' && node.hasAttribute('data-sc')) {
      const kind = node.getAttribute('data-sc'), kids = (node.content || node).childNodes;
      if (kind === 'if') { if (lookup(WHOLE.exec(node.getAttribute('value'))[1], scope)) kids.forEach((c) => renderNode(c, scope, out)); return; }
      const list = lookup(WHOLE.exec(node.getAttribute('list'))[1], scope) || [], as = node.getAttribute('as');
      list.forEach((item, i) => { const s2 = Object.assign({}, scope, { [as]: item, $index: i }); kids.forEach((c) => renderNode(c, s2, out)); });
      return;
    }
    if (tag === 'sc-if') {
      const v = lookup(WHOLE.exec(node.getAttribute('value'))[1], scope);
      if (v) node.childNodes.forEach((c) => renderNode(c, scope, out));
      return;
    }
    if (tag === 'sc-for') {
      const list = lookup(WHOLE.exec(node.getAttribute('list'))[1], scope) || [];
      const as = node.getAttribute('as');
      list.forEach((item, i) => {
        const s2 = Object.assign({}, scope, { [as]: item, $index: i });
        node.childNodes.forEach((c) => renderNode(c, s2, out));
      });
      return;
    }
    const el = node.namespaceURI === 'http://www.w3.org/2000/svg'
      ? document.createElementNS(node.namespaceURI, tag) : document.createElement(tag);
    const props = [];
    for (const a of Array.from(node.attributes)) {
      const m = WHOLE.exec(a.value);
      if (a.name.startsWith('on') && m) {
        const fn = lookup(m[1], scope);
        let ev = a.name.slice(2);
        if (ev === 'change' && (tag === 'input' && !['checkbox', 'radio'].includes(node.getAttribute('type')) || tag === 'textarea')) ev = 'input';
        if (typeof fn === 'function') { (el.__on = el.__on || {})[ev] = fn; }
        else window.__dcWarnings.push('handler not a function: ' + m[1]);
        continue;
      }
      if ((a.name === 'value' || a.name === 'checked') && m) { props.push([a.name, lookup(m[1], scope)]); continue; }
      if (a.name === 'ref' && m) { const fn = lookup(m[1], scope); if (typeof fn === 'function') window.__dcRefs.push([fn, el]); continue; }
      el.setAttribute(a.name, interp(a.value, scope));
    }
    const kids = [];
    node.childNodes.forEach((c) => renderNode(c, scope, kids));
    kids.forEach((k) => el.appendChild(k));
    for (const [k, v] of props) el[k] = k === 'checked' ? !!v : (v == null ? '' : v);
    out.push(el);
  }

  // Patch the live DOM in place so elements persist between renders
  // (keeps CSS animations, transitions, hover and focus intact).
  function bindEvents(real, fresh) {
    const on = fresh.__on || {};
    real.__on = on;
    real.__bound = real.__bound || {};
    for (const ev in on) {
      if (!real.__bound[ev]) { real.__bound[ev] = true; real.addEventListener(ev, (e) => { const f = real.__on && real.__on[ev]; if (f) f(e); }); }
    }
  }
  function sameKind(a, b) {
    return a.nodeType === b.nodeType && a.nodeName === b.nodeName && (a.nodeType !== 1 || a.namespaceURI === b.namespaceURI);
  }
  function adopt(fresh) {
    // first insertion of a freshly built subtree: wire its events
    if (fresh.nodeType === 1) {
      bindEvents(fresh, fresh); fresh.__real = fresh;
      fresh.querySelectorAll('*').forEach((n) => { bindEvents(n, n); n.__real = n; });
    }
    return fresh;
  }
  function morphEl(real, fresh) {
    fresh.__real = real;
    for (const a of Array.from(real.attributes)) if (!fresh.hasAttribute(a.name)) real.removeAttribute(a.name);
    for (const a of Array.from(fresh.attributes)) if (real.getAttribute(a.name) !== a.value) real.setAttribute(a.name, a.value);
    bindEvents(real, fresh);
    if ('value' in fresh && (real.localName === 'input' || real.localName === 'textarea' || real.localName === 'select')) {
      if (real.value !== fresh.value) real.value = fresh.value;
      if (real.checked !== fresh.checked) real.checked = fresh.checked;
    }
    morphChildren(real, Array.from(fresh.childNodes));
  }
  function morphChildren(parent, freshKids) {
    const realKids = Array.from(parent.childNodes);
    freshKids.forEach((f, i) => {
      const r = realKids[i];
      if (!r) { parent.appendChild(adopt(f)); return; }
      if (!sameKind(r, f)) { parent.replaceChild(adopt(f), r); return; }
      if (f.nodeType === 3) { if (r.nodeValue !== f.nodeValue) r.nodeValue = f.nodeValue; return; }
      morphEl(r, f);
    });
    for (let i = realKids.length - 1; i >= freshKids.length; i--) parent.removeChild(realKids[i]);
  }

  document.addEventListener('DOMContentLoaded', () => {
    window.__dcWarnings = [];
    const host = document.querySelector('x-dc');
    const tpl = document.createElement('template');
    tpl.innerHTML = host.innerHTML;
    const helmet = tpl.content.querySelector('helmet');
    const style = document.createElement('style');
    style.textContent = faces.join('\n');
    document.head.appendChild(style);
    if (helmet) Array.from(helmet.children).forEach((c) => { if (c.localName !== 'link') document.head.appendChild(c.cloneNode(true)); });
    const code = document.querySelector('script[data-dc-script]').textContent;
    const Component = new Function(code + '\nreturn Component;')();
    const pd = (()=>{try{const j=JSON.parse(document.querySelector('[data-dc-script]').getAttribute('data-props')||'{}');const o={};for(const k in j){if(k[0]!=='$'&&j[k].default!==undefined)o[k]=j[k].default;}return o;}catch(e){return {};}})();
    const comp = new Component(pd);
    let queued = false;
    window.__dcRender = () => {
      if (queued) return; queued = true;
      Promise.resolve().then(() => {
        queued = false;
        const active = document.activeElement && document.activeElement.id;
        const out = [];
        window.__dcRefs = [];
        const vals = comp.renderVals();
        tpl.content.childNodes.forEach((c) => renderNode(c, vals, out));
        morphChildren(host, out);
        window.__dcRefs.forEach(([fn, el]) => fn(el.__real || el));
        if (window.__dcMounted && comp.componentDidUpdate) comp.componentDidUpdate();
        if (active) { const a = document.getElementById(active); if (a) a.focus(); }
        window.__dcRenders = (window.__dcRenders || 0) + 1;
        document.documentElement.classList.toggle('is-dark', !!host.querySelector('.theme.dark'));
        if (window.__dcRenders === 1) requestAnimationFrame(() => { host.classList.add('dc-on'); document.documentElement.classList.add('dc-ready'); const bt = document.getElementById('boot'); if (bt) setTimeout(() => bt.remove(), 500); });
      });
    };
    host.style.display = 'block';
    window.__dcRender();
    setTimeout(() => { window.__dcMounted = true; if (comp.componentDidMount) comp.componentDidMount(); }, 0);
  });
})();
