/**
 * Cloudflare Worker: tanitxr.org dynamic bits — volunteer profiles, reaction counts,
 * and view/click tracking for the opportunities board.
 *
 * Routes:
 *   POST /          or /profile  -> volunteer profile submission (GitHub commit)
 *   POST /track     {type, id}   -> increment a counter (view|click|thumbs|applied)
 *   GET  /stats                  -> all counters as {id: {type: count}}
 *
 * Extra setup vs. the profile-only version: add a KV namespace binding named STATS
 * (Worker -> Settings -> Bindings -> KV namespace).
 *
 * Replaces the old JetEngine "form creates a page" flow on the static site:
 *   1. create-profile.html POSTs here.
 *   2. The worker saves the submission as profiles/<slug>.json in the GitHub repo
 *      (so it is baked into the site at the next build), AND
 *   3. appends it to docs/profiles-live.json, which people.html reads at page load —
 *      so the profile card appears on Our People within ~1 minute, no rebuild needed.
 *
 * Setup: see worker/README.md
 * Secrets/vars: GITHUB_TOKEN (repo-scoped fine-grained token, Contents: read+write),
 *   REPO ("inesTanitXR/tanitxr.org"), AUTO_APPROVE ("true" to publish instantly,
 *   anything else = held for review with approved:false).
 */

const ALLOWED_ORIGINS = [
  "https://tanitxr.org",
  "https://www.tanitxr.org",
  "https://inestanitxr.github.io",
];

const cors = (origin) => ({
  "Access-Control-Allow-Origin": ALLOWED_ORIGINS.includes(origin) ? origin : ALLOWED_ORIGINS[0],
  "Access-Control-Allow-Methods": "POST, OPTIONS",
  "Access-Control-Allow-Headers": "Content-Type",
});

const slugify = (s) =>
  s.toLowerCase().normalize("NFKD").replace(/[̀-ͯ]/g, "")
    .replace(/[^a-z0-9]+/g, "-").replace(/^-+|-+$/g, "").slice(0, 60);

const clean = (v, max = 2000) =>
  String(v || "").replace(/<[^>]*>/g, "").trim().slice(0, max);

const cleanUrl = (v) => {
  const s = String(v || "").trim().slice(0, 300);
  return /^https:\/\/[\w.-]+\.[a-z]{2,}([/?#]\S*)?$/i.test(s) ? s : "";
};

async function gh(env, method, path, body) {
  const r = await fetch(`https://api.github.com/repos/${env.REPO}/${path}`, {
    method,
    headers: {
      Authorization: `Bearer ${env.GITHUB_TOKEN}`,
      "User-Agent": "tanitxr-profile-worker",
      Accept: "application/vnd.github+json",
    },
    body: body ? JSON.stringify(body) : undefined,
  });
  if (r.status === 404) return null;
  if (!r.ok) throw new Error(`GitHub ${path}: ${r.status} ${await r.text()}`);
  return r.json();
}

const b64encode = (s) => btoa(unescape(encodeURIComponent(s)));
const b64decode = (s) => decodeURIComponent(escape(atob(s.replace(/\n/g, ""))));

export default {
  async fetch(request, env) {
    const origin = request.headers.get("Origin") || "";
    if (request.method === "OPTIONS") {
      return new Response(null, { headers: cors(origin) });
    }
    const path = new URL(request.url).pathname;

    if (path === "/stats" && request.method === "GET") {
      const out = {};
      if (env.STATS) {
        let cursor;
        do {
          const page = await env.STATS.list({ prefix: "cnt:", cursor });
          for (const k of page.keys) {
            const [, type, ...idParts] = k.name.split(":");
            const id = idParts.join(":");
            out[id] = out[id] || {};
            out[id][type] = parseInt((await env.STATS.get(k.name)) || "0", 10);
          }
          cursor = page.list_complete ? null : page.cursor;
        } while (cursor);
      }
      return new Response(JSON.stringify(out), {
        headers: { "Content-Type": "application/json", "Cache-Control": "max-age=60", ...cors(origin) },
      });
    }

    if (request.method !== "POST") {
      return new Response("POST only", { status: 405, headers: cors(origin) });
    }

    if (path === "/track") {
      if (!env.STATS) return new Response("no STATS binding", { status: 500, headers: cors(origin) });
      let body = {};
      try { body = await request.json(); } catch {}
      const type = String(body.type || "");
      const id = String(body.id || "").toLowerCase().replace(/[^a-z0-9-]/g, "").slice(0, 80);
      if (!["view", "click", "thumbs", "applied"].includes(type) || !id) {
        return new Response("bad request", { status: 400, headers: cors(origin) });
      }
      const key = `cnt:${type}:${id}`;
      const cur = parseInt((await env.STATS.get(key)) || "0", 10);
      await env.STATS.put(key, String(cur + 1));
      return new Response("ok", { headers: cors(origin) });
    }

    let data;
    const ct = request.headers.get("Content-Type") || "";
    if (ct.includes("application/json")) data = await request.json();
    else data = Object.fromEntries((await request.formData()).entries());

    if (data._honey) return new Response("ok", { headers: cors(origin) }); // bot trap

    const profile = {
      name: clean(data.name, 80),
      role: clean(data.role, 100),
      bio: clean(data.bio, 1200),
      photo: cleanUrl(data.photo_url || data.photo),
      linkedin: cleanUrl(data.linkedin),
      instagram: cleanUrl(data.instagram),
      website: cleanUrl(data.website),
      email: clean(data.email, 120), // kept in profiles/ (private repo data), never rendered
      submitted: new Date().toISOString(),
      approved: env.AUTO_APPROVE === "true",
    };
    if (!profile.name || !profile.role || !profile.bio) {
      return new Response("Missing required fields", { status: 400, headers: cors(origin) });
    }

    const slug = slugify(profile.name) || `volunteer-${Date.now()}`;

    // 1. store the submission for the next site build
    const path = `contents/profiles/${slug}.json`;
    const existing = await gh(env, "GET", path);
    await gh(env, "PUT", path, {
      message: `Volunteer profile submission: ${profile.name}`,
      content: b64encode(JSON.stringify(profile, null, 1)),
      ...(existing ? { sha: existing.sha } : {}),
    });

    // 2. surface it on the live site immediately (people.html reads this file)
    if (profile.approved) {
      const livePath = "contents/docs/profiles-live.json";
      const liveFile = await gh(env, "GET", livePath);
      let live = [];
      try { live = JSON.parse(b64decode(liveFile ? liveFile.content : "W10=")); } catch {}
      live = live.filter((p) => slugify(p.name || "") !== slug);
      const { email, ...pub } = profile; // never publish the email address
      live.push(pub);
      await gh(env, "PUT", livePath, {
        message: `Publish live profile: ${profile.name}`,
        content: b64encode(JSON.stringify(live, null, 1)),
        ...(liveFile ? { sha: liveFile.sha } : {}),
      });
    }

    // friendly redirect back to the site for plain form posts
    if (!ct.includes("application/json")) {
      const back = ALLOWED_ORIGINS.includes(origin) ? origin : ALLOWED_ORIGINS[0];
      return Response.redirect(`${back}/people.html?submitted=1`, 303);
    }
    return new Response(JSON.stringify({ ok: true, slug, approved: profile.approved }), {
      headers: { "Content-Type": "application/json", ...cors(origin) },
    });
  },
};
