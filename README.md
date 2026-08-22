# WilderThings — Survival Guide Collection

A comprehensive, mobile-first survival knowledge base — searchable, and genuinely usable with no internet connection.

## What Is This?

89 survival guides across 13 categories covering medical emergencies, wilderness skills, wildlife encounters, climate-specific survival, disaster preparedness, and real-world scenarios.

The primary deliverable is a **self-contained offline copy** — a folder you can put on a phone, USB stick, or SD card and open in any browser with no internet, no server, and no install. A hosted site exists as an online convenience mirror.

**Content accuracy is a life-safety matter.** Every guide is sourced from military field manuals, medical references, and established survival literature. See [SECURITY.md](SECURITY.md) for how to report inaccurate or dangerous content.

## Quick Start

### For Users — the offline copy (recommended)

Get `wilderthings-offline.zip`, unzip it, and open `index.html` in any browser. That is the whole procedure. Full-text search across all 89 guides works with no connection.

Copy the folder anywhere you like — phone storage, USB stick, SD card, another machine. It keeps working with no signal and no access to this repository.

To build it yourself:

```bash
pip install -r requirements.txt
./scripts/build-offline.sh
# -> site-offline/index.html  and  wilderthings-offline.zip
```

The build script verifies the result makes **zero external network requests** and fails if that is ever untrue.

### For Users — the online site

Browse at <https://mmayden.github.io/WilderThings/>. You can add it to your home screen for an app icon.

> [!WARNING]
> The hosted site currently **requires a connection**. "Add to Home Screen" gives
> you an icon and a full-screen window, but does not yet store the guides on your
> device — there is no service worker. For true no-signal access, use the offline
> copy. See [TASKS.md](TASKS.md).

### For Contributors

