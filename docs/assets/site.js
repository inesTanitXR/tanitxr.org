
const SHEET = "https://script.google.com/macros/s/AKfycbwS1EdGOzYjIOJ7DlM0JhKBfZ3IWpD_4cWp8e5x56ckd7WR3tK03bqgiw6nOfmgIVNI0w/exec";
// One place to record what people do, so the numbers exist when a grant asks for them.
// Works with whatever analytics is configured in ref/analytics.json, and does nothing if none is.
window.tx = function(name, props){
  try{
    // the thing that matters becomes part of the path (object slug, share network, badge, ask, gallery,
    // tour step, device), so counts exist per item as well as in total; GoatCounter drops everything else
    const KEYS = ['net', 'object', 'badge', 'ask', 'artist', 'room', 'step', 'person', 'from', 'device', 'on'];
    let dim = '';
    if (props) for (const k of KEYS) { if (props[k] !== undefined && props[k] !== null && props[k] !== '') { dim = String(props[k]); break; } }
    dim = dim.toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '').replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
    const path = name + (dim ? '/' + dim : '');
    if (window.counter && typeof counter.count === 'function') counter.count({path: path});
    if (window.goatcounter && goatcounter.count) goatcounter.count({path: path, event: true});
    if (typeof gtag === 'function') gtag('event', name, props || {});
  }catch(e){ /* never let counting break the page */ }
};
document.addEventListener('click', e => {
  const a = e.target.closest('a[href*="donors.tuesday.app"], a[href*="donate"]');
  if (a) window.tx('donate_click', { from: location.pathname.split('/').filter(Boolean)[0] || 'home' });
});
const PAGE_OPENED = Date.now();

