#!/usr/bin/env python3
"""
Build a single self-contained HTML file from all WilderThings markdown guides.

Reads mkdocs.yml for nav order, converts each .md file to HTML,
and outputs a single offline-capable mobile-first HTML file.
"""

import os
import re
import sys
import html as html_module

# ---------------------------------------------------------------------------
# Dependencies
# ---------------------------------------------------------------------------
try:
    import yaml
except ImportError:
    print("ERROR: PyYAML is required. Install with: pip install pyyaml")
    sys.exit(1)

try:
    import markdown
    from markdown.extensions.toc import TocExtension
    HAS_MARKDOWN = True
except ImportError:
    HAS_MARKDOWN = False

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DOCS_DIR = os.path.join(BASE_DIR, "docs")
MKDOCS_YML = os.path.join(BASE_DIR, "mkdocs.yml")
OUTPUT_FILE = os.path.join(BASE_DIR, "wilderthings-mobile.html")

# ---------------------------------------------------------------------------
# Nav parsing
# ---------------------------------------------------------------------------

def flatten_nav(nav_items, prefix=""):
    """Recursively flatten the mkdocs nav structure into [(title, filepath), ...]."""
    result = []
    for item in nav_items:
        if isinstance(item, str):
            # bare filename (unlikely in this config but handle it)
            result.append((item, item))
        elif isinstance(item, dict):
            for key, value in item.items():
                if isinstance(value, str):
                    # "Title: path.md"
                    result.append((key, value))
                elif isinstance(value, list):
                    # Section with children
                    result.extend(flatten_nav(value, prefix=key + " / "))
    return result


def parse_nav():
    """Read mkdocs.yml and return ordered list of (title, filepath) tuples."""
    with open(MKDOCS_YML, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)
    nav = config.get("nav", [])
    return flatten_nav(nav)

# ---------------------------------------------------------------------------
# Admonition styling
# ---------------------------------------------------------------------------
# Admonitions carry the safety-critical content (DANGER / WARNING blocks), so
# they are rendered by the `admonition` and `pymdownx.details` extensions —
# the same ones MkDocs uses — and styled here by class. They are deliberately
# NOT hand-parsed: doing so previously escaped the body, which meant bold text,
# links and tables inside safety warnings rendered as literal markup.

ADMONITION_COLORS = {
    "danger":  ("#ff5252", "#4a0000", "#2d0000"),  # border, bg-dark, bg-darker
    "warning": ("#ff9100", "#4a3000", "#2d1d00"),
    "caution": ("#ff9100", "#4a3000", "#2d1d00"),
    "tip":     ("#00c853", "#003d1a", "#002510"),
    "note":    ("#6ba5ff", "#0d2a5c", "#081a3a"),
    "info":    ("#6ba5ff", "#0d2a5c", "#081a3a"),
    "example": ("#9c27b0", "#3a0a42", "#240628"),
    "abstract":("#00b0ff", "#003d5c", "#00253a"),
    "success": ("#00c853", "#003d1a", "#002510"),
    "question":("#64dd17", "#1a3d00", "#102500"),
    "quote":   ("#9e9e9e", "#2a2a2a", "#1a1a1a"),
    "bug":     ("#ff5c78", "#4a0011", "#2d000a"),
}

# Material uses "danger"/"warning" as the visible titles; python-markdown emits
# the type as a class, so map aliases onto the same styling.
ADMONITION_ALIASES = {"attention": "warning", "important": "warning", "hint": "tip", "failure": "bug"}


