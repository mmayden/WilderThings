# WilderThings — AI Context

> Read this first in every session. It replaces the need to explore the repo from scratch.

## Quick Reference

```bash
pip install -r requirements.txt   # one-time setup
mkdocs serve                      # dev server at http://localhost:8000
mkdocs build --strict             # online build — fail on warnings
./scripts/build-offline.sh        # OFFLINE folder + zip  <-- primary deliverable
python3 build_single_file.py      # ONE self-contained .html file
python3 scripts/verify.py --offline site-offline --single wilderthings-mobile.html
codespell docs/ --config .codespellrc --quiet-level=2  # spell check
```

## What This Project Is

**Scope: someone stranded in the wilderness who needs to survive.** That is the whole
test. If a guide would only matter to someone who is already safe, already settled, or
somewhere other than the wilderness, it does not belong — 22 guides were archived on
2026-08-24 for failing it, including all plant and fungus identification. See
`archive/README.md` for the reasoning, and apply the same test before adding anything.

The priority order is the corpus's own: **3 minutes without air, 3 hours without shelter,
3 days without water, 3 weeks without food.** Coverage should reflect it. It did not
before the cut — food had more than twice the coverage of water.

60 survival guides across 12 categories, shipped **three ways from one content source**:

| | Build | Output | Needs network |
|---|---|---|---|
| **Primary** — offline folder | `mkdocs.offline.yml` | `site-offline/` + 2.8 MB zip | **No** |
| **Primary** — single file | `build_single_file.py` | `wilderthings-mobile.html`, 1.45 MB | **No** |
| Secondary — online mirror | `mkdocs.yml` | GitHub Pages | Yes (for now) |

```
                      ┌─ mkdocs.offline.yml ─→ site-offline/ ─→ zip   (full UI, offline)
docs/*.md ─→ nav ─────┼─ build_single_file.py ─→ one .html file       (max portability)
 (content)            └─ mkdocs.yml ──────────→ GitHub Pages          (online mirror)
```

The two offline builds are not redundant — the zip keeps the full Material UI
(sidebar nav, lunr search); the single file is one attachment you can email or
AirDrop, searched with Ctrl+F. Both must work with no network.

**The offline copy is the product.** It must work with no internet, no server, and
no install — someone opens `index.html` from a USB stick and everything works,
search included. Treat any change that introduces a network request into that
build as a defect; `scripts/build-offline.sh` fails the build if one appears.

**Maintain only content (`docs/`) and config (the two `mkdocs*.yml` files).**

## Current State

| Item | Status |
|------|--------|
| Guides | 60 across 12 categories (22 archived 2026-08-24 — see `archive/README.md`) |
| Milestones 0–4 | Complete |
| Milestone 5 | **In progress** — offline copy done and verified; hosted offline caching + device install testing remain |
| Offline copy | **Working.** `./scripts/build-offline.sh` → 12 MB folder / 2.8 MB zip, 0 external requests, search index of 2,777 docs loads under `file://` |
| Hosted site | Live at https://mmayden.github.io/WilderThings/. Installable (manifest + icons + apple-* tags) but **no service worker — requires a connection** |
| Cross-links | 496 links across all 89 guides |
| Tags | YAML frontmatter tags on all 89 guides; tags index at `docs/tags.md` |
| Spell-check | Clean; `.codespellrc` suppresses valid domain words |
| Tables | All ≤4 columns (mobile-compliant) |
| CI | `lint.yml` (codespell + build check on PRs), `deploy.yml` (build + deploy on push to main) |
| Dependabot | Weekly PRs for pip and GitHub Actions updates |

## Content Accuracy — Read First

The highest-risk guides (medical, plant/mushroom ID, water, wildlife, food
preservation) were reviewed in Aug 2026 against current clinical and
wilderness-medicine standards. Corrections applied are recorded in TASKS.md.

