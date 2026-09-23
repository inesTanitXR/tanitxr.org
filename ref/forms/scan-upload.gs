/**
 * Tanit XR: receive a volunteer's scan file straight into Drive, from the drop zone on
 * tanitxr.org/scanning-guide/.
 *
 * PASTE THIS AT THE BOTTOM OF THE SAME SCRIPT that already has submissions.gs in it, then
 * Deploy > Manage deployments > pencil > Version: New version > Deploy. Google will ask for
 * permission to use your Drive the first time, because the files land there.
 *
 * Scans are big: the ones already in the Drive run from under a megabyte to 130 MB, and a
 * web app can only take about 50 MB in one request. So the file arrives in pieces. The
 * browser tries to send the pieces straight to Drive first, which is fastest; where the
 * browser is not allowed to talk to Drive directly, it sends each piece here instead and
 * this script passes it on. Either way the file is never held in one piece in memory.
 *
 * Everything lands in a Drive folder called "Tanit XR volunteer scans" and a row goes in the
 * "scans" tab of the submissions sheet, so an upload shows up next to every other form.
 */

var UPLOAD_FOLDER = 'Tanit XR volunteer scans';
var CHUNK_CACHE_HOURS = 6;

function uploadFolder_() {
  var it = DriveApp.getFoldersByName(UPLOAD_FOLDER);
  return it.hasNext() ? it.next() : DriveApp.createFolder(UPLOAD_FOLDER);
}

/** Ask Drive to open a resumable session, and hand back the address it gives us. */
function startUpload_(d) {
  var folder = uploadFolder_();
  var name = String(d.name || 'scan').replace(/[\\/\r\n]/g, '_').slice(0, 180);
  var size = Number(d.size || 0);
  if (!size || size > 2 * 1024 * 1024 * 1024) return reply('too-big');

  var res = UrlFetchApp.fetch(
    'https://www.googleapis.com/upload/drive/v3/files?uploadType=resumable&supportsAllDrives=true',
    {
      method: 'post',
      contentType: 'application/json; charset=UTF-8',
      headers: {
        Authorization: 'Bearer ' + ScriptApp.getOAuthToken(),
        'X-Upload-Content-Type': String(d.mime || 'application/octet-stream'),
        'X-Upload-Content-Length': String(size),
        // binds the session to the site, which is what lets the browser send pieces itself
        Origin: 'https://tanitxr.org',
      },
      payload: JSON.stringify({ name: name, parents: [folder.getId()] }),
      muteHttpExceptions: true,
    });
  if (res.getResponseCode() >= 300) return reply('no-session', { detail: res.getContentText().slice(0, 200) });

  var headers = res.getAllHeaders();
  var uri = headers.Location || headers.location;
  if (!uri) return reply('no-session');

  var key = Utilities.getUuid();
  CacheService.getScriptCache().put('up_' + key, JSON.stringify({
    uri: uri, size: size, name: name,
    who: String(d.who || ''), email: String(d.email || ''),
    about: String(d.about || ''), place: String(d.place || ''),
  }), CHUNK_CACHE_HOURS * 3600);
  return reply('ready', { key: key, direct: uri });
}

function session_(key) {
  var raw = CacheService.getScriptCache().get('up_' + key);
  return raw ? JSON.parse(raw) : null;
}

/** One piece of the file, passed on to Drive. */
function sendChunk_(d) {
  var s = session_(d.key);
  if (!s) return reply('expired');
  var bytes = Utilities.base64Decode(String(d.data || ''));
  var start = Number(d.offset || 0);
  var end = start + bytes.length - 1;

  var res = UrlFetchApp.fetch(s.uri, {
    method: 'put',
    contentType: 'application/octet-stream',
    headers: { 'Content-Range': 'bytes ' + start + '-' + end + '/' + s.size },
    payload: Utilities.newBlob(bytes).getBytes(),
    muteHttpExceptions: true,
  });
  var code = res.getResponseCode();
  if (code === 308) return reply('more', { received: end + 1 });         // Drive wants the next piece
  if (code === 200 || code === 201) return finish_(d.key, s, JSON.parse(res.getContentText()));
  return reply('chunk-failed', { code: code, detail: res.getContentText().slice(0, 200) });
}