def build_admonition_css():
    """Generate CSS for every admonition type, for both !!! blocks and ??? details."""
    rules = [
        ".admonition, details.admonition, details[class] {",
        "  border-left: 4px solid #6ba5ff; background: #0d2a5c;",
        "  border-radius: 4px; margin: 16px 0; padding: 12px 16px;",
        "}",
        ".admonition > :last-child, details > :last-child { margin-bottom: 0; }",
        ".admonition-title, details > summary {",
        "  font-weight: 700; display: block; margin: 0 0 6px; color: #6ba5ff; cursor: default;",
        "}",
        "details > summary { cursor: pointer; }",
        # Body elements need spacing now that real markdown renders inside them.
        ".admonition p, details p { margin: 0 0 8px; }",
        ".admonition ul, .admonition ol, details ul, details ol { margin: 0 0 8px 1.2em; }",
        ".admonition table, details table { margin: 8px 0; }",
    ]
    for kind, (border, bg, _) in ADMONITION_COLORS.items():
        names = [kind] + [a for a, t in ADMONITION_ALIASES.items() if t == kind]
        sel = ", ".join(f".admonition.{n}, details.{n}" for n in names)
        title_sel = ", ".join(f".admonition.{n} > .admonition-title, details.{n} > summary" for n in names)
        rules.append(f"{sel} {{ border-left-color: {border}; background: {bg}; }}")
        rules.append(f"{title_sel} {{ color: {border}; }}")

    # pymdownx.tabbed (alternate_style) — content tabs
    rules += [
        ".tabbed-set { margin: 16px 0; }",
        ".tabbed-set > input { display: none; }",
        ".tabbed-labels { display: flex; flex-wrap: wrap; gap: 4px; border-bottom: 1px solid #333; }",
        ".tabbed-labels > label {",
        "  padding: 6px 12px; cursor: pointer; font-weight: 600; font-size: 0.9rem;",
        "  color: #9e9e9e; border-bottom: 2px solid transparent; min-height: 2.4rem;",
        "}",
        ".tabbed-content { padding-top: 10px; }",
        ".tabbed-block { display: none; }",
    ]
    # Show the block whose radio is checked (supports up to 8 tabs per set).
    for n in range(1, 9):
        rules.append(
            f".tabbed-set > input:nth-child({n}):checked ~ .tabbed-labels > label:nth-child({n}) "
            "{ color: #ff9100; border-bottom-color: #ff9100; }"
        )
        rules.append(
            f".tabbed-set > input:nth-child({n}):checked ~ .tabbed-content > .tabbed-block:nth-child({n}) "
            "{ display: block; }"
        )
    return "\n".join(rules)

# ---------------------------------------------------------------------------
# Markdown conversion
# ---------------------------------------------------------------------------

# Mirrors markdown_extensions in mkdocs.yml. Keeping these in sync is what makes
# the single-file build render identically to the MkDocs builds — the guides are
# authored against this feature set, so anything missing here silently degrades
# content rather than failing loudly.
MARKDOWN_EXTENSIONS = [
    'tables',
    'admonition',           # !!! danger "..."  — safety warnings depend on this
    'pymdownx.details',     # ??? collapsible admonitions
    'pymdownx.superfences',
    'pymdownx.tabbed',      # === "Tab"
    'pymdownx.mark',
    'attr_list',
    'md_in_html',
    'fenced_code',
    'codehilite',
]

MARKDOWN_EXTENSION_CONFIGS = {
    'codehilite': {'css_class': 'code-block', 'guess_lang': False},
    'pymdownx.tabbed': {'alternate_style': True},
}


def md_to_html(md_text):
    """Convert markdown text to HTML using the same extensions as mkdocs.yml."""
    if not HAS_MARKDOWN:
        return fallback_md_to_html(md_text)

    md = markdown.Markdown(
        extensions=MARKDOWN_EXTENSIONS + [TocExtension(permalink=False)],
        extension_configs=MARKDOWN_EXTENSION_CONFIGS,
    )
    return md.convert(md_text)


