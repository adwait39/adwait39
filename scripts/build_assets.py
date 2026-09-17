"""Generates every dark-theme SVG card used by README.md into ../assets/.

Run:  python scripts/build_assets.py
Plain SVG only (system fonts, no external images) so GitHub's image proxy always renders it,
and the cards look identical in GitHub's light and dark themes.
"""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "assets"
OUT.mkdir(exist_ok=True)

FONT = "Segoe UI, Inter, -apple-system, Helvetica Neue, Arial, sans-serif"
MONO = "Cascadia Code, JetBrains Mono, Fira Code, Consolas, Menlo, monospace"

BG, CARD, CARD2, BORDER = "#0d1117", "#161b22", "#1c2129", "#30363d"
TEXT, BODY, MUTED = "#f0f6fc", "#c9d1d9", "#8b949e"
BLUE, PURPLE, GREEN, ORANGE, PINK, CYAN = "#58a6ff", "#bc8cff", "#3fb950", "#d29922", "#f778ba", "#39d2c0"


def esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def wrap(text: str, max_chars: int) -> list[str]:
    words, lines, cur = text.split(), [], ""
    for w in words:
        if len(cur) + len(w) + 1 > max_chars and cur:
            lines.append(cur)
            cur = w
        else:
            cur = f"{cur} {w}".strip()
    if cur:
        lines.append(cur)
    return lines


def defs() -> str:
    return f"""<defs>
    <linearGradient id="accent" x1="0" x2="1"><stop offset="0" stop-color="{BLUE}"/><stop offset="1" stop-color="{PURPLE}"/></linearGradient>
    <radialGradient id="glowA" cx="0%" cy="0%" r="70%"><stop offset="0" stop-color="#1f6feb" stop-opacity="0.35"/><stop offset="1" stop-color="#1f6feb" stop-opacity="0"/></radialGradient>
    <radialGradient id="glowB" cx="100%" cy="100%" r="70%"><stop offset="0" stop-color="#8957e5" stop-opacity="0.30"/><stop offset="1" stop-color="#8957e5" stop-opacity="0"/></radialGradient>
    <pattern id="dots" width="24" height="24" patternUnits="userSpaceOnUse"><circle cx="1.5" cy="1.5" r="1.2" fill="{BORDER}"/></pattern>
  </defs>"""


def card_bg(W: int, H: int, r: int = 18, glow: bool = True) -> str:
    g = f'<rect width="{W}" height="{H}" fill="url(#dots)"/><rect width="{W}" height="{H}" fill="url(#glowA)"/><rect width="{W}" height="{H}" fill="url(#glowB)"/>' if glow else ""
    return f"""<clipPath id="clip"><rect width="{W}" height="{H}" rx="{r}"/></clipPath>
  <g clip-path="url(#clip)"><rect width="{W}" height="{H}" fill="{BG}"/>{g}</g>
  <rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="{r}" fill="none" stroke="{BORDER}"/>"""


def chips(items: list[tuple[str, str]], x: int, y: int, max_x: int, size: float = 12) -> tuple[str, int]:
    """Rounded pill chips that wrap; returns (svg, y of last row)."""
    out, cx, cy, cw = "", x, y, size * 0.62
    for label, color in items:
        w = int(len(label) * cw + 30)
        if cx + w > max_x:
            cx, cy = x, cy + 32
        out += (
            f'<rect x="{cx}" y="{cy}" width="{w}" height="24" rx="12" fill="{CARD2}" stroke="{BORDER}"/>'
            f'<circle cx="{cx+13}" cy="{cy+12}" r="3.5" fill="{color}"/>'
            f'<text x="{cx+23}" y="{cy+16.5}" font-family="{MONO}" font-size="{size}" fill="{BODY}">{esc(label)}</text>'
        )
        cx += w + 8
    return out, cy


