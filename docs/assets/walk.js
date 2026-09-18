// Tanit XR - The Collection. The simple one.
// One artifact at a time, centred in soft light. Scroll moves to the next, drag turns it.
// No room, no floor, no plinths: nothing for an object to sink into or collide with.
// Real measurements live in the label, where they belong.
import * as THREE from 'three';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';
import { MeshoptDecoder } from 'three/addons/libs/meshopt_decoder.module.js';

const CFG = window.WALK_CFG || { items: [] };
const MODEL_BASE = new URL('models/', import.meta.url).href;
// thumbnails are stored as 'assets/img/x.jpg'; resolve them beside this script, not beside
// the page, or a pretty URL like /walk/ turns them into /walk/assets/img/x.jpg
const ASSET_BASE = new URL('./', import.meta.url).href;
const assetUrl = p => p ? new URL(p.replace(/^assets\//, ''), ASSET_BASE).href : '';
// Links in the config are site-root relative, like 'archive/x.html'. The build rewrites
// such paths in real markup but cannot see inside a JSON blob, so from a pretty URL like
// /walk/ they would resolve to /walk/archive/x.html and 404. Resolve them off the root.
const SITE_ROOT = new URL('../', import.meta.url).href;
const AUDIO_BASE = new URL('audio/', import.meta.url).href;
const linkUrl = p => p ? new URL(p, SITE_ROOT).href : '';
const stage = document.getElementById('walk-stage');
const canvas = document.getElementById('walk-canvas');
const cueEl = document.getElementById('rotate-cue');
const sections = [...document.querySelectorAll('.wst[data-i]')];

function useFallback() {
  // the Sketchfab players only start loading now; with a src from the start, 75 hidden
  // viewers would download behind the page and starve the models on a slow connection
  document.querySelectorAll('.wst-fallback iframe[data-src]').forEach(f => { f.src = f.dataset.src; });
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
  const narrow = () => camera.aspect < 0.8;
  function homeCamera() {
    camera.fov = narrow() ? 46 : 36;
    camera.updateProjectionMatrix();
    if (narrow()) { camera.position.set(0, -0.05, 6.9); camera.lookAt(0, -0.05, 0); }
    else { camera.position.set(0, 0.1, 6.9); camera.lookAt(0, 0, 0); }
  }
  homeCamera();

  // soft, even light from a few directions so any object reads without a set around it
  const amb = new THREE.AmbientLight(0xf3ece0, 1.15);
  const l1 = new THREE.DirectionalLight(0xfff3e0, 1.9); l1.position.set(-4, 5, 6);
  const l2 = new THREE.DirectionalLight(0xe8f0f6, 0.8); l2.position.set(5, 1, -3);
  const l3 = new THREE.DirectionalLight(0xfff6ea, 0.5); l3.position.set(0, -4, 4);
  scene.add(amb, l1, l2, l3);
  // one shaft of light for the entrance, so the first object comes out of the dark
  const shaft = new THREE.SpotLight(0xffe9c4, 90, 14, Math.PI / 9, 0.62, 1.5);
  shaft.position.set(-1.7, 4.4, 3.2);
  scene.add(shaft, shaft.target);
  const LIT = { amb: 1.15, l1: 1.9, l2: 0.8, l3: 0.5 };
  // the page opens straight into the experience; the light just eases up over the first
  // moment so the first object arrives rather than snapping on
  let entryK = 0;

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

  const dust = new THREE.Group();
  for (let i = 0; i < 90; i++) {
    const m = new THREE.Mesh(new THREE.SphereGeometry(0.008 + Math.random() * 0.018, 6, 5),
      new THREE.MeshBasicMaterial({ color: 0xffe6bb, transparent: true, opacity: 0.5 }));
    m.position.set((Math.random() - 0.5) * 9, (Math.random() - 0.5) * 6, (Math.random() - 0.5) * 5);
    m.userData.s = 0.1 + Math.random() * 0.35;
    dust.add(m);
  }
  scene.add(dust);

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
      s.fileMax = Math.max(size.x, size.y, size.z) || 1;
      s.fitH = size.y * (FIT / s.fileMax);
      s.fit = fit;
      fit.scale.setScalar(FIT / s.fileMax);
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
      if (s.i === 0) document.body.classList.add('first-loaded');   // lifts the loading glow
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
      camera.updateMatrixWorld();          // the ray needs a current camera matrix
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

  let voiceEl = null;
  function sayLine(text, item) {
    hushNura();
    duckMusic(true);
    const it = item || (slots[shown] && slots[shown].it);
    if (it && it.voice) {                          // her own recorded line
      voiceEl = new Audio(AUDIO_BASE + it.voice);
      voiceEl.onended = () => { speaking = false; duckMusic(false); if (speakBtn) speakBtn.classList.remove('on'); };
      voiceEl.onerror = () => { speaking = false; duckMusic(false); if (speakBtn) speakBtn.classList.remove('on'); };
      speaking = true;
      if (speakBtn) speakBtn.classList.add('on');
      voiceEl.play().catch(() => { speaking = false; duckMusic(false); if (speakBtn) speakBtn.classList.remove('on'); });
      return;
    }
    if (!('speechSynthesis' in window) || !text) return;
    const u = new SpeechSynthesisUtterance(text);
    u.rate = 0.98; u.pitch = 1.08;
    u.onend = () => { speaking = false; duckMusic(false); if (speakBtn) speakBtn.classList.remove('on'); };
    speaking = true;
    if (speakBtn) speakBtn.classList.add('on');
    speechSynthesis.speak(u);
  }
  function hushNura() {
    duckMusic(false);
    if (voiceEl) { voiceEl.pause(); voiceEl = null; }
    if ('speechSynthesis' in window) speechSynthesis.cancel();
    speaking = false;
    if (speakBtn) speakBtn.classList.remove('on');
  }
  function openBubble() {
    sfx('pop');
    const s = slots[shown];
    if (!s || !bubble) return;
    bubbleOpen = true; expanded = false;
    bubble.hidden = false;
    if (moreBtn) { moreBtn.dataset.offer = ''; moreBtn.classList.remove('nb-offer'); }
    if (dot) dot.classList.remove('in');
    if (bubbleText) bubbleText.textContent = s.it.hi || s.it.title;
    if (speakBtn) speakBtn.title = s.it.voice ? 'Hear Nura tell it' : 'Read this aloud';
    if (speakBtn) speakBtn.classList.toggle('real', !!s.it.voice);
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
    if (moreBtn.dataset.offer === '1') {          // she offered the demo, you said yes
      moreBtn.dataset.offer = '';
      moreBtn.classList.remove('nb-offer');
      closeBubble();
      goToScanDemo();
      return;
    }
    expanded = !expanded;
    if (bubbleLong) bubbleLong.hidden = !expanded;
    moreBtn.textContent = expanded ? 'That is enough' : 'Tell me more';
    // she reads the longer line too, in her own voice where it has been recorded
    const cur = slots[shown];
    if (expanded && cur && cur.it.note) sayLine(cur.it.note, { voice: cur.it.voiceMore });
    else hushNura();
    if (expanded) bump(p => { p.more++; });
  });
  if (speakBtn) speakBtn.addEventListener('click', () => {
    if (speaking) { hushNura(); return; }
    const s = slots[shown];
    if (!s) return;
    sayLine(expanded ? (s.it.hi + ' ' + s.it.note) : (s.it.hi || s.it.title));
  });

  // ---- the closing demo: how a scan is actually made, three circles around the object
  const scanPanel = document.getElementById('scan-panel');
  let demoOn = false;
  function goToScanDemo() {
    demoOn = true;                                   // runs around the object you are on
    if (scanPanel) scanPanel.hidden = false;
    closeBubble();
    if (window.tx) tx('scan_demo_opened');
  }
  function endScanDemo() {
    demoOn = false;
    if (scanPanel) scanPanel.hidden = true;
  }
  const scanBtn = document.getElementById('scan-entry');
  if (scanBtn) scanBtn.addEventListener('click', () => demoOn ? endScanDemo() : goToScanDemo());
  const scanDone = document.getElementById('scan-done');
  if (scanDone) scanDone.addEventListener('click', endScanDemo);
  addEventListener('keydown', e => { if (e.key === 'Escape' && demoOn) endScanDemo(); });
  let scanT = 0, scanTarget = 0, phone = null, demoObj = null, demoAngle = 0, demoY = 0;
  const demo = new THREE.Group();
  demo.visible = false;
  scene.add(demo);

  const RINGS = [-0.75, 0.05, 0.85];                 // low pass, eye level, high pass
  RINGS.forEach(y => {
    const pts = [];
    for (let i = 0; i <= 96; i++) {
      const a = (i / 96) * Math.PI * 2;
      pts.push(new THREE.Vector3(Math.cos(a) * 1.75, y, Math.sin(a) * 1.75));
    }
    const geo = new THREE.BufferGeometry().setFromPoints(pts);
    const line = new THREE.Line(geo, new THREE.LineDashedMaterial({
      color: 0xa35f3f, dashSize: 0.1, gapSize: 0.08, transparent: true, opacity: 0.55 }));
    line.computeLineDistances();
    demo.add(line);
  });

  (function buildPhone() {
    phone = new THREE.Group();
    const body = new THREE.Mesh(new THREE.BoxGeometry(0.15, 0.3, 0.022),
      new THREE.MeshStandardMaterial({ color: 0x2e2724, roughness: 0.42, metalness: 0.25 }));
    const screen = new THREE.Mesh(new THREE.PlaneGeometry(0.128, 0.265),
      new THREE.MeshBasicMaterial({ color: 0xbfd8e6 }));
    screen.position.z = -0.013;
    screen.rotation.y = Math.PI;                     // the screen faces the object
    const lens = new THREE.Mesh(new THREE.CircleGeometry(0.023, 18),
      new THREE.MeshStandardMaterial({ color: 0x14110d, roughness: 0.3 }));
    lens.position.set(0.042, 0.09, 0.013);
    phone.add(body, screen, lens);
    demo.add(phone);
  })();

  function jumpTo(pred) {
    const i = CFG.items.findIndex(pred);
    if (i < 0 || !sections[i]) return;
    // this can be forty screens away, which a smooth scroll never finishes in time
    target = i;
    cursor = i;
    scrollTo({ top: midOf(sections[i]), behavior: 'instant' });
    readScroll();
  }
  // a persistent switch between the two bodies of work, not a gate in front of them
  document.querySelectorAll('.tsw').forEach(b => b.addEventListener('click', () => {
    document.querySelectorAll('.tsw').forEach(o => o.classList.toggle('on', o === b));
    const made = b.dataset.track === 'made';
    jumpTo(it => made ? !it.real : it.real);
    if (window.tx) tx(made ? 'track_made' : 'track_scans');
  }));

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
  let pressed = false, downX = 0, downY = 0;
  stage.addEventListener('pointerdown', e => {
    dragging = true; pressed = true; idle = 0;
    lastX = downX = e.clientX; lastY = downY = e.clientY;
    stage.classList.add('grabbing');
    moved = 0;
    if (cueEl) { cueEl.classList.remove('show'); cueEl.classList.add('gone'); }
  });
  // A tap, as opposed to a drag, selects. In a gallery room it picks a piece; in the normal
  // view it picks the object under the cursor so Nura can talk about it.
  stage.addEventListener('pointerup', e => {
    if (!pressed) return;
    pressed = false;
    if (Math.abs(e.clientX - downX) > 5 || Math.abs(e.clientY - downY) > 5) return;
    if (roomMode) { pickInRoom(e); return; }
    const r = stage.getBoundingClientRect();
    ndc.set(((e.clientX - r.left) / r.width) * 2 - 1, -((e.clientY - r.top) / r.height) * 2 + 1);
    camera.updateMatrixWorld();
    ray.setFromCamera(ndc, camera);
    if (nura && ray.intersectObject(nuraHolder, true).length) {
      bubbleOpen ? closeBubble() : openBubble();
      return;
    }
    const s = current();
    if (s && s.loaded && ray.intersectObject(s.wrap, true).length) openBubble();
  });
  addEventListener('pointermove', e => {
    if (!dragging) return;
    moved += Math.abs(e.clientX - lastX);
    if (moved > 24 && !turned) {
      turned = true;
      if (window.tx) tx('collection_rotate');
      bump(p => { p.rotated++; });
      maybeOfferDemo();
    }
    const s = roomMode ? roomFocus : current();
    if (s) {
      s.pivot.rotation.y += (e.clientX - lastX) * 0.01;
      s.pivot.rotation.x = clamp(s.pivot.rotation.x + (e.clientY - lastY) * 0.005, -0.7, 0.7);
    } else if (roomMode) {                    // look around the room
      roomYawT -= (e.clientX - lastX) * 0.005;
      roomPitchT = clamp(roomPitchT + (e.clientY - lastY) * 0.003, -0.35, 0.3);
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

  // ---- where it was scanned: one OpenStreetMap tile, the pin at the exact spot, a link out
  const mapA = document.getElementById('wf-map');
  const mapImg = document.getElementById('wf-map-img');
  const mapPin = document.querySelector('.wf-pin');
  function paintMap(it) {
    if (!mapA) return;
    if (!it.gps) { mapA.hidden = true; return; }
    const [lat, lon] = it.gps, z = 15, n = Math.pow(2, z);
    const xf = (lon + 180) / 360 * n;
    const la = lat * Math.PI / 180;
    const yf = (1 - Math.log(Math.tan(la) + 1 / Math.cos(la)) / Math.PI) / 2 * n;
    const x = Math.floor(xf), y = Math.floor(yf);
    const px = (xf - x) * 256, py = (yf - y) * 256;
    mapImg.src = 'https://tile.openstreetmap.org/' + z + '/' + x + '/' + y + '.png';
    // slide the tile so the pin sits in the middle of the little window
    mapImg.style.left = (32 - px) + 'px';
    mapImg.style.top = (22 - py) + 'px';
    mapPin.style.left = '32px'; mapPin.style.top = '22px';
    mapA.href = 'https://www.openstreetmap.org/?mlat=' + lat + '&mlon=' + lon + '#map=17/' + lat + '/' + lon;
    mapA.hidden = false;
  }

  // ---- how many people have seen and saved this object, from the public counter, so the
  // page itself shows the numbers a report would ask for. Silent until analytics is on.
  const statsEl = document.getElementById('wf-stats');
  const statCache = {};
  function counter(path) {
    if (!CFG.gc) return Promise.resolve(null);
    if (!statCache[path]) {
      statCache[path] = fetch('https://' + CFG.gc + '.goatcounter.com/counter/' + path + '.json')
        .then(r => r.ok ? r.json() : null)
        .then(j => j ? (parseInt(String(j.count).replace(/\D/g, ''), 10) || 0) : null)
        .catch(() => null);
    }
    return statCache[path];
  }
  function paintStats(it) {
    if (!statsEl) return;
    if (!CFG.gc) { statsEl.hidden = true; return; }
    Promise.all([counter('collection_view/' + it.slug), counter('collection_save/' + it.slug)])
      .then(([v, sv]) => {
        if (!slots[shown] || slots[shown].it.slug !== it.slug) return;
        const bits = [];
        if (v) bits.push('seen ' + v.toLocaleString() + (v === 1 ? ' time' : ' times'));
        if (sv) bits.push('saved by ' + sv.toLocaleString());
        statsEl.textContent = bits.join(' · ');
        statsEl.hidden = !bits.length;
      });
  }

  // ---- paint(): everything that has to change when a different object comes to the front.
  // This is the hinge of the page, so keep it in one place.
  let shown = -1, turned = false, cueTimer = null, moved = 0;
  function paint(i) {
    const s = slots[i];
    if (!s || shown === i) return;
    const wasShown = shown;
    shown = i;
    const it = s.it;
    if (wasShown >= 0) sfx('whoosh');

    if (uiTitle) uiTitle.textContent = it.title;
    if (uiId) uiId.textContent = [it.place, it.size].filter(Boolean).join(' \u00b7 ');
    if (uiRecord) uiRecord.href = linkUrl(it.href || 'archive.html');
    const by = document.getElementById('wf-by');
    if (by) by.textContent = it.credit || '';
    paintSave(it);
    paintMap(it);
    paintStats(it);

    // the switch follows where you actually are
    document.querySelectorAll('.tsw').forEach(b =>
      b.classList.toggle('on', (b.dataset.track === 'made') === !it.real));

    // Nura goes quiet on a new object and glances over at it
    if (cameo) cameo.hidden = true;
    clearTimeout(cameoTimer);
    closeBubble();
    if (dot) dot.classList.add('in');
    glance = 1.6;
    showCameo(it);

    // keep signalling that it turns until someone has actually turned one
    if (cueEl && !turned) {
      clearTimeout(cueTimer);
      cueEl.classList.remove('gone');
      cueTimer = setTimeout(() => cueEl.classList.add('show'), 500);
    }

    paintStrip();
    bump(p => {
      if (!p.seen.includes(it.slug)) p.seen.push(it.slug);
      if (it.real && it.place && !p.places.includes(it.place)) p.places.push(it.place);
    });
    if (window.tx) tx('collection_view', { object: it.slug });
    history.replaceState(null, '', '#' + it.slug);
  }

  // ---- badges: a quiet scavenger hunt through the collection
  // ---- sound. Small cues and a quiet background, all made in the browser, nothing
  // downloaded. One tap turns it all off, and the choice is remembered.
  let audioCtx = null, music = null, gestured = false;
  const SOUND_KEY = 'tanitxr.sound';
  let soundOn = true;
  try { soundOn = localStorage.getItem(SOUND_KEY) !== 'off'; } catch (e) { /* private mode */ }
  function actx() {
    audioCtx = audioCtx || new (window.AudioContext || window.webkitAudioContext)();
    if (audioCtx.state === 'suspended') audioCtx.resume().catch(() => {});
    return audioCtx;
  }
  function tone(c, f, t0, dur, peak, type, dest) {
    const o = c.createOscillator(), g = c.createGain();
    o.type = type; o.frequency.value = f;
    g.gain.setValueAtTime(0.0001, t0);
    g.gain.exponentialRampToValueAtTime(peak, t0 + 0.02);
    g.gain.exponentialRampToValueAtTime(0.0001, t0 + dur);
    o.connect(g).connect(dest || c.destination);
    o.start(t0); o.stop(t0 + dur + 0.05);
  }
  function sfx(kind) {
    if (!soundOn || !gestured) return;
    try {
      const c = actx(), now = c.currentTime;
      if (kind === 'badge') [523.25, 659.25, 783.99].forEach((f, i) => tone(c, f, now + i * 0.11, 0.5, 0.14, 'sine'));
      else if (kind === 'save') [659.25, 783.99].forEach((f, i) => tone(c, f, now + i * 0.11, 0.5, 0.13, 'sine'));
      else if (kind === 'tap') tone(c, 987.77, now, 0.14, 0.09, 'triangle');
      else if (kind === 'pop') {                     // a bubble opening: one quick upward blip
        const o = c.createOscillator(), g = c.createGain();
        o.type = 'sine';
        o.frequency.setValueAtTime(620, now);
        o.frequency.exponentialRampToValueAtTime(1180, now + 0.07);
        g.gain.setValueAtTime(0.0001, now);
        g.gain.exponentialRampToValueAtTime(0.16, now + 0.012);
        g.gain.exponentialRampToValueAtTime(0.0001, now + 0.18);
        o.connect(g).connect(c.destination); o.start(now); o.stop(now + 0.18);
      } else if (kind === 'whoosh') {                // an object arriving: a breath of air
        const n = Math.floor(c.sampleRate * 0.36), buf = c.createBuffer(1, n, c.sampleRate);
        const d = buf.getChannelData(0);
        for (let i = 0; i < n; i++) d[i] = Math.random() * 2 - 1;
        const src = c.createBufferSource(); src.buffer = buf;
        const bp = c.createBiquadFilter(); bp.type = 'bandpass'; bp.Q.value = 0.9;
        bp.frequency.setValueAtTime(300, now);
        bp.frequency.exponentialRampToValueAtTime(1500, now + 0.17);
        bp.frequency.exponentialRampToValueAtTime(450, now + 0.36);
        const g = c.createGain();
        g.gain.setValueAtTime(0.0001, now);
        g.gain.exponentialRampToValueAtTime(0.07, now + 0.08);
        g.gain.exponentialRampToValueAtTime(0.0001, now + 0.36);
        src.connect(bp).connect(g).connect(c.destination); src.start(now); src.stop(now + 0.37);
      }
    } catch (e) { /* no audio here */ }
  }
  const chime = kind => sfx(kind === 'badge' ? 'badge' : 'save');

  // The background: a low drone and sparse plucked notes in maqam Hijaz, the scale under
  // much Tunisian music, generated live so nothing is downloaded and nothing needs a licence.
  // It stands in until a recorded track we have the rights to takes its place.
  const HIJAZ = [146.83, 155.56, 185.0, 196.0, 220.0, 233.08, 261.63, 293.66, 311.13, 369.99, 392.0, 440.0];
  let track = null;
  function duckMusic(on) {
    if (track) track.volume = on ? 0.08 : 0.26;
    if (music && music.duck) music.duck(on);
  }
  function startMusic() {
    if (music || !soundOn || !gestured) return;
    if (CFG.music && CFG.music.src) {           // a recording we hold the rights to
      try {
        track = new Audio(AUDIO_BASE + CFG.music.src);
        track.loop = true; track.volume = 0.0001;
        track.play().then(() => {
          let v = 0.0001;
          const up = setInterval(() => { v = Math.min(0.26, v + 0.012); track.volume = v; if (v >= 0.26) clearInterval(up); }, 120);
        }).catch(() => { track = null; });
        music = { stop() { const t = track; track = null; if (!t) return;
                           const down = setInterval(() => { t.volume = Math.max(0, t.volume - 0.02); if (t.volume <= 0.001) { clearInterval(down); t.pause(); } }, 80); } };
      } catch (e) { music = null; track = null; }
      return;
    }
    try {
      const c = actx();
      const master = c.createGain();
      master.gain.setValueAtTime(0.0001, c.currentTime);
      master.gain.exponentialRampToValueAtTime(0.5, c.currentTime + 5);
      const lp = c.createBiquadFilter(); lp.type = 'lowpass'; lp.frequency.value = 1500;
      master.connect(lp).connect(c.destination);
      const drone = [73.42, 73.42 * 1.004, 110.0].map((f, i) => {
        const o = c.createOscillator(), g = c.createGain();
        o.type = i === 2 ? 'sine' : 'triangle'; o.frequency.value = f;
        g.gain.value = i === 2 ? 0.05 : 0.03;
        o.connect(g).connect(master); o.start(); return o;
      });
      let timer = null, last = -1;
      const pluck = () => {
        if (!music) return;
        if (c.state !== 'running') { timer = setTimeout(pluck, 1500); return; }
        let k; do { k = Math.floor(Math.random() * HIJAZ.length); } while (k === last);
        last = k;
        const f = HIJAZ[k], t0 = c.currentTime;
        const o = c.createOscillator(), g = c.createGain(), fl = c.createBiquadFilter();
        o.type = 'sawtooth'; o.frequency.value = f;
        fl.type = 'lowpass';
        fl.frequency.setValueAtTime(f * 6, t0);
        fl.frequency.exponentialRampToValueAtTime(f * 1.5, t0 + 0.9);
        g.gain.setValueAtTime(0.0001, t0);
        g.gain.exponentialRampToValueAtTime(0.1, t0 + 0.008);
        g.gain.exponentialRampToValueAtTime(0.0001, t0 + 1.7);
        o.connect(fl).connect(g).connect(master); o.start(t0); o.stop(t0 + 1.8);
        if (Math.random() < 0.4) tone(c, f * 2, t0 + 0.26, 1.1, 0.025, 'triangle', master);
        timer = setTimeout(pluck, 1900 + Math.random() * 3400);
      };
      music = {
        duck(on) { const t = c.currentTime; master.gain.cancelScheduledValues(t);
                   master.gain.setValueAtTime(Math.max(master.gain.value, 0.0001), t);
                   master.gain.exponentialRampToValueAtTime(on ? 0.15 : 0.5, t + 0.6); },
        stop() {
          clearTimeout(timer);
          const t = c.currentTime;
          master.gain.cancelScheduledValues(t);
          master.gain.setValueAtTime(Math.max(master.gain.value, 0.0001), t);
          master.gain.exponentialRampToValueAtTime(0.0001, t + 1.2);
          setTimeout(() => drone.forEach(o => { try { o.stop(); } catch (e) { /* done */ } }), 1400);
        }
      };
      timer = setTimeout(pluck, 1400);
    } catch (e) { music = null; }
  }
  function stopMusic() { if (music) { const m = music; music = null; m.stop(); } }
  const sndBtn = document.getElementById('sound-toggle');
  function paintSound() {
    if (!sndBtn) return;
    sndBtn.classList.toggle('off', !soundOn);
    sndBtn.setAttribute('aria-pressed', soundOn ? 'true' : 'false');
    const cr = CFG.music && CFG.music.credit ? ' ' + CFG.music.credit : '';
    sndBtn.title = (soundOn ? 'Sound is on. Tap to mute.' : 'Sound is off. Tap to turn it on.') + cr;
  }
  paintSound();
  if (sndBtn) sndBtn.addEventListener('click', () => {
    soundOn = !soundOn;
    try { localStorage.setItem(SOUND_KEY, soundOn ? 'on' : 'off'); } catch (e) { /* private mode */ }
    paintSound();
    if (soundOn) { gestured = true; startMusic(); sfx('tap'); } else stopMusic();
    if (window.tx) tx('sound_toggle', { on: soundOn });
  });
  // browsers only allow sound after a real gesture, so everything waits for the first one
  const firstGesture = () => { gestured = true; startMusic(); };
  ['pointerdown', 'keydown', 'touchstart'].forEach(ev =>
    addEventListener(ev, firstGesture, { once: true, passive: true }));

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
      test: p => PLACES.every(pl => p.places.includes(pl)) },
    { id: 'guardian', icon: '\u2691', name: 'Guardian',
      how: 'Share an object so others see it', test: p => p.shared >= 1 },
    { id: 'completionist', icon: '\u2726', name: 'Whole Collection',
      how: 'Look at every object', test: p => p.seen.length >= CFG.items.length },
  ];
  // only the places we scanned on location count as sites; the hand-made shelf is not one
  const PLACES = Array.from(new Set(CFG.items.filter(i => i.real).map(i => i.place).filter(Boolean)));
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
      chime('badge');
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
  function roomKey(it) { return it.artist ? 'artist:' + it.artist : 'place:' + it.place; }
  function checkRoomDone(p, it) {
    const key = roomKey(it);
    p.rooms = p.rooms || [];
    if (p.rooms.includes(key)) return;
    const members = CFG.items.filter(x => roomKey(x) === key);
    if (members.length < 2 || !members.every(x => p.seen.includes(x.slug))) return;
    p.rooms.push(key);
    flare = 1.6;
    beHappy();
    if (bubble && bubbleText) {
      bubbleOpen = true; bubble.hidden = false;
      if (dot) dot.classList.remove('in');
      bubbleText.textContent = it.artist
        ? 'That is everything ' + it.artist.split(' ')[0] + ' has made so far.'
        : 'That is every piece we have from ' + it.place + '. ' + (CFG.items.length - p.seen.length)
          + ' left in the whole collection.';
      if (bubbleLong) bubbleLong.hidden = true;
      if (moreBtn) moreBtn.hidden = true;
    }
    chime('badge');
    if (window.tx) tx('room_complete', { room: key });
  }
  function bump(fn) {
    const p = readProg();
    fn(p);
    award(p);
    const cur = slots[shown] && slots[shown].it;
    if (cur) checkRoomDone(p, cur);
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
  // LinkedIn cannot be handed a caption or an image by a link, so do the three things a
  // person would otherwise do by hand: save the picture, copy the words, open the composer.
  async function shareToLinkedIn(caption, badge) {
    makePoster(badge);                                   // the picture lands in Downloads
    let copied = false;
    try { await navigator.clipboard.writeText(caption); copied = true; } catch (e) { copied = false; }
    const url = 'https://www.linkedin.com/sharing/share-offsite/?url='
      + encodeURIComponent(location.origin + location.pathname);
    window.open(url, '_blank', 'noopener');
    return copied;
  }
  const btShare = document.getElementById('bt-share');
  if (btShare) btShare.addEventListener('click', async () => {
    const p = readProg(), b = lastBadge;
    toast.hidden = true;
    const pic = await makePoster(b);
    openShare({
      title: b ? b.name : 'Badge earned',
      caption: 'I earned the "' + (b ? b.name : 'explorer') + '" badge in the Tanit XR '
        + 'collection: ' + p.seen.length + ' of ' + CFG.items.length + ' Tunisian artifacts, '
        + 'all scanned by volunteers with their phones.',
      link: pageLink(),
      picture: pic,
    });
  });

  // ---- introduce each volunteer once, when you first meet their work
  const cameo = document.getElementById('vol-cameo');
  const cameoPhoto = document.getElementById('vc-photo');
  const cameoLine = document.getElementById('vc-line');
  const cameoLink = document.getElementById('vc-link');
  const metPeople = new Set();
  let cameoTimer = null;
  function showCameo(it) {
    if (roomMode) return;
    const p = it.person;
    if (!cameo || !p || metPeople.has(p.name)) return;
    metPeople.add(p.name);
    clearTimeout(cameoTimer);
    const forSlug = it.slug;                        // remember which object this belongs to
    cameoTimer = setTimeout(() => {
      if (document.body.classList.contains('demoing')) return;
      // if you have scrolled on, this card would name the wrong person for what is on screen
      const now = slots[shown];
      if (!now || now.it.slug !== forSlug) { metPeople.delete(p.name); return; }
      cameoPhoto.src = assetUrl(p.photo);
      cameoPhoto.alt = p.name;
      cameoLine.textContent = 'I ' + p.verb + ' this one.';
      const who = document.getElementById('vc-who');
      if (who) who.textContent = p.name;
      cameoLink.href = linkUrl(p.href);
      // a direct route into that artist's own room, where they have one
      const roomBtn = document.getElementById('vc-room');
      if (roomBtn) {
        const n = CFG.items.filter(x => inRoomOf(x, p.name)).length;
        roomBtn.hidden = n < 2;
        roomBtn.textContent = 'See ' + p.name.split(' ')[0] + "'s room (" + n + ')';
        roomBtn.onclick = () => {
          cameo.hidden = true;
          openRoom(p.name);            // the real room: everything of theirs in one space
        };
      }
      cameoLink.textContent = 'See what else ' + p.name.split(' ')[0] + ' has made';
      cameo.hidden = false;
      if (window.tx) tx('volunteer_cameo', { person: p.name });
    }, 1400);
  }
  // ---- the Save button, its label, and the one-time offer of the scan demo.
  // These definitions were lost in an earlier refactor while their call sites survived,
  // which threw ReferenceError and stopped the scene from ever drawing.
  function paintSave(it) {
    if (!uiSave) return;
    const on = it && it.slug ? readSaved().includes(it.slug) : false;
    uiSave.classList.toggle('on', on);
    uiSave.textContent = on ? 'Saved \u2665' : 'Save \u2661';
  }
  if (uiSave) uiSave.addEventListener('click', () => {
    const s0 = slots[shown];
    if (!s0) return;
    const l = readSaved(), i = l.indexOf(s0.it.slug);
    i >= 0 ? l.splice(i, 1) : l.push(s0.it.slug);
    writeSaved(l);
    paintSave(s0.it);
    paintTray();
    if (i < 0) chime('save');
    bump(p => { p.saved = l.slice(); });
    if (window.tx && i < 0) tx('collection_save', { object: s0.it.slug });
  });

  const shareBtn = document.getElementById('wf-share');
  if (shareBtn) shareBtn.addEventListener('click', async () => {
    const s0 = slots[shown];
    if (!s0) return;
    const pic = await makePoster();
    openShare({
      title: 'Share to protect it',
      caption: s0.it.title + ', scanned in Tunisia by Tanit XR volunteers before it is lost. '
        + 'Share it to help protect it.',
      link: pageLink() + '#' + s0.it.slug,
      picture: pic,
    });
    bump(p => { p.shared++; });
    if (window.tx) tx('collection_share', { object: s0.it.slug });
  });

  // She offers the demo once, after you have turned a few things, and never nags again.
  const OFFERED = 'tanitxr.demoOffered';
  function maybeOfferDemo() {
    let done = false;
    try { done = localStorage.getItem(OFFERED) === '1'; } catch (e) { done = true; }
    if (done || readProg().rotated < 3 || !bubble) return;
    try { localStorage.setItem(OFFERED, '1'); } catch (e) { /* private mode */ }
    bubbleOpen = true;
    bubble.hidden = false;
    if (dot) dot.classList.remove('in');
    if (bubbleText) bubbleText.textContent = 'Want to see how we make these?';
    if (bubbleLong) bubbleLong.hidden = true;
    if (moreBtn) {
      moreBtn.textContent = 'Show me';
      moreBtn.hidden = false;
      moreBtn.classList.add('nb-offer');
      moreBtn.dataset.offer = '1';
    }
    beHappy();
    flare = 1;
  }

  const cameoClose = document.getElementById('vc-close');
  if (cameoClose) cameoClose.addEventListener('click', () => { cameo.hidden = true; });

  // ---- the map: every object as a thumbnail, the one you are on marked, click to jump
  const strip = document.getElementById('filmstrip');
  const stripBtn = document.getElementById('map-toggle');
  let stripBuilt = false;
  function buildStrip() {
    if (!strip || stripBuilt) return;
    stripBuilt = true;
    const frag = document.createDocumentFragment();
    let lastRoom = null;
    CFG.items.forEach((it, i) => {
      const room = it.artist || it.place;
      if (room !== lastRoom) {
        const h = document.createElement('div');
        h.className = 'fs-room'; h.textContent = room;
        frag.appendChild(h); lastRoom = room;
      }
      const b = document.createElement('button');
      b.className = 'fs-item'; b.dataset.i = i; b.title = it.title;
      b.innerHTML = it.thumb ? '<img src="' + assetUrl(it.thumb) + '" alt="' + it.title.replace(/"/g,'') + '">' : '';
      b.addEventListener('click', () => {
        target = i; cursor = i;
        if (sections[i]) scrollTo({ top: midOf(sections[i]), behavior: 'instant' });
        readScroll();
        if (window.tx) tx('map_jump', { object: it.slug });
      });
      frag.appendChild(b);
    });
    strip.appendChild(frag);
  }
  function paintStrip() {
    if (!strip || strip.hidden) return;
    const p = readProg();
    strip.querySelectorAll('.fs-item').forEach(b => {
      const it = CFG.items[+b.dataset.i];
      b.classList.toggle('on', +b.dataset.i === shown);
      b.classList.toggle('seen', p.seen.includes(it.slug));
    });
    const on = strip.querySelector('.fs-item.on');
    if (on) on.scrollIntoView({ inline: 'center', block: 'nearest', behavior: 'smooth' });
  }
  if (stripBtn && strip) stripBtn.addEventListener('click', () => {
    buildStrip();
    strip.hidden = !strip.hidden;
    stripBtn.classList.toggle('on', !strip.hidden);
    paintStrip();
    if (window.tx && !strip.hidden) tx('map_opened');
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
      b.innerHTML = (it.thumb ? '<img src="' + assetUrl(it.thumb) + '" alt="">' : '<img alt="">')
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
    const pic = await makePoster();
    openShare({
      title: 'My collection',
      caption: 'My collection of Tunisian heritage scanned by Tanit XR volunteers, '
        + list.length + ' objects. Share them to help protect them.',
      link: pageLink() + '#saved=' + list.join(','),
      picture: pic,
    });
  });


  const jump = d => {
    if (roomMode) { roomStep(d); return; }
    const i = clamp(Math.round(cursor) + d, 0, sections.length - 1);
    const el = sections[i];
    if (el) scrollTo({ top: midOf(el), behavior: 'smooth' });
  };
  const bindClick = (id, fn) => {
    const el = document.getElementById(id);
    if (el) el.addEventListener('click', fn);
  };
  bindClick('wf-prev', () => jump(-1));
  bindClick('wf-next', () => jump(1));
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

    if (window.tx) tx('collection_poster', { object: s.it.slug });
    return new Promise(res => out.toBlob(b => res({
      blob: b,
      name: 'tanitxr-' + (badge ? 'badge-' + badge.id : s.it.slug) + '.png',
    }), 'image/png'));
  }

  // ---- one share sheet for everything: the picture, the words, and where it can go
  const sheet = document.getElementById('share-sheet');
  const ssPreview = document.getElementById('ss-preview');
  const ssCaption = document.getElementById('ss-caption');
  const ssTitle = document.getElementById('ss-title');
  let ssUrlObj = null;
  function closeSheet() {
    if (!sheet) return;
    sheet.hidden = true;
    if (ssUrlObj) { URL.revokeObjectURL(ssUrlObj); ssUrlObj = null; }
  }
  const ssClose = document.getElementById('ss-close');
  if (ssClose) ssClose.addEventListener('click', closeSheet);
  if (sheet) sheet.addEventListener('click', e => { if (e.target === sheet) closeSheet(); });
  addEventListener('keydown', e => { if (e.key === 'Escape' && sheet && !sheet.hidden) closeSheet(); });

  async function openShare({ title, caption, link, picture }) {
    if (!sheet) return;
    ssTitle.textContent = title || 'Share this';
    ssCaption.textContent = caption;
    if (ssUrlObj) URL.revokeObjectURL(ssUrlObj);
    ssUrlObj = picture && picture.blob ? URL.createObjectURL(picture.blob) : null;
    ssPreview.src = ssUrlObj || '';
    ssPreview.hidden = !ssUrlObj;

    const enc = encodeURIComponent;
    const set = (net, href) => {
      const el = sheet.querySelector('[data-net="' + net + '"]');
      if (el) el.href = href;
    };
    set('linkedin', 'https://www.linkedin.com/sharing/share-offsite/?url=' + enc(link));
    set('facebook', 'https://www.facebook.com/sharer/sharer.php?u=' + enc(link));
    set('x', 'https://twitter.com/intent/tweet?text=' + enc(caption) + '&url=' + enc(link));
    set('whatsapp', 'https://wa.me/?text=' + enc(caption + ' ' + link));

    // the device sheet is the only route that can reach Instagram, so offer it where it exists
    const nativeBtn = sheet.querySelector('[data-net="native"]');
    let file = null;
    if (picture && picture.blob && window.File) {
      try { file = new File([picture.blob], picture.name, { type: 'image/png' }); } catch (e) { file = null; }
    }
    const canFiles = !!(file && navigator.canShare && navigator.canShare({ files: [file] }));
    if (nativeBtn) {
      nativeBtn.hidden = !(navigator.share);
      nativeBtn.onclick = async () => {
        try {
          if (canFiles) await navigator.share({ files: [file], text: caption });
          else await navigator.share({ text: caption, url: link });
        } catch (e) { /* dismissed */ }
      };
    }
    const copyBtn = sheet.querySelector('[data-net="copy"]');
    if (copyBtn) copyBtn.onclick = async () => {
      try { await navigator.clipboard.writeText(caption + '\n' + link);
            copyBtn.textContent = 'Caption copied';
            setTimeout(() => { copyBtn.textContent = 'Copy caption'; }, 1800); } catch (e) { /* denied */ }
    };
    const saveBtn = sheet.querySelector('[data-net="save"]');
    if (saveBtn) {
      saveBtn.hidden = !(picture && picture.blob);
      saveBtn.onclick = () => {
        const a = document.createElement('a');
        a.href = ssUrlObj;
        a.download = picture.name;
        a.click();
      };
    }
    sheet.hidden = false;
    if (window.tx) tx('share_sheet_opened');
  }
  const pageLink = () => location.origin + location.pathname;
  const posterBtn = document.getElementById('wf-poster');
  if (posterBtn) posterBtn.addEventListener('click', async () => {
    const s0 = slots[shown];
    if (!s0) return;
    posterBtn.disabled = true;
    const pic = await makePoster();
    posterBtn.disabled = false;
    openShare({
      title: s0.it.title,
      caption: s0.it.title + ', ' + s0.it.place + (s0.it.size ? ', ' + s0.it.size : '')
        + '. Scanned in Tunisia by Tanit XR volunteers. ' + (s0.it.credit || ''),
      link: pageLink() + '#' + s0.it.slug,
      picture: pic,
    });
  });

  // ---- immersive mode: the same experience as the page, in a headset. One object in front
  // of you at a comfortable size, Nura beside it, the label as a panel in the world. Push
  // the thumbstick, or pull the trigger on empty space, for the next object; squeeze for
  // the one before; hold the trigger on the object and swing to turn it; point at the
  // label and pull to save it; point at Nura and pull to hear her.
  let xrMode = false, xrCursor = 0, xrTarget = 0;
  const XR_EYE = 1.55, XR_DIST = 2.5, XR_SCALE = 0.62;
  const xrRoot = new THREE.Group();
  xrRoot.visible = false;
  scene.add(xrRoot);
  const xrLight = new THREE.DirectionalLight(0xfff3e0, 1.2);
  xrLight.position.set(2, 5, 3);
  xrRoot.add(xrLight);
  // the same warm room as the page: a soft gradient all round and a floor to stand on
  const skyTex = (() => {
    const c = document.createElement('canvas'); c.width = 4; c.height = 256;
    const x = c.getContext('2d');
    const g = x.createLinearGradient(0, 0, 0, 256);
    g.addColorStop(0, '#e6d8c0'); g.addColorStop(0.5, '#f7f1e6'); g.addColorStop(1, '#d6c5a8');
    x.fillStyle = g; x.fillRect(0, 0, 4, 256);
    const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace; return t;
  })();
  xrRoot.add(new THREE.Mesh(new THREE.SphereGeometry(30, 32, 24),
    new THREE.MeshBasicMaterial({ map: skyTex, side: THREE.BackSide })));
  const xrFloor = new THREE.Mesh(new THREE.CircleGeometry(14, 48),
    new THREE.MeshBasicMaterial({ color: 0xe2d3b9 }));
  xrFloor.rotation.x = -Math.PI / 2; xrFloor.position.y = 0.001;
  xrRoot.add(xrFloor);
  const xrShade = new THREE.Mesh(new THREE.PlaneGeometry(5, 5),
    new THREE.MeshBasicMaterial({ map: shadowTex, transparent: true, depthWrite: false }));
  xrShade.rotation.x = -Math.PI / 2; xrShade.position.set(0, 0.004, -XR_DIST);
  xrRoot.add(xrShade);

  // A headset renders only the 3D scene, so the label has to exist as an object in the
  // world. This paints one onto a canvas. With `saved` given it also shows the save state.
  function makeLabel(it, saved) {
    const W = 1024, H = 420;
    const c = document.createElement('canvas');
    c.width = W; c.height = H;
    const x = c.getContext('2d');
    x.fillStyle = 'rgba(253,249,242,0.96)';
    x.strokeStyle = 'rgba(74,53,43,0.25)';
    x.lineWidth = 4;
    const rr = (a, b, w, h, r) => {
      x.beginPath();
      x.moveTo(a + r, b); x.lineTo(a + w - r, b); x.quadraticCurveTo(a + w, b, a + w, b + r);
      x.lineTo(a + w, b + h - r); x.quadraticCurveTo(a + w, b + h, a + w - r, b + h);
      x.lineTo(a + r, b + h); x.quadraticCurveTo(a, b + h, a, b + h - r);
      x.lineTo(a, b + r); x.quadraticCurveTo(a, b, a + r, b); x.closePath();
    };
    rr(6, 6, W - 12, H - 12, 26); x.fill(); x.stroke();
    x.fillStyle = '#8a735c';
    x.font = '600 30px Roboto, Helvetica, Arial, sans-serif';
    x.fillText([it.place, it.size].filter(Boolean).join('   ·   ').toUpperCase(), 44, 84);
    x.fillStyle = '#2e2118';
    let size = 74;
    x.font = '400 ' + size + 'px "Yeseva One", Georgia, serif';
    while (x.measureText(it.title).width > W - 88 && size > 34) {
      size -= 4; x.font = '400 ' + size + 'px "Yeseva One", Georgia, serif';
    }
    x.fillText(it.title, 44, 190);
    x.fillStyle = '#5d4c3c';
    x.font = '400 32px Roboto, Helvetica, Arial, sans-serif';
    const words = (it.credit || '').split(' ');
    let line = '', y = 260;
    for (const w of words) {
      if (x.measureText(line + w + ' ').width > W - 88) { x.fillText(line, 44, y); line = w + ' '; y += 42; }
      else line += w + ' ';
    }
    x.fillText(line, 44, y);
    x.fillStyle = '#a35f3f';
    x.font = '700 28px Roboto, Helvetica, Arial, sans-serif';
    x.fillText('TANIT XR', 44, H - 40);
    if (saved !== undefined) {
      x.textAlign = 'right';
      x.fillStyle = saved ? '#a35f3f' : '#8a735c';
      x.font = '600 26px Roboto, Helvetica, Arial, sans-serif';
      x.fillText(saved ? '♥  SAVED' : 'POINT HERE AND PULL THE TRIGGER TO SAVE', W - 44, H - 40);
      x.textAlign = 'left';
    }
    const tex = new THREE.CanvasTexture(c);
    tex.colorSpace = THREE.SRGBColorSpace;
    return new THREE.Mesh(new THREE.PlaneGeometry(1.06, 0.435),
      new THREE.MeshBasicMaterial({ map: tex, transparent: true }));
  }

  // one label, repainted for each object, hung low and to the left like the page's panel
  let xrLabel = null, xrLabelSlug = null;
  function paintXRLabel(it) {
    if (xrLabel) { xrRoot.remove(xrLabel); xrLabel.material.map.dispose(); xrLabel = null; }
    xrLabel = makeLabel(it, readSaved().includes(it.slug));
    xrLabel.position.set(-0.82, 0.95, -XR_DIST + 0.35);
    xrLabel.rotation.y = 0.32;
    xrLabelSlug = it.slug;
    xrRoot.add(xrLabel);
  }

  // A way to inspect the immersive layout without a headset: ?xrpreview=1 builds the same
  // scene and puts the camera where a standing viewer's eyes would be. Drag to look around.
  const XR_PREVIEW = /[?&]xrpreview=1/.test(location.search);
  let previewYaw = 0;
  const xrCurrent = () => slots[Math.round(clamp(xrCursor, 0, slots.length - 1))];
  function xrStep(n) {
    xrTarget = clamp(Math.round(xrTarget) + n, 0, slots.length - 1);
    if (window.tx) tx('xr_step', { dir: n });
  }
  let xrStickCool = 0;
  function xrPollInput(dt) {
    xrStickCool = Math.max(0, xrStickCool - dt);
    const sess = renderer.xr.getSession();
    if (!sess || xrStickCool > 0) return;
    for (const src of sess.inputSources) {
      const gp = src.gamepad;
      if (!gp || !gp.axes) continue;
      const x = gp.axes[2] || gp.axes[0] || 0, y = gp.axes[3] || gp.axes[1] || 0;
      if (Math.abs(x) > 0.6 || Math.abs(y) > 0.6) {
        xrStep(Math.abs(y) > Math.abs(x) ? (y > 0 ? 1 : -1) : (x > 0 ? 1 : -1));
        xrStickCool = 0.6;
        return;
      }
    }
  }

  function enterXR() {
    xrMode = true;
    document.body.classList.add('in-xr');
    xrRoot.visible = true;
    xrCursor = xrTarget = Math.max(0, shown);
    xrLabelSlug = null;
    if (nuraPanel) { nuraHolder.remove(nuraPanel); nuraPanel = null; }
    if (window.tx) tx('xr_entered', { from: slots[shown] && slots[shown].it.slug });
  }
  function exitXR() {
    xrMode = false;
    document.body.classList.remove('in-xr');
    xrRoot.visible = false;
    xrGrab = null;
    if (xrLabel) { xrRoot.remove(xrLabel); xrLabel = null; xrLabelSlug = null; }
    if (nuraPanel) { nuraHolder.remove(nuraPanel); nuraPanel = null; }
    slots.forEach(s => { s.shadow.material.opacity = 0.8; });
    homeCamera();
    // carry on down the page from the object you were looking at in the headset
    const i = Math.round(clamp(xrCursor, 0, slots.length - 1));
    if (sections[i]) scrollTo({ top: midOf(sections[i]), behavior: 'instant' });
  }

  // Controllers: a visible ray. What the trigger does depends on what it points at.
  const xrCtrl = [], xrRay = new THREE.Raycaster();
  let xrGrab = null;
  function wireXRControllers() {
    for (const i of [0, 1]) {
      const c = renderer.xr.getController(i);
      const line = new THREE.Line(
        new THREE.BufferGeometry().setFromPoints(
          [new THREE.Vector3(0, 0, 0), new THREE.Vector3(0, 0, -1)]),
        new THREE.LineBasicMaterial({ color: 0xffcd05, transparent: true, opacity: 0.75 }));
      line.scale.z = 3;
      c.add(line);
      c.addEventListener('selectstart', () => {
        if (!xrMode) return;
        const hit = xrPick(c);
        if (!hit) { xrStep(1); return; }
        if (hit.kind === 'nura') {
          if (nuraPanel) { nuraHolder.remove(nuraPanel); nuraPanel = null; hushNura(); }
          else { showNuraLine(hit.slot.it); bump(p => { p.more++; }); }
          return;
        }
        if (hit.kind === 'label') {
          if (uiSave) uiSave.click();
          paintXRLabel(hit.slot.it);
          return;
        }
        xrGrab = { slot: hit.slot, ctrl: c, lastYaw: ctrlYaw(c) };
        if (!turned) { turned = true; bump(p => { p.rotated++; }); }
      });
      c.addEventListener('selectend', () => { xrGrab = null; });
      c.addEventListener('squeezestart', () => { if (xrMode) xrStep(-1); });
      xrRoot.add(c);
      xrCtrl.push(c);
    }
  }
  function ctrlYaw(c) {
    const d = new THREE.Vector3(0, 0, -1).applyQuaternion(c.quaternion);
    return Math.atan2(d.x, d.z);
  }
  function xrPick(c) {
    const o = new THREE.Vector3().setFromMatrixPosition(c.matrixWorld);
    const d = new THREE.Vector3(0, 0, -1).applyQuaternion(c.quaternion).normalize();
    xrRay.set(o, d);
    const slot = xrCurrent();
    if (nura && nuraHolder.visible && xrRay.intersectObject(nuraHolder, true).length) return { kind: 'nura', slot };
    if (xrLabel && xrRay.intersectObject(xrLabel).length) return { kind: 'label', slot };
    if (slot && slot.loaded && xrRay.intersectObject(slot.wrap, true).length) return { kind: 'object', slot };
    return null;
  }
  // Nura's line, as a panel above her head, and read aloud if the headset browser allows it
  let nuraPanel = null;
  function showNuraLine(it) {
    if (nuraPanel) { nuraHolder.remove(nuraPanel); nuraPanel = null; }
    const p = makeLabel({ title: it.title, place: it.place, size: it.size, credit: it.hi || '' });
    p.position.set(0, NURA_H * 1.18, 0.02);
    p.scale.setScalar(0.9);
    nuraPanel = p;
    nuraHolder.add(p);
    sayLine(it.hi || it.title, it);
    if (window.tx) tx('xr_pick', { object: it.slug });
  }

  // Only offer this where a headset can actually answer. On a laptop three.js would
  // otherwise render a dead "VR NOT SUPPORTED" chip, which reads as a broken feature.
  if (navigator.xr && navigator.xr.isSessionSupported) {
    navigator.xr.isSessionSupported('immersive-vr').then(ok => {
      if (!ok) return;
      return import('three/addons/webxr/VRButton.js').then(mod => {
        renderer.xr.enabled = true;
        const btn = mod.VRButton.createButton(renderer);
        btn.id = 'vr-button';
        btn.textContent = 'See it in VR';
        document.body.appendChild(btn);
        wireXRControllers();
        renderer.xr.addEventListener('sessionstart', () => { btn.textContent = 'Leave VR'; enterXR(); });
        renderer.xr.addEventListener('sessionend', () => { btn.textContent = 'See it in VR'; exitXR(); });
      });
    }).catch(() => { /* no immersive mode here, the flat page is unaffected */ });
  }

  // ---- gallery room: a small round gallery you stand inside. One maker's pieces on plinths
  // around you, what they modelled on one side and the scans they optimized on the other,
  // warm plaster walls, pools of light on the floor, a card on every plinth. Drag to look
  // around, tap a piece to walk up to it. Built from primitives on purpose: simple, quiet,
  // and a place rather than a menu.
  const roomBar = document.getElementById('room-bar');
  const roomTitle = document.getElementById('room-title');
  const roomCount = document.getElementById('room-count');
  const roomEyebrow = document.getElementById('room-eyebrow');
  const roomPlinths = new THREE.Group();
  scene.add(roomPlinths);
  let roomMode = null, roomFocus = null, roomHover = null;
  const ROOM_SCALE = 1.35 / FIT, ROOM_EYE = 1.55;
  const PL_COL = [0xf1e9db, 0x39647f, 0x3b372c, 0xb4735a];   // plaster, indigo, ink, terracotta
  let roomYaw = 0, roomYawT = 0, roomPitch = 0, roomPitchT = 0, roomOuterR = 6;
  const roomCamPos = new THREE.Vector3(0, ROOM_EYE, 0);

  const glowTex = (() => {
    const c = document.createElement('canvas'); c.width = c.height = 256;
    const x = c.getContext('2d');
    const g = x.createRadialGradient(128, 128, 0, 128, 128, 128);
    g.addColorStop(0, 'rgba(255,241,214,.95)'); g.addColorStop(.5, 'rgba(255,241,214,.35)');
    g.addColorStop(1, 'rgba(255,241,214,0)');
    x.fillStyle = g; x.fillRect(0, 0, 256, 256);
    const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace; return t;
  })();
  const wallTex = (() => {
    const c = document.createElement('canvas'); c.width = 8; c.height = 256;
    const x = c.getContext('2d');
    const g = x.createLinearGradient(0, 0, 0, 256);
    g.addColorStop(0, '#f6efe3'); g.addColorStop(0.55, '#ecdfc9'); g.addColorStop(1, '#d9c7a8');
    x.fillStyle = g; x.fillRect(0, 0, 8, 256);
    const t = new THREE.CanvasTexture(c); t.colorSpace = THREE.SRGBColorSpace; return t;
  })();
  function textPlane(draw, w, h, pxW, pxH) {
    const c = document.createElement('canvas'); c.width = pxW; c.height = pxH;
    draw(c.getContext('2d'), pxW, pxH);
    const tex = new THREE.CanvasTexture(c); tex.colorSpace = THREE.SRGBColorSpace;
    return new THREE.Mesh(new THREE.PlaneGeometry(w, h),
      new THREE.MeshBasicMaterial({ map: tex, transparent: true, depthWrite: false }));
  }
  function roomSign(text, sub) {
    return textPlane((x, W, H) => {
      x.textAlign = 'center';
      x.fillStyle = '#a35f3f'; x.font = '700 46px Roboto, Helvetica, Arial, sans-serif';
      x.fillText(text.toUpperCase().split('').join(' '), W / 2, 74);
      x.fillStyle = '#7d6a58'; x.font = '400 36px Roboto, Helvetica, Arial, sans-serif';
      x.fillText(sub, W / 2, 138);
    }, 3.6, 0.76, 1200, 254);
  }
  function plinthCard(title) {
    return textPlane((x, W, H) => {
      x.fillStyle = 'rgba(253,249,242,.96)'; x.fillRect(0, 0, W, H);
      x.fillStyle = '#2e2118'; x.textAlign = 'center';
      let size = 44; x.font = '400 ' + size + 'px "Yeseva One", Georgia, serif';
      while (x.measureText(title).width > W - 40 && size > 22) { size -= 2; x.font = '400 ' + size + 'px "Yeseva One", Georgia, serif'; }
      x.fillText(title, W / 2, H / 2 + size * 0.36);
    }, 0.62, 0.16, 620, 160);
  }
  // where a piece stands: on the ring at its angle, its bottom on the plinth top
  const ringPos = (R, a, y) => new THREE.Vector3(R * Math.sin(a), y, -R * Math.cos(a));
  const standY = (s, top) => top + ((s.fitH || FIT * 0.6) * ROOM_SCALE) / 2 + 0.01;

  function layoutRoom(list, opts) {
    roomPlinths.clear();
    const who = roomMode.artist, first = who.split(' ')[0];
    const made = list.filter(s => s.it.artist === who);
    const opt = list.filter(s => s.it.artist !== who);
    const order = made.concat(opt);
    roomMode.list = order; roomMode.made = made.length; roomMode.opt = opt.length;
    const n = order.length;
    // one ring up to twelve pieces, two rings beyond; with both kinds present the inner ring
    // holds the modelled work and the outer the optimized scans
    let inner, outer;
    if (n <= 12) { inner = order; outer = []; }
    else if (made.length && opt.length && made.length <= 14) { inner = made; outer = opt; }
    else { inner = order.slice(0, Math.ceil(n / 2)); outer = order.slice(Math.ceil(n / 2)); }
    const rings = [{ items: inner, R: n <= 12 ? 6.2 : 6.6, top: 0.95, col: [0, 1] },
                   { items: outer, R: 10.2, top: 1.25, col: [2, 3] }];
    roomOuterR = outer.length ? 10.2 : 6.2;
    const signAt = [];
    rings.forEach((ring, ri) => {
      const m = ring.items.length; if (!m) return;
      const step = Math.min(2 * Math.PI / m, 2.7 / ring.R);       // never sparser than 2.7 m
      const span = step * (m - 1);
      const start = -span / 2 + (ri === 1 && inner.length ? step / 2 : 0);
      ring.items.forEach((s, k) => {
        const a = start + k * step;
        s.roomAng = a; s.roomR = ring.R; s.roomTop = ring.top;
        const w = 0.82;
        const box = new THREE.Mesh(new THREE.BoxGeometry(w, ring.top, w),
          new THREE.MeshStandardMaterial({ color: PL_COL[ring.col[k % 2]], roughness: 0.7 }));
        box.position.copy(ringPos(ring.R, a, ring.top / 2)); box.rotation.y = -a;
        roomPlinths.add(box);
        const pool = new THREE.Mesh(new THREE.PlaneGeometry(3.6, 3.6),
          new THREE.MeshBasicMaterial({ map: glowTex, transparent: true, depthWrite: false, opacity: 0.75 }));
        pool.rotation.x = -Math.PI / 2; pool.position.copy(ringPos(ring.R, a, 0.004));
        roomPlinths.add(pool);
        const card = plinthCard(s.it.title);
        card.position.copy(ringPos(ring.R - w / 2 - 0.012, a, ring.top - 0.17)); card.rotation.y = -a;
        roomPlinths.add(card);
        s.roomPos = ringPos(ring.R, a, standY(s, ring.top));
        s.roomScale = ROOM_SCALE;
        s.wrap.position.copy(s.roomPos); s.wrap.rotation.y = -a;
        s.wrap.scale.setScalar(ROOM_SCALE); s.wrap.visible = s.loaded;
        s.mats.forEach(mm => { mm.opacity = 1; }); s.shadow.material.opacity = 0;
        if ((made.length && s === made[0]) || (opt.length && s === opt[0])) signAt.push({ s, isMade: s === made[0] && made.length > 0 });
      });
    });
    signAt.forEach(({ s, isMade }) => {
      const cnt = isMade ? made.length : opt.length;
      const sg = roomSign(isMade ? 'Modelled by ' + first : 'Optimized by ' + first,
        cnt + (isMade ? (cnt === 1 ? ' piece' : ' pieces') + ' built from scratch' : (cnt === 1 ? ' scan' : ' scans') + ' made light for the web'));
      sg.position.copy(ringPos(s.roomR + 1.2, s.roomAng, s.roomTop + 2.35)); sg.rotation.y = -s.roomAng;
      roomPlinths.add(sg);
    });
    if (!(opts && opts.hall)) {
      // the room itself: a warm plaster drum, a stone floor, a haze that softens the far side
      const RW = roomOuterR + 3.6;
      const wall = new THREE.Mesh(new THREE.CylinderGeometry(RW, RW, 9, 72, 1, true),
        new THREE.MeshBasicMaterial({ map: wallTex, side: THREE.BackSide }));
      wall.position.y = 4.5; roomPlinths.add(wall);
      const floor = new THREE.Mesh(new THREE.CircleGeometry(RW + 0.05, 72),
        new THREE.MeshStandardMaterial({ color: 0xd6c4a5, roughness: 0.95 }));
      floor.rotation.x = -Math.PI / 2; roomPlinths.add(floor);
      const skirt = new THREE.Mesh(new THREE.CylinderGeometry(RW - 0.01, RW - 0.01, 0.12, 72, 1, true),
        new THREE.MeshBasicMaterial({ color: 0xb59f7e, side: THREE.BackSide }));
      skirt.position.y = 0.06; roomPlinths.add(skirt);
    }
    roomYaw = roomYawT = made.length ? made[0].roomAng : order[0].roomAng;
    roomPitch = roomPitchT = 0;
    roomCamPos.set(0, ROOM_EYE, 0);
  }

  function placeIfInRoom(s) {
    if (!roomMode || !s.roomPos) return;
    s.roomPos.y = standY(s, s.roomTop);
    s.wrap.position.copy(s.roomPos); s.wrap.rotation.y = -s.roomAng;
    s.wrap.scale.setScalar(s.roomScale); s.wrap.visible = true;
    s.mats.forEach(m => { m.opacity = 1; }); s.shadow.material.opacity = 0;
  }
  function paintRoomBar() {
    if (!roomMode) return;
    document.body.classList.toggle('room-focus', !!roomFocus);
    if (roomTitle) roomTitle.textContent = roomMode.artist;
    if (roomEyebrow) roomEyebrow.textContent = roomFocus ? 'Up close' : 'Gallery room';
    if (roomCount) {
      const bits = [];
      if (roomMode.made) bits.push(roomMode.made + ' modelled');
      if (roomMode.opt) bits.push(roomMode.opt + ' optimized');
      roomCount.textContent = bits.join(' · ');
    }
    if (roomFocus) paint(roomFocus.i);
  }
  function setFocus(s) {
    roomFocus = s;
    if (s) { s.pivot.rotation.x = 0; load(s); roomYawT = s.roomAng; roomPitchT = 0; }
    paintRoomBar();
  }
  // the piece nearest to where you are looking, and the one after it in either direction
  function roomNearest() {
    const L = roomMode.list; let best = 0;
    const d = (a, b) => Math.abs(Math.atan2(Math.sin(a - b), Math.cos(a - b)));
    L.forEach((s, k) => { if (d(s.roomAng, roomYawT) < d(L[best].roomAng, roomYawT)) best = k; });
    return best;
  }
  function roomStep(dir) {
    const L = roomMode.list.slice().sort((a, b) => a.roomAng - b.roomAng);
    const cur = L.indexOf(roomMode.list[roomNearest()]);
    const nxt = L[clamp(cur + dir, 0, L.length - 1)];
    if (roomFocus) setFocus(nxt); else { roomYawT = nxt.roomAng; roomPitchT = 0; }
  }

  const inRoomOf = (it, who) => it.artist === who || (it.person && it.person.name === who);
  function openRoom(artist, opts) {
    const list = opts && opts.list ? opts.list : slots.filter(s => inRoomOf(s.it, artist));
    if (!list.length) return;
    if (roomMode) { roomPlinths.clear(); slots.forEach(s => { s.roomPos = null; }); }
    list.forEach(load);
    roomMode = { artist, list };
    roomFocus = null; roomHover = null;
    layoutRoom(list, opts);
    // the page underneath sits at the top while a room is open; leaving the room scrolls
    // back to the piece you were nearest to, so nothing is lost
    scrollTo({ top: 0, behavior: 'instant' });
    scene.fog = new THREE.Fog(0xefe5d4, 9, 34);
    document.body.classList.add('in-room');
    if (roomBar) roomBar.hidden = false;
    paintRoomBar();
    if (cameo) cameo.hidden = true;
    closeBubble();
    if (window.tx) tx('room_opened', { artist });
  }
  function closeRoom() {
    if (!roomMode) return;
    const back = roomFocus || roomMode.list[roomNearest()];
    roomMode = null; roomFocus = null; roomHover = null;
    roomPlinths.clear();
    scene.fog = null;
    document.body.classList.remove('in-room', 'room-focus');
    if (roomBar) roomBar.hidden = true;
    stage.classList.remove('can-pick');
    slots.forEach(s => { s.roomPos = null; s.wrap.rotation.y = 0; });
    homeCamera();
    if (back) jumpTo(x => x.slug === back.it.slug);
  }
  document.querySelectorAll('.room-open').forEach(b =>
    b.addEventListener('click', () => openRoom(b.dataset.artist)));
  const roomBack = document.getElementById('room-back');
  if (roomBack) roomBack.addEventListener('click', () => {
    if (roomFocus) { setFocus(null); return; }
    closeRoom();
  });
  addEventListener('keydown', e => {
    if (!roomMode) return;
    if (e.key === 'Escape') { if (roomFocus) setFocus(null); else closeRoom(); }
  });
  // the wheel turns you round the room instead of scrolling a page that is not there
  addEventListener('wheel', e => {
    if (!roomMode) return;
    e.preventDefault();
    if (roomFocus) return;
    const d = Math.abs(e.deltaX) > Math.abs(e.deltaY) ? e.deltaX : e.deltaY;
    roomYawT += d * 0.0022;
  }, { passive: false });

  function roomHit(e) {
    const r = stage.getBoundingClientRect();
    ndc.set(((e.clientX - r.left) / r.width) * 2 - 1, -((e.clientY - r.top) / r.height) * 2 + 1);
    camera.updateMatrixWorld();
    ray.setFromCamera(ndc, camera);
    const hits = ray.intersectObjects(roomMode.list.filter(s => s.loaded).map(s => s.wrap), true);
    if (!hits.length) return null;
    let n = hits[0].object;
    while (n && !roomMode.list.some(s => s.wrap === n)) n = n.parent;
    return roomMode.list.find(x => x.wrap === n) || null;
  }
  stage.addEventListener('pointermove', e => {
    if (!roomMode || dragging) return;
    roomHover = roomHit(e);
    stage.classList.toggle('can-pick', !!roomHover && roomHover !== roomFocus);
  }, { passive: true });
  // tap a piece to walk up to it, tap another to move on, tap the room to step back
  function pickInRoom(e) {
    const s = roomHit(e);
    if (!s) { if (roomFocus) setFocus(null); return; }
    setFocus(roomFocus === s ? null : s);
    if (roomFocus && window.tx) tx('room_pick', { object: s.it.slug });
  }

  // For curiosity only: ?hall=1 puts the same ring of scans inside Patrick's museum hall
  // instead of the plaster drum. The real museum is a separate project.
  if (/[?&]hall=1/.test(location.search)) {
    const hallList = slots.filter(s => s.it.real).slice(0, 14);
    setTimeout(() => {
      openRoom('Inside the museum hall (preview)', { hall: true, list: hallList });
      loader.load(MODEL_BASE + 'patrick-museum-main-hall.glb', g => {
        const o = g.scene;
        const box = new THREE.Box3().setFromObject(o);
        const size = box.getSize(new THREE.Vector3()), mid = box.getCenter(new THREE.Vector3());
        const k = 38 / Math.max(size.x, size.z);          // the hall as a real building
        o.scale.setScalar(k);
        o.position.set(-mid.x * k, -box.min.y * k, -mid.z * k);
        roomPlinths.add(o);
      });
    }, 600);
  }

  function resize() {
    const w = stage.clientWidth, h = stage.clientHeight;
    renderer.setSize(w, h, false);
    camera.aspect = w / h;
    camera.fov = w < 760 ? 46 : 36;
    camera.updateProjectionMatrix();
    if (!roomMode && !xrMode) homeCamera();
    readScroll();
  }
  addEventListener('resize', resize, { passive: true });
  addEventListener('scroll', readScroll, { passive: true });
  if (!matchMedia('(prefers-reduced-motion: reduce)').matches) {
    document.documentElement.style.scrollSnapType = 'y proximity';
  }
  // a backgrounded tab freezes the animation loop, so re-sync when it comes back
  document.addEventListener('visibilitychange', () => { if (!document.hidden) readScroll(); });
  resize();
  cursor = target;
  load(slots[0]);

  if (XR_PREVIEW) {
    // no headset: hold the same scene and stand where the viewer would stand
    setTimeout(enterXR, 900);
    stage.addEventListener('pointermove', e => {
      if (dragging) previewYaw -= (e.clientX - lastX) * 0.004;
    }, { passive: true });
  }

  // she introduces herself once, so the opening screen does not have to
  const GREETED = 'tanitxr.greeted';
  setTimeout(() => {
    // greet on the first visit, and welcome back on later ones once there is progress to note
    let seenBefore = false;
    try { seenBefore = localStorage.getItem(GREETED) === '1'; } catch (e) { seenBefore = true; }
    const returning = seenBefore && readProg().seen.length > 3;
    if ((seenBefore && !returning) || !bubble || demoOn) return;
    try { localStorage.setItem(GREETED, '1'); } catch (e) { /* private mode */ }
    bubbleOpen = true;
    bubble.hidden = false;
    if (dot) dot.classList.remove('in');
    const prog = readProg();
    const left = CFG.items.length - prog.seen.length;
    if (bubbleText) bubbleText.textContent = prog.seen.length > 3 && left > 0
      ? 'Welcome back. You have seen ' + prog.seen.length + ' so far, ' + left + ' to go.'
      : 'I am Nura. Drag anything to turn it, save the ones you like, and see how many of the '
        + 'six badges you can find.';
    if (bubbleLong) bubbleLong.hidden = true;
    if (moreBtn) { moreBtn.hidden = true; moreBtn.dataset.offer = ''; }
    beHappy();
    flare = 1;
  }, 4200);

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
  let dimK = 1;
  const clock = new THREE.Clock();
  function frame() {
    const dt = Math.min(clock.getDelta(), 0.05);
    if (xrMode) {                                   // the headset owns the camera
      if (XR_PREVIEW) {                             // no headset: stand where a viewer stands
        camera.position.set(0, XR_EYE, 0);
        camera.rotation.set(0, previewYaw, 0);
        camera.fov = 70;
        camera.updateProjectionMatrix();
        camera.updateMatrixWorld();
      }
      xrPollInput(dt);
      xrCursor += (xrTarget - xrCursor) * (reduce ? 1 : 0.1);
      cursor = target = xrCursor;                   // so save, share and Nura agree on the object
      const front = xrCurrent();
      paint(front.i);
      if (xrLabelSlug !== front.it.slug && Math.abs(xrCursor - front.i) < 0.3) paintXRLabel(front.it);
      const te = clock.elapsedTime;
      slots.forEach(s => {
        const d = s.i - xrCursor, ad = Math.abs(d);
        const a = Math.max(0, 1 - ad * 1.3);
        if (ad < 1.6) load(s);
        s.wrap.visible = s.loaded && a > 0.005;
        if (!s.wrap.visible) return;
        // the same rise and settle as the page, in front of you instead of down the screen
        const e = 1 - Math.pow(1 - Math.min(1, ad), 2);
        s.wrap.position.set(0, XR_EYE - 0.3 - Math.sign(d) * e * 2.4, -XR_DIST - e * 2.2);
        s.wrap.scale.setScalar(XR_SCALE * (0.78 + 0.22 * a));
        s.mats.forEach(m => { m.opacity = a; });
        s.shadow.material.opacity = 0;              // the floor carries the shadow in here
        if (!reduce && !xrGrab && ad < 0.5) s.pivot.rotation.y += dt * 0.1;
      });
      xrShade.material.opacity = 0.9;
      if (xrGrab) {                                 // hold the trigger and swing to turn it
        const y = ctrlYaw(xrGrab.ctrl);
        xrGrab.slot.pivot.rotation.y += (y - xrGrab.lastYaw) * 2.2;
        xrGrab.lastYaw = y;
      }
      if (mixer) mixer.update(dt);
      if (nura) {
        nuraHolder.visible = true;
        // beside the object, and she swings round it with you when you turn it
        const swing = clamp(front.pivot.rotation.y * 0.3, -0.65, 0.65);
        const R = 1.0;
        nuraHolder.position.set(Math.cos(swing) * R + Math.sin(te * 0.43) * 0.05,
                                XR_EYE - 1.0 + Math.sin(te * 1.05) * 0.06,
                                -XR_DIST + 0.3 + Math.sin(swing) * R * 0.55);
        // she keeps facing you; at nuraBaseYaw she faces +Z, and you stand at the origin
        nura.rotation.y = nuraBaseYaw + Math.atan2(-nuraHolder.position.x, -nuraHolder.position.z)
                          + Math.sin(te * 0.5) * 0.06;
        nura.rotation.x = 0;
        nura.rotation.z = Math.sin(te * 0.8) * 0.03;
        sparks.children.forEach(m => {
          m.userData.a += dt * m.userData.sp;
          m.position.set(Math.cos(m.userData.a) * m.userData.r,
                         m.userData.y + Math.sin(te * m.userData.sp + m.userData.a) * 0.09,
                         Math.sin(m.userData.a) * m.userData.r * 0.7);
        });
      }
      renderer.render(scene, camera);
      return;
    }
    entryK = Math.min(1, entryK + dt * 0.9);        // a short warm-up, nothing to click
    amb.intensity = LIT.amb * (0.25 + 0.75 * entryK);
    l1.intensity = LIT.l1 * (0.2 + 0.8 * entryK);
    l2.intensity = LIT.l2 * entryK;
    l3.intensity = LIT.l3 * entryK;
    shaft.intensity = 40 * (1 - entryK);
    shaft.target.position.set(0, 0, 0);
    dust.visible = entryK < 0.99;
    dust.children.forEach((m, i) => {
      m.material.opacity = 0.45 * (1 - entryK);
      if (!reduce) m.position.y += Math.sin(clock.elapsedTime * m.userData.s + i) * 0.0009;
    });
    const t = clock.elapsedTime;
    if (roomMode) {
      slots.forEach(s => { s.wrap.visible = false; });
      roomYaw += (roomYawT - roomYaw) * (reduce ? 1 : 0.1);
      roomPitch += (roomPitchT - roomPitch) * (reduce ? 1 : 0.1);
      const F = roomFocus;
      // where you stand: the middle of the room, or two and a half metres from the piece
      const wantPos = F ? ringPos(F.roomR - 2.5, F.roomAng, ROOM_EYE - 0.05) : new THREE.Vector3(0, ROOM_EYE, 0);
      roomCamPos.lerp(wantPos, reduce ? 1 : 0.08);
      camera.position.copy(roomCamPos);
      const wantFov = F ? (narrow() ? 52 : 40) : (narrow() ? 72 : 58);
      if (Math.abs(camera.fov - wantFov) > 0.05) { camera.fov += (wantFov - camera.fov) * 0.1; camera.updateProjectionMatrix(); }
      if (F) camera.lookAt(F.roomPos.x, F.roomPos.y + 0.05, F.roomPos.z);
      else camera.lookAt(roomCamPos.x + Math.sin(roomYaw) * Math.cos(roomPitch),
                         roomCamPos.y + Math.sin(roomPitch) - 0.08,
                         roomCamPos.z - Math.cos(roomYaw) * Math.cos(roomPitch));
      roomMode.list.forEach(s => {
        if (!s.loaded || !s.roomPos) return;
        s.wrap.visible = true;
        const isF = F === s, isH = roomHover === s && !F;
        const sc = isF ? s.roomScale * 1.06 : (isH ? s.roomScale * 1.05 : s.roomScale);
        s.wrap.scale.lerp(new THREE.Vector3(sc, sc, sc), 0.12);
        s.mats.forEach(m => { m.opacity = 1; });
        s.shadow.material.opacity = 0;
        if (!reduce && (isF || isH)) s.pivot.rotation.y += dt * (isF ? 0.16 : 0.3);
        else if (!isF && Math.abs(s.pivot.rotation.y) > 0.001 && !dragging) s.pivot.rotation.y *= 0.9;
      });
      if (mixer) mixer.update(dt);
      if (nuraHolder) nuraHolder.visible = false;
      renderer.render(scene, camera);
      return;
    }
    if (nuraHolder) nuraHolder.visible = true;
    cursor += (target - cursor) * (reduce ? 1 : 0.12);
    if (!dragging) idle += dt;
    paint(Math.round(clamp(cursor, 0, slots.length - 1)));
    const headingOn = !!document.querySelector('.warea.on');
    dimK += ((headingOn ? 0.3 : 1) - dimK) * (reduce ? 1 : 0.1);

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
      s.mats.forEach(m => { m.opacity = a * dimK; });
      s.shadow.material.opacity = a * 0.8 * dimK;
      if (!reduce && !dragging && idle > 2.2 && ad < 0.5) s.pivot.rotation.y += dt * 0.14;
    });

    scanTarget = demoOn ? 1 : 0;
    scanT += (scanTarget - scanT) * (reduce ? 1 : 0.1);
    demo.visible = scanT > 0.01;
    document.body.classList.toggle('demoing', scanT > 0.5);
    if (demo.visible) {
      demo.scale.setScalar(1.0);
      demo.position.set(0, 0, 0);                    // centred on the object you are viewing
      demo.children.forEach(ch => {
        if (ch.material && ch.material.isLineDashedMaterial) ch.material.opacity = 0.9 * scanT;
      });

      // one full circle per pass, stepping up a ring each time
      const per = 5.0;
      const loop = (t % (per * RINGS.length)) / per;
      const ring = Math.floor(loop) % RINGS.length;
      const a2 = (loop % 1) * Math.PI * 2;
      const y = RINGS[ring];
      demoAngle = a2; demoY = y;
      if (phone) {
        phone.position.set(Math.cos(a2) * 1.75, y, Math.sin(a2) * 1.75);
        phone.lookAt(0, y * 0.45, 0);
        phone.visible = scanT > 0.15;
      }
    }
    if (mixer) mixer.update(dt);
    if (nura) {
      // park her a fixed fraction across the frame, so she is never cut off
      const halfH = Math.tan(camera.fov * Math.PI / 360) * camera.position.z;
      const halfW = halfH * camera.aspect;
      ptr.x += (ptr.tx - ptr.x) * 0.06;
      ptr.y += (ptr.ty - ptr.y) * 0.06;
      // on a phone she is smaller and sits low on the right, beside the object's foot
      const ph = narrow();
      nuraHolder.scale.setScalar(ph ? 0.52 : 1);
      const homeX = ph ? halfW * 0.62 : clamp(halfW * 0.52, 1.0, 2.9);
      // when you turn the object, she swings around it with you, within a comfortable arc
      const frontObj = slots[shown];
      const spin = frontObj ? frontObj.pivot.rotation.y : 0;
      const swing = clamp(spin * 0.3, -0.65, 0.65);
      const hx = Math.cos(swing) * homeX + Math.sin(t * 0.43) * 0.07 + ptr.x * 0.16;
      const hz = (ph ? 0.2 : 0.9) + Math.sin(swing) * homeX * 0.55;
      const hy = (ph ? camera.position.y - halfH * 0.36 : -halfH * 0.16) + Math.sin(t * 1.05) * 0.075 - ptr.y * 0.1;
      if (scanT > 0.05) {
        // she flies the circle herself, just behind the phone, and shows you how
        const R = 1.75 * (demo.scale.x || 1) + 0.7;
        const ox = demo.position.x + Math.cos(demoAngle - 0.42) * R;
        const oz = demo.position.z + Math.sin(demoAngle - 0.42) * R;
        const oy = demo.position.y + demoY * (demo.scale.y || 1) + 0.1;
        nuraHolder.position.x += ((1 - scanT) * hx + scanT * ox - nuraHolder.position.x) * 0.12;
        nuraHolder.position.y += ((1 - scanT) * hy + scanT * oy - nuraHolder.position.y) * 0.12;
        nuraHolder.position.z += ((1 - scanT) * hz + scanT * oz - nuraHolder.position.z) * 0.12;
      } else {
        nuraHolder.position.x += (hx - nuraHolder.position.x) * 0.1;
        nuraHolder.position.y += (hy - nuraHolder.position.y) * 0.14;
        nuraHolder.position.z += (hz - nuraHolder.position.z) * 0.1;
      }
      // she looks at the new object for a moment, then back at you and your cursor
      glance = Math.max(0, glance - dt);
      const look = Math.min(1, glance) * 0.75;
      if (scanT > 0.5) {
        // turn inward and watch the object as she circles it.
        // At yaw = nuraBaseYaw she faces +Z, which is the camera, so the yaw that points
        // her at a target is simply that base plus the bearing to it.
        const dx = demo.position.x - nuraHolder.position.x;
        const dz = demo.position.z - nuraHolder.position.z;
        const want = nuraBaseYaw + Math.atan2(dx, dz);
        let diff = want - nura.rotation.y;
        while (diff > Math.PI) diff -= Math.PI * 2;
        while (diff < -Math.PI) diff += Math.PI * 2;
        nura.rotation.y += diff * 0.16;
      } else {
        nura.rotation.y = nuraBaseYaw + ptr.x * 0.5 + Math.sin(t * 0.5) * 0.06 + look
                          - clamp((frontObj ? frontObj.pivot.rotation.y : 0) * 0.3, -0.65, 0.65);
      }
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
  }
  // An exception inside setAnimationLoop silently kills the loop, so never let one escape.
  let loopFault = null;
  renderer.setAnimationLoop(() => {
    try { frame(); }
    catch (e) {
      if (!loopFault) { loopFault = e; console.error('walk: frame failed', e); }
    }
  });


  const io = new IntersectionObserver(es => es.forEach(e =>
    e.target.classList.toggle('on', e.isIntersecting && e.intersectionRatio > 0.5)),
    { threshold: [0, 0.5, 1] });
  document.querySelectorAll('.wst-intro,.wst-end,.warea').forEach(s => io.observe(s));
}
