"""Generates the dark-theme SVG assets used by README.md into ../assets/.

Run:  python scripts/build_assets.py
Everything is plain SVG (no external fonts/images) so GitHub's image proxy always renders it.
"""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "assets"
OUT.mkdir(exist_ok=True)

FONT = "Segoe UI, Inter, -apple-system, Helvetica Neue, Arial, sans-serif"
MONO = "Cascadia Code, JetBrains Mono, Fira Code, Consolas, Menlo, monospace"

BG = "#0d1117"
CARD = "#161b22"
BORDER = "#30363d"
TEXT = "#f0f6fc"
MUTED = "#8b949e"
BLUE = "#58a6ff"
PURPLE = "#bc8cff"
GREEN = "#3fb950"
ORANGE = "#d29922"


def esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


# --------------------------------------------------------------------------- hero
def hero() -> str:
    W, H = 1200, 360
    taglines = [
        "Building agentic AI that asks before it acts",
        "Event-driven ML platforms on GCP and Kubernetes",
        "Retrieval pipelines over 600K+ SEC filings",
        "Backends that stay under 200 ms at 300+ req/s",
    ]
    n = len(taglines)
    cycle = 3.2 * n
    tag_svg = ""
    for i, t in enumerate(taglines):
        # one shared cycle; line i is visible only during its 1/n slot (fade in, hold, fade out)
        s, e = i / n, (i + 1) / n
        fade = 0.15 / n
        keys = ";".join(f"{k:.4f}" for k in [0, s, s + fade, e - fade, e, 1])
        tag_svg += f"""
    <text x="88" y="300" font-family="{MONO}" font-size="20" fill="{BLUE}" opacity="0">{esc(t)}
      <animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="{keys}" dur="{cycle:.1f}s" repeatCount="indefinite" calcMode="linear"/>
    </text>"""

    term_lines = [
        ("$", "adwait --status", TEXT),
        ("role", "AI Engineer Intern @ C-Suite Comp", GREEN),
        ("study", "M.S. CS · CU Boulder · class of 2027", PURPLE),
        ("building", "agentic incident-response platform", ORANGE),
        ("stack", "python · fastapi · gcp · k8s · faiss", BLUE),
        ("focus", "LLM systems · MLOps · backends", MUTED),
    ]
    term = ""
    for i, (k, v, c) in enumerate(term_lines):
        y = 118 + i * 30
        if k == "$":
            term += f'<text x="750" y="{y}" font-family="{MONO}" font-size="15" fill="{MUTED}">$ <tspan fill="{TEXT}">{esc(v)}</tspan></text>'
        else:
            term += (
                f'<text x="750" y="{y}" font-family="{MONO}" font-size="15" fill="{MUTED}">{k:<9}</text>'
                f'<text x="852" y="{y}" font-family="{MONO}" font-size="15" fill="{c}">{esc(v)}</text>'
            )

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Adwait Desai - AI Engineer">
  <defs>
    <radialGradient id="g1" cx="12%" cy="10%" r="55%"><stop offset="0" stop-color="#1f6feb" stop-opacity="0.45"/><stop offset="1" stop-color="#1f6feb" stop-opacity="0"/></radialGradient>
    <radialGradient id="g2" cx="92%" cy="100%" r="55%"><stop offset="0" stop-color="#8957e5" stop-opacity="0.40"/><stop offset="1" stop-color="#8957e5" stop-opacity="0"/></radialGradient>
    <linearGradient id="accent" x1="0" x2="1"><stop offset="0" stop-color="#58a6ff"/><stop offset="1" stop-color="#bc8cff"/></linearGradient>
    <pattern id="dots" width="24" height="24" patternUnits="userSpaceOnUse"><circle cx="1.5" cy="1.5" r="1.2" fill="#30363d"/></pattern>
    <clipPath id="round"><rect width="{W}" height="{H}" rx="18"/></clipPath>
  </defs>
  <g clip-path="url(#round)">
    <rect width="{W}" height="{H}" fill="{BG}"/>
    <rect width="{W}" height="{H}" fill="url(#dots)"/>
    <rect width="{W}" height="{H}" fill="url(#g1)"/>
    <rect width="{W}" height="{H}" fill="url(#g2)"/>
  </g>
  <rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="18" fill="none" stroke="{BORDER}"/>

  <!-- left: name + role -->
  <rect x="60" y="78" width="6" height="150" rx="3" fill="url(#accent)"/>
  <text x="88" y="130" font-family="{FONT}" font-size="66" font-weight="800" fill="{TEXT}" letter-spacing="-1">Adwait Desai</text>
  <text x="88" y="176" font-family="{FONT}" font-size="22" font-weight="600" fill="{MUTED}">AI Engineer  ·  Backend &amp; Cloud Systems  ·  MLOps</text>
  <text x="88" y="212" font-family="{FONT}" font-size="17" fill="{MUTED}">M.S. Computer Science @ CU Boulder  ·  Patent co-author  ·  2 publications</text>

  <text x="60" y="300" font-family="{MONO}" font-size="20" fill="{GREEN}">&gt;</text>{tag_svg}

  <!-- right: terminal card -->
  <rect x="730" y="60" width="440" height="236" rx="12" fill="{CARD}" stroke="{BORDER}"/>
  <rect x="730" y="60" width="440" height="34" rx="12" fill="#21262d"/>
  <rect x="730" y="82" width="440" height="12" fill="#21262d"/>
  <circle cx="750" cy="77" r="5" fill="#ff5f56"/><circle cx="768" cy="77" r="5" fill="#ffbd2e"/><circle cx="786" cy="77" r="5" fill="#27c93f"/>
  <text x="950" y="82" text-anchor="middle" font-family="{MONO}" font-size="12" fill="{MUTED}">adwait39 — zsh</text>
  {term}
  <rect x="750" y="284" width="9" height="16" fill="{TEXT}"><animate attributeName="opacity" values="1;0;1" dur="1.1s" repeatCount="indefinite"/></rect>