# --------------------------------------------------------------------------- hero
def hero() -> str:
    W, H = 900, 330
    taglines = [
        "Building agentic AI that asks before it acts",
        "Event-driven ML platforms on GCP and Kubernetes",
        "Retrieval pipelines over 600K+ SEC filings",
        "Backends that stay under 200 ms at 300+ req/s",
    ]
    n, cycle, tag = len(taglines), 3.2 * len(taglines), ""
    for i, t in enumerate(taglines):
        s, e, fade = i / n, (i + 1) / n, 0.15 / n
        keys = ";".join(f"{k:.4f}" for k in [0, s, s + fade, e - fade, e, 1])
        tag += f'<text x="72" y="280" font-family="{MONO}" font-size="17" fill="{BLUE}" opacity="0">{esc(t)}<animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="{keys}" dur="{cycle:.1f}s" repeatCount="indefinite"/></text>'

    rows = [("role", "AI Intern @ C-Suite Comp", GREEN), ("study", "M.S. CS · CU Boulder '27", PURPLE),
            ("building", "agentic incident response", ORANGE), ("stack", "python · fastapi · gcp", BLUE),
            ("focus", "LLM systems · MLOps", MUTED)]
    term = f'<text x="566" y="112" font-family="{MONO}" font-size="14" fill="{MUTED}">$ <tspan fill="{TEXT}">adwait --status</tspan></text>'
    for i, (k, v, c) in enumerate(rows):
        y = 142 + i * 29
        term += f'<text x="566" y="{y}" font-family="{MONO}" font-size="14" fill="{MUTED}">{k}</text><text x="650" y="{y}" font-family="{MONO}" font-size="14" fill="{c}">{esc(v)}</text>'

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Adwait Desai">
  {defs()}
  {card_bg(W, H)}
  <rect x="48" y="72" width="6" height="140" rx="3" fill="url(#accent)"/>
  <text x="72" y="122" font-family="{FONT}" font-size="54" font-weight="800" fill="{TEXT}" letter-spacing="-1">Adwait Desai</text>
  <text x="72" y="162" font-family="{FONT}" font-size="20" font-weight="600" fill="{MUTED}">AI Engineer  ·  Backend &amp; Cloud  ·  MLOps</text>
  <text x="72" y="196" font-family="{FONT}" font-size="16" fill="{MUTED}">M.S. CS @ CU Boulder  ·  Patent co-author  ·  2 publications</text>
  <text x="48" y="280" font-family="{MONO}" font-size="17" fill="{GREEN}">&gt;</text>{tag}
  <rect x="548" y="56" width="304" height="230" rx="12" fill="{CARD}" stroke="{BORDER}"/>
  <rect x="548" y="56" width="304" height="34" rx="12" fill="#21262d"/><rect x="548" y="78" width="304" height="12" fill="#21262d"/>
  <circle cx="568" cy="73" r="5" fill="#ff5f56"/><circle cx="586" cy="73" r="5" fill="#ffbd2e"/><circle cx="604" cy="73" r="5" fill="#27c93f"/>
  <text x="700" y="78" text-anchor="middle" font-family="{MONO}" font-size="12" fill="{MUTED}">adwait39 — zsh</text>
  {term}
  <rect x="566" y="272" width="8" height="15" fill="{TEXT}"><animate attributeName="opacity" values="1;0;1" dur="1.1s" repeatCount="indefinite"/></rect>
