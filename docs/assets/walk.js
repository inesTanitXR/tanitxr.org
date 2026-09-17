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
const hintEl = document.getElementById('walk-hint');
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

  const renderer = new THREE.WebGLRenderer({ canvas, antialias: true, alpha: true });
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

  // ---- Nura: a companion who floats nearby, faces you, and has something to say
  let nura = null, mixer = null;
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
    nuraHolder.add(g);
    nura = g;
    if (gltf.animations && gltf.animations.length) {
      mixer = new THREE.AnimationMixer(o);
      const clip = gltf.animations.find(a => /float/i.test(a.name)) || gltf.animations[0];
      mixer.clipAction(clip).play();
    }
  }, undefined, () => { /* Nura is optional, the page still works without her */ });

  const bubble = document.getElementById('nura-bubble');
  const bubbleText = document.getElementById('nura-text');
  const speakBtn = document.getElementById('nura-speak');
  let speaking = false;
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
  if (speakBtn) speakBtn.addEventListener('click', () => {
    if (speaking) { speechSynthesis.cancel(); speaking = false; speakBtn.classList.remove('on'); return; }
    const s = slots[shown];
    if (s) sayLine(s.it.note || s.it.title);
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
  const current = () => slots[Math.round(clamp(cursor, 0, slots.length - 1))];
  stage.addEventListener('pointerdown', e => {
    dragging = true; idle = 0; lastX = e.clientX; lastY = e.clientY;
    stage.classList.add('grabbing');
    if (hintEl) hintEl.classList.add('gone');
  });
  addEventListener('pointermove', e => {
    if (!dragging) return;
    const s = current();
    if (s) {
      s.pivot.rotation.y += (e.clientX - lastX) * 0.01;
      s.pivot.rotation.x = clamp(s.pivot.rotation.x + (e.clientY - lastY) * 0.005, -0.7, 0.7);
    }
    lastX = e.clientX; lastY = e.clientY;
  }, { passive: true });
  const stopDrag = () => { dragging = false; stage.classList.remove('grabbing'); };
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
  let shown = -1;
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
    if (bubbleText) bubbleText.textContent = s.it.note || '';
    if (bubble) {
      bubble.classList.remove('in');
      void bubble.offsetWidth;                        // restart the fade
      bubble.classList.add('in');
    }
    if (speaking) speechSynthesis.cancel();
    paintSave(s.it);
    history.replaceState(null, '', '#' + s.it.slug);
  }
  const on = (id, fn) => { const el = document.getElementById(id); if (el) el.addEventListener('click', fn); };
  on('wf-save', () => {
    const s = slots[shown]; if (!s) return;
    const l = readSaved(), i = l.indexOf(s.it.slug);
    i >= 0 ? l.splice(i, 1) : l.push(s.it.slug);
    try { localStorage.setItem(SAVED, JSON.stringify(l)); } catch (e) { /* private mode */ }
    paintSave(s.it);
  });
  on('wf-share', async () => {
    const s = slots[shown]; if (!s) return;
    const url = location.origin + location.pathname + '#' + s.it.slug;
    const text = s.it.title + ', scanned in Tunisia by Tanit XR volunteers. '
      + 'Share it to help protect it.';
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
  if (wanted) {
    const i = slots.findIndex(x => x.it.slug === wanted);
    if (i >= 0 && sections[i]) scrollTo({ top: midOf(sections[i]), behavior: 'instant' });
  }

  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const clock = new THREE.Clock();
  (function frame() {
    const dt = Math.min(clock.getDelta(), 0.05);
    cursor += (target - cursor) * (reduce ? 1 : 0.12);
    if (!dragging) idle += dt;
    paint(Math.round(clamp(cursor, 0, slots.length - 1)));

    slots.forEach(s => {
      const d = s.i - cursor;                       // 0 = front and centre
      const a = Math.max(0, 1 - Math.abs(d) * 1.3);
      s.wrap.visible = s.loaded && a > 0.005;
      if (!s.wrap.visible) return;
      s.wrap.position.set(0, -d * 3.5, -Math.abs(d) * 2.7);
      s.wrap.scale.setScalar(0.82 + 0.18 * a);
      s.mats.forEach(m => { m.opacity = a; });
      s.shadow.material.opacity = a * 0.8;
      if (!reduce && !dragging && idle > 2.2 && Math.abs(d) < 0.5) s.pivot.rotation.y += dt * 0.14;
    });

    const t = clock.elapsedTime;
    if (mixer) mixer.update(dt);
    if (nura) {
      nuraHolder.position.y = -0.15 + Math.sin(t * 1.05) * 0.075;       // a gentle hover
      nuraHolder.position.x = 2.15 + Math.sin(t * 0.43) * 0.09;
      nura.rotation.y = Math.sin(t * 0.5) * 0.12;                        // she keeps facing you
      nura.rotation.z = Math.sin(t * 0.8) * 0.03;
      sparks.children.forEach(m => {
        m.userData.a += dt * m.userData.sp;
        m.position.set(Math.cos(m.userData.a) * m.userData.r,
                       m.userData.y + Math.sin(t * m.userData.sp + m.userData.a) * 0.09,
                       Math.sin(m.userData.a) * m.userData.r * 0.7);
        m.material.opacity = 0.35 + 0.5 * (0.5 + 0.5 * Math.sin(t * 2 + m.userData.a));
      });
      if (bubble) {                                   // pin the bubble above her head
        const v = new THREE.Vector3(0, NURA_H * 1.02, 0);
        nuraHolder.localToWorld(v);
        v.project(camera);
        const r = stage.getBoundingClientRect();
        bubble.style.left = (r.left + (v.x * 0.5 + 0.5) * r.width) + 'px';
        bubble.style.top = (r.top + (-v.y * 0.5 + 0.5) * r.height) + 'px';
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
