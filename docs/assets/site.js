
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
  const line = lines[pick];

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
  }
  document.getElementById('nura-hush').addEventListener('click', () => shut(true));
  go.addEventListener('click', () => { if (window.tx) tx('nura_cta', { ask: pick }); });
  tab.addEventListener('click', () => {
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
