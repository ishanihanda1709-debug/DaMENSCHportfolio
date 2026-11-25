(() => {
const $ = (s, r = document) => r.querySelector(s);
const $$ = (s, r = document) => [...r.querySelectorAll(s)];
const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
const store = {
  get(k, d) { try { const v = localStorage.getItem(k); return v ? JSON.parse(v) : d; } catch (e) { return d; } },
  set(k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch (e) {} }
};
const toastEl = $('#toast'); let toastT;
const toast = m => { toastEl.textContent = m; toastEl.classList.add('on'); clearTimeout(toastT); toastT = setTimeout(() => toastEl.classList.remove('on'), 2200); };

/* ---------- splash ---------- */
const splash = $('#splash');
const hideSplash = () => splash.classList.add('gone');
if (reduce || store.get('dm-seen', false)) hideSplash();
else {
  const t = $('#splashText'), full = 'Hi DaMENSCH,'; let i = 0;
  t.textContent = '';
  (function type() { t.textContent = full.slice(0, i); if (i++ < full.length) setTimeout(type, 70); else setTimeout(hideSplash, 900); })();
  splash.addEventListener('click', hideSplash);
  store.set('dm-seen', true);
}

/* ---------- theme ---------- */
const root = document.documentElement, themeBtn = $('#themeBtn');
const isDark = () => root.dataset.theme ? root.dataset.theme === 'dark' : matchMedia('(prefers-color-scheme: dark)').matches;
const syncTheme = () => themeBtn.setAttribute('aria-label', isDark() ? 'Switch to light mode' : 'Switch to dark mode');
themeBtn.addEventListener('click', () => { root.dataset.theme = isDark() ? 'light' : 'dark'; try { localStorage.setItem('dm-theme', root.dataset.theme); } catch (e) {} syncTheme(); });
syncTheme();

/* ---------- products ---------- */
const prods = $$('.prod');
const byId = id => document.getElementById('p-' + id);

/* ---------- hire bag ---------- */
let bag = store.get('dm-bag', []).filter(id => byId(id));
const bagList = $('#bagList'), drawer = $('#bag'), scrim = $('#scrim');
function renderBag() {
  $$('.bag-count').forEach(c => { c.textContent = bag.length; c.classList.toggle('zero', bag.length === 0); });
  prods.forEach(p => {
    const b = $('.add', p), on = bag.includes(p.dataset.id);
    b.setAttribute('aria-pressed', String(on)); $('.add-t', b).textContent = on ? 'In your bag' : 'Add to bag';
  });
  bagList.innerHTML = bag.map(id => { const p = byId(id); return `<li><div><b>${p.dataset.title}</b><small>${p.dataset.col} · ${p.dataset.stat}</small></div><button type="button" data-rm="${id}">Remove</button></li>`; }).join('');
  $('#bagEmpty').hidden = bag.length > 0;
  const lines = bag.map(id => '- ' + byId(id).dataset.title + ' (' + byId(id).dataset.stat + ')').join('\n');
  const body = 'Hi Ishani,\n\nWe looked through your store. We’d like to talk about:\n' + (lines || '- (your pick)') + '\n\n';
  $('#checkout').href = `mailto:${window.DM_EMAIL}?subject=${encodeURIComponent('Founder’s Office, Growth & Marketing: let’s talk')}&body=${encodeURIComponent(body)}`;
  store.set('dm-bag', bag);
  syncQvAdd();
}
function toggleBag(id) {
  const had = bag.includes(id);
  bag = had ? bag.filter(x => x !== id) : [...bag, id];
  renderBag(); toast(had ? 'Removed from your hire bag' : 'Added to your hire bag');
}
prods.forEach(p => $('.add', p).addEventListener('click', () => toggleBag(p.dataset.id)));
bagList.addEventListener('click', e => { const b = e.target.closest('[data-rm]'); if (b) toggleBag(b.dataset.rm); });

/* ---------- overlays ---------- */
let lastFocus = null, openEl = null;
function openLayer(el) {
  lastFocus = document.activeElement; if (openEl) closeLayer(false);
  openEl = el; el.hidden = false; scrim.hidden = false; document.body.style.overflow = 'hidden';
  const f = el.querySelector('button, a, [tabindex]'); f && f.focus();
}
function closeLayer(restore = true) {
  if (!openEl) return;
  $$('video', openEl).forEach(v => v.pause());
  openEl.hidden = true; scrim.hidden = true; document.body.style.overflow = ''; openEl = null;
  if (restore && lastFocus) lastFocus.focus();
}
scrim.addEventListener('click', () => closeLayer());
document.addEventListener('keydown', e => {
  if (e.key === 'Escape') closeLayer();
  if (e.key === 'Tab' && openEl) {
    const f = $$('button:not([disabled]), a[href], video, input', openEl).filter(x => x.offsetParent !== null);
    if (!f.length) return;
    if (e.shiftKey && document.activeElement === f[0]) { e.preventDefault(); f[f.length - 1].focus(); }
    else if (!e.shiftKey && document.activeElement === f[f.length - 1]) { e.preventDefault(); f[0].focus(); }
  }
});
$$('.bag-open').forEach(b => b.addEventListener('click', () => openLayer(drawer)));
$('#bagClose').addEventListener('click', () => closeLayer());

/* ---------- quick view ---------- */
const qv = $('#qv'); let qvId = null;
function syncQvAdd() {
  if (!qvId) return; const on = bag.includes(qvId), b = $('#qvAdd');
  b.setAttribute('aria-pressed', String(on)); $('span', b).textContent = on ? 'In your hire bag ✓' : 'Add to hire bag';
}
function openQv(id) {
  const p = byId(id); if (!p) return; qvId = id;
  $('#qvImg').innerHTML = $('.prod-img', p).innerHTML; $('.qv-hint', $('#qvImg'))?.remove();
  $('#qvCol').textContent = p.dataset.col + ' · ' + $('.prod-fab', p).textContent;
  $('#qvTitle').textContent = p.dataset.title;
  $('#qvPrice').innerHTML = $('.price', p).innerHTML;
  $('#qvTag').textContent = $('.prod-tag', p).firstChild.textContent.trim();
  $('#qvBody').innerHTML = $('.pd', p).innerHTML;
  $$('#qvBody a[href^="#"]').forEach(a => a.addEventListener('click', () => closeLayer(false)));
  syncQvAdd(); openLayer(qv);
}
document.addEventListener('click', e => { const t = e.target.closest('[data-qv]'); if (t) openQv(t.dataset.qv); });
$('#qvClose').addEventListener('click', () => closeLayer());
$('#qvAdd').addEventListener('click', () => qvId && toggleBag(qvId));

/* ---------- fit guide filter ---------- */
const dmGrid = $('#damensch .grid'), fitRows = $$('.fit-row'), fitClear = $('#fitClear');
const dmProds = $$('.prod', dmGrid), dmCount = $('[data-count-for="damensch"]');
function setFit(k) {
  fitRows.forEach(r => r.setAttribute('aria-pressed', String(r.dataset.fab === k)));
  let n = 0;
  dmProds.forEach(p => { const show = !k || p.dataset.fab.split(' ').includes(k); p.hidden = !show; if (show) n++; });
  dmCount.textContent = k ? `${n} of ${dmProds.length}` : dmProds.length;
  fitClear.hidden = !k;
}
fitRows.forEach(r => r.addEventListener('click', () => {
  const k = r.getAttribute('aria-pressed') === 'true' ? null : r.dataset.fab; setFit(k);
  if (k) dmGrid.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth', block: 'start' });
}));
fitClear.addEventListener('click', () => setFit(null));

/* ---------- search ---------- */
const q = $('#q'), results = $('#results');
const phrases = ['“ROAS”', '“D2C”', '“creators”', '“new product”', '“PhonePe”', '“GA4”', '“founder”'];
let pi = 0;
if (!reduce) setInterval(() => { if (document.activeElement !== q) { pi = (pi + 1) % phrases.length; q.placeholder = `Search ${phrases[pi]}…`; } }, 2600);
let sel = -1;
function runSearch() {
  const v = q.value.trim().toLowerCase(); sel = -1;
  if (!v) { results.hidden = true; return; }
  const hits = prods.filter(p => p.dataset.search.includes(v)).slice(0, 8);
  results.innerHTML = hits.length ? hits.map(p => `<button type="button" role="option" data-go="${p.dataset.id}">${p.dataset.title}<small>${p.dataset.col} · ${p.dataset.stat}</small></button>`).join('')
    : `<p>No match for “${v.replace(/[<>&]/g, '')}”. Try “growth”, “brand” or “creators”.</p>`;
  results.hidden = false;
}
q.addEventListener('input', runSearch);
q.addEventListener('focus', runSearch);
q.addEventListener('keydown', e => {
  const opts = $$('button', results);
  if (e.key === 'ArrowDown' || e.key === 'ArrowUp') { e.preventDefault(); if (!opts.length) return; sel = (sel + (e.key === 'ArrowDown' ? 1 : -1) + opts.length) % opts.length; opts.forEach((o, i) => o.classList.toggle('on', i === sel)); }
  if (e.key === 'Enter' && opts.length) { e.preventDefault(); (opts[sel] || opts[0]).click(); }
  if (e.key === 'Escape') { results.hidden = true; q.blur(); }
});
document.addEventListener('click', e => { if (!e.target.closest('.search')) results.hidden = true; });
results.addEventListener('click', e => {
  const b = e.target.closest('[data-go]'); if (!b) return;
  const p = byId(b.dataset.go); results.hidden = true; q.value = '';
  if (p.hidden) setFit(null);
  p.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth', block: 'center' });
  p.classList.remove('flash'); void p.offsetWidth; p.classList.add('flash');
  setTimeout(() => openQv(b.dataset.go), reduce ? 0 : 650);
});

/* ---------- order tracking: Ishani walks the route ---------- */
const STOPS = [
  { k: 'PACKED', t: 'D.A.V', name: 'D.A.V Public School', id: 'school' },
  { k: 'QUALITY CHECK', t: 'Christ', name: 'Christ University', id: 'christ' },
  { k: 'SHIPPED', t: 'PhonePe', name: 'PhonePe', id: 'phonepe' },
  { k: 'IN TRANSIT', t: 'Masters’ Union', name: 'Masters’ Union', id: 'masters' },
  { k: 'OUT FOR DELIVERY', t: 'DaMENSCH', name: 'DaMENSCH', id: 'damensch' }
];
const STATUS = ['Packed at school', 'Quality-checked at Christ', 'Shipped from PhonePe', 'In transit', 'Out for delivery'];
const FR = [0.0, 0.25, 0.5, 0.74, 1];
const road = $('#road'), done = $('#roadDone'), walker = $('#walker'), flip = $('#walkerFlip'), svg = $('#trackSvg');
const L = road.getTotalLength();
done.style.strokeDasharray = `${L} ${L}`;
const NS = 'http://www.w3.org/2000/svg';
const pins = FR.map((f, i) => {
  const p = road.getPointAtLength(f * L);
  const g = document.createElementNS(NS, 'g'); g.setAttribute('class', 'pin' + (i === 4 ? ' final' : ''));
  const up = i % 2 === 0, ty = up ? p.y - 76 : p.y + 22;
  const w = Math.max(96, Math.max(STOPS[i].t.length * 9.5, STOPS[i].k.length * 7) + 26);
  const tx = Math.min(Math.max(p.x - w / 2, 6), 1000 - w - 6);
  g.innerHTML = `<rect class="pin-tag" x="${tx}" y="${ty}" width="${w}" height="44" rx="8"/>
    <text class="pin-k" x="${tx + w / 2}" y="${ty + 17}" text-anchor="middle">${STOPS[i].k}</text>
    <text class="pin-label" x="${tx + w / 2}" y="${ty + 35}" text-anchor="middle">${STOPS[i].t}</text>
    <circle class="pin-ring" cx="${p.x}" cy="${p.y}" r="10"/><circle class="pin-dot" cx="${p.x}" cy="${p.y}" r="9"/>`;
  g.style.cursor = 'pointer';
  g.addEventListener('click', () => document.getElementById(STOPS[i].id).scrollIntoView({ behavior: reduce ? 'auto' : 'smooth' }));
  $('#pins').appendChild(g); return g;
});
const strip = $('#strip'), mw = $('#miniWalker'), mf = $('#miniFlip'), sd = $('#stripDone');
const stopIdx = f => { for (let k = 0; k < 4; k++) if (f <= FR[k + 1]) return k + (f - FR[k]) / (FR[k + 1] - FR[k]); return 4; };
let pos = 0, target = FR[3], current = -1, paused = reduce, raf = 0, lastT = 0;
function paint() {
  const p = road.getPointAtLength(pos * L);
  walker.setAttribute('transform', `translate(${p.x} ${p.y - 4})`);
  done.style.strokeDashoffset = String(L - pos * L);
  const x = 24 + stopIdx(pos) * 88;
  mw.setAttribute('transform', `translate(${x} 0)`); sd.setAttribute('d', `M24 50H${x}`);
  const map = svg.parentElement;
  if (map.scrollWidth > map.clientWidth + 2) map.scrollLeft = Math.max(0, p.x * (svg.clientWidth / 1000) - map.clientWidth / 2);
}
const stopWalk = () => { svg.classList.remove('walking'); strip.classList.remove('walking'); raf = 0; lastT = 0; };
function step(t) {
  const dt = lastT ? Math.min(50, t - lastT) : 16; lastT = t;
  const d = target - pos, sp = 0.00042 * dt;
  if (Math.abs(d) <= sp || paused) { pos = target; paint(); stopWalk(); return; }
  pos += Math.sign(d) * sp;
  const fl = d < 0 ? 'scale(-1 1)' : ''; flip.setAttribute('transform', fl); mf.setAttribute('transform', fl);
  paint(); raf = requestAnimationFrame(step);
}
function goTo(i) {
  if (i === current) return; current = i; target = FR[i];
  pins.forEach((g, j) => { g.classList.toggle('done', j < i); g.classList.toggle('here', j === i); });
  $$('.ms').forEach((g, j) => { g.classList.toggle('done', j < i); g.classList.toggle('here', j === i); });
  $$('#steps a').forEach((a, j) => { a.classList.toggle('done', j < i); a.classList.toggle('here', j === i); });
  const end = i === 4;
  $('#trackStatus').textContent = STATUS[i];
  $('#trackSub').innerHTML = end ? 'Arriving at <b>DaMENSCH</b> · every KRA matched to proof' : `Currently at <b>${STOPS[i].name}</b> · Next stop <b>${STOPS[i + 1].name}</b>`;
  $('#stripHint').textContent = end ? 'Arriving at DaMENSCH' : `At ${STOPS[i].t} · next: ${STOPS[i + 1].t}`;
  if (paused) { pos = target; paint(); return; }
  svg.classList.add('walking'); strip.classList.add('walking');
  if (!raf) raf = requestAnimationFrame(step);
}
paint(); goTo(3);
const motionBtn = $('#motionToggle');
function setMotion(p) {
  paused = p; motionBtn.setAttribute('aria-pressed', String(p)); motionBtn.textContent = p ? 'Resume motion ▷' : 'Pause motion Ⅱ';
  $('.mq-track').style.animationPlayState = p ? 'paused' : '';
  if (p) { pos = target; paint(); stopWalk(); }
}
motionBtn.addEventListener('click', () => setMotion(!paused));
if (reduce) setMotion(true);

/* scroll → current collection, strip visibility, bottom nav */
const colls = STOPS.map(s => document.getElementById(s.id));
const journey = $('#journey');
const nav = k => $$('.bottom-nav [data-nav]').forEach(a => a.classList.toggle('on', a.dataset.nav === k));
function onScroll() {
  const mid = innerHeight * 0.45;
  let idx = -1;
  colls.forEach((c, i) => { if (c.getBoundingClientRect().top < mid) idx = i; });
  if (idx >= 0) goTo(idx);
  const jr = journey.getBoundingClientRect();
  const inColls = colls[0].getBoundingClientRect().top < innerHeight && $('#drop').getBoundingClientRect().top > innerHeight * 0.5;
  strip.classList.toggle('off', !(inColls && (jr.bottom < 0 || jr.top > innerHeight)));
  const y = scrollY;
  const at = id => document.getElementById(id).getBoundingClientRect().top < mid;
  nav(at('drop') ? 'drop' : at('shop') && !at('journey') ? 'shop' : at('journey') && !at('best') ? 'journey' : at('best') ? 'shop' : y < 200 ? 'home' : 'home');
}
let ticking = false;
addEventListener('scroll', () => { if (!ticking) { ticking = true; requestAnimationFrame(() => { onScroll(); ticking = false; }); } }, { passive: true });
onScroll();

/* ---------- copy email ---------- */
$('#copyEmail').addEventListener('click', async () => {
  try { await navigator.clipboard.writeText(window.DM_EMAIL); toast('Email copied'); }
  catch (e) { toast(window.DM_EMAIL); }
});

/* ---------- game: Build the Drop ---------- */
const ROUNDS = [
  { q: 'Pick the hero message for a summer launch.', ctx: 'One line goes on every ad, creator brief and product page.',
    o: ['“The softest fabric we’ve ever made.”', '“Still comfortable at hour sixteen of a humid day.”', '“30% off, this week only.”'], mine: 1,
    fb: ['A claim every brand in the drawer can make, so it’s hard to remember and harder to prove.',
         'A moment people have lived, and a promise creators can show on camera. Proof beats adjectives.',
         'It moves units this week, but it teaches people to wait for the next sale and says nothing about the product.'] },
  { q: 'You have a creator budget. How do you spend it?', ctx: 'Same budget either way. Think reach, trust and what you learn.',
    o: ['Two big stars for maximum reach.', '40 micro creators, nothing else.', 'One macro for reach, 25 micro for trust, and product seeded to real customers.'], mine: 2,
    fb: ['Huge reach, but two data points. If one flops, you’ve learned little and spent half the budget.',
         'Great trust and lots of tests, but slow to build awareness for a launch moment.',
         'Reach, trust and reviews at once, and enough creators to see which tier brings the cheapest repeat customers.'] },
  { q: 'Week two: click-through is great, but size returns are climbing.', ctx: 'The founder wants to know what you’ll do on Monday.',
    o: ['Raise spend while the click-through is hot.', 'Hold spend, add a fit finder and a clearer size chart, then re-test.', 'Swap the creative for something new.'], mine: 1,
    fb: ['More clicks into a leaky size experience means more returns and a higher real CAC.',
         'Fix the leak first. A good ad with a bad fit experience costs you the second order, which is where innerwear makes its money.',
         'The creative is working. The problem is after the click, so new creative won’t fix it.'] }
];
const gc = $('#gameContent'), gp = $('#gameProgress');
let r = 0, score = 0, picks = [];
function renderRound() {
  if (r >= ROUNDS.length) {
    gp.textContent = 'DONE';
    gc.innerHTML = `<div class="g-end"><h3>Drop built.</h3><p>You matched my call <b>${score} of 3</b> times. ${score === 3 ? 'We’d plan well together.' : score === 2 ? 'Close. Let’s argue about the third one in the interview.' : 'Good: we’d have a useful debate in week one.'}</p>
      <p class="g-ctx">My calls: proof over adjectives, a mixed creator roster, and fixing the leak before scaling.</p>
      <button class="btn g-next" type="button" id="gAgain">Play again</button> <a class="btn ghost g-next" href="#drop">See The Ishani Drop</a></div>`;
    $('#gAgain').addEventListener('click', reset); return;
  }
  const R = ROUNDS[r]; gp.textContent = `0${r + 1} / 03`;
  gc.innerHTML = `<p class="g-q">${R.q}</p><p class="g-ctx">${R.ctx}</p><div class="g-opts">${R.o.map((o, i) => `<button class="g-opt" type="button" data-i="${i}"><i>${'ABC'[i]}</i><span>${o}</span></button>`).join('')}</div>`;
  $$('.g-opt', gc).forEach(b => b.addEventListener('click', () => choose(+b.dataset.i)));
}
function choose(i) {
  const R = ROUNDS[r]; picks.push(i); if (i === R.mine) score++;
  $$('.g-opt', gc).forEach((b, j) => { b.disabled = true; b.classList.toggle('mine', j === R.mine); b.classList.toggle('picked', j === i); });
  const fb = document.createElement('div'); fb.className = 'g-fb';
  fb.innerHTML = `<b>${i === R.mine ? 'Same call as mine.' : 'I’d go with ' + 'ABC'[R.mine] + '.'}</b>${R.fb[i]}${i !== R.mine ? '<br><br><b>Why ' + 'ABC'[R.mine] + ':</b> ' + R.fb[R.mine] : ''}`;
  gc.appendChild(fb);
  const nx = document.createElement('button'); nx.className = 'btn g-next'; nx.type = 'button'; nx.textContent = r < 2 ? 'Next call →' : 'See results';
  nx.addEventListener('click', () => { r++; renderRound(); gc.querySelector('button')?.focus(); });
  gc.appendChild(nx); nx.focus();
}
function reset() { r = 0; score = 0; picks = []; renderRound(); }
$('#gameReset').addEventListener('click', reset);
renderRound();

renderBag();
})();
