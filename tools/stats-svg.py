#!/usr/bin/env python3
"""Regenerate assets/stats.svg -- contribution calendar + LeetCode totals.

ponytail: replaces four third-party card services with one file, so the panel
matches the ASCII portrait and nothing breaks when someone's Vercel app pauses.
Needs `gh` on PATH (authenticated locally, GITHUB_TOKEN in Actions).
"""
import json, os, subprocess, sys, urllib.request

USER, LEETCODE = "manankapoor23", "manankapoor23"
BG, DIM, FG = "#0d1117", "#8b949e", "#c9d1d9"
LEVELS = ["#161b22", "#0d2d4d", "#14507f", "#1f6feb", "#58a6ff"]   # one muted hue, five steps
CELL, GAP, PAD, LABEL = 11, 3, 16, 30
FS = 12

CAL = """query($u:String!){user(login:$u){contributionsCollection{contributionCalendar{
totalContributions weeks{firstDay contributionDays{weekday contributionCount date}}}}}}"""

LC = """query($u:String!){matchedUser(username:$u){submitStatsGlobal{
acSubmissionNum{difficulty count}}}}"""


def contributions():
    out = subprocess.run(["gh", "api", "graphql", "-f", f"query={CAL}", "-F", f"u={USER}"],
                         check=True, capture_output=True, text=True).stdout
    return json.loads(out)["data"]["user"]["contributionsCollection"]["contributionCalendar"]


def leetcode():
    req = urllib.request.Request(
        "https://leetcode.com/graphql",
        data=json.dumps({"query": LC, "variables": {"u": LEETCODE}}).encode(),
        headers={"Content-Type": "application/json", "Referer": "https://leetcode.com",
                 # leetcode 403s the default python-urllib agent
                 "User-Agent": "Mozilla/5.0 (compatible; profile-readme-stats)"})
    with urllib.request.urlopen(req, timeout=20) as r:
        stats = json.load(r)["data"]["matchedUser"]["submitStatsGlobal"]["acSubmissionNum"]
    return {s["difficulty"]: s["count"] for s in stats}


def build(cal, lc):
    weeks = cal["weeks"]
    active = sorted(d["contributionCount"] for w in weeks for d in w["contributionDays"]
                    if d["contributionCount"] > 0) or [1]
    # quartiles of the ACTIVE days, not of the peak -- one 40-commit day would
    # otherwise flatten every normal day down to the same shade
    cuts = [active[int(len(active) * q)] for q in (0.25, 0.5, 0.75)]

    def level(n):
        if n == 0:
            return 0
        return 1 + sum(n > c for c in cuts)

    pitch = CELL + GAP
    grid_x, grid_y = PAD + LABEL, PAD + 18
    w = grid_x + len(weeks) * pitch - GAP + PAD
    h = grid_y + 7 * pitch - GAP + 34

    o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
         f'role="img" aria-label="contribution calendar and LeetCode totals">',
         f'<rect width="100%" height="100%" rx="6" fill="{BG}"/>',
         f'<style>text{{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,'
         f'"Liberation Mono",monospace;font-size:{FS}px}}</style>']

    # one label per month, skipped when the previous one is too close to clear it
    seen, last = set(), -99
    for i, week in enumerate(weeks):
        month = week["firstDay"][:7]
        if month in seen or i - last < 3:
            continue
        seen.add(month); last = i
        name = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"][int(month[5:7]) - 1]
        o.append(f'<text x="{grid_x + i*pitch}" y="{PAD + 8}" fill="{DIM}">{name}</text>')

    for label, row in (("Mon", 1), ("Wed", 3), ("Fri", 5)):
        o.append(f'<text x="{PAD}" y="{grid_y + row*pitch + CELL - 1}" fill="{DIM}">{label}</text>')

    for i, week in enumerate(weeks):
        for day in week["contributionDays"]:
            x = grid_x + i * pitch
            y = grid_y + day["weekday"] * pitch
            o.append(f'<rect x="{x}" y="{y}" width="{CELL}" height="{CELL}" rx="2" '
                     f'fill="{LEVELS[level(day["contributionCount"])]}">'
                     f'<title>{day["date"]}: {day["contributionCount"]}</title></rect>')

    foot = grid_y + 7 * pitch + 16
    # one left-anchored line: text-anchor="end" would overflow under font fallback
    o.append(f'<text x="{grid_x}" y="{foot}" fill="{FG}">{cal["totalContributions"]:,}'
             f'<tspan fill="{DIM}"> contributions in the last year</tspan>'
             f'<tspan fill="{DIM}">    ·    </tspan>{lc["All"]}'
             f'<tspan fill="{DIM}"> solved on leetcode </tspan>'
             f'<tspan fill="{DIM}">(</tspan>{lc["Easy"]}<tspan fill="{DIM}">e </tspan>'
             f'{lc["Medium"]}<tspan fill="{DIM}">m </tspan>'
             f'{lc["Hard"]}<tspan fill="{DIM}">h)</tspan></text>')
    o.append("</svg>")
    return "\n".join(o)


if __name__ == "__main__":
    dest = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets", "stats.svg")
    cal, lc = contributions(), leetcode()
    open(dest, "w").write(build(cal, lc) + "\n")
    print(f"wrote {os.path.normpath(dest)}  {cal['totalContributions']} contributions, "
          f"{lc['All']} leetcode", file=sys.stderr)
