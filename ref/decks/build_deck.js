// Tanit XR partnership deck. Run: node build_deck.js
const pptxgen = require('pptxgenjs');
const React = require('react'); const RD = require('react-dom/server'); const sharp = require('sharp');
const FA = require('react-icons/fa');
const IMG = '/Users/inessaid/Documents/tanitxr.org/docs/assets/img/';
const MEDIA = '/Users/inessaid/Documents/tanitxr.org/media/';
const C = { ink: '241A10', brown: '4A3527', terra: 'A35F3F', cream: 'FDF8F0', sand: 'E8DCC6', gold: 'FFCD05', mute: '7D6A58', white: 'FFFFFF', deep: '2E2118' };
const TITLE = 'Cambria', BODY = 'Calibri';

async function icon(Comp, color, size = 256) {
  const svg = RD.renderToStaticMarkup(React.createElement(Comp, { color: '#' + color, size }));
  const buf = await sharp(Buffer.from(svg)).png().toBuffer();
  return 'image/png;base64,' + buf.toString('base64');
}

(async () => {
  const pres = new pptxgen();
  pres.layout = 'LAYOUT_WIDE';            // 13.33 x 7.5
  pres.author = 'Tanit XR'; pres.title = 'Tanit XR, partnership opportunities';
  const W = 13.33, H = 7.5;
  const T = (slide, text, o) => slide.addText(text, Object.assign({ isTextBox: true, margin: 0, fontFace: BODY, color: C.deep }, o));
  const circleIcon = async (slide, Comp, x, y, d, bg, fg) => {
    slide.addShape(pres.shapes.OVAL, { x, y, w: d, h: d, fill: { color: bg }, line: { color: bg } });
    slide.addImage({ data: await icon(Comp, fg), x: x + d * 0.25, y: y + d * 0.25, w: d * 0.5, h: d * 0.5 });
  };
  const footer = (slide, dark) => T(slide, 'tanitxr.org', { x: W - 2.6, y: H - 0.55, w: 2.1, h: 0.3, fontSize: 11, color: dark ? C.sand : C.mute, align: 'right' });
  const eyebrow = (slide, text, x, y, color) => T(slide, text.toUpperCase(), { x, y, w: 8, h: 0.3, fontSize: 12, bold: true, color: color || C.terra, charSpacing: 4 });

  // 1. Title, dark, half-bleed photo
  let s = pres.addSlide(); s.background = { color: C.ink };
  s.addImage({ path: IMG + 'sv-img-0511-1800.jpg', x: 6.9, y: 0, w: 6.43, h: H, sizing: { type: 'cover', w: 6.43, h: H } });
  s.addImage({ path: MEDIA + 'tanitxr-logo_red_horizontal.png', x: 0.7, y: 0.6, w: 2.4, h: 1.0 });
  eyebrow(s, 'Partnership opportunities', 0.7, 2.3, C.gold);
  T(s, "Keep a country's memory, with your name on it", { x: 0.7, y: 2.7, w: 5.9, h: 2.2, fontFace: TITLE, fontSize: 40, bold: true, color: C.white });
  T(s, 'Tanit XR is a volunteer community on four continents that 3D-scans Tunisia\'s endangered heritage with phones and publishes it free, in 3D, AR and VR.', { x: 0.7, y: 5.0, w: 5.9, h: 1.2, fontSize: 15, color: C.sand });
  footer(s, true);
  s.addNotes('Open with the four-minute guided visit at tanitxr.org/explore?tour=1 before this deck.');

  // 2. The problem
  s = pres.addSlide(); s.background = { color: C.cream };
  s.addImage({ path: IMG + 'aug-pxl-0811-150245-1800.jpg', x: 0, y: 0, w: 5.6, h: H, sizing: { type: 'cover', w: 5.6, h: H } });
  eyebrow(s, 'The problem', 6.2, 0.9);
  T(s, 'Heritage in the open air, with no record', { x: 6.2, y: 1.3, w: 6.4, h: 1.4, fontFace: TITLE, fontSize: 32, bold: true });
  const probs = [
    ['Storms, erosion, heat and neglect', 'wear down Punic stelae, Roman mosaics and medina doors faster than institutions can document them.'],
    ['In January 2026 a storm uncovered part of Neapolis', 'for a few days. There was no 3D record to compare against. A volunteer scanned it before the sea came back.'],
    ['The tools exist, but sit with a few expert teams.', 'The people who live beside these places have had no way to take part, or to see their heritage where young people spend their time.'],
  ];
  let y = 2.95;
  for (const [b, rest] of probs) {
    s.addShape(pres.shapes.OVAL, { x: 6.2, y: y + 0.08, w: 0.16, h: 0.16, fill: { color: C.terra }, line: { color: C.terra } });
    s.addText([{ text: b + ' ', options: { bold: true } }, { text: rest }], { x: 6.55, y, w: 6.1, h: 1.1, isTextBox: true, margin: 0, fontFace: BODY, fontSize: 14, color: C.deep, valign: 'top' });
    y += 1.25;
  }
  footer(s);

  // 3. What we do: the pipeline
  s = pres.addSlide(); s.background = { color: C.white };
  eyebrow(s, 'What we do', 0.7, 0.7);
  T(s, 'From a phone in Carthage to a headset anywhere', { x: 0.7, y: 1.05, w: 12, h: 0.9, fontFace: TITLE, fontSize: 32, bold: true });
  const steps = [
    [FA.FaMobileAlt, 'Scan', 'Volunteers in Tunisia walk around an object with a free app. A stone takes minutes.'],
    [FA.FaUsers, 'Clean', 'Volunteers anywhere turn the raw scan into an archival record and a light web-ready twin.'],
    [FA.FaBookOpen, 'Research', 'The history behind each object is written up, in three languages, and credited.'],
    [FA.FaCubes, 'Publish', 'Everything goes into the open archive and Explore in 3D, free, on any phone or headset.'],
    [FA.FaShareAlt, 'Share', 'Visitors turn objects, meet our guide Nura, save and share them. Every share keeps a piece seen.'],
  ];
  let x = 0.7; const cw = 2.3;
  for (const [Ic, h, d] of steps) {
    await circleIcon(s, Ic, x + 0.05, 2.4, 0.9, C.sand, C.terra);
    T(s, h, { x, y: 3.5, w: cw, h: 0.4, fontFace: TITLE, fontSize: 18, bold: true, color: C.brown });
    T(s, d, { x, y: 3.95, w: cw, h: 1.8, fontSize: 12.5, color: C.deep, valign: 'top' });
    x += cw + 0.13;
  }
  T(s, 'Around the software is a community: 85+ volunteers on four continents who meet every Thursday, learn Tunisian history together and build pieces for a virtual museum.', { x: 0.7, y: 6.0, w: 12, h: 0.8, fontSize: 14, italic: true, color: C.mute });
  footer(s);

  // 4. See it now
  s = pres.addSlide(); s.background = { color: C.ink };
  s.addImage({ path: IMG + 'explore-og-1200.jpg', x: 0.7, y: 1.3, w: 7.4, h: 3.885 });
  s.addImage({ path: IMG + 'explore-gallery-600.jpg', x: 5.2, y: 4.3, w: 3.4, h: 2.125 });
  eyebrow(s, 'See it now', 8.9, 1.3, C.gold);
  T(s, 'Open this on your phone', { x: 8.9, y: 1.7, w: 4.0, h: 1.2, fontFace: TITLE, fontSize: 30, bold: true, color: C.white });
  T(s, 'tanitxr.org/explore', { x: 8.9, y: 2.95, w: 4.0, h: 0.5, fontSize: 20, bold: true, color: C.gold });
  T(s, 'Turn a two-thousand-year-old stone with your finger. Tap Nura and she tells you its story. Step into a volunteer\'s gallery. Put on a Quest headset and stand beside it at real size.', { x: 8.9, y: 3.6, w: 4.0, h: 1.6, fontSize: 14, color: C.sand });
  T(s, 'Add ?tour=1 for a four-minute guided visit.', { x: 8.9, y: 5.4, w: 4.0, h: 0.5, fontSize: 12, italic: true, color: C.sand });
  footer(s, true);

  // 5. Traction
  s = pres.addSlide(); s.background = { color: C.cream };
  eyebrow(s, 'Where we are, September 2026', 0.7, 0.7);
  T(s, 'Built by volunteers, before the first grant', { x: 0.7, y: 1.05, w: 12, h: 0.9, fontFace: TITLE, fontSize: 32, bold: true });
  const stats = [['99', 'public 3D scans'], ['8', 'Tunisian sites'], ['85+', 'volunteers, 4 continents'], ['75', 'objects live in 3D'], ['20+', 'course graduates'], ['3', 'languages, all free']];
  x = 0.7; for (const [n, l] of stats) {
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y: 2.3, w: 1.95, h: 1.9, fill: { color: C.white }, line: { color: 'E4D8C4' }, rectRadius: 0.12 });
    T(s, n, { x, y: 2.45, w: 1.95, h: 0.95, fontFace: TITLE, fontSize: 44, bold: true, color: C.terra, align: 'center' });
    T(s, l, { x: x + 0.1, y: 3.4, w: 1.75, h: 0.7, fontSize: 12, color: C.mute, align: 'center' });
    x += 2.07;
  }
  T(s, 'Recognition', { x: 0.7, y: 4.6, w: 4, h: 0.4, fontFace: TITLE, fontSize: 18, bold: true, color: C.brown });
  const rec = ['Auggie Awards 2026 finalist, Best Societal Impact (AWE USA)', 'Al Jazeera culture feature; Voices of VR episode 1728; Niantic Spatial video interview', 'Paper at the El Jem conference in English, French and Tunisian Arabic', 'Sponsored hackathon tracks at Georgia Tech (ImmerseGT) and CityCamp Gainesville', 'The model is being replicated in Nigeria by the Unique Mappers Network'];
  s.addText(rec.map((t, i) => ({ text: t, options: { bullet: true, breakLine: i < rec.length - 1, paraSpaceAfter: 5 } })), { x: 0.7, y: 5.05, w: 12, h: 1.9, isTextBox: true, margin: 0, fontFace: BODY, fontSize: 13.5, color: C.deep, valign: 'top' });
  footer(s);

  // 6. The community
  s = pres.addSlide(); s.background = { color: C.white };
  s.addImage({ path: IMG + 'museum-hall-arches-1200.jpg', x: 7.5, y: 0, w: 5.83, h: H, sizing: { type: 'cover', w: 5.83, h: H } });
  eyebrow(s, 'More than an archive', 0.7, 0.9);
  T(s, 'A cultural exchange that builds a museum', { x: 0.7, y: 1.3, w: 6.3, h: 1.4, fontFace: TITLE, fontSize: 32, bold: true });
  T(s, 'Every Thursday, volunteers in Tunis, Florida, Europe and Lagos review new scans and learn the history behind them. People who have never been to Tunisia model lamps, pottery and courtyards for the virtual museum, and the Tunisian volunteers learn about their countries in return.\n\nStudents get portfolio reviews, mock interviews and mentors. Every contribution is credited by name, on the site and on every object.\n\nTunisia is the pilot. Nigeria is the first proof that the model travels.', { x: 0.7, y: 2.85, w: 6.3, h: 3.6, fontSize: 14, color: C.deep, valign: 'top' });
  T(s, 'The virtual museum, modelled by volunteers, in progress', { x: 7.7, y: H - 0.55, w: 5.4, h: 0.3, fontSize: 10, color: C.white, align: 'right' });

  // 7. Why a company
  s = pres.addSlide(); s.background = { color: C.cream };
  eyebrow(s, 'Why partner', 0.7, 0.7);
  T(s, 'What this does for your company', { x: 0.7, y: 1.05, w: 12, h: 0.9, fontFace: TITLE, fontSize: 32, bold: true });
  const why = [
    [FA.FaUsers, 'Employees who learn something real', 'Skills-based volunteering: your team learns 3D capture on a phone and publishes actual heritage under their names. People talk about it afterwards.'],
    [FA.FaBullhorn, 'A story your communications team can use', 'A storm, a rescue, a volunteer, a stone: pictures and stories we take ourselves, with your part in them told plainly.'],
    [FA.FaGlobeAfrica, 'Presence in Tunisia and North Africa', 'A visible, respected role in a country\'s heritage, alongside a Tunisian-led team, at a fraction of a campaign\'s cost.'],
    [FA.FaLightbulb, 'Innovation your audience can touch', 'Phones, 3D, AR and headsets in the service of memory. A live demo at your event that nobody expects at a tech gathering.'],
  ];
  const cells = [[0.7, 2.25], [6.85, 2.25], [0.7, 4.55], [6.85, 4.55]];
  for (let i = 0; i < why.length; i++) {
    const [Ic, h, d] = why[i], [cx, cy] = cells[i];
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: cx, y: cy, w: 5.8, h: 2.05, fill: { color: C.white }, line: { color: 'E4D8C4' }, rectRadius: 0.12 });
    await circleIcon(s, Ic, cx + 0.25, cy + 0.3, 0.7, C.sand, C.terra);
    T(s, h, { x: cx + 1.15, y: cy + 0.3, w: 4.45, h: 0.5, fontFace: TITLE, fontSize: 16, bold: true, color: C.brown });
    T(s, d, { x: cx + 1.15, y: cy + 0.85, w: 4.45, h: 1.1, fontSize: 12.5, color: C.deep, valign: 'top' });
  }
  footer(s);

  // 8. Ways to partner
  s = pres.addSlide(); s.background = { color: C.white };
  eyebrow(s, 'Ways to partner', 0.7, 0.7);
  T(s, 'Pick one, or shape one with us', { x: 0.7, y: 1.05, w: 12, h: 0.9, fontFace: TITLE, fontSize: 32, bold: true });
  const offers = [
    [FA.FaMobileAlt, 'Your team learns to scan', 'A half day or a six-week course, online or on site. Your employees publish a real piece of heritage under their names.'],
    [FA.FaLandmark, 'Adopt a site or a gallery', 'Fund the scanning of one site, or one gallery in the virtual museum, and it carries your name in 3D and in the headset.'],
    [FA.FaVrCardboard, 'Bring a room to your event', 'The 3D experience and a headset at your conference or office, with a volunteer to guide people through it.'],
    [FA.FaMicrophone, 'A talk or a workshop', 'Our founder and team speak on phone photogrammetry, community XR and heritage at risk: AWE, Voices of VR, Georgia Tech, El Jem.'],
    [FA.FaCode, 'Sponsor a hackathon track', 'Real scans as the material. You set the challenge, meet the students, see what they build in a weekend.'],
    [FA.FaRoute, 'Fund a scanning season', 'Bus fares, data, backups and a modest fee for local volunteers, with sites, counts and stories reported monthly.'],
  ];
  const grid = [[0.7, 2.15], [4.87, 2.15], [9.04, 2.15], [0.7, 4.55], [4.87, 4.55], [9.04, 4.55]];
  for (let i = 0; i < offers.length; i++) {
    const [Ic, h, d] = offers[i], [cx, cy] = grid[i];
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: cx, y: cy, w: 3.6, h: 2.15, fill: { color: C.cream }, line: { color: 'E9DFCC' }, rectRadius: 0.12 });
    await circleIcon(s, Ic, cx + 0.25, cy + 0.25, 0.6, C.white, C.terra);
    T(s, h, { x: cx + 1.0, y: cy + 0.3, w: 2.45, h: 0.5, fontFace: TITLE, fontSize: 14.5, bold: true, color: C.brown });
    T(s, d, { x: cx + 0.25, y: cy + 0.95, w: 3.1, h: 1.1, fontSize: 11.5, color: C.deep, valign: 'top' });
  }
  footer(s);

  // 9. What you get back
  s = pres.addSlide(); s.background = { color: C.ink };
  eyebrow(s, 'What you get back', 0.7, 0.7, C.gold);
  T(s, 'Impact you can point at', { x: 0.7, y: 1.05, w: 12, h: 0.9, fontFace: TITLE, fontSize: 32, bold: true, color: C.white });
  const gets = [
    'Every object your support made possible is public, in 3D, with your name beside it.',
    'Numbers, monthly: visits, objects viewed, people trained, sites documented, from the same counter we use ourselves.',
    'Stories and pictures for your communications team, told plainly, with your part in them.',
    'Your logo on the site, in the experience and at our events, and a mention in every newsletter edition.',
    'Employees who learned something real and can show their families what they helped keep.',
    'A tax-deductible gift through our fiscal sponsor, Florida Community Innovation, a U.S. 501(c)(3).',
  ];
  s.addText(gets.map((t, i) => ({ text: t, options: { bullet: true, breakLine: i < gets.length - 1, paraSpaceAfter: 10 } })), { x: 0.7, y: 2.2, w: 7.6, h: 4.2, isTextBox: true, margin: 0, fontFace: BODY, fontSize: 15, color: C.sand, valign: 'top' });
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 8.9, y: 2.2, w: 3.75, h: 2.6, fill: { color: C.brown }, line: { color: C.brown }, rectRadius: 0.14 });
  T(s, 'One promise, whatever the partnership', { x: 9.15, y: 2.4, w: 3.3, h: 0.7, fontFace: TITLE, fontSize: 15, bold: true, color: C.gold });
  T(s, 'The archive stays free and open, and our volunteers are never made to work so that someone else earns. We sell training, events and our time. Never the heritage.', { x: 9.15, y: 3.1, w: 3.3, h: 1.6, fontSize: 12.5, color: C.cream, valign: 'top' });
  footer(s, true);

  // 10. Levels (proposed)
  s = pres.addSlide(); s.background = { color: C.cream };
  eyebrow(s, 'Partnership levels', 0.7, 0.7);
  T(s, 'A first step, and a way to grow', { x: 0.7, y: 1.05, w: 12, h: 0.9, fontFace: TITLE, fontSize: 32, bold: true });
  const tiers = [
    ['Scanning day', '$2,500', 'One volunteer\'s season of site visits: transport, data, backups.', 'Named on the objects scanned that season'],
    ['Adopt a site', '$10,000', 'Every object from one site, scanned, researched, published.', 'Your name on the site\'s gallery'],
    ['Sponsor a track', '$25,000', 'A year of one volunteer track, or a full course cohort of 20.', 'Featured in materials, quarterly reports'],
    ['Founding partner', '$100,000', 'A custom year-round volunteer programme for your team on one track.', 'Lead recognition, quarterly reports'],
    ['Title sponsor', '$300,000', 'All four tracks, the virtual museum, and core team capacity.', 'Title sponsor of the museum, monthly reports'],
  ];
  x = 0.7; const tw = 2.32;
  for (let i = 0; i < tiers.length; i++) {
    const [n, amt, what, get] = tiers[i]; const top = i >= 3;
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y: 2.2, w: tw, h: 4.1, fill: { color: top ? C.brown : C.white }, line: { color: top ? C.brown : 'E4D8C4' }, rectRadius: 0.12 });
    T(s, n, { x: x + 0.2, y: 2.4, w: tw - 0.4, h: 0.5, fontFace: TITLE, fontSize: 15, bold: true, color: top ? C.gold : C.brown });
    T(s, amt, { x: x + 0.2, y: 2.95, w: tw - 0.4, h: 0.6, fontFace: TITLE, fontSize: 24, bold: true, color: top ? C.white : C.terra });
    T(s, what, { x: x + 0.2, y: 3.7, w: tw - 0.4, h: 1.3, fontSize: 11.5, color: top ? C.cream : C.deep, valign: 'top' });
    T(s, get, { x: x + 0.2, y: 5.15, w: tw - 0.4, h: 1.0, fontSize: 11, italic: true, color: top ? C.sand : C.mute, valign: 'top' });
    x += tw + 0.14;
  }
  T(s, 'Every level includes credit on the site and in the 3D experience, monthly numbers, and a tax receipt through our fiscal sponsor.', { x: 0.7, y: 6.5, w: 12, h: 0.5, fontSize: 12, italic: true, color: C.mute });
  footer(s);
  s.addNotes('Amounts are proposals for the team to confirm before this deck is sent.');

  // 11. Team
  s = pres.addSlide(); s.background = { color: C.white };
  eyebrow(s, 'The people', 0.7, 0.7);
  T(s, 'Local roots, global reach', { x: 0.7, y: 1.05, w: 12, h: 0.9, fontFace: TITLE, fontSize: 32, bold: true });
  s.addImage({ path: MEDIA + 'InesSaid_EE30U30_1.jpg', x: 0.7, y: 2.3, w: 3.9, h: 2.75, sizing: { type: 'cover', w: 3.9, h: 2.75 }, rounding: false });
  T(s, 'Ines Said, Founder', { x: 0.7, y: 5.15, w: 3.9, h: 0.4, fontFace: TITLE, fontSize: 15, bold: true, color: C.brown });
  T(s, 'Tunisian XR developer who grew up beside the ruins of Carthage. Smithsonian installations, IEEE best paper, AWE 2026 speaker, Auggie Awards finalist.', { x: 0.7, y: 5.55, w: 3.9, h: 1.2, fontSize: 11.5, color: C.deep, valign: 'top' });
  const team = [['Julia Moreno-Molen', 'Project Manager'], ['Melek Said', 'Regional Manager, Tunisia'], ['Dr. Laura Harrison', 'Chief Scientist, archaeology'], ['Dr. Caroline Nickerson', 'Partnerships and Community'], ['Margarita Johnson', 'Research and Writing'], ['Fatma Slama', 'Community Liaison, Tunisia']];
  const tg = [[5.1, 2.3], [8.9, 2.3], [5.1, 3.55], [8.9, 3.55], [5.1, 4.8], [8.9, 4.8]];
  for (let i = 0; i < team.length; i++) {
    const [n, r] = team[i], [cx, cy] = tg[i];
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: cx, y: cy, w: 3.55, h: 1.05, fill: { color: C.cream }, line: { color: 'E9DFCC' }, rectRadius: 0.1 });
    T(s, n, { x: cx + 0.2, y: cy + 0.18, w: 3.2, h: 0.4, fontFace: TITLE, fontSize: 14, bold: true, color: C.brown });
    T(s, r, { x: cx + 0.2, y: cy + 0.58, w: 3.2, h: 0.35, fontSize: 11.5, color: C.mute });
  }
  T(s, 'And 85+ volunteers: 3D artists, Unity developers, researchers, writers, teachers, in Tunisia, the United States, Europe and Nigeria.', { x: 5.1, y: 6.05, w: 7.4, h: 0.7, fontSize: 12.5, italic: true, color: C.mute });
  footer(s);

  // 12. Close
  s = pres.addSlide(); s.background = { color: C.ink };
  s.addImage({ path: IMG + 'hero-baths-flipped-1920.jpg', x: 0, y: 0, w: W, h: H, sizing: { type: 'cover', w: W, h: H }, transparency: 70 });
  eyebrow(s, 'Start the conversation', 0.7, 2.0, C.gold);
  T(s, 'Fifteen minutes is enough to see if this fits', { x: 0.7, y: 2.4, w: 9, h: 1.6, fontFace: TITLE, fontSize: 38, bold: true, color: C.white });
  T(s, 'Tell us about your team and what matters to you. We come back with two or three ways to work together, with real numbers.', { x: 0.7, y: 4.05, w: 8, h: 0.9, fontSize: 15, color: C.sand });
  T(s, 'info@tanitxr.org', { x: 0.7, y: 5.1, w: 6, h: 0.5, fontSize: 22, bold: true, color: C.gold });
  T(s, 'tanitxr.org/partners  ·  tanitxr.org/explore?tour=1', { x: 0.7, y: 5.65, w: 8, h: 0.4, fontSize: 14, color: C.sand });
  T(s, 'Tanit XR is fiscally sponsored by Florida Community Innovation, a U.S. 501(c)(3). Gifts are tax-deductible.', { x: 0.7, y: 6.6, w: 10, h: 0.35, fontSize: 10.5, color: C.sand });

  await pres.writeFile({ fileName: 'tanitxr-partnership-deck.pptx' });
  console.log('written');
})().catch(e => { console.error(e); process.exit(1); });
