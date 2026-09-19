// Instagram carousel from a newsletter edition's HIGHLIGHTS block. Run: node build_carousel.js ../newsletter-edition-18.md
const fs = require('fs'); const pptxgen = require('pptxgenjs');
const src = process.argv[2] || '/Users/inessaid/Documents/tanitxr.org/ref/newsletter-edition-18.md';
const md = fs.readFileSync(src, 'utf8');
const edition = (md.match(/Edition (\d+)/) || [,'?'])[1];
const block = md.split(/## 🔥 HIGHLIGHTS/)[1].split(/\n─|\n## /)[0];
const skip = process.argv[3] ? new RegExp(process.argv[3], 'i') : null;   // e.g. "Fast Forward" once it has closed
const items = block.split('\n').filter(l => l.trim().startsWith('- ')).map(l => l.replace(/^- /, '').trim()).filter(l => !skip || !skip.test(l));
const MEDIA = '/Users/inessaid/Documents/tanitxr.org/media/';
const C = { ink: '241A10', brown: '4A3527', terra: 'A35F3F', cream: 'FDF8F0', sand: 'E8DCC6', gold: 'FFCD05', mute: '7D6A58', white: 'FFFFFF', deep: '2E2118' };
const pres = new pptxgen();
pres.defineLayout({ name: 'IG', width: 10.8, height: 13.5 }); pres.layout = 'IG';
const T = (s, text, o) => s.addText(text, Object.assign({ isTextBox: true, margin: 0, fontFace: 'Calibri', color: C.deep }, o));
const foot = (s, dark) => { s.addImage({ path: MEDIA + 'tanitxr-logo_red_horizontal.png', x: 0.8, y: 12.1, w: 1.9, h: 0.8 }); T(s, 'tanitxr.org/opportunities', { x: 5.0, y: 12.35, w: 5.0, h: 0.4, fontSize: 18, align: 'right', color: dark ? C.sand : C.mute }); };
// cover
let s = pres.addSlide(); s.background = { color: C.ink };
T(s, `EDITION ${edition}`, { x: 0.8, y: 1.4, w: 9, h: 0.5, fontSize: 20, bold: true, color: C.gold, charSpacing: 6 });
T(s, 'Art, XR & Impact Opportunities', { x: 0.8, y: 2.1, w: 9.2, h: 3.6, fontFace: 'Cambria', fontSize: 64, bold: true, color: C.white });
T(s, `${items.length} deadlines worth your time this month.\nGrants, residencies, awards and open calls for artists, XR makers and nonprofits. Only things we would apply to ourselves.`, { x: 0.8, y: 6.0, w: 9.2, h: 2.6, fontSize: 24, color: C.sand });
T(s, 'Swipe →', { x: 0.8, y: 10.6, w: 4, h: 0.6, fontSize: 24, bold: true, color: C.gold });
foot(s, true);
// one per highlight
items.forEach((raw, i) => {
  const emoji = (raw.match(/^\p{Extended_Pictographic}/u) || [''])[0];
  let rest = raw.replace(/^\p{Extended_Pictographic}\s*/u, '').replace(/🚨/g, '').trim();
  const [head, ...tail] = rest.split(/\.\s+/);
  const [name, ...sub] = head.split(/,\s+/);
  const deadline = tail.join('. ').replace(/^Deadline\s*/i, '').replace(/^Closes\s*/i, 'Closes ').trim();
  s = pres.addSlide(); s.background = { color: i % 2 ? C.cream : C.white };
  T(s, `${i + 1} / ${items.length}`, { x: 0.8, y: 1.0, w: 3, h: 0.5, fontSize: 20, bold: true, color: C.terra });
  if (emoji) T(s, emoji, { x: 0.8, y: 2.0, w: 2, h: 1.6, fontSize: 80 });
  T(s, name, { x: 0.8, y: 3.9, w: 9.2, h: 3.2, fontFace: 'Cambria', fontSize: 54, bold: true, color: C.deep, valign: 'top' });
  if (sub.length) T(s, sub.join(', '), { x: 0.8, y: 7.3, w: 9.2, h: 1.6, fontSize: 30, color: C.brown, valign: 'top' });
  if (deadline) { s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 0.8, y: 9.4, w: 9.2, h: 1.4, fill: { color: C.ink }, line: { color: C.ink }, rectRadius: 0.2 }); T(s, deadline, { x: 1.2, y: 9.4, w: 8.4, h: 1.4, fontSize: 30, bold: true, color: C.gold, valign: 'middle' }); }
  foot(s, false);
});
// close
s = pres.addSlide(); s.background = { color: C.ink };
T(s, 'ALL OF THEM, WITH COUNTDOWNS', { x: 0.8, y: 1.4, w: 9, h: 0.5, fontSize: 20, bold: true, color: C.gold, charSpacing: 4 });
T(s, 'The full list is on tanitxr.org', { x: 0.8, y: 2.1, w: 9.2, h: 3.0, fontFace: 'Cambria', fontSize: 58, bold: true, color: C.white });
T(s, 'Filter by type, watch the deadlines count down, and subscribe to get the next edition in your inbox. Free.\n\nLink in bio, or type tanitxr.org/opportunities', { x: 0.8, y: 5.4, w: 9.2, h: 3.4, fontSize: 26, color: C.sand });
T(s, 'Save this post for the deadlines. Share it with someone who should apply.', { x: 0.8, y: 9.4, w: 9.2, h: 1.4, fontSize: 24, italic: true, color: C.gold });
foot(s, true);
pres.writeFile({ fileName: `tanitxr-ig-edition-${edition}.pptx` }).then(() => console.log('written', items.length + 2, 'slides'));