```bash
git clone https://github.com/mmayden/WilderThings.git
cd WilderThings
pip install -r requirements.txt
mkdocs serve
# Open http://localhost:8000
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for content standards, [STYLE_GUIDE.md](STYLE_GUIDE.md) for formatting rules, and [SECURITY.md](SECURITY.md) for the security policy.

## Tech Stack

| Layer | Tool |
|-------|------|
| Content | Markdown files in `docs/` |
| Site generator | [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) 9.x |
| Offline build | `mkdocs.offline.yml` — Material `offline` plugin, system fonts, vendored shim |
| Search | Built-in lunr.js (index inlined for offline use) |
| Tags | MkDocs Material tags plugin |
| Hosting | GitHub Pages (online mirror only) |
| CI/CD | GitHub Actions (build + deploy, least-privilege) |
| Deps | Pinned in `requirements.txt`, auto-updated by Dependabot |

## Guide Categories

### Core Survival

| Category | Guides | Description |
|----------|--------|-------------|
| [Medical](docs/medical/) | 10 | First aid, CPR, trauma, fractures, hypothermia, bites, infections, poisoning, improvised medicine |
| [Water](docs/water/) | 5 | Finding, purifying, filtering, storing, desert/sea procurement |
| [Shelter](docs/shelter/) | 6 | Principles, debris hut, snow, desert, tarp/poncho, long-term structures |
| [Fire](docs/fire/) | 7 | Principles, friction, spark/lens, from nothing, wet conditions, fire types, maintenance |

### Skills and Knowledge

| Category | Guides | Description |
|----------|--------|-------------|
| [Food](docs/food/) | 11 | Foraging, edible plants (temperate + tropical), mushrooms, hunting, trapping, fishing, insects, butchering, preservation, cooking without gear |
| [Navigation](docs/navigation/) | 5 | Map/compass, natural navigation, signaling, GPS/electronics, terrain association |
| [Wildlife](docs/wildlife/) | 9 | Bears, big cats, snakes, spiders, insects, wolves, marine dangers, moose/ungulates, gators/crocs |
| [Tools & Craft](docs/tools-and-craft/) | 6 | Knives, knots, cordage, improvised tools, containers, clothing/insulation |

### Environment and Preparedness

| Category | Guides | Description |
|----------|--------|-------------|
| [Climate-Specific](docs/climate-specific/) | 6 | Arctic, desert, jungle, mountain, ocean, urban survival |
| [Preparedness](docs/preparedness/) | 6 | Bug-out bag, EDC, vehicle kit, home preparedness, communications, financial |

### Mindset and Scenarios

| Category | Guides | Description |
|----------|--------|-------------|
| [Psychology](docs/psychology/) | 4 | Survival mindset, stress management, group dynamics, solo survival |
| [Scenarios](docs/scenarios/) | 6 | Lost in woods, animal attack, injured alone, vehicle breakdown, natural disaster, water crossing |

### Reference

| Category | Items | Description |
|----------|-------|-------------|
| [References](docs/references/) | 8 | Glossary, book list, sources, 5 field checklists |

**89 guides total** | ~21,000 lines of content | 496 cross-category links | Tags on every guide

## The Rule of Threes

Guides are prioritized around the survival rule of threes:

- **3 minutes** without air (medical/CPR)
- **3 hours** without shelter (in harsh conditions)
- **3 days** without water
- **3 weeks** without food

## Project Structure

```
WilderThings/
├── mkdocs.yml                  # Site configuration and navigation (online build)
├── mkdocs.offline.yml          # Offline build — self-contained, no network
├── scripts/
│   ├── build-offline.sh        # Builds + verifies + zips the offline copy
│   └── generate-icons.py       # Regenerates the PWA/favicon icon set
├── overrides/main.html         # Manifest link + iOS install meta tags
├── requirements.txt            # Pinned Python dependencies
├── .codespellrc                # Spell-check config (domain-specific word exceptions)
├── .gitignore
├── docs/                       # All guide content (MkDocs serves this as the site root)
│   ├── index.md                # Homepage
│   ├── tags.md                 # Auto-generated tags index
│   ├── assets/css/custom.css   # Mobile-first CSS overrides
│   ├── medical/                # 10 guides
│   ├── water/                  # 5 guides
│   ├── shelter/                # 6 guides
│   ├── fire/                   # 7 guides
│   ├── food/                   # 11 guides
│   ├── navigation/             # 5 guides
│   ├── wildlife/               # 9 guides
│   ├── tools-and-craft/        # 6 guides
│   ├── climate-specific/       # 6 guides
│   ├── preparedness/           # 6 guides
│   ├── psychology/             # 4 guides
│   ├── scenarios/              # 6 guides
│   └── references/             # Glossary, checklists, book list, sources
├── templates/                  # Guide and checklist templates (not served)
├── .github/
│   ├── workflows/
│   │   ├── deploy.yml          # Build + deploy (least-privilege, split jobs)
│   │   └── lint.yml            # Spell-check + build check on PRs
│   └── dependabot.yml          # Automated dependency security updates
├── SECURITY.md                 # Security policy and content accuracy reporting
├── CONTRIBUTING.md             # Content standards and dev workflow
├── STYLE_GUIDE.md              # Formatting rules
├── PROJECT_OUTLINE.md          # Architecture, inventory, milestones
├── TASKS.md                    # Work backlog
└── CLAUDE.md                   # AI assistant context
```

## Current Status

All content milestones are complete, and the offline copy — the primary deliverable — works:

| Milestone | Scope | Status |
|-----------|-------|--------|
| 0 — Platform | MkDocs, CI/CD, theme, CSS | Complete |
| 1 — Foundation (P0) | 14 life-critical guides | Complete |
| 2 — Critical Skills (P1) | 36 guides | Complete |
| 3 — Advanced (P2) | 34 guides | Complete |
| 4 — Polish (P3) | Tags, review pass, spell-check, mobile UX | Complete |
| 5 — Delivery | Offline build, icons, manifest | Offline copy **done**; hosted offline caching outstanding |

Remaining: a service worker so the hosted site also works without signal, plus
home-screen install testing on real iOS/Android hardware. See [TASKS.md](TASKS.md).

## GitHub Pages Setup

This project uses the modern GitHub Actions deployment approach (OIDC, no long-lived tokens). **One-time configuration required:**

1. Go to **Settings → Pages**
2. Under *Source*, select **GitHub Actions** (not "Deploy from branch")
3. Push to `main` — the workflow handles the rest

## Disclaimer

This collection is for **educational and reference purposes only**. It is not a substitute for professional medical advice, certified wilderness training, or hands-on practice. Always seek professional instruction for critical skills like CPR, wound care, and navigation. The authors assume no liability for actions taken based on this content.

## License

This project is unlicensed pending a decision on open-source licensing. Content is currently for personal use.