**Review process:** [CONTRIBUTING.md](CONTRIBUTING.md#reviewing-content-for-accuracy).

**Triage first — do not review everything.** Ask: if a reader acts on this and
it is wrong, what happens? Only "could die or be seriously injured" gets the
full treatment. Doses, times, temperatures, thresholds, and any "never"/"always"
always escalate.

Then four checks, each of which caught a real defect here:

| # | Check | Caught |
|---|-------|--------|
| 1 | True, including the *why*? | "Cook to avoid PSP" (saxitoxin is heat stable); a rain-catchment figure 30x low; "cold water closes your pores" |
| 2 | Current? | Elevation/pressure points for bleeding; the 80/70/60 rule; flail chest taping |
| 3 | **False confidence?** | The lightning crouch (displaces shelter); "smell the fermented fish" (botulinum toxin is odorless) |
| 4 | Missing? | No shellfish cross-allergy in the insect guide; no carbon monoxide in the disaster guide |

Check 3 is the one most easily missed and the reason the framework exists. The
NWS withdrew the lightning crouch in 2008 not because the posture harms you but
because believing you have a protective position delays you seeking shelter.
Ask: **if this does not work, what does the reader lose by having tried it?**

**Consistency is mechanical — script it, do not think about it.** Grep for any
number or procedure you change, including the reference checklists, which
drifted from their parent guides during the audit. Extend `scripts/verify.py`
rather than adding a manual step.

**Signal words carry severity (ANSI Z535):** DANGER = will kill or seriously
injure; WARNING = could; CAUTION = lesser harm. Severity is earned — if every
block is red the lethal ones lose their force.

**Say how sure you are.** Where trials do not exist and expert consensus is
carrying the weight, write it that way. Do not launder tradition into fact.

**Prefer checking to recalling.** Every source check during the audit changed
something — including one that corrected an earlier correction.

**Citations are the known weak point — check any you rely on.** Eight wrong citations
have been found across eight guides, five of them works that do not exist at all
(details in TASKS.md). They were found by opening sources, never by scanning
bibliographies, and every one looked plausible. `scripts/verify.py` cannot help here: it
checks that the corpus cites each work *the same way everywhere*, which a consistently
fabricated citation passes cleanly. **Internal consistency is not accuracy.** Assume any
unchecked citation is unverified, and if you are about to lean on one, open it first.

**Still outstanding:** no licensed clinician or regional botanist has reviewed
this content, and most cited sources have not been verified against the originals.
Do not describe the content as expert-reviewed.

## Sourcing Standard

Every guide's `## Sources` is split into two tiers, and the split is the point.

**Primary** — authoritative, revised, and publicly checkable. Eight families:

| For | Cite |
|---|---|
| Field technique — shelter, fire, water, navigation, signaling | `ATP 3-50.21` (2018, current), `FM 21-76`, `AFH 10-644`, `AFR 64-4` |
| Trauma and first aid | TCCC, PHTLS, ATLS, ILCOR / AHA / ANZCOR / Red Cross |
| Wilderness medicine | WMS clinical practice guidelines (per topic, revised), Auerbach |
| Disease, water, toxins | CDC (incl. Yellow Book), EPA, WHO |
| Weather and rescue | NOAA / NWS, COSPAS-SARSAT |
| Specific claims | Peer-reviewed journal articles |

**Additional reading** — trade books and first-hand accounts. Kochanski, Wiseman,
Canterbury, Mears, Gonzales and the rest. Useful, and not what a claim should rest on.

**Do not cite a military survival manual for medical content.** FM 21-76 is 1992, and
several errors corrected in this corpus came straight out of it — the lightning crouch,
pressure points for bleeding, elevation for shock. It is excellent on building a shelter
and dangerously stale on treating a casualty. Field technique from the manuals; medicine
from WMS, TCCC, and the resuscitation councils.

**A citation is a promise that someone can check it.** Twelve fabricated or wrong
citations have been found in this corpus (TASKS.md has the table). `scripts/verify.py`
checks that a work is cited the same way everywhere; it cannot check that the work
exists. If you add a source, open it first.

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
├── mkdocs.yml              # Nav tree, theme, plugins, extensions (online build)
├── mkdocs.offline.yml      # Offline build — INHERITs mkdocs.yml, no network
├── scripts/
│   ├── build-offline.sh    # Build + verify-no-network + zip the offline copy
│   ├── verify.py           # Test suite — run by CI on every push
│   └── generate-icons.py   # Regenerates the icon set (compass rose, deep orange)
├── requirements.txt        # Pinned: mkdocs-material==9.7.7, mkdocs-minify-plugin==0.8.0
├── .codespellrc            # Spell-check exceptions (sting, HACE, trough, etc.)
├── .gitignore
├── docs/                   # Content root — 13 category folders + index + assets + references + tags.md
│   ├── manifest.webmanifest    # PWA manifest (icons, start_url, theme_color)
│   └── assets/images/          # PWA icon set (favicons, apple-touch, 192/512, maskable)
├── overrides/              # Theme overrides — main.html adds manifest + apple-* install tags
├── templates/              # guide-template.md, checklist-template.md (not served)
├── .github/
│   ├── workflows/
│   │   ├── deploy.yml      # Build (contents:read) + Deploy (pages:write, OIDC)
│   │   └── lint.yml        # Codespell + build --strict on every push/PR
│   └── dependabot.yml      # Weekly pip + Actions updates
├── LICENSE                 # CC BY-SA 4.0 (guides) + MIT (tooling)
├── build_single_file.py    # Single-file HTML build
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
!!! danger "DANGER"        # Red — acting wrongly here WILL kill or maim
!!! danger "WARNING"       # Red — COULD kill or seriously injure
!!! warning "CAUTION"      # Orange — moderate/minor injury, or worsens the situation
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

## Milestone 5 — What's Left

**Done:** the offline copy (`mkdocs.offline.yml` + `scripts/build-offline.sh`), the icon set in `docs/assets/images/`, `docs/manifest.webmanifest`, and `overrides/main.html`.

**Remaining:**

1. Test "Add to Home Screen" on real iOS Safari and Android Chrome hardware
2. Decide whether the hosted site also needs offline caching (a service worker)
3. Decide how the offline zip is distributed (release asset vs. committed) — deliberately deferred

### Two different meanings of "offline" — don't conflate them

| | Offline copy (done) | Hosted offline caching (not done) |
|---|---|---|
| Mechanism | Material `offline` plugin, `file://` | Service worker on GitHub Pages |
| Config | `mkdocs.offline.yml` | Would need a hand-written `sw.js` |
| Status | **Working and verified** | Not implemented |

The `offline` plugin sets `use_directory_urls=false` and inlines the search index;
it installs **no service worker** and cannot make the *hosted* site work offline.
Those are separate problems with separate solutions — solving one does not solve
the other. A `sw.js` would be this project's first custom application code.

### Rules for keeping the offline copies genuinely offline

Anything that fetches at runtime breaks the product's core promise:

- **Never** add a webfont (`theme.font` is `false` in the offline build for exactly this reason).
- **Never** reference a CDN. Vendor it into `docs/assets/` instead — see `iframe-worker.shim.js`.
- **Never** add external images to guide content. External links in `## Sources` are fine — they are citations, not loads.
- Run `scripts/verify.py` before shipping. CI runs it on every push.

### Testing

`scripts/verify.py` is the test suite. It exists because each check corresponds
to a bug that actually shipped here:

| Check | The bug it catches |
|---|---|
| No external resource loads | A webfont/CDN silently making the "offline" copy need a network |
| All local refs resolve | Broken links in a copy with no online fallback |
| Search index present | Search silently doing nothing under `file://` |
| Unique ids (single file) | 91 documents concatenated → duplicate ids merged all content-tab radio groups, leaving every tab unselected |
| Anchors resolve (single file) | `guide.md#heading` rewritten to malformed `#guide#heading` |
| No literal `**` in text | Admonition bodies HTML-escaped instead of rendered, so **safety warnings showed raw markup** |

If you change how anything is built, add the corresponding check. A build step
without a check is a regression waiting to ship.

### Keeping the single-file build correct

`build_single_file.py` renders each guide with its own `Markdown()` instance and
concatenates them. Two consequences to respect:

1. **Its extension list must mirror `markdown_extensions` in `mkdocs.yml`**
   (`MARKDOWN_EXTENSIONS`). Guides are authored against that feature set; a
   missing extension degrades content silently rather than failing.
2. **All generated ids must stay namespaced per guide** (`namespace_ids`).
   Without it, ids collide across guides.