/** The browser sent the pieces itself and Drive says it has them all. */
function finishDirect_(d) {
  var s = session_(d.key);
  if (!s) return reply('expired');
  var id = String(d.fileId || '');
  if (!id) return reply('no-file');
  return finish_(d.key, s, { id: id, name: s.name });
}

function finish_(key, s, file) {
  CacheService.getScriptCache().remove('up_' + key);
  var url = 'https://drive.google.com/file/d/' + file.id + '/view';
  try {
    var sheet = tabFor('scans');
    var header = growHeader(sheet, ['name', 'email', 'file', 'link', 'size_mb', 'about', 'place']);
    var row = header.map(function (h) {
      if (h === 'received') return new Date();
      if (h === 'status') return 'waiting';
      if (h === 'name') return s.who;
      if (h === 'email') return s.email;
      if (h === 'file') return s.name;
      if (h === 'link') return url;
      if (h === 'size_mb') return Math.round(s.size / 104857.6) / 10;
      if (h === 'about') return s.about;
      if (h === 'place') return s.place;
      return '';
    });
    sheet.appendRow(row);
  } catch (err) {
    console.error(err);      // the file is safely in Drive either way
  }
  try {
    MailApp.sendEmail({
      to: 'info@tanitxr.org',
      subject: 'New scan uploaded: ' + s.name,
      body: [s.who + ' <' + s.email + '> uploaded a scan.', '', 'File: ' + s.name,
             'Size: ' + Math.round(s.size / 1048576) + ' MB', 'What it is: ' + s.about,
             'Where: ' + s.place, '', url].join('\n'),
    });
  } catch (err) {
    console.error(err);
  }
  return reply('saved', { url: url });
}

/** Called by doPost in submissions.gs when the form says it is an upload. */
function handleUpload(data) {
  var act = String(data.action || '');
  if (act === 'upload-start') return startUpload_(data);
  if (act === 'upload-chunk') return sendChunk_(data);
  if (act === 'upload-done') return finishDirect_(data);
  if (act === 'upload-ping') return reply('uploads-on');
  return null;
}


/**
 * A plain view counter, because GoatCounter cannot be one.
 *
 * GoatCounter records one hit per visitor per day on purpose: it is built to count people,
 * not visits, and visiting the same page again today does not move its number at all (tested:
 * two more visits, number unchanged). That makes it the wrong instrument for "how many times
 * has this been opened", which is the number a video shows and the one Ines asked for.
 *
 * So the count is kept here instead, in the script's own properties: one number per page,
 * one up per load. It counts reloads, because that is what a view is.
 */
function pageViews_(d, bump) {
  var page = String(d.page || '').replace(/[^a-z0-9-]/gi, '').slice(0, 40) || 'explore';
  var key = 'views_' + page;
  var props = PropertiesService.getScriptProperties();
  if (!bump) return reply('views', { page: page, views: Number(props.getProperty(key) || 0) });

  var lock = LockService.getScriptLock();
  try {
    lock.waitLock(8000);
  } catch (e) {
    return reply('views', { page: page, views: Number(props.getProperty(key) || 0) });
  }
  try {
    var n = Number(props.getProperty(key) || 0) + 1;
    props.setProperty(key, String(n));
    return reply('views', { page: page, views: n });
  } finally {
    lock.releaseLock();
  }
}

/** Called by doPost in submissions.gs when the form says it is a view. */
function handleViews(data) {
  var act = String(data.action || '');
  if (act === 'view-bump') return pageViews_(data, true);
  if (act === 'view-read') return pageViews_(data, false);
  return null;
}
