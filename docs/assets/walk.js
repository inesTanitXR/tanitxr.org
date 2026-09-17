// Tanit XR - The Collection.
// You walk forward through a line of rooms, passing under a horseshoe arch into each one.
// Objects stand at their real size relative to each other, with a 1.7 m figure for scale.
// Flat pieces such as mosaics hang on the side walls. Whitewash, Sidi Bou Said blue, sand.
import * as THREE from 'three';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';
import { MeshoptDecoder } from 'three/addons/libs/meshopt_decoder.module.js';

const CFG = window.WALK_CFG || { clusters: [] };
const MODEL_BASE = new URL('models/', import.meta.url).href;
const stage = document.getElementById('walk-stage');
const canvas = document.getElementById('walk-canvas');
const hintEl = document.getElementById('walk-hint');
const areaEls = [...document.querySelectorAll('.warea[data-c]')];

function useFallback() {
  document.body.classList.add('walk-fallback');
  document.querySelectorAll('.wst-fallback').forEach(el => { el.hidden = false; });
}
let gl = null;
try { gl = canvas.getContext('webgl2') || canvas.getContext('webgl'); } catch (e) { gl = null; }
if (!gl || !CFG.clusters.length) { useFallback(); } else { start(); }

function start() {
  const ROOM = 17, HALF = 6.4, WALL_H = 6.8, EYE = 1.62;
  const WHITEWASH = 0xf1e9db, BLUE = 0x39647f, SAND = 0xd9c7a6, OLIVE = 0x3b372c;
  const clamp = (v, a, b) => Math.min(b, Math.max(a, v));
  const roomZ = ci => -ci * ROOM;                       // front edge of a room
  const nRooms = CFG.clusters.length;

  const renderer = new THREE.WebGLRenderer({ canvas, antialias: true });
  renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
  renderer.outputColorSpace = THREE.SRGBColorSpace;
  renderer.toneMapping = THREE.ACESFilmicToneMapping;
  renderer.toneMappingExposure = 1.12;
  renderer.shadowMap.enabled = true;
  renderer.shadowMap.type = THREE.PCFSoftShadowMap;

  const scene = new THREE.Scene();
  scene.background = new THREE.Color(0xe7ddc9);
  scene.fog = new THREE.Fog(0xe7ddc9, ROOM * 1.4, ROOM * 3.4);
  const camera = new THREE.PerspectiveCamera(46, 1, 0.1, 400);

  // low ambient so the light pools on the objects read as sunlight, not flat fill
  scene.add(new THREE.AmbientLight(0xdfe8ee, 0.55));
  const sun = new THREE.DirectionalLight(0xfff0d4, 1.5);
  sun.position.set(-9, 14, 6);
  sun.castShadow = true;
  sun.shadow.mapSize.set(2048, 2048);
  Object.assign(sun.shadow.camera,
    { near: 1, far: 70, left: -14, right: 14, top: 14, bottom: -14 });
  sun.shadow.camera.updateProjectionMatrix();
  sun.shadow.bias = -0.0009;
  const sunHolder = new THREE.Group();
  sunHolder.add(sun, sun.target);
  scene.add(sunHolder);

  // ---- whitewashed plaster, with the shadow of a carved screen raking across it
  function plaster(scale) {
    const W = 512;
    const c = document.createElement('canvas'); c.width = c.height = W;
    const x = c.getContext('2d');
    x.fillStyle = '#f4ecdf'; x.fillRect(0, 0, W, W);
    for (let i = 0; i < 1400; i++) {
      x.fillStyle = `rgba(${192 + Math.random() * 40},${178 + Math.random() * 40},${154 + Math.random() * 40},.12)`;
      x.fillRect(Math.random() * W, Math.random() * W, 2, 2);
    }
    const lat = document.createElement('canvas'); lat.width = lat.height = W;
    const l = lat.getContext('2d');
    const step = 74, r = 20;
    l.fillStyle = 'rgba(74,58,40,.14)';
    for (let gy = -1; gy < W / step + 2; gy++) {
      for (let gx = -1; gx < W / step + 2; gx++) {
        const cx = gx * step + (gy % 2 ? step / 2 : 0), cy = gy * step;
        for (const rot of [0, Math.PI / 4]) {
          l.save(); l.translate(cx, cy); l.rotate(rot);
          l.beginPath();
          l.rect(-r, -r * 0.4, r * 2, r * 0.8);
          l.rect(-r * 0.4, -r, r * 0.8, r * 2);
          l.fill(); l.restore();
        }
      }
    }
    x.save(); x.transform(1, 0.3, 0, 1, -80, -90);
    x.globalAlpha = 0.6; x.filter = 'blur(2px)';
    x.drawImage(lat, 0, 0);
    x.restore();
    const t = new THREE.CanvasTexture(c);
    t.wrapS = t.wrapT = THREE.RepeatWrapping;
    t.repeat.set(scale, scale);
    t.colorSpace = THREE.SRGBColorSpace;
    return t;
  }
  const wallMat = new THREE.MeshStandardMaterial({ map: plaster(2), color: WHITEWASH, roughness: .97 });
  const floorMat = new THREE.MeshStandardMaterial({ map: plaster(14), color: SAND, roughness: 1 });

  const depth = nRooms * ROOM + 30;
  const floor = new THREE.Mesh(new THREE.PlaneGeometry(HALF * 2, depth), floorMat);
  floor.rotation.x = -Math.PI / 2;
  floor.position.z = -depth / 2 + ROOM / 2;
  floor.receiveShadow = true;
  scene.add(floor);
  [-HALF, HALF].forEach(x => {
    const w = new THREE.Mesh(new THREE.PlaneGeometry(depth, WALL_H), wallMat);
    w.rotation.y = x < 0 ? Math.PI / 2 : -Math.PI / 2;
    w.position.set(x, WALL_H / 2, -depth / 2 + ROOM / 2);
    w.receiveShadow = true;
    scene.add(w);
  });

  // a horseshoe arch cut out of a cross wall
  function archWall(w, h, aw, ah) {
    const shape = new THREE.Shape();
    shape.moveTo(-w / 2, 0); shape.lineTo(-w / 2, h);
    shape.lineTo(w / 2, h); shape.lineTo(w / 2, 0); shape.closePath();
    const hole = new THREE.Path();
    const r = aw / 2, spring = ah - r * 1.15;
    hole.moveTo(-r, 0); hole.lineTo(-r, spring);
    hole.absarc(0, spring, r, Math.PI, 0, true);
    hole.lineTo(r, 0); hole.closePath();
    shape.holes.push(hole);
    const geo = new THREE.ExtrudeGeometry(shape, { depth: 0.5, bevelEnabled: false });
    geo.translate(0, 0, -0.25);
    return geo;
  }

  const specks = new THREE.Group();
  for (let i = 0; i < 80; i++) {
    const m = new THREE.Mesh(new THREE.SphereGeometry(0.014 + Math.random() * 0.026, 6, 5),
      new THREE.MeshStandardMaterial({ color: 0xe6d6b8, roughness: 1 }));
    m.position.set((Math.random() - 0.5) * 11, Math.random() * 4 + 0.5,
                   -Math.random() * depth + ROOM / 2);
    m.userData.s = 0.12 + Math.random() * 0.3;
    specks.add(m);
  }
  scene.add(specks);

  const loader = new GLTFLoader().setMeshoptDecoder(MeshoptDecoder);
  const slots = [], roomGroups = [];

  CFG.clusters.forEach((cl, ci) => {
    const zFront = roomZ(ci), zBack = zFront - ROOM;
    const g = new THREE.Group();
    scene.add(g);
    roomGroups.push(g);

    const heightOf = it => (it.real && it.dims ? Math.max(it.dims[1], 0.05) : 0.45);
    const isFlat = it => it.real && it.dims && it.dims[1] < 0.15 &&
                         Math.max(it.dims[0], it.dims[2]) > 0.4;
    const tallest = Math.max(...cl.items.map(it => isFlat(it) ? 1.4 : heightOf(it)), 0.6);
    const RS = clamp(3.6 / tallest, 0.24, 1.9);

    // the cross wall you walk through to leave this room
    const cross = new THREE.Mesh(archWall(HALF * 2, WALL_H, 3.4, 4.9), wallMat);
    cross.position.set(0, 0, zBack);
    cross.castShadow = cross.receiveShadow = true;
    g.add(cross);
    // painted reveal inside the arch, so the next room reads as a separate space
    const reveal = new THREE.Mesh(new THREE.BoxGeometry(HALF * 2, WALL_H, 0.1),
      new THREE.MeshStandardMaterial({ color: ci % 3 === 1 ? BLUE : WHITEWASH,
                                       roughness: 0.9, transparent: true, opacity: 0.0 }));
    reveal.position.set(0, WALL_H / 2, zBack - 0.3);
    g.add(reveal);

    const flats = cl.items.filter(isFlat);
    const standing = cl.items.filter(it => !isFlat(it));

    // standing pieces alternate left and right down the room, spaced by real footprint
    const foot = it => ((it.real && it.dims ? Math.max(it.dims[0], it.dims[2]) : 0.45) * RS) + 1.5;
    let zL = zFront - 4.2, zR = zFront - 6.6;
    let si = 0;

    cl.items.forEach(it => {
      const h = heightOf(it) * RS;
      const wrap = new THREE.Group();
      const pivot = new THREE.Group();
      wrap.add(pivot);
      wrap.visible = false;
      let lookAtY = h * 0.5;

      if (isFlat(it)) {                                  // hang it on a side wall
        const n = flats.indexOf(it);
        const left = n % 2 === 0;
        const z = zFront - 5 - Math.floor(n / 2) * 4.4;
        wrap.position.set(left ? -HALF + 0.35 : HALF - 0.35, 2.35, z);
        wrap.rotation.y = left ? Math.PI / 2 : -Math.PI / 2;
        wrap.userData.flat = true;
        const surround = new THREE.Mesh(new THREE.BoxGeometry(2.4, 2.4, 0.14),
          new THREE.MeshStandardMaterial({ color: WHITEWASH, roughness: 0.55 }));
        surround.position.copy(wrap.position);
        surround.rotation.y = wrap.rotation.y;
        surround.translateZ(-0.14);
        surround.castShadow = true;
        g.add(surround);
        lookAtY = 0;
      } else {
        const left = si % 2 === 0;
        const w = foot(it);
        const z = left ? (zL -= w * 0.62) : (zR -= w * 0.62);
        const x = left ? -HALF + 1.9 + (si % 3) * 0.35 : HALF - 1.9 - (si % 3) * 0.35;
        const ph = clamp(1.35 * RS - h * 0.6, 0.05, 1.45 * RS);
        if (ph > 0.12) {
          const kind = ['white', 'blue', 'olive', 'white', 'cyl'][si % 5];
          const pw = kind === 'cyl' ? 0.82 : 0.86 + ((si * 3) % 3) * 0.16;
          const p = new THREE.Mesh(
            kind === 'cyl' ? new THREE.CylinderGeometry(pw / 2, pw / 2, ph, 44)
                           : new THREE.BoxGeometry(pw, ph, pw),
            new THREE.MeshStandardMaterial({
              color: kind === 'blue' ? BLUE : kind === 'olive' ? OLIVE : WHITEWASH,
              roughness: kind === 'white' ? 0.55 : 0.75 }));
          p.position.set(x, ph / 2, z);
          p.castShadow = p.receiveShadow = true;
          g.add(p);
        }
        wrap.position.set(x, Math.max(ph, 0), z);
        wrap.rotation.y = left ? 0.45 : -0.45;            // angle it toward the walkway
        // a pool of sunlight on each piece
        const spot = new THREE.SpotLight(0xfff3dc, 26, 9, Math.PI / 7, 0.55, 1.4);
        spot.position.set(x * 0.55, 5.4, z + 1.1);
        spot.target.position.set(x, ph + h * 0.5, z);
        g.add(spot, spot.target);
        si++;
      }
      g.add(wrap);
      slots.push({ it, wrap, pivot, ci, dispH: h, flat: isFlat(it), lookAtY,
                   z: wrap.position.z, mats: [], loaded: false, loading: false });
    });

    // a 1.7 m figure standing in the walkway, so real size reads at a glance
    const figH = 1.7 * RS;
    const figMat = new THREE.MeshStandardMaterial({ color: 0xc3b49b, roughness: 1,
                                                    transparent: true, opacity: 0.32 });
    const fig = new THREE.Group();
    const body = new THREE.Mesh(new THREE.CapsuleGeometry(figH * .112, figH * .5, 6, 14), figMat);
    body.position.y = figH * 0.42;
    const head = new THREE.Mesh(new THREE.SphereGeometry(figH * .08, 16, 12), figMat);
    head.position.y = figH * 0.91;
    fig.add(body, head);
    fig.position.set(1.5, 0, zFront - 3.0);
    g.add(fig);
  });

  function load(s) {
    if (!s || s.loaded || s.loading) return;
    s.loading = true;
    loader.load(MODEL_BASE + s.it.slug + '.glb', (gltf) => {
      const o = gltf.scene;
      o.updateMatrixWorld(true);
      const box = new THREE.Box3().setFromObject(o);
      const size = box.getSize(new THREE.Vector3());
      const mid = box.getCenter(new THREE.Vector3());
      const fit = new THREE.Group();
      fit.add(o);
      if (s.flat) {
        o.position.set(-mid.x, -mid.y, -mid.z);
        fit.rotation.x = -Math.PI / 2;                   // stand a pavement up to face the room
        fit.scale.setScalar(2.0 / (Math.max(size.x, size.z) || 1));
      } else {
        o.position.set(-mid.x, -box.min.y, -mid.z);
        fit.scale.setScalar(s.dispH / (size.y || 1));
      }
      if (s.it.rotate) {
        const r = s.it.rotate;
        fit.rotation.set((r[0] || 0) * Math.PI / 180, (r[1] || 0) * Math.PI / 180,
                         (r[2] || 0) * Math.PI / 180);
      }
      o.traverse(n => {
        if (!n.isMesh || !n.material) return;
        n.castShadow = n.receiveShadow = true;
        // scans are unlit with light baked into the texture; relighting them without
        // normals renders them black, so leave unlit materials as they are
        if (!n.material.isMeshBasicMaterial && !n.geometry.attributes.normal) {
          n.geometry.computeVertexNormals();
        }
        s.mats.push(n.material);
      });
      s.pivot.add(fit);
      s.wrap.visible = true;
      s.loaded = true; s.loading = false;
    }, undefined, () => {
      s.loading = false;
      const fb = document.querySelector('.warea[data-c="' + s.ci + '"] .wst-fallback');
      if (fb) fb.hidden = false;
    });
  }

  // ---- scroll walks you forward; each room is entered as you reach its card
  let camZv = ROOM * 0.5, targetZ = ROOM * 0.5, keys = [];
  const midOf = el => el.offsetTop + el.offsetHeight / 2 - innerHeight / 2;
  function buildKeys() {
    keys = [];
    const intro = document.querySelector('.wst-intro');
    if (intro) keys.push({ s: midOf(intro), z: ROOM * 0.62 });
    areaEls.forEach(el => keys.push({ s: midOf(el), z: roomZ(+el.dataset.c) - ROOM * 0.42 }));
    const end = document.querySelector('.wst-end');
    if (end) keys.push({ s: midOf(end), z: roomZ(nRooms - 1) - ROOM * 1.1 });
    keys.sort((a, b) => a.s - b.s);
  }
  const ease = t => t * t * (3 - 2 * t);
  function readScroll() {
    if (!keys.length || focused) return;
    const y = scrollY;
    if (y <= keys[0].s) targetZ = keys[0].z;
    else if (y >= keys[keys.length - 1].s) targetZ = keys[keys.length - 1].z;
    else for (let i = 0; i < keys.length - 1; i++) {
      const a = keys[i], b = keys[i + 1];
      if (y >= a.s && y <= b.s) { targetZ = a.z + (b.z - a.z) * ease((y - a.s) / (b.s - a.s || 1)); break; }
    }
    slots.forEach(s => { if (Math.abs(s.z - targetZ) < ROOM * 1.8) load(s); });
  }

  // ---- focus: the camera walks over to the object you pick
  const ui = document.getElementById('walk-focus');
  const uiTitle = document.getElementById('wf-title');
  const uiId = document.getElementById('wf-id');
  const uiSave = document.getElementById('wf-save');
  const uiRecord = document.getElementById('wf-record');
  let focused = null, mode = 'scroll', fly = null;
  const camPos = new THREE.Vector3(0, EYE, ROOM * 0.5);
  const camAim = new THREE.Vector3(0, EYE - 0.1, -ROOM);
  const easeInOut = t => t < .5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2;
  const _w = new THREE.Vector3();

  function shotFor(s) {
    s.wrap.getWorldPosition(_w);
    const aim = _w.clone().add(new THREE.Vector3(0, s.flat ? 0 : s.dispH * 0.45, 0));
    const back = 1.9 + Math.max(s.dispH, 1.0) * 1.05;
    const dir = s.flat ? new THREE.Vector3(Math.sign(-_w.x) * back, 0.25, 0.1)
                       : new THREE.Vector3(-Math.sign(_w.x) * back * 0.45, 0.22, back);
    return { p: aim.clone().add(dir), t: aim };
  }
  const scrollShot = () => ({ p: new THREE.Vector3(0, EYE, camZv),
                              t: new THREE.Vector3(0, EYE - 0.1, camZv - ROOM) });
  function startFly(to, dur, then) {
    fly = { from: { p: camPos.clone(), t: camAim.clone() }, to, k: 0, dur: dur || .85, then };
    mode = 'flying';
  }
  const SAVED = 'tanitxr.saved';
  const readSaved = () => { try { return JSON.parse(localStorage.getItem(SAVED) || '[]'); }
                            catch (e) { return []; } };
  function paintSave() {
    if (!uiSave || !focused) return;
    const on = readSaved().includes(focused.it.slug);
    uiSave.classList.toggle('on', on);
    uiSave.textContent = on ? 'Saved ♥' : 'Save ♡';
  }
  function openFocus(s, dur) {
    if (!s || !s.loaded) return;
    const first = !focused;
    focused = s;
    if (ui) ui.hidden = false;
    document.body.classList.add('focusing');
    if (uiTitle) uiTitle.textContent = s.it.title;
    if (uiId) uiId.textContent = [s.it.place, s.it.size].filter(Boolean).join(' · ');
    if (uiRecord) uiRecord.href = s.it.href || 'archive.html';
    paintSave();
    startFly(shotFor(s), dur || (first ? .95 : .7), 'focus');
    history.replaceState(null, '', '#' + s.it.slug);
  }
  function closeFocus() {
    if (!focused) return;
    focused = null;
    if (ui) ui.hidden = true;
    document.body.classList.remove('focusing');
    startFly(scrollShot(), .8, 'scroll');
    history.replaceState(null, '', location.pathname);
  }
  function step(dir) {
    if (!focused) return;
    const i = slots.indexOf(focused);
    for (let k = 1; k <= slots.length; k++) {
      const n = slots[(i + dir * k + slots.length * 2) % slots.length];
      if (!n) continue;
      load(n);
      if (n.loaded) { openFocus(n, .7); return; }
    }
  }
  const on = (id, fn) => { const el = document.getElementById(id); if (el) el.addEventListener('click', fn); };
  on('wf-back', () => closeFocus());
  on('wf-prev', () => step(-1));
  on('wf-next', () => step(1));
  on('wf-save', () => {
    if (!focused) return;
    const l = readSaved(), i = l.indexOf(focused.it.slug);
    i >= 0 ? l.splice(i, 1) : l.push(focused.it.slug);
    try { localStorage.setItem(SAVED, JSON.stringify(l)); } catch (e) { /* private mode */ }
    paintSave();
  });
  on('wf-share', async () => {
    if (!focused) return;
    const url = location.origin + location.pathname + '#' + focused.it.slug;
    const text = focused.it.title + ', scanned in Tunisia by Tanit XR volunteers. '
      + 'Share it to help protect it.';
    const btn = document.getElementById('wf-share');
    try {
      if (navigator.share) await navigator.share({ title: focused.it.title, text, url });
      else {
        await navigator.clipboard.writeText(url);
        btn.textContent = 'Link copied';
        setTimeout(() => { btn.textContent = 'Share to protect it'; }, 2000);
      }
    } catch (e) { /* dismissed */ }
  });
  addEventListener('keydown', e => {
    if (!focused) return;
    if (e.key === 'Escape') closeFocus();
    if (e.key === 'ArrowLeft') step(-1);
    if (e.key === 'ArrowRight') step(1);
  });

  // ---- drag to turn, click to walk over
  let dragging = false, lastX = 0, idle = 0, downX = 0, downY = 0, pressed = false;
  const ray = new THREE.Raycaster(), ndc = new THREE.Vector2();
  function nearest() {
    let best = null, bd = Infinity;
    slots.forEach(s => {
      if (!s.loaded) return;
      const d = Math.abs(s.z - (camPos.z - 4));
      if (d < bd) { bd = d; best = s; }
    });
    return bd < 7 ? best : null;
  }
  stage.addEventListener('pointerdown', e => {
    dragging = true; pressed = true; idle = 0;
    lastX = downX = e.clientX; downY = e.clientY;
    stage.classList.add('grabbing');
    if (hintEl) hintEl.classList.add('gone');
  });
  addEventListener('pointermove', e => {
    if (!dragging) return;
    const s = focused || nearest();
    if (s) {
      if (s.flat) s.pivot.rotation.z = clamp(s.pivot.rotation.z - (e.clientX - lastX) * .006, -.5, .5);
      else s.pivot.rotation.y += (e.clientX - lastX) * .01;   // a turntable, it cannot tip over
    }
    lastX = e.clientX;
  }, { passive: true });
  const stopDrag = () => { dragging = false; stage.classList.remove('grabbing'); };
  addEventListener('pointerup', stopDrag);
  addEventListener('pointercancel', stopDrag);
  stage.addEventListener('pointerup', e => {
    if (!pressed) return;
    pressed = false;
    if (Math.abs(e.clientX - downX) > 5 || Math.abs(e.clientY - downY) > 5) return;
    if (focused) return;
    const r = stage.getBoundingClientRect();
    ndc.set(((e.clientX - r.left) / r.width) * 2 - 1, -((e.clientY - r.top) / r.height) * 2 + 1);
    ray.setFromCamera(ndc, camera);
    const hits = ray.intersectObjects(slots.filter(s => s.loaded).map(s => s.wrap), true);
    if (!hits.length) return;
    let n = hits[0].object;
    while (n && !slots.some(s => s.wrap === n)) n = n.parent;
    const s = slots.find(x => x.wrap === n);
    if (s) openFocus(s);
  });

  function resize() {
    const w = stage.clientWidth, h = stage.clientHeight;
    renderer.setSize(w, h, false);
    camera.aspect = w / h;
    camera.fov = w < 760 ? 60 : 46;
    camera.updateProjectionMatrix();
    buildKeys();
    readScroll();
  }
  addEventListener('resize', resize, { passive: true });
  addEventListener('scroll', readScroll, { passive: true });
  resize();
  camZv = targetZ;
  load(slots[0]);

  const wanted = decodeURIComponent(location.hash.slice(1));
  if (wanted) {
    const s = slots.find(x => x.it.slug === wanted);
    if (s) {
      load(s);
      const t = setInterval(() => { if (s.loaded) { clearInterval(t); openFocus(s, .6); } }, 120);
      setTimeout(() => clearInterval(t), 15000);
    }
  }

  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const clock = new THREE.Clock();
  (function frame() {
    const dt = Math.min(clock.getDelta(), .05);
    camZv += (targetZ - camZv) * (reduce ? 1 : .08);
    if (!dragging) idle += dt;

    if (mode === 'flying') {
      fly.k = Math.min(1, fly.k + dt / fly.dur);
      const k = easeInOut(fly.k);
      camPos.lerpVectors(fly.from.p, fly.to.p, k);
      camAim.lerpVectors(fly.from.t, fly.to.t, k);
      if (fly.k >= 1) mode = fly.then === 'focus' ? 'focused' : 'scroll';
    } else if (mode === 'focused' && focused) {
      const sh = shotFor(focused);
      camPos.lerp(sh.p, .12); camAim.lerp(sh.t, .12);
    } else {
      camPos.set(0, EYE, camZv);
      camAim.set(0, EYE - 0.12, camZv - ROOM);
    }
    camera.position.copy(camPos);
    camera.lookAt(camAim);
    sunHolder.position.z = camPos.z;

    if (!reduce) {
      const n = focused || nearest();
      if (n && !dragging && idle > 2.4 && !n.flat) n.pivot.rotation.y += dt * .12;
      specks.children.forEach((m, i) => {
        m.position.y += Math.sin(clock.elapsedTime * m.userData.s + i) * .0012;
      });
    }
    renderer.render(scene, camera);
    requestAnimationFrame(frame);
  })();

  const io = new IntersectionObserver(es => es.forEach(e =>
    e.target.classList.toggle('on', e.isIntersecting && e.intersectionRatio > .4)),
    { threshold: [0, .4, 1] });
  document.querySelectorAll('.warea,.wst-intro,.wst-end').forEach(s => io.observe(s));
}