def fallback_md_to_html(text):
    """Regex-based minimal markdown to HTML conversion."""
    # Escape HTML first
    # (skip - we want to allow our admonition HTML through)

    # Headers
    text = re.sub(r'^###### (.+)$', r'<h6>\1</h6>', text, flags=re.MULTILINE)
    text = re.sub(r'^##### (.+)$', r'<h5>\1</h5>', text, flags=re.MULTILINE)
    text = re.sub(r'^#### (.+)$', r'<h4>\1</h4>', text, flags=re.MULTILINE)
    text = re.sub(r'^### (.+)$', r'<h3>\1</h3>', text, flags=re.MULTILINE)
    text = re.sub(r'^## (.+)$', r'<h2>\1</h2>', text, flags=re.MULTILINE)
    text = re.sub(r'^# (.+)$', r'<h1>\1</h1>', text, flags=re.MULTILINE)

    # Bold and italic
    text = re.sub(r'\*\*\*(.+?)\*\*\*', r'<strong><em>\1</em></strong>', text)
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)

    # Links
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', text)

    # Code
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)

    # Horizontal rules
    text = re.sub(r'^---+$', '<hr>', text, flags=re.MULTILINE)

    # Paragraphs (simple)
    text = re.sub(r'\n\n+', '\n</p><p>\n', text)
    text = '<p>' + text + '</p>'

    return text


def namespace_ids(html_content, prefix):
    """Make every generated id/name unique to one guide.

    Each guide is converted by its own Markdown instance, so python-markdown
    restarts its heading-id and tab counters for all 91 of them. Concatenating
    the results into a single document produced 148 duplicate ids ("see-also"
    appeared 89 times) and duplicate radio-group names, which merged every
    guide's content tabs into one group document-wide and left all tabs
    unselected. Prefixing per guide keeps anchors and tab groups independent.
    """
    # Collect this guide's own ids BEFORE rewriting, so intra-guide fragment
    # links can be distinguished from links pointing at other guides.
    local_ids = set(re.findall(r'\sid="([^"]+)"', html_content))

    def prefixed(value):
        return f"{prefix}--{value}"

    def sub_attr(match):
        return f'{match.group(1)}{prefixed(match.group(2))}{match.group(3)}'

    html_content = re.sub(r'(\sid=")([^"]+)(")', sub_attr, html_content)
    html_content = re.sub(r'(\sfor=")([^"]+)(")', sub_attr, html_content)
    # Radio groups for content tabs — collisions here are what break tab state.
    html_content = re.sub(r'(\sname=")(__tabbed_[^"]+)(")', sub_attr, html_content)

    def sub_href(match):
        fragment = match.group(2)
        # Only namespace fragments that point inside this guide. Links to other
        # guides target section ids, which are already globally unique.
        if fragment in local_ids:
            return f'{match.group(1)}{prefixed(fragment)}{match.group(3)}'
        return match.group(0)

    return re.sub(r'(\shref="#)([^"]+)(")', sub_href, html_content)


def make_anchor(title):
    """Create a URL-safe anchor from a title."""
    anchor = title.lower()
    anchor = re.sub(r'[^a-z0-9\s-]', '', anchor)
    anchor = re.sub(r'[\s]+', '-', anchor.strip())
    return anchor

# ---------------------------------------------------------------------------
# HTML template
# ---------------------------------------------------------------------------

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes">
<meta name="theme-color" content="#1a1a2e">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<title>WilderThings — Survival Guide</title>
<style>
/* ===== RESET & BASE ===== */
*, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}

html {{
  font-size: 17px;
  scroll-behavior: smooth;
  -webkit-text-size-adjust: 100%;
}}

body {{
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  background: #121212;
  color: #e0e0e0;
  line-height: 1.7;
  padding: 0;
  margin: 0;
  overflow-x: hidden;
}}

/* ===== HEADER BAR ===== */
.header {{
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  height: 56px;
  background: #1a1a2e;
  border-bottom: 1px solid #333;
  display: flex;
  align-items: center;
  padding: 0 16px;
  z-index: 1000;
  gap: 12px;
}}

.header h1 {{
  font-size: 1.1rem;
  color: #ff9100;
  margin: 0;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}}

.menu-btn {{
  background: none;
  border: none;
  color: #e0e0e0;
  font-size: 1.6rem;
  cursor: pointer;
  padding: 4px 8px;
  border-radius: 4px;
  flex-shrink: 0;
  line-height: 1;
}}
.menu-btn:hover {{ background: rgba(255,255,255,0.1); }}

