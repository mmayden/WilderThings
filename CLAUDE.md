# WilderThings — AI Context

> Read this first in every session. It replaces the need to explore the repo from scratch.

## Quick Reference

```bash
pip install -r requirements.txt   # one-time setup
mkdocs serve                      # dev server at http://localhost:8000
mkdocs build --strict             # production build — fail on warnings
codespell docs/ --config .codespellrc --quiet-level=2  # spell check
```

## What This Project Is

A **mobile-first PWA** delivering 89 survival guides across 13 categories. Zero custom application code — MkDocs Material handles rendering, search, navigation, offline caching, and tag browsing through configuration alone.

```
docs/*.md  →  mkdocs.yml  →  MkDocs Material  →  GitHub Pages  →  PWA (offline)
 (content)     (config)         (build)              (deploy)         (client)
```

**Maintain only two things: content (`docs/`) and config (`mkdocs.yml`).**

## Current State

| Item | Status |
|------|--------|
| Guides | 89 across 13 categories, ~21,000 lines |
| Milestones 0–4 | Complete |
| Milestone 5 | **Up next** — PWA icons, offline plugin, GitHub remote, mobile install test |
| Cross-links | 496 links across all 89 guides |
| Tags | YAML frontmatter tags on all 89 guides; tags index at `docs/tags.md` |
| Spell-check | Clean; `.codespellrc` suppresses valid domain words |
| Tables | All ≤4 columns (mobile-compliant) |
| CI | `lint.yml` (codespell + build check on PRs), `deploy.yml` (build + deploy on push to main) |
| Dependabot | Weekly PRs for pip and GitHub Actions updates |

## Security — Read First

**Content accuracy is a life-safety matter.** This project contains medical, foraging, and emergency guidance. Treat inaccurate content as a defect, not an inconvenience.

- Never fabricate survival advice. Every claim must be traceable to a credible source.
- Safety warnings must precede dangerous procedures — no exceptions.
- Medical content must include disclaimers. Never imply it replaces professional care.
- Plant/mushroom ID must include look-alike warnings.
- Regulated activities (hunting, trapping) must note legal requirements.

See [SECURITY.md](SECURITY.md) for the full security policy and how to report content issues.

## Repository Layout

```
WilderThings/
├── mkdocs.yml              # Nav tree, theme, plugins, extensions
├── requirements.txt        # Pinned: mkdocs-material==9.7.6, mkdocs-minify-plugin==0.8.0
├── .codespellrc            # Spell-check exceptions (sting, HACE, trough, etc.)
├── .gitignore
├── docs/                   # Content root — 13 category folders + index + assets + references + tags.md
├── templates/              # guide-template.md, checklist-template.md (not served)
├── .github/
│   ├── workflows/
│   │   ├── deploy.yml      # Build (contents:read) + Deploy (pages:write, OIDC)
│   │   └── lint.yml        # Codespell + build --strict on every push/PR
│   └── dependabot.yml      # Weekly pip + Actions updates
├── SECURITY.md             # Content accuracy policy + infrastructure security
├── CONTRIBUTING.md         # Content standards, review criteria, security guidelines
├── STYLE_GUIDE.md          # Formatting rules, mobile standards
├── PROJECT_OUTLINE.md      # Architecture, inventory, milestones, quality gates
├── TASKS.md                # Active work backlog
└── CLAUDE.md               # This file
```

## Content Architecture

Each guide is a standalone `.md` file with YAML frontmatter tags. Adding a guide = create file + add nav entry in `mkdocs.yml`.

### Categories (13)

| Category | Folder | Count |
|----------|--------|-------|
| Medical | `medical/` | 10 |
| Water | `water/` | 5 |
| Shelter | `shelter/` | 6 |
| Fire | `fire/` | 7 |
| Food | `food/` | 11 |
| Navigation | `navigation/` | 5 |
| Wildlife | `wildlife/` | 9 |
| Tools & Craft | `tools-and-craft/` | 6 |
| Psychology | `psychology/` | 4 |
| Scenarios | `scenarios/` | 6 |
| Climate-Specific | `climate-specific/` | 6 |
| Preparedness | `preparedness/` | 6 |
| References | `references/` | 8 |