</svg>
"""


# ----------------------------------------------------------------------- projects
PROJECTS = [
    dict(slug="drift", title="Distributed Data Drift Detection", tag="Open source · Jan – Mar 2026", color=BLUE,
         body="Event-driven MLOps platform: uploads return instantly while background workers run four drift detectors (semantic, lexical, topic, OOD) and persist results. 5 independently deployable services with retries, idempotency and dead-letter queues.",
         chips=[("FastAPI", GREEN), ("Pub/Sub", BLUE), ("RabbitMQ", ORANGE), ("MinIO", PINK), ("PostgreSQL", BLUE), ("Terraform", PURPLE)]),
    dict(slug="msaas", title="Music Separation as a Service", tag="Open source · Sep – Dec 2025", color=PURPLE,
         body="Kubernetes/GKE backend that splits songs into four stems with Demucs. Jobs run 3–4x the audio length, so they flow through Redis queues to worker pods and land in MinIO; API, queue and workers scale independently, observed with Prometheus and Grafana.",
         chips=[("Kubernetes", BLUE), ("GKE", BLUE), ("Redis", PINK), ("MinIO", PINK), ("Prometheus", ORANGE), ("Grafana", ORANGE)]),
    dict(slug="incident", title="Agentic AI Incident Response", tag="In progress · design doc first", color=ORANGE,
         body="An on-call copilot. Alertmanager fires, a LangGraph state machine triages, diagnoses and verifies against logs, metrics, Kubernetes state and runbooks, then proposes a fix that only runs after a human approves.",
         chips=[("LangGraph", GREEN), ("FastAPI", GREEN), ("Prometheus", ORANGE), ("Kubernetes", BLUE), ("Human-in-the-loop", PURPLE)]),
    dict(slug="agents", title="Multi-Agent Financial Research", tag="Private · May – Aug 2026", color=GREEN,
         body="Four cooperating agents (planner, evidence-gatherer over 8+ tools, analyst, fact-checker) research a company end to end. On 100+ questions: 87% task completion, +15 pts over single-agent, 95% of claims cited.",
         chips=[("Tool calling", BLUE), ("MCP", PURPLE), ("FAISS", BLUE), ("LLM-as-a-Judge", ORANGE), ("SEC filings", MUTED)]),
    dict(slug="matching", title="AI Resume Screening & Matching", tag="Private · May – Aug 2026", color=PINK,
         body="Two-tower embedding retrieval with FAISS narrows 5M+ candidate–job interactions by 99.9% while keeping 97% of true matches in the top 100; LightGBM reranks on 30+ features (+18% NDCG@10). Served under 80 ms p95 at 1,000+ req/s.",
         chips=[("PyTorch", ORANGE), ("FAISS", BLUE), ("LightGBM", GREEN), ("FastAPI", GREEN), ("Redis", PINK)]),
    dict(slug="network", title="Network Protocol Regression Platform", tag="Private · Oct – Dec 2025", color=CYAN,
         body="A testbed of 20+ containerized routers running OSPF-style link-state routing, validated by 100+ PyTest/Scapy regression tests and 50+ injected failures. Angular + RxJS + WebSockets dashboard renders the live topology.",
         chips=[("Angular", PINK), ("RxJS", PURPLE), ("WebSockets", BLUE), ("Docker", BLUE), ("Scapy", GREEN)]),
]


def project_card(p: dict, fixed_h: int | None = None) -> str:
    W = 440
    lines = wrap(p["body"], 50)[:7]
    body = "".join(f'<text x="24" y="{102 + i*23}" font-family="{FONT}" font-size="15" fill="{BODY}">{esc(l)}</text>' for i, l in enumerate(lines))
    chip_y = 102 + len(lines) * 23 + 4
    ch, last = chips(p["chips"], 24, chip_y, W - 16, 12)
    H = fixed_h or (last + 24 + 22)
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{esc(p['title'])}">
  {defs()}
  {card_bg(W, H, 16, glow=False)}
  <rect x="0" y="0" width="{W}" height="4" fill="{p['color']}" clip-path="url(#clip)"/>
  <text x="24" y="46" font-family="{FONT}" font-size="20" font-weight="700" fill="{TEXT}">{esc(p['title'])}</text>
  <text x="24" y="70" font-family="{MONO}" font-size="12.5" fill="{MUTED}">{esc(p['tag'])}</text>
  {body}
  {ch}
</svg>
"""