// A badge for reaching the end of something worth finishing: an article, or an object's page.
// It marks finishing, never arriving, which is why there is none on the home page or a form.
// Earned badges live in this browser only, so treat them as a small pleasure, not a record.
(function () {
  const end = document.getElementById('read-end');
  const toast = document.getElementById('read-toast');
  if (!end || !toast) return;
  const KEY = 'tanitxr.read';
  const id = end.dataset.badge || 'read';
  const here = location.pathname;
  const read = () => { try { return JSON.parse(localStorage.getItem(KEY) || '{}'); } catch (e) { return {}; } };
  const write = (v) => { try { localStorage.setItem(KEY, JSON.stringify(v)); } catch (e) { /* private mode */ } };
  const MILESTONE = id === 'read-story' ? 3 : 10;

  let done = false;
  function earn() {
    if (done) return;
    if (document.hidden) {         // a page left open in another tab has not been read yet
      document.addEventListener('visibilitychange', () => setTimeout(earn, 1500), { once: true });
      return;
    }
    done = true;
    const state = read();
    const seen = Array.isArray(state[id]) ? state[id] : [];
    const first = seen.length === 0;
    if (seen.indexOf(here) === -1) seen.push(here);
    state[id] = seen;
    const hit = seen.length === MILESTONE;
    write(state);
    if (!first && !hit) return;                       // only the first, and the milestone
    if (hit) {
      toast.querySelector('.rt-first').hidden = true;
      toast.querySelector('.rt-more').hidden = false;
    }
    toast.hidden = false;
    void toast.offsetWidth;        // not requestAnimationFrame: it never runs in a background
    toast.classList.add('on');     // tab, which would award the badge and show nothing
    if (window.tx) tx('badge_earned', { badge: hit ? id + '-' + MILESTONE : id });
    setTimeout(hide, 11000);
  }
  function hide() {
    toast.classList.remove('on');
    setTimeout(() => { toast.hidden = true; }, 400);
  }
  const closer = document.getElementById('rt-close');
  if (closer) closer.addEventListener('click', hide);

  // Reaching the end counts only if enough time passed to have actually read it. A scroll check
  // rather than an observer, because the end marker sits above the footer and a jump to the
  // bottom of the page can pass straight over it without the observer ever firing.
  function look() {
    if (done) return;
    if (Date.now() - PAGE_OPENED < 20000) return;     // jumped to the bottom, or just landed
    const r = end.getBoundingClientRect();
    if (r.top <= window.innerHeight) {
      window.removeEventListener('scroll', look);
      earn();
    }
  }
  window.addEventListener('scroll', look, { passive: true });
  setTimeout(look, 20500);                            // already at the end and simply reading
})();
// Sending us a model: the file itself, a link to it, or a Sketchfab address.
// A scan is anything from under a megabyte to well over a hundred, and a web app can only
// accept about fifty in one request, so the file goes up in pieces against a resumable Drive
// session. The browser tries to send the pieces straight to Drive, which is fast; where the
// browser is not allowed to talk to Drive directly it sends them through our script instead,
// which is slower but always works. Either way nothing is held whole in memory.
(function () {
  const form = document.getElementById('send-model');
  if (!form) return;
  const CHUNK = 5 * 1024 * 1024;                  // a multiple of 256 KB, as Drive requires
  const MAX = 2 * 1024 * 1024 * 1024;
  const drop = document.getElementById('drop');
  const input = document.getElementById('dropin');
  const card = document.getElementById('drop-file');
  const bar = document.getElementById('df-bar');
  const fill = document.getElementById('df-fill');
  const say = document.getElementById('df-say');
  const out = document.getElementById('sm-say');
  const go = document.getElementById('sm-go');
  let chosen = null, sending = false;

  function which() {
    const on = form.querySelector('.way[aria-selected="true"]');
    return on ? on.dataset.way : 'file';
  }
  form.querySelectorAll('.way').forEach((b) => b.addEventListener('click', () => {
    form.querySelectorAll('.way').forEach((o) => o.setAttribute('aria-selected', String(o === b)));
    form.querySelectorAll('.wayp').forEach((p) => p.classList.toggle('on', p.dataset.way === b.dataset.way));
    tell(out, '', '');
  }));

  function tell(el, text, kind) {
    el.textContent = text;
    el.className = 'df-say' + (kind ? ' ' + kind : '');
  }
  function size(n) {
    return n > 1048576 ? (n / 1048576).toFixed(1) + ' MB' : Math.max(1, Math.round(n / 1024)) + ' KB';
  }

  function take(file) {
    if (!file) return;
    if (file.size > MAX) { tell(out, 'That file is over 2 GB. Send us a link to it instead.', 'bad'); return; }
    chosen = file;
    document.getElementById('df-name').textContent = file.name;
    document.getElementById('df-size').textContent = size(file.size);
    card.hidden = false;
    drop.hidden = true;
    tell(say, '', '');
  }
  drop.addEventListener('click', () => input.click());
  drop.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); input.click(); }
  });
  input.addEventListener('change', () => take(input.files[0]));
  ['dragenter', 'dragover'].forEach((n) => drop.addEventListener(n, (e) => {
    e.preventDefault(); drop.classList.add('over');
  }));
  ['dragleave', 'drop'].forEach((n) => drop.addEventListener(n, (e) => {
    e.preventDefault(); drop.classList.remove('over');
  }));
  drop.addEventListener('drop', (e) => {
    const f = e.dataTransfer && e.dataTransfer.files && e.dataTransfer.files[0];
    take(f);
  });
  document.getElementById('df-drop').addEventListener('click', () => {
    if (sending) return;
    chosen = null; input.value = ''; card.hidden = true; drop.hidden = false;
    bar.hidden = true; fill.style.width = '0';
  });

  const b64 = (buf) => {
    let s = '';
    const b = new Uint8Array(buf);
    for (let i = 0; i < b.length; i += 0x8000) s += String.fromCharCode.apply(null, b.subarray(i, i + 0x8000));
    return btoa(s);
  };
  async function ask(fields) {
    const body = new URLSearchParams(fields);
    const r = await fetch(SHEET, { method: 'POST', body: body });
    return r.json();
  }

  async function sendFile(file, meta) {
    const start = await ask(Object.assign({
      action: 'upload-start', name: file.name, size: file.size,
      mime: file.type || 'application/octet-stream', _js: '1', _t: String(Date.now() - PAGE_OPENED),
    }, meta));
    if (start.result !== 'ready') throw new Error(start.result || 'no session');

    let sent = 0, direct = start.direct;
    while (sent < file.size) {
      const end = Math.min(sent + CHUNK, file.size);
      const buf = await file.slice(sent, end).arrayBuffer();
      let done = null;

      if (direct) {
        // the quick way: the piece goes to Drive itself
        try {
          const r = await fetch(direct, {
            method: 'PUT',
            headers: { 'Content-Range': 'bytes ' + sent + '-' + (end - 1) + '/' + file.size },
            body: buf,
          });
          if (r.status === 308) { sent = end; tick(sent, file.size); continue; }
          if (r.status === 200 || r.status === 201) { done = await r.json(); }
          else { throw new Error('drive said ' + r.status); }
        } catch (e) {
          direct = null;                      // not allowed to talk to Drive: go the long way
          tell(say, 'Sending it through our server instead, this takes a little longer.', '');
          continue;
        }
      } else {
        const r = await ask({ action: 'upload-chunk', key: start.key, offset: sent, data: b64(buf) });
        if (r.result === 'more') { sent = r.received; tick(sent, file.size); continue; }
        if (r.result === 'saved') return r.url;
        throw new Error(r.detail || r.result || 'upload failed');
      }

      if (done) {
        const fin = await ask({ action: 'upload-done', key: start.key, fileId: done.id });
        if (fin.result !== 'saved') throw new Error(fin.result);
        tick(file.size, file.size);
        return fin.url;
      }
    }
    throw new Error('upload ended early');
  }
  function tick(sent, total) {
    bar.hidden = false;
    fill.style.width = Math.round((sent / total) * 100) + '%';
    tell(say, 'Sending, ' + Math.round((sent / total) * 100) + '% of ' + size(total) + '.', '');
  }

  form.addEventListener('submit', async (e) => {
    const way = which();
    if (way === 'link' || way === 'sketchfab') {
      const f = form.querySelector(way === 'link' ? '#sm-link' : '#sm-sf');
      if (!f.value.trim()) { e.preventDefault(); tell(out, 'Put the link in first.', 'bad'); f.focus(); }
      return;                                   // the ordinary form post handles these
    }
    e.preventDefault();
    if (sending) return;
    if (!chosen) { tell(out, 'Choose a file, or switch to pasting a link.', 'bad'); return; }
    if (!form.reportValidity()) return;
    sending = true;
    go.disabled = true;
    tell(out, '', '');
    try {
      const url = await sendFile(chosen, {
        who: form.name.value, email: form.email.value,
        about: [form.title.value, form.place.value, form.about.value, form.captured.value]
          .filter(Boolean).join(' | '),
        place: form.place.value,
      });
      tell(say, 'Sent. Thank you.', 'good');
      if (window.tx) tx('model_uploaded', { from: 'submit' });
      const nx = form.querySelector('input[name=_next]');
      location.href = nx && nx.value ? nx.value : new URL('../thank-you/?from=model', location.href).href;
    } catch (err) {
      sending = false;
      go.disabled = false;
      tell(out, 'That did not go through (' + err.message + '). Paste a link to the file instead, '
        + 'or email it to info@tanitxr.org.', 'bad');
    }
  });
})();
// The scanning guide is one long document split across tabs. The panels are all in the page
// already: this only hides the ones you are not reading, and only once it is running, so a
// browser with no JavaScript, a printout and anything crawling the site still get the lot.
(function () {
  const guide = document.getElementById('guide');
  if (!guide) return;
  const tabs = [].slice.call(guide.querySelectorAll('.gtab'));
  const panels = [].slice.call(guide.querySelectorAll('.gpanel'));
  if (!tabs.length || tabs.length !== panels.length) return;
  guide.setAttribute('data-tabs', 'on');

  function open(key, push) {
    let found = false;
    tabs.forEach((t, i) => {
      const on = t.id === 't-' + key;
      if (on) found = true;
      t.setAttribute('aria-selected', on ? 'true' : 'false');
      t.tabIndex = on ? 0 : -1;
      panels[i].classList.toggle('on', on);
    });
    if (!found) { open(tabs[0].id.slice(2), false); return; }
    if (push && history.replaceState) history.replaceState(null, '', '#' + key);
    if (window.tx) tx('guide_tab', { step: key });
  }

  tabs.forEach((t) => t.addEventListener('click', () => {
    open(t.id.slice(2), true);
    guide.scrollIntoView({ block: 'start', behavior: 'smooth' });
  }));

  // arrow keys move along the row, the way a set of tabs is expected to behave
  guide.querySelector('.gtabs').addEventListener('keydown', (e) => {
    const i = tabs.indexOf(document.activeElement);
    if (i < 0) return;
    let j = -1;
    if (e.key === 'ArrowRight') j = (i + 1) % tabs.length;
    if (e.key === 'ArrowLeft') j = (i - 1 + tabs.length) % tabs.length;
    if (e.key === 'Home') j = 0;
    if (e.key === 'End') j = tabs.length - 1;
    if (j < 0) return;
    e.preventDefault();
    tabs[j].focus();
    open(tabs[j].id.slice(2), true);
  });

  // a link into a panel, from the page itself or from somebody else's bookmark
  document.addEventListener('click', (e) => {
    const a = e.target.closest('a[data-go]');
    if (!a) return;
    e.preventDefault();
    open(a.dataset.go, true);
    guide.scrollIntoView({ block: 'start', behavior: 'smooth' });
  });
  addEventListener('hashchange', () => open(location.hash.slice(1), false));
  open((location.hash || '#').slice(1) || tabs[0].id.slice(2), false);
})();
// Nura, wandering the rest of the site. The whole design here is restraint: she says one
// thing per page at most, never in the first seconds, never while the reading badge is on
// screen, and she stops for the visit the second time somebody closes her. The donation ask
// waits until they have been through a few pages, and then keeps away for a month.
(function () {
  const box = document.getElementById('nura');
  if (!box) return;
  let lines = {};
  try { lines = JSON.parse(box.dataset.lines || '{}'); } catch (e) { return; }
  if (!lines.hello) return;

  const SKEY = 'tanitxr.nura', LKEY = 'tanitxr.nura.ask';
  const MONTH = 30 * 24 * 60 * 60 * 1000;
  const sess = () => { try { return JSON.parse(sessionStorage.getItem(SKEY) || '{}'); } catch (e) { return {}; } };
  const keep = (v) => { try { sessionStorage.setItem(SKEY, JSON.stringify(v)); } catch (e) { /* private mode */ } };
  const asked = () => { try { return Number(localStorage.getItem(LKEY) || 0); } catch (e) { return Date.now(); } };
  const noteAsk = () => { try { localStorage.setItem(LKEY, String(Date.now())); } catch (e) { /* private mode */ } };

  const st = sess();
  st.pages = (st.pages || 0) + 1;
  keep(st);
  if (st.hushed) return;                        // closed twice already: not this visit

  // what she has to say here, in order of how much it has been earned. Thanks come before
  // the ask, and "a few of these" has to be true when she says it
  let pick = 'hello';
  if (lines.ask && st.pages >= 5 && st.praised && !st.asked && Date.now() - asked() > MONTH) pick = 'ask';
  else if (lines.praise && st.pages >= 3 && !st.praised) pick = 'praise';

  // each page has a few things she could say. Pick one she has not already used this visit,
  // so a second archive page does not get the same sentence back.
  const said = Array.isArray(st.said) ? st.said : [];
  const choices = lines[pick] || [];
  if (!choices.length) return;
  const fresh = choices.filter((l) => said.indexOf(l.t) === -1);
  const pool = fresh.length ? fresh : choices;
  const line = pool[Math.floor(Math.random() * pool.length)];

  const words = document.getElementById('nura-words');
  const say = document.getElementById('nura-say');
  const tab = document.getElementById('nura-tab');
  const go = document.getElementById('nura-do');
  words.textContent = line.t;
  if (line.cta && line.cta[0] && line.cta[1]) {
    go.textContent = line.cta[0];
    go.href = line.cta[1];
    if (/^https?:/.test(line.cta[1])) { go.target = '_blank'; go.rel = 'noopener'; }
    go.hidden = false;
  }

  let open = false, spoken = false;
  function speak() {
    if (spoken) return;
    // somebody with the page open in a background tab is not reading it, and she has only
    // one thing to say per page: she waits until they are actually looking
    if (document.hidden) {
      document.addEventListener('visibilitychange', () => setTimeout(speak, 3000), { once: true });
      return;
    }
    // the reading badge owns the bottom of the screen while it is up, and on a phone they
    // would sit on top of each other
    const toast = document.getElementById('read-toast');
    if (toast && !toast.hidden) { setTimeout(speak, 6000); return; }
    spoken = true;
    box.hidden = false;
    say.hidden = false;
    show();
    open = true;
    const s2 = sess();
    if (pick === 'ask') { s2.asked = 1; noteAsk(); }
    if (pick === 'praise') s2.praised = 1;
    s2.said = (Array.isArray(s2.said) ? s2.said : []).concat([line.t]).slice(-12);
    keep(s2);
    if (window.tx) tx('nura_said', { ask: pick });
    setTimeout(() => { if (open) shut(false); }, pick === 'ask' ? 20000 : 14000);
  }
  function shut(byHand) {
    open = false;
    box.classList.remove('say');
    setTimeout(() => { say.hidden = true; }, 400);
    if (byHand) {
      const s2 = sess();
      s2.shut = (s2.shut || 0) + 1;
      if (s2.shut >= 2) { s2.hushed = 1; box.hidden = true; }
      keep(s2);
      if (window.tx) tx('nura_closed', { ask: pick });
    }
  }
  function show() {
    void box.offsetWidth;            // let the browser paint the hidden state, so it animates
    box.classList.add('in');
    box.classList.add('say');
    wake();
  }

  // ---- Nura in three dimensions, once somebody has stayed long enough to meet her.
  // The picture in the button is only a poster. When she has actually spoken, and the visitor
  // is on a connection and a device that can take it, the real model loads and takes over:
  // the same figure, the same float, breathing rather than printed. Nothing is downloaded for
  // somebody who leaves in the first half minute, and if any of it fails the poster stays.
  const face = document.getElementById('nura-face');
  const canvas = document.getElementById('nura-live');
  const MODEL = '/assets/models/nura.glb';
  let woke = false, frame = null, mixer = null, clips = null, glance = 0, lastT = 0;

  function tiny() {
    const c = navigator.connection || {};
    if (c.saveData) return true;                                  // they asked for less data
    if (/(^|-)2g$/.test(c.effectiveType || '')) return true;      // it would never arrive
    if ((navigator.deviceMemory || 4) < 1) return true;
    return matchMedia('(prefers-reduced-motion: reduce)').matches;
  }

  async function wake() {
    if (woke || !canvas || tiny()) return;
    woke = true;
    try {
      const THREE = await import('three');
      const { GLTFLoader } = await import('three/addons/loaders/GLTFLoader.js');
      const { MeshoptDecoder } = await import('three/addons/libs/meshopt_decoder.module.js');
      const box0 = face.getBoundingClientRect();
      const wide = Math.max(40, box0.width), tall = Math.max(40, box0.height);
      const renderer = new THREE.WebGLRenderer({ canvas: canvas, alpha: true, antialias: true,
                                                 powerPreference: 'low-power' });
      renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
      renderer.setSize(wide, tall, false);
      renderer.outputColorSpace = THREE.SRGBColorSpace;
      renderer.toneMapping = THREE.ACESFilmicToneMapping;
      renderer.toneMappingExposure = 1.1;
      const scene = new THREE.Scene();
      scene.add(new THREE.AmbientLight(0xf3ece0, 1.15));
      const key = new THREE.DirectionalLight(0xfff3e0, 1.9); key.position.set(-4, 5, 6);
      const fill = new THREE.DirectionalLight(0xe8f0f6, .8); fill.position.set(5, 1, -3);
      const under = new THREE.DirectionalLight(0xfff6ea, .5); under.position.set(0, -4, 4);
      scene.add(key); scene.add(fill); scene.add(under);
      // all of her, standing, the same crop as the poster: crescent at the top, feet at the
      // bottom, and room at the sides for her arms as she turns
      const TOP = 1.03, BOT = -0.03, DIST = 5.5, MID = (TOP + BOT) / 2;
      const cam = new THREE.PerspectiveCamera(30, wide / tall, .01, 100);
      cam.position.set(0, MID, DIST);
      cam.lookAt(0, MID, 0);
      cam.fov = 2 * Math.atan(((TOP - BOT) / 2) / DIST) * 180 / Math.PI;
      cam.updateProjectionMatrix();

      const gltf = await new Promise((ok, fail) => new GLTFLoader()
        .setMeshoptDecoder(MeshoptDecoder).load(MODEL, ok, undefined, fail));
      const o = gltf.scene;
      o.updateMatrixWorld(true);
      const bb = new THREE.Box3().setFromObject(o);
      const sz = bb.getSize(new THREE.Vector3());
      const mid = bb.getCenter(new THREE.Vector3());
      o.position.set(-mid.x, -bb.min.y, -mid.z);
      const her = new THREE.Group();
      her.add(o);
      her.scale.setScalar(1 / (sz.y || 1));           // she is exactly one unit tall
      her.rotation.y = Math.PI;                        // facing the visitor
      scene.add(her);
      if (gltf.animations && gltf.animations.length) {
        mixer = new THREE.AnimationMixer(o);
        clips = {};
        gltf.animations.forEach(a => { clips[a.name.toLowerCase()] = a; });
        const float = gltf.animations.find(a => /float|idle/i.test(a.name)) || gltf.animations[0];
        mixer.clipAction(float).play();
      }

      // she looks towards the pointer, the way she does in the Collection
      let want = 0;
      addEventListener('pointermove', (e) => {
        want = Math.max(-1, Math.min(1, (e.clientX / innerWidth - .5) * 2)) * 0.34;
      }, { passive: true });

      // She breathes while somebody is with her and holds still when they are not: a WebGL
      // loop running on every page of the site for as long as a tab stays open would be a
      // real cost on a phone, and a resting render looks exactly like the picture it replaced.
      const clock = new THREE.Clock();
      let until = 0;
      function tick() {
        if (Date.now() > until) { frame = null; return; }
        frame = requestAnimationFrame(tick);
        const d = clock.getDelta();
        if (mixer) mixer.update(d);
        glance += (want - glance) * Math.min(1, d * 3);
        her.rotation.y = Math.PI + glance;
        renderer.render(scene, cam);
      }
      function run(ms) {
        until = Math.max(until, Date.now() + (ms || 22000));
        if (!frame && !document.hidden) { clock.getDelta(); tick(); }
      }
      function rest() { if (frame) { cancelAnimationFrame(frame); frame = null; } }
      document.addEventListener('visibilitychange', () => document.hidden ? rest() : run(8000));
      box.addEventListener('pointerenter', () => run(14000));
      box.addEventListener('pointermove', () => run(14000), { passive: true });
      window.nuraStir = run;                            // opening her bubble wakes her too
      canvas.hidden = false;
      run();
      face.style.opacity = '0';                        // cross-fade the poster out under her
      window.nuraHappy = () => {                       // a small flourish when she is tapped
        if (!mixer || !clips || !clips['happy']) return;
        const a = mixer.clipAction(clips['happy']);
        a.setLoop(THREE.LoopOnce, 1);
        a.reset().fadeIn(.15).play();
      };
    } catch (e) {
      woke = false;                                    // the poster is a perfectly good Nura
    }
  }
  document.getElementById('nura-hush').addEventListener('click', () => shut(true));
  go.addEventListener('click', () => { if (window.tx) tx('nura_cta', { ask: pick }); });
  tab.addEventListener('click', () => {
    if (window.nuraStir) window.nuraStir(22000);
    if (window.nuraHappy) window.nuraHappy();
    if (open) { shut(false); return; }
    say.hidden = false;
    show();
    open = true;
  });

  // She waits: long enough that she is never the first thing that happens on a page, and
  // she comes sooner for somebody who is clearly reading than for somebody passing through.
  const WAIT = pick === 'hello' ? 26000 : 18000;
  setTimeout(speak, WAIT);
  function onScroll() {
    const h = document.documentElement;
    const seen = (h.scrollTop + window.innerHeight) / (h.scrollHeight || 1);
    if (seen > 0.55 && Date.now() - PAGE_OPENED > 9000) {
      window.removeEventListener('scroll', onScroll);
      speak();
    }
  }
  window.addEventListener('scroll', onScroll, { passive: true });
})();
document.addEventListener('submit', e => {
  const f = e.target;
  // Two things a real visitor produces and a script posting the form does not: time spent on
  // the page, and a value written by JavaScript. The submissions sheet drops anything missing
  // them, which keeps the bots that fill this form out of the approval queue.
  try {
    const t = f.querySelector('input[name="_t"]');
    const j = f.querySelector('input[name="_js"]');
    if (t) t.value = String(Date.now() - PAGE_OPENED);
    if (j) j.value = String(Date.now()).split('').reverse().join('').slice(0, 8);
  } catch (err) { /* never block a real person from sending the form */ }
  if (f && /kit\.com\/forms/.test(f.action || '')) window.tx('newsletter_signup', { from: location.pathname.split('/').filter(Boolean)[0] || 'home' });
  else if (f && /formsubmit\.co/.test(f.action || '')) window.tx('form_submit', { from: location.pathname.split('/').filter(Boolean)[0] || 'home' });
  // Send a copy of the submission to the submissions sheet, so it can be reviewed and approved
  // rather than living only in an inbox. sendBeacon is used because the page is about to
  // navigate away and a normal fetch would be cancelled. The email still goes out as before,
  // and if this copy fails the form is unaffected.
  try {
    if (SHEET && f && /formsubmit\.co/.test(f.action || '')) {
      navigator.sendBeacon(SHEET, new URLSearchParams(new FormData(f)));
    }
  } catch (err) { /* never let the copy break the form */ }
});
// first or returning visitor, once per visit (a flag in this browser only, no cookie, no id)
(function(){
  try {
    if (sessionStorage.getItem('tanitxr.counted')) return;
    sessionStorage.setItem('tanitxr.counted', '1');
    const back = localStorage.getItem('tanitxr.seen');
    localStorage.setItem('tanitxr.seen', String(Date.now()));
    window.tx('visit', { from: back ? 'returning' : 'first' });
  } catch (e) { /* private mode */ }
})();

