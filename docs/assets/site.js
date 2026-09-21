
const SHEET = "";
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
document.addEventListener('submit', e => {
  const f = e.target;
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