### Guide Structure

Every guide follows `templates/guide-template.md`:

```
---
tags:
  - category-tag
  - topic-tag
---
# Title
> One-line summary
## At a Glance          (3-5 critical bullet points)
## [Body Sections]      (H2 major, H3 sub)
## Common Mistakes      (what people get wrong)
## Quick Reference      (condensed lookup table — ≤4 cols)
## See Also             (3-8 cross-category links with em-dash descriptions)
## Sources              (citations)
```

All sections are required. Tables must be ≤4 columns. See `STYLE_GUIDE.md` for full rules.

## Cross-Linking

Every guide has `## See Also` with links to related guides **across categories**.

- **Use relative paths**: `../category/guide.md` cross-category, `guide.md` same-category
- **Em-dash description** after each link explaining the relationship
- **3-8 links per guide** — enough to be useful, not so many it's noise
- **Add reciprocal links**: if A links to B, add B → A
- **Place between Quick Reference and Sources**

## Quality Gates (before marking a guide complete)

1. Follows guide template — all required sections present
2. YAML frontmatter with `tags:`
3. 3-8 cross-category See Also links with descriptions
4. Admonitions used (no raw `> **WARNING:**` blockquotes)
5. Tables ≤4 columns
6. Metric + imperial measurements throughout
7. Safety warnings precede dangerous procedures
8. Passes `codespell docs/ --config .codespellrc --quiet-level=2`
9. Passes `mkdocs build --strict`

## MkDocs Quick Reference

### Admonitions

```markdown
!!! danger "WARNING"       # Red — risk of death/serious injury
!!! warning "CAUTION"      # Orange — risk of worsening situation
!!! note                   # Blue — important context
!!! tip                    # Green — helpful technique
```

### Collapsible (for long warnings)

```markdown
??? danger "Toxic look-alikes"
    Content collapsed by default.
```

### Content Tabs

```markdown
=== "North America"
    Content here.

=== "Europe"
    Content here.
```

### Internal Links

```markdown
See [Guide Title](../category/guide-name.md) for details.
```

### Tags Frontmatter

```yaml
---
tags:
  - medical
  - first-aid
  - emergency
---
```

## Commit Convention

```
content: add [guide-name]       — new guide
content: update [guide-name]    — revisions to existing guide
docs: [description]             — project documentation changes
fix: [description]              — corrections to factual content
chore: [description]            — structural/organizational changes
build: [description]            — MkDocs config, CI/CD, dependencies
style: [description]            — CSS, theme, layout changes
security: [description]         — security policy, CI hardening
```

## Tech Stack

| Layer | Tool |
|-------|------|
| Content | Markdown in `docs/` |
| Build | MkDocs Material 9.7.6 |
| Tags | MkDocs Material built-in tags plugin |
| Search | lunr.js (built-in, offline-capable) |
| Hosting | GitHub Pages |
| CI/CD | GitHub Actions (deploy.yml + lint.yml) |
| Deps | Python: pinned in requirements.txt, auto-updated by Dependabot |
| Spell-check | codespell 2.4.2 via lint.yml |

## Milestone 5 — What's Next

1. Generate PWA icons: favicon (16×16, 32×32), apple-touch-icon (180×180), manifest icons (192×192, 512×512)
2. Add `manifest.webmanifest` to `docs/` with name, icons, display, theme_color
3. Enable MkDocs Material offline plugin in `mkdocs.yml`
4. Configure `extra.manifest` in `mkdocs.yml`
5. Push to GitHub remote (`git remote add origin ...`)
6. Verify GitHub Actions deploys (Settings → Pages → Source: GitHub Actions)
7. Test "Add to Home Screen" on iOS Safari and Android Chrome
