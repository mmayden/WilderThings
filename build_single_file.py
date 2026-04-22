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
# Admonition pre-processing (before markdown conversion)
# ---------------------------------------------------------------------------

ADMONITION_COLORS = {
    "danger":  ("#ff5252", "#4a0000", "#2d0000"),  # border, bg-dark, bg-darker
    "warning": ("#ff9100", "#4a3000", "#2d1d00"),
    "caution": ("#ff9100", "#4a3000", "#2d1d00"),
    "tip":     ("#00c853", "#003d1a", "#002510"),
    "note":    ("#448aff", "#0d2a5c", "#081a3a"),
    "info":    ("#448aff", "#0d2a5c", "#081a3a"),
    "example": ("#9c27b0", "#3a0a42", "#240628"),
    "abstract":("#00b0ff", "#003d5c", "#00253a"),
    "success": ("#00c853", "#003d1a", "#002510"),
    "question":("#64dd17", "#1a3d00", "#102500"),
    "quote":   ("#9e9e9e", "#2a2a2a", "#1a1a1a"),
    "bug":     ("#ff1744", "#4a0011", "#2d000a"),
}

def convert_admonitions(md_text):
    """Convert MkDocs-style admonitions to HTML before markdown processing."""
    lines = md_text.split("\n")
    result = []
    i = 0
    while i < len(lines):
        # Match !!! type "Title" or !!! type
        m = re.match(r'^!!! (\w+)\s*(?:"([^"]*)")?', lines[i])
        if m:
            adm_type = m.group(1).lower()
            adm_title = m.group(2) or adm_type.upper()
            colors = ADMONITION_COLORS.get(adm_type, ("#448aff", "#0d2a5c", "#081a3a"))
            border_color, bg_color, _ = colors

            # Collect indented body lines
            body_lines = []
            i += 1
            while i < len(lines) and (lines[i].startswith("    ") or lines[i].strip() == ""):
                if lines[i].strip() == "" and i + 1 < len(lines) and not lines[i + 1].startswith("    "):
                    break
                body_lines.append(lines[i][4:] if lines[i].startswith("    ") else "")
                i += 1

            body_text = "\n".join(body_lines).strip()
            # We'll wrap in a special HTML block that markdown will pass through
            result.append(f'<div class="admonition adm-{adm_type}" style="border-left:4px solid {border_color}; background:{bg_color}; padding:12px 16px; margin:16px 0; border-radius:4px;">')
            result.append(f'<strong style="color:{border_color}; display:block; margin-bottom:6px;">{html_module.escape(adm_title)}</strong>')
            result.append(f'<span class="adm-body">{html_module.escape(body_text)}</span>')
            result.append('</div>')
            result.append('')
        else:
            result.append(lines[i])
            i += 1
    return "\n".join(result)


def convert_content_tabs(md_text):
    """Convert === \"Tab Title\" blocks to simple labeled sections."""
    lines = md_text.split("\n")
    result = []
    i = 0
    while i < len(lines):
        m = re.match(r'^=== "([^"]*)"', lines[i])
        if m:
            tab_title = m.group(1)
            result.append(f'**{tab_title}:**\n')
            i += 1
            # Collect indented body
            while i < len(lines) and (lines[i].startswith("    ") or lines[i].strip() == ""):
                if lines[i].strip() == "" and i + 1 < len(lines) and not lines[i + 1].startswith("    ") and not re.match(r'^=== "', lines[i + 1] if i + 1 < len(lines) else ""):
                    result.append("")
                    i += 1
                    break
                result.append(lines[i][4:] if lines[i].startswith("    ") else "")
                i += 1
        else:
            result.append(lines[i])
            i += 1
    return "\n".join(result)


# ---------------------------------------------------------------------------
# Markdown conversion
# ---------------------------------------------------------------------------

def md_to_html(md_text):
    """Convert markdown text to HTML."""
    # Pre-process admonitions and content tabs
    md_text = convert_content_tabs(md_text)
    md_text = convert_admonitions(md_text)

    if HAS_MARKDOWN:
        md = markdown.Markdown(extensions=[
            'tables',
            'fenced_code',
            'codehilite',
            'attr_list',
            TocExtension(permalink=False),
        ], extension_configs={
            'codehilite': {'css_class': 'code-block', 'guess_lang': False},
        })
        try:
            return md.convert(md_text)
        except Exception:
            # Fallback if extensions cause issues
            md = markdown.Markdown(extensions=['tables', 'fenced_code'])
            return md.convert(md_text)
    else:
        return fallback_md_to_html(md_text)


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

/* ===== ADMONITIONS ===== */
.admonition {{
  border-radius: 4px;
  margin: 16px 0;
  padding: 12px 16px;
}}
.adm-body {{
  white-space: pre-line;
  display: block;
  margin-top: 2px;
}}

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
  color: #666;
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
  Use browser search (Ctrl+F / Cmd+F) to find specific topics.
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
                fragment = ""
                if "#" in link_target:
                    fragment = "#" + link_target.split("#")[1]
                return f"[{link_text}](#{make_anchor(base)}{fragment})"
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

        # Convert to HTML
        html_content = md_to_html(md_text)

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
