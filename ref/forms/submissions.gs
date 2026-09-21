/**
 * Tanit XR: catch every form submission from tanitxr.org into a Google Sheet.
 *
 * The site's forms keep emailing info@tanitxr.org as they do now. This receives a copy so the
 * submissions also pile up somewhere readable, which is what makes an approval step possible:
 * a profile can sit as "waiting" until a human says yes, instead of living only in an inbox.
 *
 * HOW TO INSTALL, once, about five minutes:
 *  1. Go to script.google.com and press "New project".
 *  2. Delete whatever is in the editor and paste this whole file in.
 *  3. Name the project "Tanit XR site submissions" (top left).
 *  4. Press Deploy, then "New deployment". Click the gear next to "Select type" and choose
 *     "Web app". Set:
 *        Description:    site forms
 *        Execute as:     Me
 *        Who has access: Anyone
 *     "Anyone" is needed because visitors are not signed in. They can only add rows through
 *     this script; nobody can read the sheet.
 *  5. Press Deploy, allow the permissions it asks for, and copy the Web app URL it shows.
 *     It looks like https://script.google.com/macros/s/AKfy..../exec
 *  6. Send that URL to Claude. It goes into ref/forms.json and the site starts using it.
 *
 * If you ever change this file, press Deploy, "Manage deployments", the pencil, then set
 * Version to "New version" and Deploy. Without that step the old code keeps running.
 */

// The sheet this writes into: "Tanit XR site submissions" in Ines's Drive.
const SHEET_ID = '1bboWu3dxD_KRhSZooK39Bc1kYhuY2IsjNftF9lr04wc';

// Fields the forms use for their own plumbing, not worth a column.
const SKIP = ['_captcha', '_template', '_next', '_subject', '_honey', '_form'];

function doPost(e) {
  const lock = LockService.getScriptLock();
  lock.waitLock(20000);          // two people submitting at once must not collide
  try {
    const data = readBody(e);
    if (data._honey) return reply('ignored');          // the hidden field only bots fill in
    const name = String(data._form || 'other').replace(/[^a-z0-9-]/gi, '').slice(0, 40) || 'other';
    const sheet = tabFor(name);
    const fields = Object.keys(data).filter(k => SKIP.indexOf(k) === -1);
    const header = growHeader(sheet, fields);
    const row = header.map(h => {
      if (h === 'received') return new Date();
      if (h === 'status') return 'waiting';
      return data[h] === undefined ? '' : String(data[h]).slice(0, 4000);
    });
    sheet.appendRow(row);
    return reply('saved');
  } catch (err) {
    console.error(err);
    return reply('error');
  } finally {
    lock.releaseLock();
  }
}

function doGet() {
  return reply('ready');      // opening the URL in a browser should say something harmless
}

/** Form-encoded, or JSON, whichever the page sent. */
function readBody(e) {
  if (e && e.parameter && Object.keys(e.parameter).length) return e.parameter;
  if (e && e.postData && e.postData.contents) {
    try { return JSON.parse(e.postData.contents); } catch (x) { /* not JSON */ }
  }
  return {};
}

/** One tab per form, created the first time that form is used. */
function tabFor(name) {
  const ss = SpreadsheetApp.openById(SHEET_ID);
  let sheet = ss.getSheetByName(name);
  if (!sheet) {
    sheet = ss.insertSheet(name);
    sheet.appendRow(['received', 'status']);
    sheet.setFrozenRows(1);
    // "Sheet1" is the empty default; drop it once a real tab exists
    const first = ss.getSheetByName('Sheet1');
    if (first && first.getLastRow() === 0 && ss.getSheets().length > 1) ss.deleteSheet(first);
  }
  return sheet;
}

/** Header row that grows when a form gains a field, so nothing is silently dropped. */
function growHeader(sheet, fields) {
  let header = sheet.getLastColumn()
    ? sheet.getRange(1, 1, 1, sheet.getLastColumn()).getValues()[0].map(String)
    : [];
  if (header.indexOf('received') === -1) header.unshift('received');
  if (header.indexOf('status') === -1) header.splice(1, 0, 'status');
  const added = fields.filter(f => header.indexOf(f) === -1);
  if (added.length) {
    header = header.concat(added);
    sheet.getRange(1, 1, 1, header.length).setValues([header]);
    sheet.setFrozenRows(1);
  }
  return header;
}

function reply(word) {
  return ContentService.createTextOutput(JSON.stringify({ result: word }))
    .setMimeType(ContentService.MimeType.JSON);
}