const hd=document.querySelector('header.site');
addEventListener('scroll',()=>{hd.classList.toggle('scrolled',scrollY>40)},{passive:true});
const nt=document.getElementById('nav-toggle');
if(nt){nt.addEventListener('click',()=>{document.getElementById('mobnav').classList.toggle('open')})}
// "View in 3D": swap a card thumbnail for the live Sketchfab viewer
document.addEventListener('click',e=>{
  const b=e.target.closest('[data-embed]');if(!b)return;
  e.preventDefault();
  const ph=b.closest('.ph');if(!ph)return;
  const f=document.createElement('iframe');
  f.src='https://sketchfab.com/models/'+b.dataset.embed+'/embed?autostart=1&ui_theme=dark&ui_infos=0&ui_watermark=0';
  f.allow='autoplay; fullscreen; xr-spatial-tracking';f.allowFullscreen=true;f.title='3D model';
  ph.innerHTML='';ph.classList.add('live');ph.appendChild(f);
});
// count-up animation on impact numbers
(function(){
  const els=document.querySelectorAll('.cnt');
  if(!els.length)return;
  if(matchMedia('(prefers-reduced-motion: reduce)').matches)return;
  const io=new IntersectionObserver(entries=>{
    entries.forEach(en=>{
      if(!en.isIntersecting)return;
      io.unobserve(en.target);
      const el=en.target,n=+el.dataset.n,s=el.dataset.s||'+',t0=performance.now(),dur=1400;
      function tick(t){
        const p=Math.min(1,(t-t0)/dur),e=1-Math.pow(1-p,3);
        el.textContent=Math.round(n*e)+s;
        if(p<1)requestAnimationFrame(tick);
      }
      requestAnimationFrame(tick);
    });
  },{threshold:.4});
  els.forEach(e=>io.observe(e));
})();