# --------------------------------------------------------------------- experience
EXPERIENCE = [
    ("AI Engineer Intern", "C-Suite Comp · Houston, TX (remote)", "Jul 2026 – Present", GREEN,
     "4 production data + LLM pipelines on GCP over 609K SEC filings · multi-company RAG 15 min → 3 min · projected AI cost $20K → $75/yr"),
    ("Graduate Teaching Assistant", "Remote Sensing Lab · CU Boulder", "Aug 2026 – Present", CYAN,
     "Debug Python/MATLAB ML code with 100+ students across 6 modules; code reviews and technical interviews for research projects"),
    ("Graduate Research Assistant", "Quantitative ML · CU Boulder", "May – Aug 2026", PURPLE,
     "Dividend-date forecasting over 340+ companies: 83% date accuracy, 91% precision on rare events · versioned artifacts + gated releases"),
    ("Full Stack Engineer Intern", "Techpeek · Bengaluru, India", "Sep 2024 – Jan 2025", ORANGE,
     "Billing + LLM gateway for 3 subscription tiers · 10K payment events replayed with zero duplicates · 300+ req/s under 200 ms p95"),
]


def experience() -> str:
    W, step, top = 900, 122, 40
    H = top + step * len(EXPERIENCE)
    out = f'<line x1="48" y1="{top}" x2="48" y2="{H-34}" stroke="{BORDER}" stroke-width="2"/>'
    for i, (role, org, when, color, hl) in enumerate(EXPERIENCE):
        y = top + i * step + 12
        hl_lines = wrap(hl, 98)[:2]
        hl_svg = "".join(f'<text x="78" y="{y+60+j*22}" font-family="{FONT}" font-size="15" fill="{BODY}">{esc(l)}</text>' for j, l in enumerate(hl_lines))
        out += f"""
  <circle cx="48" cy="{y+4}" r="9" fill="{BG}" stroke="{color}" stroke-width="3"/>
  <text x="78" y="{y+11}" font-family="{FONT}" font-size="21" font-weight="700" fill="{TEXT}">{esc(role)}</text>
  <text x="78" y="{y+35}" font-family="{FONT}" font-size="15" fill="{MUTED}">{esc(org)}</text>
  <text x="{W-32}" y="{y+11}" text-anchor="end" font-family="{MONO}" font-size="14" fill="{color}">{esc(when)}</text>
  {hl_svg}"""
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Experience">
  {defs()}
  {card_bg(W, H)}
  {out}
</svg>
"""


# ------------------------------------------------------------------------- skills
SKILLS = [
    ("Languages", BLUE, ["Python", "TypeScript", "JavaScript", "Java", "C++", "Go", "SQL", "MATLAB", "Bash"]),
    ("LLM & Agents", PURPLE, ["RAG", "Multi-agent orchestration", "Tool calling", "MCP", "Structured outputs", "Guardrails & approval gates", "Semantic caching", "Model routing", "LLM-as-a-Judge", "Inference gateways"]),
    ("Retrieval & ML", PINK, ["FAISS", "BM25", "Dense embeddings", "Hybrid retrieval", "Reranking", "LightGBM", "Ensembles", "Calibrated probabilities", "Hazard modeling", "Time-aware validation", "PyTorch", "scikit-learn", "Pandas", "NumPy"]),
    ("Backend & Data", GREEN, ["FastAPI", "Flask", "Django", "Node.js", "Express", "REST", "Webhooks", "Idempotency", "Rate limiting", "PostgreSQL", "MongoDB Atlas", "Redis", "MinIO", "RabbitMQ", "Google Pub/Sub", "Event-driven architecture"]),
    ("Cloud & DevOps", ORANGE, ["GCP", "Cloud Run", "Cloud Build", "Secret Manager", "VPC", "AWS", "Docker", "Kubernetes / GKE", "Terraform", "CI/CD", "GitHub Actions", "Distributed locking", "Checkpointing", "OpenTelemetry", "Prometheus", "Grafana", "Linux"]),
    ("Frontend & Testing", CYAN, ["React", "Angular", "Svelte / SvelteKit", "Redux Toolkit", "RxJS", "WebSockets", "Tailwind CSS", "PyTest", "Playwright", "React Testing Library", "Load testing", "Fault injection"]),
]


def skills() -> str:
    W, y, out = 900, 30, ""
    for label, color, items in SKILLS:
        out += f'<text x="28" y="{y+17}" font-family="{MONO}" font-size="14" font-weight="700" fill="{color}">{esc(label)}</text>'
        ch, last = chips([(s, color) for s in items], 200, y, W - 24, 12.5)
        out += ch
        y = last + 46
    H = y - 6
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Skills">
  {defs()}
  {card_bg(W, H, 18, glow=False)}
  {out}
</svg>
"""


