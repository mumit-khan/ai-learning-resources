#!/usr/bin/env python3
"""
md_to_html.py — turn the curated learning-resources Markdown file into the
interactive, filterable HTML page (search box + source/level/area filter
chips).

USAGE
    python3 md_to_html.py [input.md] [output.html]

    Defaults: input.md  = ai_learning_resources.md
              output.html = ai_learning_resources.html

DEPENDENCIES
    pip install --break-system-packages mistune

PARSER
    This uses mistune's block/inline AST (mistune.create_markdown(renderer=None))
    rather than hand-rolled regex/line-scanning, so real Markdown edge cases
    (escaped characters, code spans, nested emphasis, tight vs. loose lists,
    HTML comments, etc.) are handled by a proper parser instead of ad-hoc
    string splitting.

MARKDOWN SCHEMA THIS PARSER EXPECTS
    ## Category Name
        Starts a new category section. Categories are rendered in the HTML
        in the order they first appear in the file.

    - **Title** — Author — *Level* — Area1, Area2[, Area3] [— **NEW**]
          Description paragraph (single line).
          https://example.com/optional-link
        A resource entry, as one Markdown list item. The parser walks the
        item's inline AST (not raw text):
          1. The first `strong` (bold) inline node is the Title.
          2. A later `strong` node whose text is exactly "NEW" flags the
             entry as newly added (isNew).
          3. The `emphasis` (italic) node is the Level — one or more of
             Foundational / Intermediate / Advanced, joined with "/".
          4. Everything else on the header line (i.e. before the first
             softbreak) is plain text, split on " — " into Author (before
             the Level) and Areas (after the Level).
          5. Areas are free text, comma-separated, matched case-insensitively
             against keywords (AREA_KEYWORDS) to bucket into filter chips.
          6. The next line (after the first softbreak) is the description.
          7. If a further line contains a URL (bare, or as a Markdown link),
             it's used as the card's link.

    > Freeform note
        A blockquote attaches a note to the CURRENT category, rendered as
        an italic callout above that category's card grid. A blockquote
        that appears under a heading with no list items (e.g. a trailing
        "## Notes" section) is instead rendered as a page-level footnote.

Re-run this script any time the .md file changes to regenerate the HTML.
"""
import json
import re
import sys
from collections import OrderedDict

try:
    import mistune
except ImportError:  # pragma: no cover
    sys.exit(
        "This script requires the 'mistune' package.\n"
        "Install it with: pip install --break-system-packages mistune"
    )

# ---------------------------------------------------------------------------
# 1. AREA / LEVEL VOCAB
# ---------------------------------------------------------------------------

AREA_KEYWORDS = [
    ("genai", ["genai", "llm engineering"]),
    ("core", ["core ml", "deep learning"]),
    ("agent", ["agentic"]),
    ("mlops", ["mlops"]),
    ("eval", ["evaluation", "governance", "safety"]),
    ("ainative", ["ai-native", "ai native"]),
]

AREA_LABELS = {
    "genai": "GenAI / LLM engineering",
    "core": "Core ML & DL foundations",
    "agent": "Agentic AI & frameworks",
    "mlops": "MLOps & production",
    "eval": "Evaluation, governance & safety",
    "ainative": "AI-native software development",
}

VALID_LEVELS = {"Foundational", "Intermediate", "Advanced"}

URL_RE = re.compile(r"https?://\S+")


def normalize_areas(raw):
    """Split a comma-separated area string into our internal area keys, in order."""
    keys = []
    for token in raw.split(","):
        token_l = token.strip().lower()
        for key, kws in AREA_KEYWORDS:
            if any(kw in token_l for kw in kws) and key not in keys:
                keys.append(key)
                break
    return keys


# ---------------------------------------------------------------------------
# 2. AST WALKING HELPERS
# ---------------------------------------------------------------------------

def inline_text(children):
    """Flatten a list of inline AST nodes to plain text (ignores structure)."""
    out = []
    for node in children or []:
        t = node.get("type")
        if t == "text":
            out.append(node.get("raw", ""))
        elif t == "codespan":
            out.append(node.get("raw", ""))
        elif t in ("softbreak", "linebreak"):
            out.append(" ")
        elif t == "link":
            out.append(node.get("attrs", {}).get("url", "") or inline_text(node.get("children")))
        elif "children" in node:
            out.append(inline_text(node["children"]))
        elif "raw" in node:
            out.append(node["raw"])
    return "".join(out)