// ---------------- galleries: feature viewers + the object overlay ----------------
(function(){
  const ov=document.getElementById('gov');
  if(!ov)return;
  const objs=window.GAL||[];
  const stage=ov.querySelector('.stage'), label=ov.querySelector('.label');
  let idx=-1;

  // a feature object loads its viewer on click, in place
  document.querySelectorAll('.feat .go').forEach(b=>{
    b.addEventListener('click',()=>{
      const st=b.closest('.stage'), f=document.createElement('iframe');
      f.src='https://sketchfab.com/models/'+st.dataset.uid+'/embed?autostart=1&transparent=1&ui_theme=dark&ui_infos=0&ui_watermark=0';
      f.allow='autoplay; fullscreen; xr-spatial-tracking';f.allowFullscreen=true;
      f.title=st.dataset.title||'3D model';
      st.classList.add('live');st.appendChild(f);
    });
  });

  function esc(t){const d=document.createElement('div');d.textContent=t==null?'':t;return d.innerHTML}

  function show(i){
    if(i<0||i>=objs.length)return;
    idx=i;const o=objs[i];
    stage.innerHTML='';
    const f=document.createElement('iframe');
    f.src='https://sketchfab.com/models/'+o.uid+'/embed?autostart=1&transparent=1&ui_theme=dark&ui_infos=0&ui_watermark=0';
    f.allow='autoplay; fullscreen; xr-spatial-tracking';f.allowFullscreen=true;f.title=o.t+' 3D model';
    stage.appendChild(f);
    let rows='<dt>'+esc(o.hallLabel)+'</dt><dd>'+esc(o.place)+'</dd>';
    if(o.period)rows+='<dt>Period</dt><dd>'+esc(o.period)+'</dd>';
    if(o.scan)rows+='<dt>Scanned by</dt><dd>'+o.scan+'</dd>';
    if(o.opt)rows+='<dt>Optimized by</dt><dd>'+o.opt+'</dd>';
    rows+='<dt>Record</dt><dd>'+(o.gr?'Preservation scan and game-ready twin':'Preservation scan')+'</dd>';
    label.innerHTML='<div class="k">'+esc(o.hall)+'</div><h3>'+esc(o.t)+'</h3>'
      +'<dl>'+rows+'</dl><p>'+esc(o.d)+'</p>'
      +'<a class="more" href="'+o.h+'">Open the full record</a>';
    ov.classList.add('on');document.body.style.overflow='hidden';
    ov.querySelector('.x').focus();
  }
  function close(){ov.classList.remove('on');stage.innerHTML='';document.body.style.overflow=''}

  document.querySelectorAll('.plinth').forEach(p=>{
    p.addEventListener('click',()=>show(+p.dataset.i));
  });
  ov.querySelector('.x').addEventListener('click',close);
  ov.querySelector('.prev').addEventListener('click',()=>show((idx-1+objs.length)%objs.length));
  ov.querySelector('.next').addEventListener('click',()=>show((idx+1)%objs.length));
  ov.addEventListener('click',e=>{if(e.target===ov)close()});
  addEventListener('keydown',e=>{
    if(!ov.classList.contains('on'))return;
    if(e.key==='Escape')close();
    if(e.key==='ArrowLeft')show((idx-1+objs.length)%objs.length);
    if(e.key==='ArrowRight')show((idx+1)%objs.length);
  });
})();
