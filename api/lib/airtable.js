const Airtable = require("airtable");

const base = new Airtable({ apiKey: process.env.AIRTABLE_API_KEY }).base(
  process.env.AIRTABLE_BASE_ID
);

const TABLE_ID = process.env.AIRTABLE_TABLE_ID;

// Cache Slack user profiles to avoid redundant API calls
const slackUserCache = new Map();
const SLACK_CACHE_MAX = 500;
const SLACK_ID_RE = /^U[A-Z0-9]{8,}$/;

async function fetchSlackUser(slackId) {
  if (!slackId) return null;
  if (!SLACK_ID_RE.test(slackId)) return null;
  if (slackUserCache.has(slackId)) return slackUserCache.get(slackId);
  if (slackUserCache.size >= SLACK_CACHE_MAX) {
    // Evict the oldest entry
    slackUserCache.delete(slackUserCache.keys().next().value);
  }

  try {
    const response = await fetch(
      `https://slack.com/api/users.info?user=${encodeURIComponent(slackId)}`,
      {
        headers: {
          Authorization: `Bearer ${process.env.SLACK_BOT_TOKEN}`,
        },
      }
    );
    const data = await response.json();
    if (!data.ok) return null;

    const profile = data.user.profile;
    const user = {
      displayName: profile.display_name || profile.real_name || slackId,
      avatar: profile.image_72 || profile.image_48 || null,
    };
    slackUserCache.set(slackId, user);
    return user;
  } catch {
    return null;
  }
}

async function fetchAllHackpads() {
  const records = await base(TABLE_ID)
    .select({
      view: "Grid view",
    })
    .all();

  const hackpads = await Promise.all(
    records.map(async (record) => {
      const slackId = record.get("Slack ID");
      const slackUser = await fetchSlackUser(slackId);
      const pictures = record.get("Picture") || [];

      return {
        id: record.id,
        description: record.get("Description"),
        repoUrl: record.get("Repo URL"),
        program: record.get("Program"),
        hoursSpent: record.get("hours_spent"),
        createdAt: record.get("Created"),
        images: pictures.map((p) => ({
          url: p.url,
          thumbnail: p.thumbnails?.large?.url || p.url,
        })),
        slackId,
        submitter: slackUser
          ? {
              displayName: slackUser.displayName,
              avatar: slackUser.avatar,
            }
          : null,
      };
    })
  );

  return hackpads;
}

async function fetchHackpadById(id) {
  const record = await base(TABLE_ID).find(id);
  const slackId = record.get("Slack ID");
  const slackUser = await fetchSlackUser(slackId);
  const pictures = record.get("Picture") || [];

  return {
    id: record.id,
    description: record.get("Description"),
    repoUrl: record.get("Repo URL"),
    program: record.get("Program"),
    hoursSpent: record.get("hours_spent"),
    createdAt: record.get("Created"),
    images: pictures.map((p) => ({
      url: p.url,
      thumbnail: p.thumbnails?.large?.url || p.url,
    })),
    slackId,
    submitter: slackUser
      ? {
          displayName: slackUser.displayName,
          avatar: slackUser.avatar,
        }
      : null,
  };
}

function computeStats(hackpads) {
  return {
    totalSubmissions: hackpads.length,
    programs: [...new Set(hackpads.map((h) => h.program))].filter(Boolean),
    totalHoursSpent: hackpads.reduce((sum, h) => sum + (h.hoursSpent || 0), 0),
  };
}

const SIGNUPS_TABLE_ID =
  process.env.AIRTABLE_SIGNUPS_TABLE_ID || "tblTGUmUnqZ6NlCUL";

async function signupExists(email) {
  const escaped = email.replace(/\\/g, "\\\\").replace(/"/g, '\\"');
  const records = await base(SIGNUPS_TABLE_ID)
    .select({
      filterByFormula: `LOWER({email}) = "${escaped}"`,
      maxRecords: 1,
      fields: ["email"],
    })
    .firstPage();
  return records.length > 0;
}

async function createSignup({ email, source, ipAddress }) {
  if (await signupExists(email)) return { duplicate: true };
  await base(SIGNUPS_TABLE_ID).create([
    { fields: { email, source, ip_address: ipAddress } },
  ]);
  return { duplicate: false };
}

module.exports = {
  createSignup,
  fetchAllHackpads,
  fetchHackpadById,
  computeStats,
};