</svg>
"""


# ------------------------------------------------------------------ section headers
def section(index: str, title: str, subtitle: str = "") -> str:
    W, H = 1200, 76
    sub = f'<text x="{W-32}" y="47" text-anchor="end" font-family="{FONT}" font-size="15" fill="{MUTED}">{esc(subtitle)}</text>' if subtitle else ""
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{esc(title)}">
  <defs><linearGradient id="a" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#58a6ff"/><stop offset="1" stop-color="#bc8cff"/></linearGradient></defs>
  <rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="12" fill="{CARD}" stroke="{BORDER}"/>
  <rect x="0" y="14" width="6" height="{H-28}" rx="3" fill="url(#a)"/>
  <text x="32" y="48" font-family="{MONO}" font-size="20" fill="{BLUE}">{index}</text>
  <text x="76" y="49" font-family="{FONT}" font-size="26" font-weight="700" fill="{TEXT}">{esc(title)}</text>
  {sub}
</svg>
"""


# ------------------------------------------------------------------------ footer
def footer() -> str:
    W, H = 1200, 150
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="footer">
  <defs>
    <linearGradient id="w" x1="0" x2="1"><stop offset="0" stop-color="#1f6feb"/><stop offset="1" stop-color="#8957e5"/></linearGradient>
    <clipPath id="r"><rect width="{W}" height="{H}" rx="18"/></clipPath>
  </defs>
  <g clip-path="url(#r)">
    <rect width="{W}" height="{H}" fill="{BG}"/>
    <path d="M0 95 C 200 60, 400 130, 600 95 S 1000 60, 1200 95 L1200 150 L0 150 Z" fill="url(#w)" opacity="0.35"/>
    <path d="M0 110 C 250 80, 450 140, 700 105 S 1050 80, 1200 110 L1200 150 L0 150 Z" fill="url(#w)" opacity="0.55"/>
  </g>
  <rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="18" fill="none" stroke="{BORDER}"/>
  <text x="600" y="52" text-anchor="middle" font-family="{FONT}" font-size="22" font-weight="700" fill="{TEXT}">Open to AI / backend / platform engineering roles</text>
  <text x="600" y="80" text-anchor="middle" font-family="{MONO}" font-size="15" fill="{MUTED}">adwaitd393@gmail.com  ·  linkedin.com/in/adwaitpdesai  ·  github.com/adwait39</text>
</svg>
"""


if __name__ == "__main__":
    files = {
        "hero.svg": hero(),
        "footer.svg": footer(),
        "section-about.svg": section("01", "About", "who I am and what I am working on"),
        "section-experience.svg": section("02", "Experience", "internships, research and teaching"),
        "section-projects.svg": section("03", "Projects", "open source and selected private work"),
        "section-skills.svg": section("04", "Skills", "consolidated from what I have actually shipped"),
        "section-achievements.svg": section("05", "Research & Achievements", "patent, publications, competitions"),
        "section-github.svg": section("06", "GitHub Activity", "auto-updated daily"),
    }
    for name, svg in files.items():
        (OUT / name).write_text(svg, encoding="utf-8", newline="\n")
        print("wrote", OUT / name)