.back-to-top {{
  margin-left: auto;
  background: none;
  border: none;
  color: #888;
  font-size: 0.8rem;
  cursor: pointer;
  padding: 4px 8px;
  flex-shrink: 0;
}}
.back-to-top:hover {{ color: #ff9100; }}

/* ===== NAV SIDEBAR ===== */
.nav-overlay {{
  display: none;
  position: fixed;
  inset: 0;
  background: rgba(0,0,0,0.6);
  z-index: 1001;
}}
.nav-overlay.open {{ display: block; }}

.nav-sidebar {{
  position: fixed;
  top: 0;
  left: -300px;
  width: 280px;
  max-width: 85vw;
  height: 100vh;
  background: #1a1a2e;
  z-index: 1002;
  overflow-y: auto;
  transition: left 0.25s ease;
  padding: 16px 0;
  border-right: 1px solid #333;
}}
.nav-sidebar.open {{ left: 0; }}

.nav-sidebar .nav-header {{
  padding: 8px 20px 16px;
  font-size: 1rem;
  color: #ff9100;
  font-weight: 700;
  border-bottom: 1px solid #333;
  margin-bottom: 8px;
}}

.nav-section {{
  padding: 4px 0;
}}
.nav-section-title {{
  padding: 8px 20px;
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: #888;
  font-weight: 600;
}}

.nav-link {{
  display: block;
  padding: 8px 20px 8px 28px;
  color: #ccc;
  text-decoration: none;
  font-size: 0.88rem;
  border-left: 3px solid transparent;
  transition: background 0.15s, border-color 0.15s;
}}
.nav-link:hover,
.nav-link:active {{
  background: rgba(255,145,0,0.08);
  border-left-color: #ff9100;
  color: #fff;
}}

/* ===== MAIN CONTENT ===== */
.content {{
  margin-top: 56px;
  padding: 24px 16px 80px;
  max-width: 780px;
  margin-left: auto;
  margin-right: auto;
}}

/* ===== GUIDE SECTIONS ===== */
.guide-section {{
  margin-bottom: 48px;
  padding-bottom: 32px;
  border-bottom: 1px solid #2a2a2a;
}}

.section-category {{
  display: inline-block;
  font-size: 0.7rem;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: #ff9100;
  background: rgba(255,145,0,0.12);
  padding: 2px 10px;
  border-radius: 3px;
  margin-bottom: 8px;
}}

/* ===== TYPOGRAPHY ===== */
h1 {{ font-size: 1.6rem; color: #fff; margin: 20px 0 12px; line-height: 1.3; }}
h2 {{ font-size: 1.35rem; color: #ff9100; margin: 28px 0 10px; padding-bottom: 4px; border-bottom: 1px solid #333; }}
h3 {{ font-size: 1.15rem; color: #e0e0e0; margin: 22px 0 8px; }}
h4 {{ font-size: 1.05rem; color: #ccc; margin: 18px 0 6px; }}
h5, h6 {{ font-size: 0.95rem; color: #bbb; margin: 14px 0 6px; }}

p {{ margin: 10px 0; }}

a {{ color: #64b5f6; text-decoration: none; }}
a:hover {{ text-decoration: underline; }}

strong {{ color: #fff; }}

blockquote {{
  border-left: 3px solid #ff9100;
  padding: 8px 16px;
  margin: 16px 0;
  color: #ccc;
  background: rgba(255,145,0,0.05);
  border-radius: 0 4px 4px 0;
}}

hr {{
  border: none;
  border-top: 1px solid #333;
  margin: 24px 0;
}}

/* ===== LISTS ===== */
ul, ol {{
  padding-left: 24px;
  margin: 10px 0;
}}
li {{
  margin: 4px 0;
}}
li > ul, li > ol {{
  margin: 4px 0;
}}

/* ===== CODE ===== */
code {{
  font-family: "SF Mono", "Fira Code", "Fira Mono", Menlo, Consolas, monospace;
  font-size: 0.88em;
  background: #1e1e3a;
  color: #ce9178;
  padding: 2px 6px;
  border-radius: 3px;
}}

pre {{
  background: #1e1e3a;
  padding: 16px;
  border-radius: 6px;
  overflow-x: auto;
  margin: 16px 0;
  border: 1px solid #333;
}}
pre code {{
  background: none;
  padding: 0;
  color: #d4d4d4;
}}

/* ===== TABLES ===== */
.table-wrap {{
  overflow-x: auto;
  margin: 16px 0;
  -webkit-overflow-scrolling: touch;
}}

table {{
  border-collapse: collapse;
  width: 100%;
  min-width: 400px;
  font-size: 0.9rem;
}}

th {{
  background: #1a1a2e;
  color: #ff9100;
  text-align: left;
  padding: 10px 12px;
  border-bottom: 2px solid #ff9100;
  white-space: nowrap;
}}

td {{
  padding: 8px 12px;
  border-bottom: 1px solid #2a2a2a;
  vertical-align: top;
}}

tr:hover td {{ background: rgba(255,255,255,0.03); }}

/* ===== ADMONITIONS & CONTENT TABS (generated) ===== */
{admonition_css}

/* ===== IMAGES ===== */
img {{
  max-width: 100%;
  height: auto;
  border-radius: 4px;
}}

/* ===== FOOTER ===== */
.footer {{
  text-align: center;
  padding: 32px 16px;
  color: #9e9e9e;
  font-size: 0.8rem;
  border-top: 1px solid #2a2a2a;
}}

/* ===== SCROLLBAR ===== */
::-webkit-scrollbar {{ width: 6px; height: 6px; }}
::-webkit-scrollbar-track {{ background: #1a1a1a; }}
::-webkit-scrollbar-thumb {{ background: #444; border-radius: 3px; }}
::-webkit-scrollbar-thumb:hover {{ background: #666; }}

/* ===== PRINT ===== */
@media print {{
  body {{ background: #fff; color: #000; }}
  .header, .nav-overlay, .nav-sidebar, .back-to-top {{ display: none !important; }}
  .content {{ margin-top: 0; }}
  h2 {{ color: #333; border-bottom-color: #999; }}
  a {{ color: #0066cc; }}
}}
</style>
</head>
<body>

<!-- Header bar -->
<div class="header">
  <button class="menu-btn" onclick="toggleNav()" aria-label="Menu">&#9776;</button>
  <h1>WilderThings</h1>
  <button class="back-to-top" onclick="window.scrollTo({{top:0,behavior:'smooth'}})">&#9650; Top</button>
</div>

<!-- Nav overlay -->
<div class="nav-overlay" id="navOverlay" onclick="toggleNav()"></div>

<!-- Nav sidebar -->
<nav class="nav-sidebar" id="navSidebar">
  <div class="nav-header">WilderThings</div>
  {toc_html}
</nav>

<!-- Content -->
<div class="content">
  {content_html}
</div>

<div class="footer">
  WilderThings Survival Guide &mdash; Offline Reference<br>
  Use browser search (Ctrl+F / Cmd+F) to find specific topics.<br><br>
  Guides licensed <a href="https://creativecommons.org/licenses/by-sa/4.0/" rel="license">CC BY-SA 4.0</a>
  &middot; tooling MIT &middot; &copy; WilderThings Contributors.<br>
  Share and adapt freely; credit the source and keep derivatives under the same license.<br><br>
  <strong>Reference material only.</strong> Not a substitute for training, professional
  medical care, or emergency services. Plant and mushroom identification carries a risk
  of death from misidentification.
</div>

<script>
function toggleNav() {{
  document.getElementById('navSidebar').classList.toggle('open');
  document.getElementById('navOverlay').classList.toggle('open');
}}

// Close nav when clicking a link
document.querySelectorAll('.nav-link').forEach(function(link) {{
  link.addEventListener('click', function() {{
    document.getElementById('navSidebar').classList.remove('open');
    document.getElementById('navOverlay').classList.remove('open');
  }});
}});

// Wrap tables for responsive scrolling
document.querySelectorAll('.content table').forEach(function(table) {{
  if (!table.parentElement.classList.contains('table-wrap')) {{
    var wrapper = document.createElement('div');
    wrapper.className = 'table-wrap';
    table.parentNode.insertBefore(wrapper, table);
    wrapper.appendChild(table);
  }}
}});
</script>

</body>
</html>"""


# ---------------------------------------------------------------------------
# Build
# ---------------------------------------------------------------------------

def get_section_name(filepath):
    """Extract the section/category name from the file path."""
    parts = filepath.replace("\\", "/").split("/")
    if len(parts) > 1:
        return parts[0].replace("-", " ").title()
    return ""


def build():
    nav_items = parse_nav()
    print(f"Found {len(nav_items)} guides in nav")

    toc_entries = []
    content_sections = []
    current_section = None
    seen_anchors = set()

    for title, filepath in nav_items:
        full_path = os.path.join(DOCS_DIR, filepath)
        if not os.path.exists(full_path):
            print(f"  WARNING: {filepath} not found, skipping")
            continue

        with open(full_path, "r", encoding="utf-8") as f:
            md_text = f.read()

        # Rewrite internal .md links to anchors within this file
        def rewrite_link(m):
            link_text = m.group(1)
            link_target = m.group(2)
            if link_target.endswith(".md") or ".md#" in link_target:
                # Extract just the filename part for anchor
                base = link_target.split("/")[-1].replace(".md", "").split("#")[0]
                target = make_anchor(base)
                if "#" in link_target:
                    # Heading anchors are namespaced per guide by namespace_ids,
                    # so "guide.md#heading" resolves to "#guide--heading".
                    # Previously this emitted "#guide#heading", which is a single
                    # malformed fragment matching nothing.
                    target = f"{target}--{link_target.split('#', 1)[1]}"
                return f"[{link_text}](#{target})"
            return m.group(0)

        md_text = re.sub(r'\[([^\]]+)\]\(([^)]*\.md[^)]*)\)', rewrite_link, md_text)

        # Generate anchor
        anchor = make_anchor(os.path.splitext(os.path.basename(filepath))[0])
        # Ensure unique
        orig_anchor = anchor
        counter = 1
        while anchor in seen_anchors:
            anchor = f"{orig_anchor}-{counter}"
            counter += 1
        seen_anchors.add(anchor)

        section_name = get_section_name(filepath)

        # Build TOC
        if section_name and section_name != current_section:
            current_section = section_name
            toc_entries.append(f'<div class="nav-section-title">{html_module.escape(section_name)}</div>')
        toc_entries.append(f'<a class="nav-link" href="#{anchor}">{html_module.escape(title)}</a>')

        # Convert to HTML, then scope its ids to this guide.
        html_content = namespace_ids(md_to_html(md_text), anchor)

        section_html = f'<section class="guide-section" id="{anchor}">\n'
        if section_name:
            section_html += f'<span class="section-category">{html_module.escape(section_name)}</span>\n'
        section_html += html_content
        section_html += '\n</section>\n'
        content_sections.append(section_html)

        print(f"  Converted: {filepath}")

    toc_html = "\n".join(toc_entries)
    content_html = "\n".join(content_sections)

    final_html = HTML_TEMPLATE.format(
        toc_html=toc_html,
        content_html=content_html,
        admonition_css=build_admonition_css(),
    )

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(final_html)

    file_size = os.path.getsize(OUTPUT_FILE)
    size_mb = file_size / (1024 * 1024)
    print(f"\nDone! Output: {OUTPUT_FILE}")
    print(f"File size: {file_size:,} bytes ({size_mb:.2f} MB)")
    print(f"Guides included: {len(content_sections)}")


if __name__ == "__main__":
    build()
