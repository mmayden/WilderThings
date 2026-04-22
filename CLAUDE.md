# WilderThings — AI Context

> Context for Claude Code sessions. Read this first; reference linked docs for details.

## Quick Reference

```bash
pip install -r requirements.txt   # one-time setup
mkdocs serve                      # dev server at http://localhost:8000
mkdocs build                      # build to site/
```

## What This Project Is

A **mobile-first PWA** delivering 89 survival guides across 13 categories. Zero custom application code — MkDocs Material handles rendering, search, navigation, and offline caching through configuration alone.

```
docs/*.md  -->  mkdocs.yml  -->  MkDocs Material  -->  GitHub Pages  -->  PWA (offline)
 (content)      (config)          (build)               (deploy)          (client)
```

**The only things to maintain are content (`docs/`) and config (`mkdocs.yml`).**

## Current State

| Item | Status |
|------|--------|
| Guides | 89 across 13 categories, ~21,000 lines |
| Milestones 0-3 | Complete (platform, P0, P1, P2) |
| Milestone 4 | **In progress** — cross-linking done; search tags, review pass, spell-check, mobile UX remain |
| Platform | MkDocs builds clean; PWA icons + offline plugin + GitHub remote still TODO |
| Cross-links | 496 links across all 89 guides (all categories interlinked) |

## Repository Layout

```
WilderThings/
├── mkdocs.yml              # Nav tree, theme, plugins, extensions
├── requirements.txt        # mkdocs-material, mkdocs-minify-plugin
├── docs/                   # Content root (13 category folders + index + assets + references)
├── templates/              # guide-template.md, checklist-template.md (not served)
├── .github/workflows/      # deploy.yml — auto-deploy on push to main
├── CONTRIBUTING.md          -> Content standards, review criteria, dev workflow
├── STYLE_GUIDE.md           -> Formatting rules, admonitions, tables, mobile
├── PROJECT_OUTLINE.md       -> Full roadmap, guide inventory, milestones
├── TASKS.md                 -> Active work backlog
└── CLAUDE.md               # This file
```

## Content Architecture

Each guide is a standalone `.md` file in a category folder under `docs/`. Adding a guide = create the file + add a nav entry in `mkdocs.yml`.

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
# Title
> One-line summary
## At a Glance          (3-5 critical bullet points)
## [Body Sections]      (H2 major, H3 sub)
## Common Mistakes      (what people get wrong)
## Quick Reference      (condensed lookup table)
## See Also             (cross-category links with descriptions)
## Sources              (citations)
```

All sections are required. See `STYLE_GUIDE.md` for formatting details.

## Cross-Linking Conventions

Every guide has a `## See Also` section with links to related guides **across categories**. This is a core navigation feature.

### Format

```markdown
## See Also

- [Guide Title](relative-path.md) — one-line description of why it's related.
```

### Rules

- **Link across categories, not just within.** A medical guide should link to relevant scenarios, tools, and psychology guides — not only other medical guides.
- **Use relative paths** from the current file: `../category/guide.md` for cross-category, `guide.md` for same-category.
- **Include a description** after the em dash explaining the relationship.
- **3-8 links per guide** is the target range. Enough to be useful, not so many it's noise.
- **Place See Also between Quick Reference and Sources** in every guide.
- When adding a new guide, add See Also links to it **and** add reciprocal links from related existing guides.

## Writing Guides

### Process

1. Follow `STYLE_GUIDE.md` for formatting
2. Start from `templates/guide-template.md`
3. Follow `CONTRIBUTING.md` for content standards
4. Place in the correct `docs/` subfolder
5. Add nav entry in `mkdocs.yml`
6. Add cross-category See Also links (and reciprocal links in related guides)
7. Verify with `mkdocs serve`

### Key Principles

- **Accuracy over volume.** Source from military manuals, medical references, established literature. Never fabricate survival advice.
- **Actionable under stress.** Short sentences. Numbered steps. Critical info first.
- **No filler.** Every sentence must add value.
- **Dual measurements.** Always include metric and imperial.
- **Safety first.** Warnings before procedures.
- **Mobile-first.** Narrow tables (3-4 cols max), short paragraphs, scannable at phone width.

### Content Safety

- Medical content: include disclaimers, never replace professional training
- Plant/mushroom ID: warn about look-alikes and regional variation
- Hunting/trapping: note legal jurisdictional variation
- Financial/legal: disclaim professional advice

## MkDocs Quick Reference

### Admonitions

```markdown
!!! danger "WARNING"       # Red — risk of death/serious injury
!!! warning "CAUTION"      # Orange — risk of worsening situation
!!! note                   # Blue — important context
!!! tip                    # Green — helpful technique
```

### Content Tabs

```markdown
=== "Tab 1"
    Content for tab 1.

=== "Tab 2"
    Content for tab 2.
```

### Internal Links

```markdown
See [Guide Title](../category/guide-name.md) for details.
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
```

## Tech Stack

| Layer | Tool |
|-------|------|
| Content | Markdown in `docs/` |
| Build | MkDocs Material 9.x |
| Search | lunr.js (built-in, offline-capable) |
| Hosting | GitHub Pages |
| CI/CD | GitHub Actions (`deploy.yml`) |
| Deps | Python: `mkdocs-material`, `mkdocs-minify-plugin` |