def split_into_lines(children):
    """
    Split an inline AST node list into "lines" (breaking on softbreak /
    linebreak), preserving node type info for each run so we can tell a
    bold Title from a plain-text Author, etc.
    """
    lines = [[]]
    for node in children or []:
        t = node.get("type")
        if t in ("softbreak", "linebreak"):
            lines.append([])
            continue
        if t == "strong":
            lines[-1].append(("strong", inline_text(node.get("children"))))
        elif t == "emphasis":
            lines[-1].append(("em", inline_text(node.get("children"))))
        elif t == "link":
            url = node.get("attrs", {}).get("url", "")
            lines[-1].append(("link", inline_text(node.get("children")) or url, url))
        elif t == "codespan":
            lines[-1].append(("text", "`" + node.get("raw", "") + "`"))
        elif t == "text":
            lines[-1].append(("text", node.get("raw", "")))
        else:
            lines[-1].append(("text", inline_text(node.get("children") or [node])))
    return lines


def parse_entry(item_children):
    """Parse one resource list-item's inline AST into a structured dict, or None."""
    # A list item's content is either a single 'paragraph' or 'block_text'
    # block (tight vs. loose list) — both carry the same inline children.
    inline_children = []
    for block in item_children:
        if block.get("type") in ("paragraph", "block_text"):
            inline_children.extend(block.get("children", []))
            inline_children.append({"type": "softbreak"})

    lines = split_into_lines(inline_children)
    lines = [ln for ln in lines if ln]  # drop empty trailing lines
    if not lines:
        return None

    header_runs = lines[0]

    # Title = first 'strong' run on the header line.
    title = None
    header_rest = []
    seen_title = False
    is_new = False
    for run in header_runs:
        kind = run[0]
        text = run[1]
        if kind == "strong" and not seen_title:
            title = text
            seen_title = True
            continue
        if kind == "strong" and text.strip().upper() == "NEW":
            is_new = True
            continue
        header_rest.append(run)

    if title is None:
        return None  # not a resource entry (malformed / no bold title)

    # Rebuild the "rest of the header" as a string, marking the emphasis
    # (Level) run with a sentinel so we can find it after splitting on " — ".
    SENTINEL = "\x00"
    rest_str = ""
    for kind, text, *_ in header_rest:
        if kind == "em":
            rest_str += f"{SENTINEL}{text}{SENTINEL}"
        else:
            rest_str += text
    rest_str = rest_str.strip()
    rest_str = re.sub(r"^—\s*", "", rest_str)

    segments = [s.strip() for s in re.split(r"\s+—\s+", rest_str) if s.strip()]
    level_idx = next((i for i, s in enumerate(segments) if SENTINEL in s), None)
    if level_idx is None:
        return None  # no *Level* found — malformed entry, skip

    author = " — ".join(segments[:level_idx]).strip()
    level_raw = segments[level_idx].replace(SENTINEL, "").strip()
    levels = [lvl.strip() for lvl in level_raw.split("/") if lvl.strip() in VALID_LEVELS]
    areas_raw = segments[level_idx + 1] if level_idx + 1 < len(segments) else ""
    areas = normalize_areas(areas_raw)

    # Description = 2nd line, flattened to plain text.
    desc = ""
    if len(lines) > 1:
        desc = "".join(t for _, t, *_ in lines[1]).strip()

    # URL = look at line 3+ for a link node or a bare URL.
    url = ""
    for extra_line in lines[2:]:
        for run in extra_line:
            if run[0] == "link":
                url = run[2]
                break
            m = URL_RE.search(run[1])
            if m:
                url = m.group(0)
                break
        if url:
            break

    return {
        "title": title.strip(),
        "author": author,
        "desc": desc,
        "url": url,
        "levels": levels,
        "areas": areas,
        "isNew": is_new,
    }


def blockquote_text(token):
    parts = []
    for child in token.get("children", []):
        if child.get("type") == "paragraph":
            parts.append(inline_text(child.get("children")))
    return " ".join(p.strip() for p in parts if p.strip())


# ---------------------------------------------------------------------------
# 3. TOP-LEVEL PARSE
# ---------------------------------------------------------------------------