# --------------------------------------------------------------------- highlights
def highlights() -> str:
    W, H = 900, 168
    tiles = [("1", "patent co-authored", "NLP and information retrieval, shipped as a product", PURPLE),
             ("2", "international publications", "Journal of Scientific Computing, and one more", BLUE),
             ("Top 10", "AWS GameDay 2026", "3rd place, PICT Hackathon 2025", ORANGE),
             ("Bloomberg", "and CFO.com cited research", "built the data infrastructure behind it", GREEN)]
    gap = 16
    tw = (W - 5 * gap) // 4
    out = ""
    for i, (big, cap, sub, color) in enumerate(tiles):
        x = gap + i * (tw + gap)
        out += f"""
  <rect x="{x}" y="{gap}" width="{tw}" height="{H-2*gap}" rx="14" fill="{CARD}" stroke="{BORDER}"/>
  <rect x="{x}" y="{gap}" width="4" height="{H-2*gap}" rx="2" fill="{color}"/>
  <text x="{x+20}" y="{gap+48}" font-family="{FONT}" font-size="32" font-weight="800" fill="{TEXT}">{esc(big)}</text>
  <text x="{x+20}" y="{gap+72}" font-family="{FONT}" font-size="14" font-weight="600" fill="{color}">{esc(cap)}</text>""" + "".join(f'<text x="{x+20}" y="{gap+94+j*17}" font-family="{FONT}" font-size="12.5" fill="{MUTED}">{esc(l)}</text>' for j, l in enumerate(wrap(sub, 30)[:2]))
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Highlights">
  {defs()}
  {card_bg(W, H)}
  {out}
</svg>
"""


# ------------------------------------------------------------------------ footer
def footer() -> str:
    W, H = 900, 140
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="footer">
  {defs()}
  <linearGradient id="w" x1="0" x2="1"><stop offset="0" stop-color="#1f6feb"/><stop offset="1" stop-color="#8957e5"/></linearGradient>
  <clipPath id="r"><rect width="{W}" height="{H}" rx="18"/></clipPath>
  <g clip-path="url(#r)">
    <rect width="{W}" height="{H}" fill="{BG}"/>
    <path d="M0 88 C 150 56, 300 120, 450 88 S 750 56, 900 88 L900 140 L0 140 Z" fill="url(#w)" opacity="0.35"/>
    <path d="M0 102 C 190 74, 340 130, 525 98 S 790 74, 900 102 L900 140 L0 140 Z" fill="url(#w)" opacity="0.55"/>
  </g>
  <rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="18" fill="none" stroke="{BORDER}"/>
  <text x="450" y="50" text-anchor="middle" font-family="{FONT}" font-size="22" font-weight="700" fill="{TEXT}">Open to AI / backend / platform engineering roles</text>
  <text x="450" y="78" text-anchor="middle" font-family="{MONO}" font-size="14" fill="{MUTED}">adwaitd393@gmail.com  ·  linkedin.com/in/adwaitpdesai  ·  github.com/adwait39</text>
</svg>
"""


if __name__ == "__main__":
    for old in OUT.glob("section-*.svg"):
        old.unlink()
    files = {"hero.svg": hero(), "experience.svg": experience(), "skills.svg": skills(),
             "highlights.svg": highlights(), "footer.svg": footer()}
    import re
    tallest = max(int(re.search(r'height="(\d+)"', project_card(p)).group(1)) for p in PROJECTS)
    for p in PROJECTS:
        files[f"project-{p['slug']}.svg"] = project_card(p, tallest)
    for name, svg in files.items():
        (OUT / name).write_text(svg, encoding="utf-8", newline="\n")
        print("wrote", name)
