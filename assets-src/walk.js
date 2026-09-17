// Tanit XR - The Collection. The simple one.
// One artifact at a time, centred in soft light. Scroll moves to the next, drag turns it.
// No room, no floor, no plinths: nothing for an object to sink into or collide with.
// Real measurements live in the label, where they belong.
import * as THREE from 'three';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';
import { MeshoptDecoder } from 'three/addons/libs/meshopt_decoder.module.js';

const CFG = window.WALK_CFG || { items: [] };
const MODEL_BASE = new URL('models/', import.meta.url).href;
const stage = document.getElementById('walk-stage');
const canvas = document.getElementById('walk-canvas');
const cueEl = document.getElementById('rotate-cue');
const sections = [...document.querySelectorAll('.wst[data-i]')];

function useFallback() {
  document.body.classList.add('walk-fallback');
  document.querySelectorAll('.wst-fallback').forEach(el => { el.hidden = false; });
}
let gl = null;
try { gl = canvas.getContext('webgl2') || canvas.getContext('webgl'); } catch (e) { gl = null; }
if (!gl || !CFG.items.length) { useFallback(); } else { start(); }

function start() {
  // Every object is shown at one comfortable size; the real measurement is in the label.
  // Nura is a companion, not a ruler: she floats nearby, faces you, and says a line.
  const FIT = 2.15, NURA_H = 1.25;
  const clamp = (v, a, b) => Math.min(b, Math.max(a, v));

  const renderer = new THREE.WebGLRenderer({ canvas, antialias: true, alpha: true,
                                             preserveDrawingBuffer: true });
  renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
  renderer.outputColorSpace = THREE.SRGBColorSpace;
  renderer.toneMapping = THREE.ACESFilmicToneMapping;
  renderer.toneMappingExposure = 1.1;

  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(36, 1, 0.1, 100);
  camera.position.set(0, 0.1, 6.9);
  camera.lookAt(0, 0, 0);

  // soft, even light from a few directions so any object reads without a set around it
  scene.add(new THREE.AmbientLight(0xf3ece0, 1.15));
  const l1 = new THREE.DirectionalLight(0xfff3e0, 1.9); l1.position.set(-4, 5, 6);
  const l2 = new THREE.DirectionalLight(0xe8f0f6, 0.8); l2.position.set(5, 1, -3);
  const l3 = new THREE.DirectionalLight(0xfff6ea, 0.5); l3.position.set(0, -4, 4);
  scene.add(l1, l2, l3);

  // a soft shadow beneath, so an object sits in space instead of floating in a void
  const shadowTex = (() => {
    const c = document.createElement('canvas'); c.width = c.height = 256;
    const x = c.getContext('2d');
    const g = x.createRadialGradient(128, 128, 0, 128, 128, 128);
    g.addColorStop(0, 'rgba(92,68,44,.34)');
    g.addColorStop(.55, 'rgba(92,68,44,.11)');
    g.addColorStop(1, 'rgba(92,68,44,0)');
    x.fillStyle = g; x.fillRect(0, 0, 256, 256);
    const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace; return t;
  })();

  const slots = CFG.items.map((it, i) => {
    const wrap = new THREE.Group();          // position + fade
    const pivot = new THREE.Group();         // drag turns this
    const shadow = new THREE.Mesh(new THREE.PlaneGeometry(FIT * 1.6, FIT * 1.6),
      new THREE.MeshBasicMaterial({ map: shadowTex, transparent: true, depthWrite: false }));
    shadow.rotation.x = -Math.PI / 2;
    shadow.position.y = -FIT * 0.6;
    wrap.add(pivot, shadow);
    wrap.visible = false;
    scene.add(wrap);
    return { it, i, wrap, pivot, shadow, mats: [], loaded: false, loading: false };
  });

  const loader = new GLTFLoader().setMeshoptDecoder(MeshoptDecoder);
  function load(s) {
    if (!s || s.loaded || s.loading) return;
    s.loading = true;
    loader.load(MODEL_BASE + s.it.slug + '.glb', (gltf) => {
      const o = gltf.scene;
      o.updateMatrixWorld(true);
      const box = new THREE.Box3().setFromObject(o);
      const size = box.getSize(new THREE.Vector3());
      const mid = box.getCenter(new THREE.Vector3());
      o.position.set(-mid.x, -mid.y, -mid.z);            // centred on itself
      const fit = new THREE.Group();
      fit.add(o);
      fit.scale.setScalar(FIT / (Math.max(size.x, size.y, size.z) || 1));
      if (s.it.rotate) {
        const r = s.it.rotate;
        fit.rotation.set((r[0] || 0) * Math.PI / 180, (r[1] || 0) * Math.PI / 180,
                         (r[2] || 0) * Math.PI / 180);
      }
      o.traverse(n => {
        if (!n.isMesh || !n.material) return;
        // scans are exported unlit with light baked into the texture; relighting them
        // without normals renders them black, so leave unlit materials as they are
        if (!n.material.isMeshBasicMaterial && !n.geometry.attributes.normal) {
          n.geometry.computeVertexNormals();
        }
        n.material.transparent = true;
        s.mats.push(n.material);
      });
      s.pivot.add(fit);
      s.loaded = true; s.loading = false;
    }, undefined, () => {
      s.loading = false;
      const fb = sections[s.i] && sections[s.i].querySelector('.wst-fallback');
      if (fb) fb.hidden = false;
    });
  }

  // where the pointer is, so Nura can look at it
  const ptr = { x: 0, y: 0, tx: 0, ty: 0, over: false };
  stage.addEventListener('pointermove', e => {
    const r = stage.getBoundingClientRect();
    ptr.tx = clamp(((e.clientX - r.left) / r.width) * 2 - 1, -1, 1);
    ptr.ty = clamp(((e.clientY - r.top) / r.height) * 2 - 1, -1, 1);
  }, { passive: true });
  stage.addEventListener('pointerleave', () => { ptr.tx = 0; ptr.ty = 0; });
  // show the turn cursor only when the pointer is actually over an object
  let hoverRaf = 0;
  stage.addEventListener('pointermove', e => {
    if (hoverRaf) return;
    hoverRaf = requestAnimationFrame(() => {
      hoverRaf = 0;
      if (dragging) return;
      const s = current();
      if (!s || !s.loaded) return;
      const r = stage.getBoundingClientRect();
      ndc.set(((e.clientX - r.left) / r.width) * 2 - 1, -((e.clientY - r.top) / r.height) * 2 + 1);
      ray.setFromCamera(ndc, camera);
      stage.classList.toggle('on-object', ray.intersectObject(s.wrap, true).length > 0);
    });
  }, { passive: true });

  // ---- Nura: a companion who floats nearby, faces you, and has something to say
  let nura = null, mixer = null, clips = null, idleAction = null, happyAction = null,
      nuraBaseYaw = 0, flare = 0, glance = 0;
  const nuraHolder = new THREE.Group();
  nuraHolder.position.set(2.15, -0.15, 1.1);
  scene.add(nuraHolder);
  const sparks = new THREE.Group();
  const sparkMat = new THREE.MeshBasicMaterial({ color: 0xffd76a, transparent: true, opacity: .85 });
  for (let i = 0; i < 7; i++) {
    const m = new THREE.Mesh(new THREE.SphereGeometry(0.018 + Math.random() * 0.016, 7, 6), sparkMat);
    m.userData = { a: Math.random() * Math.PI * 2, r: .34 + Math.random() * .3,
                   y: .2 + Math.random() * .9, sp: .5 + Math.random() * .9 };
    sparks.add(m);
  }
  nuraHolder.add(sparks);
  loader.load(MODEL_BASE + 'nura.glb', (gltf) => {
    const o = gltf.scene;
    o.updateMatrixWorld(true);
    const b = new THREE.Box3().setFromObject(o);
    const sz = b.getSize(new THREE.Vector3());
    const c = b.getCenter(new THREE.Vector3());
    o.position.set(-c.x, -b.min.y, -c.z);
    const g = new THREE.Group();
    g.add(o);
    g.scale.setScalar(NURA_H / (sz.y || 1));
    // turn her to face the viewer; CFG.nuraYaw lets this be corrected without a code change
    g.rotation.y = (CFG.nuraYaw != null ? CFG.nuraYaw : 180) * Math.PI / 180;
    nuraBaseYaw = g.rotation.y;
    nuraHolder.add(g);
    nura = g;
    if (gltf.animations && gltf.animations.length) {
      mixer = new THREE.AnimationMixer(o);
      clips = {};
      gltf.animations.forEach(a => { clips[a.name.toLowerCase()] = a; });
      const float = gltf.animations.find(a => /float/i.test(a.name)) || gltf.animations[0];
      idleAction = mixer.clipAction(float);
      idleAction.play();
    }
  }, undefined, () => { /* Nura is optional, the page still works without her */ });

  function beHappy() {
    if (!mixer || !clips) return;
    const c = clips['happy'];
    if (!c || (happyAction && happyAction.isRunning())) return;
    happyAction = mixer.clipAction(c);
    happyAction.setLoop(THREE.LoopOnce, 1);
    happyAction.clampWhenFinished = false;
    happyAction.reset().fadeIn(0.2).play();
    if (idleAction) idleAction.crossFadeTo(happyAction, 0.2, false);
    setTimeout(() => {
      if (idleAction) { idleAction.reset().fadeIn(0.3).play(); }
      if (happyAction) happyAction.fadeOut(0.3);
    }, Math.max(900, c.duration * 1000));
  }

  const bubble = document.getElementById('nura-bubble');
  const bubbleText = document.getElementById('nura-text');
  const bubbleLong = document.getElementById('nura-long');
  const moreBtn = document.getElementById('nura-more');
  const speakBtn = document.getElementById('nura-speak');
  const closeBtn = document.getElementById('nura-close');
  const dot = document.getElementById('nura-dot');
  let speaking = false, bubbleOpen = false, expanded = false;

  function sayLine(text) {
    if (!('speechSynthesis' in window) || !text) return;
    speechSynthesis.cancel();
    const u = new SpeechSynthesisUtterance(text);
    u.rate = 0.98; u.pitch = 1.08;
    u.onend = () => { speaking = false; if (speakBtn) speakBtn.classList.remove('on'); };
    speaking = true;
    if (speakBtn) speakBtn.classList.add('on');
    speechSynthesis.speak(u);
  }
  function hushNura() {
    if (speaking) { speechSynthesis.cancel(); speaking = false; }
    if (speakBtn) speakBtn.classList.remove('on');
  }
  function openBubble() {
    const s = slots[shown];
    if (!s || !bubble) return;
    bubbleOpen = true; expanded = false;
    bubble.hidden = false;
    if (dot) dot.classList.remove('in');
    if (bubbleText) bubbleText.textContent = s.it.hi || s.it.title;
    if (bubbleLong) { bubbleLong.textContent = s.it.note || ''; bubbleLong.hidden = true; }
    if (moreBtn) {
      moreBtn.textContent = 'Tell me more';
      moreBtn.hidden = !(s.it.note && s.it.note !== s.it.hi);
    }
    beHappy();
    flare = 1;
  }
  function closeBubble() {
    bubbleOpen = false;
    if (bubble) bubble.hidden = true;
    hushNura();
  }
  if (closeBtn) closeBtn.addEventListener('click', closeBubble);
  if (dot) dot.addEventListener('click', openBubble);
  if (moreBtn) moreBtn.addEventListener('click', () => {
    expanded = !expanded;
    if (bubbleLong) bubbleLong.hidden = !expanded;
    moreBtn.textContent = expanded ? 'That is enough' : 'Tell me more';
    if (expanded) bump(p => { p.more++; });
  });
  if (speakBtn) speakBtn.addEventListener('click', () => {
    if (speaking) { hushNura(); return; }
    const s = slots[shown];
    if (!s) return;
    sayLine(expanded ? (s.it.hi + ' ' + s.it.note) : (s.it.hi || s.it.title));
  });

  // ---- scroll moves along the list, one object per section
  let cursor = 0, target = 0;
  const midOf = el => el.offsetTop + el.offsetHeight / 2 - innerHeight / 2;
  function readScroll() {
    if (!sections.length) return;
    const y = scrollY;
    if (y <= midOf(sections[0])) target = 0;
    else if (y >= midOf(sections[sections.length - 1])) target = sections.length - 1;
    else for (let i = 0; i < sections.length - 1; i++) {
      const a = midOf(sections[i]), b = midOf(sections[i + 1]);
      if (y >= a && y <= b) { target = i + (y - a) / (b - a || 1); break; }
    }
    const c = Math.round(target);
    for (let i = c - 1; i <= c + 2; i++) load(slots[i]);
  }

  // ---- drag to turn whichever object is in front
  let dragging = false, lastX = 0, lastY = 0, idle = 0;
  const ray = new THREE.Raycaster(), ndc = new THREE.Vector2();
  const current = () => slots[Math.round(clamp(cursor, 0, slots.length - 1))];
  stage.addEventListener('pointerdown', e => {
    dragging = true; idle = 0; lastX = e.clientX; lastY = e.clientY;
    stage.classList.add('grabbing');
    moved = 0;
    if (cueEl) { cueEl.classList.remove('show'); cueEl.classList.add('gone'); }
  });
  addEventListener('pointermove', e => {
    if (!dragging) return;
    moved += Math.abs(e.clientX - lastX);
    if (moved > 24 && !turned) {
      turned = true;
      if (window.tx) tx('collection_rotate');
      bump(p => { p.rotated++; });
    }
    const s = current();
    if (s) {
      s.pivot.rotation.y += (e.clientX - lastX) * 0.01;
      s.pivot.rotation.x = clamp(s.pivot.rotation.x + (e.clientY - lastY) * 0.005, -0.7, 0.7);
    }
    lastX = e.clientX; lastY = e.clientY;
  }, { passive: true });
  const stopDrag = () => {
    dragging = false;
    stage.classList.remove('grabbing');
    if (!turned && cueEl) {                   // a tap is not a turn, keep showing the cue
      cueEl.classList.remove('gone');
      cueEl.classList.add('show');
    }
  };
  addEventListener('pointerup', stopDrag);
  addEventListener('pointercancel', stopDrag);

  // ---- the label follows whichever object is in front
  const uiTitle = document.getElementById('wf-title');
  const uiId = document.getElementById('wf-id');
  const uiSave = document.getElementById('wf-save');
  const uiRecord = document.getElementById('wf-record');
  const SAVED = 'tanitxr.saved';
  const readSaved = () => { try { return JSON.parse(localStorage.getItem(SAVED) || '[]'); }
                            catch (e) { return []; } };
  const writeSaved = l => { try { localStorage.setItem(SAVED, JSON.stringify(l)); }
                            catch (e) { /* private mode */ } };

  // ---- badges: a quiet scavenger hunt through the collection
  const PROG = 'tanitxr.progress';
  const BADGES = [
    { id: 'first-turn', icon: '\u21bb', name: 'First Turn',
      how: 'Turn an object with your cursor', test: p => p.rotated >= 1 },
    { id: 'curator', icon: '\u2665', name: 'Curator',
      how: 'Save five objects', test: p => p.saved.length >= 5 },
    { id: 'listener', icon: '\u25cf', name: 'Good Listener',
      how: 'Ask Nura for more on ten objects', test: p => p.more >= 10 },
    { id: 'surveyor', icon: '\u25c8', name: 'Site Surveyor',
      how: 'See something from every place we have scanned',
      test: p => p.places.length >= PLACES.length },
    { id: 'guardian', icon: '\u2691', name: 'Guardian',
      how: 'Share an object so others see it', test: p => p.shared >= 1 },
    { id: 'completionist', icon: '\u2726', name: 'Whole Collection',
      how: 'Look at every object', test: p => p.seen.length >= CFG.items.length },
  ];
  const PLACES = Array.from(new Set(CFG.items.map(i => i.place).filter(Boolean)));
  const blank = { seen: [], places: [], saved: [], rotated: 0, more: 0, shared: 0, badges: [] };
  function readProg() {
    try { return Object.assign({}, blank, JSON.parse(localStorage.getItem(PROG) || '{}')); }
    catch (e) { return Object.assign({}, blank); }
  }
  function writeProg(p) {
    try { localStorage.setItem(PROG, JSON.stringify(p)); } catch (e) { /* private mode */ }
  }
  const toast = document.getElementById('badge-toast');
  const toastName = document.getElementById('bt-name');
  let lastBadge = null;
  function award(p) {
    BADGES.forEach(b => {
      if (p.badges.includes(b.id) || !b.test(p)) return;
      p.badges.push(b.id);
      lastBadge = b;
      if (toast && toastName) {
        toast.querySelector('.bt-icon').textContent = b.icon;
        toastName.textContent = b.name;
        toast.hidden = false;
        clearTimeout(toast._t);
        toast._t = setTimeout(() => { toast.hidden = true; }, 9000);
      }
      if (window.tx) tx('badge_earned', { badge: b.id });
    });
  }
  function bump(fn) {
    const p = readProg();
    fn(p);
    award(p);
    writeProg(p);
    paintChip(p);
    paintBadges(p);
  }
  function paintChip(p) {
    p = p || readProg();
    if (chipCount) chipCount.textContent = p.saved.length;
    const prog = document.querySelector('#saved-chip .sc-prog');
    if (prog) prog.textContent = p.seen.length + '/' + CFG.items.length;
    if (chip) chip.style.display = (p.saved.length || p.seen.length > 2) ? '' : 'none';
  }
  function paintBadges(p) {
    p = p || readProg();
    const list = document.getElementById('badge-list');
    if (!list) return;
    list.innerHTML = '';
    BADGES.forEach(b => {
      const got = p.badges.includes(b.id);
      const d = document.createElement('div');
      d.className = 'bd' + (got ? '' : ' locked');
      d.innerHTML = '<span class="bi">' + b.icon + '</span><span><b>' + b.name
        + '</b><span>' + b.how + '</span></span>';
      list.appendChild(d);
    });
  }
  document.querySelectorAll('.st-tab').forEach(tb => tb.addEventListener('click', () => {
    document.querySelectorAll('.st-tab').forEach(o => o.classList.toggle('on', o === tb));
    const badges = tb.dataset.tab === 'badges';
    document.getElementById('saved-list').hidden = badges;
    document.getElementById('badge-list').hidden = !badges;
    if (badges) paintBadges();
  }));
  const btClose = document.getElementById('bt-close');
  if (btClose) btClose.addEventListener('click', () => { toast.hidden = true; });
  const btShare = document.getElementById('bt-share');
  if (btShare) btShare.addEventListener('click', () => {
    toast.hidden = true;
    makePoster(lastBadge);
  });

  // ---- the saved tray, so saving actually leads somewhere
  const chip = document.getElementById('saved-chip');
  const chipCount = document.getElementById('saved-count');
  const tray = document.getElementById('saved-tray');
  const trayList = document.getElementById('saved-list');
  function goTo(slug) {
    const i = slots.findIndex(x => x.it.slug === slug);
    if (i >= 0 && sections[i]) scrollTo({ top: midOf(sections[i]), behavior: 'smooth' });
  }
  function paintTray() {
    const list = readSaved();
    if (chipCount) chipCount.textContent = list.length;
    if (chip) chip.style.display = list.length ? '' : 'none';
    if (!trayList) return;
    trayList.innerHTML = '';
    if (!list.length) {
      trayList.innerHTML = '<p>Nothing saved yet. Press Save on any object.</p>';
      return;
    }
    list.forEach(slug => {
      const it = (CFG.items.find(x => x.slug === slug));
      if (!it) return;
      const b = document.createElement('button');
      b.className = 'si';
      b.innerHTML = (it.thumb ? '<img src="' + it.thumb + '" alt="">' : '<img alt="">')
        + '<span><b>' + it.title.replace(/[<>&]/g, '') + '</b>'
        + '<span>' + (it.place || '').replace(/[<>&]/g, '') + '</span></span>';
      b.addEventListener('click', () => { tray.hidden = true; goTo(slug); });
      trayList.appendChild(b);
    });
  }
  if (chip) chip.addEventListener('click', () => {
    tray.hidden = !tray.hidden;
    if (!tray.hidden) paintTray();
  });
  const closeTray = document.getElementById('saved-close');
  if (closeTray) closeTray.addEventListener('click', () => { tray.hidden = true; });
  const clearBtn = document.getElementById('saved-clear');
  if (clearBtn) clearBtn.addEventListener('click', () => {
    writeSaved([]); paintTray(); paintSave(slots[shown] ? slots[shown].it : {});
  });
  const shareColl = document.getElementById('saved-share');
  if (shareColl) shareColl.addEventListener('click', async () => {
    const list = readSaved();
    if (!list.length) return;
    const url = location.origin + location.pathname + '#saved=' + list.join(',');
    const text = 'My collection of Tunisian heritage scanned by Tanit XR volunteers, '
      + list.length + ' objects. Share them to help protect them.';
    if (window.tx) tx('collection_share', { count: list.length });
    try {
      if (navigator.share) await navigator.share({ title: 'My Tanit XR collection', text, url });
      else {
        await navigator.clipboard.writeText(url);
        shareColl.textContent = 'Link copied';
        setTimeout(() => { shareColl.textContent = 'Share my collection'; }, 2000);
      }
    } catch (e) { /* dismissed */ }
  });
  let shown = -1, turned = false, cueTimer = null, moved = 0;
  function paintSave(it) {
    if (!uiSave) return;
    const on = readSaved().includes(it.slug);
    uiSave.classList.toggle('on', on);
    uiSave.textContent = on ? 'Saved ♥' : 'Save ♡';
  }
  function paint(i) {
    const s = slots[i];
    if (!s || shown === i) return;
    shown = i;
    if (uiTitle) uiTitle.textContent = s.it.title;
    if (uiId) uiId.textContent = [s.it.place, s.it.size].filter(Boolean).join(' · ');
    if (uiRecord) uiRecord.href = s.it.href || 'archive.html';
    const by = document.getElementById('wf-by');
    if (by) by.textContent = s.it.credit || '';
    closeBubble();                                    // she stays quiet until you ask
    if (dot) dot.classList.add('in');
    glance = 1.6;                                     // she looks over at the new piece
    if (cueEl && !turned) {                       // keep signalling until they try it once
      clearTimeout(cueTimer);
      cueEl.classList.remove('gone');
      cueTimer = setTimeout(() => cueEl.classList.add('show'), 500);
    }
    paintSave(s.it);
    if (window.tx) tx('collection_view', { object: s.it.slug });
    bump(p => {
      if (!p.seen.includes(s.it.slug)) p.seen.push(s.it.slug);
      if (s.it.place && !p.places.includes(s.it.place)) p.places.push(s.it.place);
    });
    history.replaceState(null, '', '#' + s.it.slug);
  }
  const on = (id, fn) => { const el = document.getElementById(id); if (el) el.addEventListener('click', fn); };
  on('wf-save', () => {
    const s = slots[shown]; if (!s) return;
    const l = readSaved(), i = l.indexOf(s.it.slug);
    i >= 0 ? l.splice(i, 1) : l.push(s.it.slug);
    writeSaved(l);
    paintSave(s.it);
    paintTray();
  paintChip();
  paintBadges();
    bump(p => { p.saved = l.slice(); });
    if (window.tx && i < 0) tx('collection_save', { object: s.it.slug });
  });
  on('wf-share', async () => {
    const s = slots[shown]; if (!s) return;
    const url = location.origin + location.pathname + '#' + s.it.slug;
    const text = s.it.title + ', scanned in Tunisia by Tanit XR volunteers. '
      + 'Share it to help protect it.';
    if (window.tx) tx('collection_share', { object: s.it.slug });
    bump(p => { p.shared++; });
    const btn = document.getElementById('wf-share');
    try {
      if (navigator.share) await navigator.share({ title: s.it.title, text, url });
      else {
        await navigator.clipboard.writeText(url);
        btn.textContent = 'Link copied';
        setTimeout(() => { btn.textContent = 'Share to protect it'; }, 2000);
      }
    } catch (e) { /* dismissed */ }
  });
  const jump = d => {
    const i = clamp(Math.round(cursor) + d, 0, sections.length - 1);
    const el = sections[i];
    if (el) scrollTo({ top: midOf(el), behavior: 'smooth' });
  };
  on('wf-prev', () => jump(-1));
  on('wf-next', () => jump(1));
  addEventListener('keydown', e => {
    if (e.key === 'ArrowLeft') jump(-1);
    if (e.key === 'ArrowRight') jump(1);
  });

  // ---- a square post image of whatever you are looking at, ready for LinkedIn
  function makePoster(badge) {
    const s = slots[shown];
    if (!s || !s.loaded) return;
    const S = 1200;
    const oldW = stage.clientWidth, oldH = stage.clientHeight, oldFov = camera.fov;
    const wasDot = dot ? dot.className : '';
    const nuraWas = nuraHolder.visible;
    nuraHolder.visible = false;                       // the object alone, no guide
    renderer.setSize(S, S, false);
    camera.aspect = 1; camera.fov = 34; camera.updateProjectionMatrix();
    const held = slots.map(x => [x, x.wrap.visible, x.wrap.position.clone()]);
    slots.forEach(x => { x.wrap.visible = (x === s); });
    s.wrap.position.set(0, 0, 0);
    s.mats.forEach(m => { m.opacity = 1; });
    renderer.render(scene, camera);

    const out = document.createElement('canvas');
    out.width = out.height = S;
    const x = out.getContext('2d');
    const g = x.createRadialGradient(S * .5, S * .38, 0, S * .5, S * .38, S * .8);
    g.addColorStop(0, '#fdf8ef'); g.addColorStop(.5, '#f2e9da'); g.addColorStop(1, '#e2d4bd');
    x.fillStyle = g; x.fillRect(0, 0, S, S);
    x.drawImage(renderer.domElement, 0, -40, S, S);

    const pad = 70;
    x.textAlign = 'left';
    const p = readProg();
    const eyebrow = badge ? 'BADGE EARNED'
      : [s.it.place, s.it.size].filter(Boolean).join('  \u00b7  ').toUpperCase();
    const heading = badge ? badge.name : s.it.title;
    const under = badge
      ? p.seen.length + ' of ' + CFG.items.length + ' objects seen in the Tanit XR collection'
      : (s.it.credit || 'Scanned by a Tanit XR volunteer');
    x.fillStyle = badge ? '#a35f3f' : '#8a735c';
    x.font = '700 22px Roboto, Helvetica, Arial, sans-serif';
    x.fillText(eyebrow, pad, S - 190);
    x.fillStyle = '#2e2118';
    let size = 62;
    x.font = '400 ' + size + 'px "Yeseva One", Georgia, serif';
    while (x.measureText(heading).width > S - pad * 2 && size > 30) {
      size -= 3;
      x.font = '400 ' + size + 'px "Yeseva One", Georgia, serif';
    }
    x.fillText(heading, pad, S - 130);
    x.fillStyle = '#5d4c3c';
    x.font = '400 24px Roboto, Helvetica, Arial, sans-serif';
    x.fillText(under, pad, S - 88);
    x.fillStyle = '#a35f3f';
    x.font = '700 22px Roboto, Helvetica, Arial, sans-serif';
    x.fillText('TANIT XR', pad, S - 44);
    x.fillStyle = '#8a735c';
    x.font = '400 22px Roboto, Helvetica, Arial, sans-serif';
    x.fillText('tanitxr.org', pad + 130, S - 44);

    held.forEach(([o, vis, pos]) => { o.wrap.visible = vis; o.wrap.position.copy(pos); });
    nuraHolder.visible = nuraWas;
    if (dot) dot.className = wasDot;
    camera.fov = oldFov; camera.aspect = oldW / oldH; camera.updateProjectionMatrix();
    renderer.setSize(oldW, oldH, false);

    out.toBlob(b => {
      if (!b) return;
      const a = document.createElement('a');
      a.href = URL.createObjectURL(b);
      a.download = 'tanitxr-' + (badge ? 'badge-' + badge.id : s.it.slug) + '.png';
      a.click();
      setTimeout(() => URL.revokeObjectURL(a.href), 4000);
    }, 'image/png');
    if (window.tx) tx('collection_poster', { object: s.it.slug });
  }
  const posterBtn = document.getElementById('wf-poster');
  if (posterBtn) posterBtn.addEventListener('click', () => {
    posterBtn.textContent = 'Saving...';
    setTimeout(() => {
      makePoster();
      posterBtn.textContent = 'Make a post image';
    }, 40);
  });

  function resize() {
    const w = stage.clientWidth, h = stage.clientHeight;
    renderer.setSize(w, h, false);
    camera.aspect = w / h;
    camera.fov = w < 760 ? 46 : 36;
    camera.updateProjectionMatrix();
    readScroll();
  }
  addEventListener('resize', resize, { passive: true });
  addEventListener('scroll', readScroll, { passive: true });
  resize();
  cursor = target;
  load(slots[0]);

  const wanted = decodeURIComponent(location.hash.slice(1));
  if (wanted.startsWith('saved=')) {              // someone shared their collection
    const list = wanted.slice(6).split(',').filter(sl => CFG.items.some(x => x.slug === sl));
    if (list.length) {
      writeSaved(Array.from(new Set(readSaved().concat(list))));
      paintTray();
      if (tray) tray.hidden = false;
      goTo(list[0]);
    }
  } else if (wanted) {
    const i = slots.findIndex(x => x.it.slug === wanted);
    if (i >= 0 && sections[i]) scrollTo({ top: midOf(sections[i]), behavior: 'instant' });
  }
  paintTray();

  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const clock = new THREE.Clock();
  (function frame() {
    const dt = Math.min(clock.getDelta(), 0.05);
    cursor += (target - cursor) * (reduce ? 1 : 0.12);
    if (!dragging) idle += dt;
    const t = clock.elapsedTime;
    paint(Math.round(clamp(cursor, 0, slots.length - 1)));

    slots.forEach(s => {
      const d = s.i - cursor;                       // 0 = front and centre
      const ad = Math.abs(d);
      const a = Math.max(0, 1 - ad * 1.3);
      s.wrap.visible = s.loaded && a > 0.005;
      if (!s.wrap.visible) return;
      // ease the travel so an object rises and settles rather than sliding past
      const e = 1 - Math.pow(1 - Math.min(1, ad), 2);
      s.wrap.position.set(0, -Math.sign(d) * e * 3.6, -e * 3.0);
      s.wrap.scale.setScalar(0.78 + 0.22 * a);
      const breathe = ad < 0.5 && !reduce ? Math.sin(t * 0.8) * 0.012 : 0;
      s.wrap.position.y += breathe;                 // the faintest float, so it feels alive
      s.mats.forEach(m => { m.opacity = a; });
      s.shadow.material.opacity = a * 0.8;
      if (!reduce && !dragging && idle > 2.2 && ad < 0.5) s.pivot.rotation.y += dt * 0.14;
    });

    if (mixer) mixer.update(dt);
    if (nura) {
      // park her a fixed fraction across the frame, so she is never cut off
      const halfH = Math.tan(camera.fov * Math.PI / 360) * camera.position.z;
      const halfW = halfH * camera.aspect;
      ptr.x += (ptr.tx - ptr.x) * 0.06;
      ptr.y += (ptr.ty - ptr.y) * 0.06;
      const homeX = clamp(halfW * 0.52, 1.0, 2.9);
      nuraHolder.position.x = homeX + Math.sin(t * 0.43) * 0.07 + ptr.x * 0.16;
      nuraHolder.position.y = -halfH * 0.16 + Math.sin(t * 1.05) * 0.075 - ptr.y * 0.1;
      nuraHolder.position.z = 0.9;
      // she looks at the new object for a moment, then back at you and your cursor
      glance = Math.max(0, glance - dt);
      const look = Math.min(1, glance) * 0.75;
      nura.rotation.y = nuraBaseYaw + ptr.x * 0.5 + Math.sin(t * 0.5) * 0.06 + look;
      nura.rotation.x = -ptr.y * 0.16;
      nura.rotation.z = Math.sin(t * 0.8) * 0.03;
      sparks.children.forEach(m => {
        m.userData.a += dt * m.userData.sp;
        m.position.set(Math.cos(m.userData.a) * m.userData.r,
                       m.userData.y + Math.sin(t * m.userData.sp + m.userData.a) * 0.09,
                       Math.sin(m.userData.a) * m.userData.r * 0.7);
        m.material.opacity = clamp(0.3 + 0.5 * (0.5 + 0.5 * Math.sin(t * 2 + m.userData.a))
                                   + flare * 0.7, 0, 1);
        m.scale.setScalar(1 + flare * 1.4);
      });
      flare = Math.max(0, flare - dt * 1.1);
      const head = new THREE.Vector3(0, NURA_H * 1.02, 0);
      nuraHolder.localToWorld(head);
      head.project(camera);
      const r = stage.getBoundingClientRect();
      const sx = r.left + (head.x * 0.5 + 0.5) * r.width;
      const sy = r.top + (-head.y * 0.5 + 0.5) * r.height;
      if (bubble && !bubble.hidden) {
        const bw = bubble.offsetWidth || 290;
        const lx = clamp(sx, r.left + bw / 2 + 12, r.right - bw / 2 - 12);
        bubble.style.left = Math.round(lx) + 'px';
        bubble.style.top = Math.round(Math.max(sy - 10, r.top + bubble.offsetHeight + 16)) + 'px';
      }
      if (dot) {
        dot.style.left = Math.round(sx) + 'px';
        dot.style.top = Math.round(sy) + 'px';
      }
    }

    renderer.render(scene, camera);
    requestAnimationFrame(frame);
  })();

  const io = new IntersectionObserver(es => es.forEach(e =>
    e.target.classList.toggle('on', e.isIntersecting && e.intersectionRatio > 0.5)),
    { threshold: [0, 0.5, 1] });
  document.querySelectorAll('.wst-intro,.wst-end,.warea').forEach(s => io.observe(s));
}