def parse_markdown(text):
    md = mistune.create_markdown(renderer=None)
    tokens = md(text)

    categories = OrderedDict()  # cat -> {"items": [...], "notes": [...]}
    current_cat = None

    for tok in tokens:
        ttype = tok.get("type")

        if ttype == "heading" and tok.get("attrs", {}).get("level") == 2:
            current_cat = inline_text(tok.get("children")).strip()
            categories.setdefault(current_cat, {"items": [], "notes": []})
            continue

        if ttype == "block_quote" and current_cat is not None:
            note = blockquote_text(tok)
            if note:
                categories[current_cat]["notes"].append(note)
            continue

        if ttype == "list" and current_cat is not None:
            for item in tok.get("children", []):
                if item.get("type") != "list_item":
                    continue
                parsed = parse_entry(item.get("children", []))
                if parsed is not None:
                    parsed["cat"] = current_cat
                    categories[current_cat]["items"].append(parsed)
            continue

        # headings level 1, paragraphs, thematic breaks, block_html
        # (e.g. the schema-doc HTML comment), blank_line — all ignored.

    return categories


# ---------------------------------------------------------------------------
# 4. RENDER
# ---------------------------------------------------------------------------

PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Agentic AI / ML / GenAI Learning Resources</title>
<style>
  :root {{
    color-scheme: light;
    --bg: #ffffff;
    --panel: #f7f7f8;
    --border: #e5e5e7;
    --text: #1a1a1e;
    --text-muted: #6b6b73;
    --accent: #6d4de6;
    --accent-soft: #efe9fd;
    --foundational: #2f9e6b;
    --intermediate: #2b7de0;
    --advanced: #c0392b;
  }}
  * {{ box-sizing: border-box; }}
  body {{
    margin: 0; background: var(--bg); color: var(--text);
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
    font-size: 14px; line-height: 1.5;
  }}
  .wrap {{ max-width: 1180px; margin: 0 auto; padding: 28px 24px 60px; }}
  header h1 {{ font-size: 22px; margin: 0 0 4px; }}
  header p.sub {{ color: var(--text-muted); margin: 0 0 20px; max-width: 820px; }}
  .legend {{ display:flex; gap:14px; flex-wrap:wrap; margin-bottom: 18px; font-size: 12px; color: var(--text-muted); }}
  .legend span.dot {{ display:inline-block; width:8px; height:8px; border-radius:50%; margin-right:5px; vertical-align:middle; }}

  nav.source-nav {{ display:flex; flex-wrap:wrap; gap:6px; margin-bottom: 12px; }}
  nav.source-nav .chip {{ font-size: 12px; }}

  .controls {{ display:flex; flex-wrap:wrap; gap:10px; align-items:center; margin-bottom: 20px; padding: 14px; background: var(--panel); border: 1px solid var(--border); border-radius: 10px; }}
  .controls input[type="search"] {{
    flex: 1 1 220px; padding: 8px 12px; border: 1px solid var(--border);
    border-radius: 8px; font-size: 14px; background: #fff; color: var(--text);
  }}
  .chip-group {{ display:flex; gap:6px; flex-wrap:wrap; }}
  .chip {{
    padding: 5px 11px; border-radius: 999px; border: 1px solid var(--border);
    background: #fff; color: var(--text-muted); font-size: 12.5px;
    cursor: pointer; user-select: none; transition: all .12s ease;
  }}
  .chip:hover {{ border-color: var(--accent); color: var(--text); }}
  .chip.active {{ background: var(--accent); border-color: var(--accent); color: #fff; }}
  .count {{ color: var(--text-muted); font-size: 12.5px; margin-left: auto; white-space: nowrap; }}

  .category-block {{ margin-bottom: 30px; scroll-margin-top: 16px; }}
  .category-block h2 {{
    font-size: 15px; text-transform: uppercase; letter-spacing: .04em;
    color: var(--accent); border-bottom: 2px solid var(--accent-soft);
    padding-bottom: 6px; margin: 0 0 14px;
  }}
  .cat-note {{ color: var(--text-muted); font-size: 12.5px; font-style: italic; margin: -8px 0 14px; }}
  .grid {{ display:grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 12px; }}
  .card {{ border: 1px solid var(--border); border-radius: 10px; padding: 14px 16px; background: #fff; }}
  .card.is-new {{ border-color: var(--foundational); box-shadow: 0 0 0 1px var(--foundational) inset; }}
  .card-top {{ display:flex; justify-content:space-between; align-items:flex-start; gap:8px; margin-bottom:4px; }}
  .card h3 {{ font-size: 14.5px; margin: 0; }}
  .card h3 a {{ color: var(--text); text-decoration: none; }}
  .card h3 a:hover {{ color: var(--accent); text-decoration: underline; }}
  .new-badge {{ font-size: 10px; font-weight: 700; color: #fff; background: var(--foundational); padding: 2px 6px; border-radius: 999px; white-space: nowrap; }}
  .card .author {{ color: var(--text-muted); font-size: 12.5px; margin: 2px 0 8px; }}
  .card p.desc {{ margin: 0 0 10px; color: #333; font-size: 13px; }}
  .tags {{ display:flex; flex-wrap:wrap; gap:5px; }}
  .tag {{ font-size: 11px; padding: 2px 8px; border-radius: 999px; font-weight: 600; }}
  .tag.level-Foundational {{ background: #e6f5ee; color: var(--foundational); }}
  .tag.level-Intermediate {{ background: #e8f1fd; color: var(--intermediate); }}
  .tag.level-Advanced {{ background: #fbe6e3; color: var(--advanced); }}
  .tag.area {{ background: var(--accent-soft); color: var(--accent); font-weight: 500; }}
  .empty {{ color: var(--text-muted); padding: 40px 0; text-align:center; }}
  footer {{ margin-top: 40px; color: var(--text-muted); font-size: 12px; border-top: 1px solid var(--border); padding-top: 14px; }}
  footer .global-note {{ margin-top: 6px; }}
</style>
</head>
<body>
<div class="wrap">
  <header>
    <h1>Agentic AI / ML / GenAI — Curated Learning Resources</h1>
    <p class="sub">A vetted, high-signal list for engineers from foundational on-ramps through staff-level depth. Click a source below to jump straight to it, or filter by level/focus area, or search by keyword. Items flagged in the most recent review are marked <span class="new-badge">NEW</span>.</p>
  </header>

  <nav class="source-nav" id="sourceNav"></nav>

  <div class="legend">
    <span><span class="dot" style="background:var(--foundational)"></span>Foundational — well-regarded, accessible on-ramp (not 101, a notch below Intermediate)</span>
    <span><span class="dot" style="background:var(--intermediate)"></span>Intermediate — solid ML/software background, ready to go deeper</span>
    <span><span class="dot" style="background:var(--advanced)"></span>Advanced — senior/staff depth, research-adjacent or production-critical</span>
  </div>

  <div class="controls">
    <input type="search" id="search" placeholder="Search by name, author, or keyword…">
    <div class="chip-group" id="levelChips"></div>
    <div class="chip-group" id="areaChips"></div>
    <div class="count" id="count"></div>
  </div>

  <div id="results"></div>

  <footer>
    Generated by md_to_html.py from ai_learning_resources.md — edit the Markdown, then re-run the script to refresh this page.
    {global_notes_html}
  </footer>
</div>

<script>
const AREAS = {areas_json};
const CATEGORY_ORDER = {category_order_json};
const CATEGORY_NOTES = {category_notes_json};
const DATA = {data_json};

function levelBadges(levels) {{
  return levels.map(l => `<span class="tag level-${{l}}">${{l}}</span>`).join("");
}}
function areaBadges(areas) {{
  return areas.map(a => `<span class="tag area">${{AREAS[a] || a}}</span>`).join("");
}}

let activeSource = null;
let activeLevel = null;
let activeArea = null;

function slug(s) {{ return s.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/(^-|-$)/g, ""); }}

function buildSourceNav() {{
  const nav = document.getElementById("sourceNav");
  nav.innerHTML = "";
  CATEGORY_ORDER.forEach(cat => {{
    const chip = document.createElement("div");
    chip.className = "chip" + (activeSource === cat ? " active" : "");
    chip.textContent = cat;
    chip.onclick = () => {{
      const wasActive = activeSource === cat;
      activeSource = wasActive ? null : cat;
      render();
      buildSourceNav();
      if (!wasActive) {{
        const el = document.getElementById("cat-" + slug(cat));
        if (el) el.scrollIntoView({{ behavior: "smooth", block: "start" }});
      }}
    }};
    nav.appendChild(chip);
  }});
}}

function buildChips() {{
  const levelWrap = document.getElementById("levelChips");
  levelWrap.innerHTML = "";
  ["Foundational","Intermediate","Advanced"].forEach(l => {{
    const chip = document.createElement("div");
    chip.className = "chip" + (activeLevel === l ? " active" : "");
    chip.textContent = l;
    chip.onclick = () => {{ activeLevel = activeLevel === l ? null : l; render(); buildChips(); }};
    levelWrap.appendChild(chip);
  }});

  const areaWrap = document.getElementById("areaChips");
  areaWrap.innerHTML = "";
  Object.keys(AREAS).forEach(key => {{
    const chip = document.createElement("div");
    chip.className = "chip" + (activeArea === key ? " active" : "");
    chip.textContent = AREAS[key];
    chip.onclick = () => {{ activeArea = activeArea === key ? null : key; render(); buildChips(); }};
    areaWrap.appendChild(chip);
  }});
}}

function render() {{
  const q = document.getElementById("search").value.trim().toLowerCase();
  const filtered = DATA.filter(item => {{
    if (activeSource && item.cat !== activeSource) return false;
    if (activeLevel && !item.levels.includes(activeLevel)) return false;
    if (activeArea && !item.areas.includes(activeArea)) return false;
    if (q) {{
      const hay = (item.title + " " + item.author + " " + item.desc + " " + item.cat).toLowerCase();
      if (!hay.includes(q)) return false;
    }}
    return true;
  }});

  document.getElementById("count").textContent = `${{filtered.length}} of ${{DATA.length}} resources`;

  const results = document.getElementById("results");
  results.innerHTML = "";

  if (filtered.length === 0) {{
    results.innerHTML = `<div class="empty">No resources match those filters.</div>`;
    return;
  }}

  const cats = [...new Set(filtered.map(i => i.cat))];
  CATEGORY_ORDER.filter(c => cats.includes(c)).forEach(cat => {{
    const items = filtered.filter(i => i.cat === cat);
    const block = document.createElement("div");
    block.className = "category-block";
    block.id = "cat-" + slug(cat);
    const note = CATEGORY_NOTES[cat];
    const noteHtml = note ? `<div class="cat-note">${{note}}</div>` : "";
    block.innerHTML = `<h2>${{cat}} (${{items.length}})</h2>${{noteHtml}}<div class="grid"></div>`;
    const grid = block.querySelector(".grid");
    items.forEach(item => {{
      const card = document.createElement("div");
      card.className = "card" + (item.isNew ? " is-new" : "");
      const titleHtml = item.url ? `<a href="${{item.url}}" target="_blank" rel="noopener">${{item.title}}</a>` : item.title;
      const newBadge = item.isNew ? `<span class="new-badge">NEW</span>` : "";
      card.innerHTML = `
        <div class="card-top"><h3>${{titleHtml}}</h3>${{newBadge}}</div>
        <div class="author">${{item.author}}</div>
        <p class="desc">${{item.desc}}</p>
        <div class="tags">${{levelBadges(item.levels)}}${{areaBadges(item.areas)}}</div>
      `;
      grid.appendChild(card);
    }});
    results.appendChild(block);
  }});
}}

document.getElementById("search").addEventListener("input", render);
buildSourceNav();
buildChips();
render();
</script>
</body>
</html>
"""


def build_html(categories):
    category_order = [c for c in categories if categories[c]["items"]]
    data = []
    for cat in category_order:
        for item in categories[cat]["items"]:
            data.append(
                {
                    "cat": cat,
                    "title": item["title"],
                    "author": item["author"],
                    "desc": item["desc"],
                    "url": item["url"],
                    "levels": item["levels"],
                    "areas": item["areas"],
                    "isNew": item["isNew"],
                }
            )

    category_notes = {
        cat: " ".join(categories[cat]["notes"])
        for cat in category_order
        if categories[cat]["notes"]
    }

    # Categories with notes but zero items (e.g. a trailing "## Notes"
    # section) become page-level footnotes instead of a card grid.
    global_notes = []
    for cat, payload in categories.items():
        if not payload["items"] and payload["notes"]:
            global_notes.append(" ".join(payload["notes"]))
    global_notes_html = "".join(f'<div class="global-note">{n}</div>' for n in global_notes)

    return PAGE_TEMPLATE.format(
        areas_json=json.dumps(AREA_LABELS),
        category_order_json=json.dumps(category_order),
        category_notes_json=json.dumps(category_notes),
        data_json=json.dumps(data, indent=2),
        global_notes_html=global_notes_html,
    )


# ---------------------------------------------------------------------------
# 5. CLI
# ---------------------------------------------------------------------------

def main():
    in_path = sys.argv[1] if len(sys.argv) > 1 else "ai_learning_resources.md"
    out_path = sys.argv[2] if len(sys.argv) > 2 else "ai_learning_resources.html"

    with open(in_path, "r", encoding="utf-8") as f:
        text = f.read()

    categories = parse_markdown(text)
    total_items = sum(len(c["items"]) for c in categories.values())
    if total_items == 0:
        print("Warning: parsed 0 resource entries — check the Markdown format.", file=sys.stderr)

    html_out = build_html(categories)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html_out)

    n_cats = sum(1 for c in categories.values() if c["items"])
    print(f"Parsed {total_items} entries across {n_cats} categories.")
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
