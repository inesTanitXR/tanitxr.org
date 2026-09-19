const pptxgen = require('pptxgenjs');
const IMG = '/Users/inessaid/Documents/tanitxr.org/docs/assets/img/', MEDIA = '/Users/inessaid/Documents/tanitxr.org/media/';
const C = { ink: '241A10', brown: '4A3527', terra: 'A35F3F', cream: 'FDF8F0', sand: 'E8DCC6', gold: 'FFCD05', mute: '7D6A58', white: 'FFFFFF', deep: '2E2118' };
const pres = new pptxgen();
pres.defineLayout({ name: 'LETTER', width: 8.5, height: 11 });
pres.layout = 'LETTER';
const s = pres.addSlide(); s.background = { color: C.cream };
const T = (text, o) => s.addText(text, Object.assign({ isTextBox: true, margin: 0, fontFace: 'Calibri', color: C.deep }, o));
// header band with photo
s.addImage({ path: IMG + 'hero-baths-flipped-1920.jpg', x: 0, y: 0, w: 8.5, h: 2.6, sizing: { type: 'cover', w: 8.5, h: 2.6 } });
s.addShape(pres.shapes.RECTANGLE, { x: 0, y: 0, w: 8.5, h: 2.6, fill: { color: C.ink, transparency: 30 }, line: { color: C.ink, transparency: 100 } });
s.addImage({ path: MEDIA + 'tanitxr-logo_red_horizontal.png', x: 0.5, y: 0.35, w: 1.7, h: 0.7 });
T('TANIT XR  ×  TAYP   ·   WASHINGTON, DC   ·   THURSDAY, OCTOBER 22, 2026, 6 TO 9 PM', { x: 0.5, y: 1.2, w: 7.5, h: 0.3, fontSize: 9.5, bold: true, color: C.gold, charSpacing: 2 });
T('Tunisia in 3D: an evening with Tanit XR', { x: 0.5, y: 1.5, w: 7.5, h: 0.9, fontFace: 'Cambria', fontSize: 26, bold: true, color: C.white });
// intro
T('A volunteer community on four continents is putting Tunisia\'s endangered heritage online in 3D, free, for anyone. For one evening in Washington, the people behind it are in the room: an archaeologist just back from the field, the partnerships lead who turns a room into volunteers, and the founder as host. Two short talks and a live demo, then headsets and phones so guests can hold a two-thousand-year-old stone from Carthage in their hands. 60 to 100 guests from the Tunisian-American, tech, policy and university communities of DC.', { x: 0.5, y: 2.85, w: 7.5, h: 1.35, fontSize: 10.5, color: C.deep, valign: 'top' });
// speakers
T('ON STAGE', { x: 0.5, y: 4.3, w: 3, h: 0.25, fontSize: 9, bold: true, color: C.terra, charSpacing: 3 });
const sp = [['Dr. Laura Harrison', 'Archaeologist, Chief Scientist of Tanit XR. Her time in Tunisia: the sites, the people who look after them, and what a phone can and cannot record.'],
            ['Dr. Caroline Nickerson', 'Partnerships and Community; Executive Director, Florida Community Innovation. Citizen science, the Thursday community, and how a room becomes volunteers.'],
            ['Ines Said, host', 'Founder of Tanit XR and XR artist (Smithsonian FUTURES installations, Auggie Awards 2026 finalist). A live walk through Explore in 3D.']];
let y = 4.6;
for (const [n, d] of sp) { T(n, { x: 0.5, y, w: 2.2, h: 0.5, fontFace: 'Cambria', fontSize: 11.5, bold: true, color: C.brown }); T(d, { x: 2.7, y, w: 5.3, h: 0.5, fontSize: 9.5, color: C.deep, valign: 'top' }); y += 0.56; }
// levels
T('WHAT WE NEED, IN KIND FIRST', { x: 0.5, y: 6.4, w: 5, h: 0.25, fontSize: 9, bold: true, color: C.terra, charSpacing: 3 });
const lv = [['In kind', 'a room · Tunisian food · drinks · two headsets · printing', 'This is what makes the evening happen. Your name on the screen, the invitation and our posts, and a thank-you from the stage.'],
            ['Friend', '$250', 'Logo on the screen all evening, thank-you from the stage and in our posts to about 8,000 people.'],
            ['Partner', '$750', 'Logo on the invitation and posters, one minute at the mic, a headset station in your name.'],
            ['Presenting', '$1,500', '"Presented by" on everything, a phone 3D-capture workshop for your team afterwards, a gallery credit in the virtual museum.']];
let x = 0.5; const cw = 1.8;
for (const [n, a, d] of lv) {
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y: 6.75, w: cw, h: 2.35, fill: { color: n === 'In kind' ? C.brown : C.white }, line: { color: n === 'In kind' ? C.brown : 'E4D8C4' }, rectRadius: 0.1 });
  const ik = n === 'In kind';
  T(n, { x: x + 0.15, y: 6.9, w: cw - 0.3, h: 0.3, fontFace: 'Cambria', fontSize: 12, bold: true, color: ik ? C.gold : C.brown });
  T(a, { x: x + 0.15, y: 7.22, w: cw - 0.3, h: 0.55, fontFace: 'Cambria', fontSize: ik ? 9.5 : 18, bold: true, color: ik ? C.white : C.terra, valign: 'top' });
  T(d, { x: x + 0.15, y: 7.82, w: cw - 0.3, h: 1.2, fontSize: 8.8, color: ik ? C.cream : C.deep, valign: 'top' });
  x += cw + 0.1;
}
T('Every level includes a tax receipt through our fiscal sponsor, Florida Community Innovation, a U.S. 501(c)(3), and a follow-up report with photos and numbers. Guests are asked for a suggested donation of $20; students free.', { x: 0.5, y: 9.2, w: 7.5, h: 0.5, fontSize: 9, italic: true, color: C.mute });
// footer
s.addShape(pres.shapes.RECTANGLE, { x: 0, y: 9.85, w: 8.5, h: 1.15, fill: { color: C.ink }, line: { color: C.ink } });
T('Say yes by October 8', { x: 0.5, y: 9.98, w: 3.5, h: 0.35, fontFace: 'Cambria', fontSize: 14, bold: true, color: C.gold });
T('Ines Said, Founder  ·  ines@tanitxr.org  ·  tanitxr.org/partners', { x: 0.5, y: 10.35, w: 5.5, h: 0.3, fontSize: 10, color: C.cream });
T('See the experience first, four minutes:\ntanitxr.org/explore/?tour=1', { x: 5.4, y: 9.98, w: 2.7, h: 0.7, fontSize: 9.5, color: C.sand, align: 'right' });
pres.writeFile({ fileName: 'tanitxr-dc-oct22-sponsor-sheet.pptx' }).then(() => console.log('written'));
