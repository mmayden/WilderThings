# WilderThings — Survival Guide Collection

A comprehensive, mobile-first survival knowledge base — searchable, offline-capable, and installable on any phone.

## What Is This?

89 survival guides across 13 categories covering medical emergencies, wilderness skills, wildlife encounters, climate-specific survival, disaster preparedness, and real-world scenarios. Built as a Progressive Web App (PWA) so you can install it on your phone and access it anywhere — even without signal.

## Quick Start

### For Users

Visit the site URL, tap **"Add to Home Screen"** on your phone, and you have an offline survival reference app.

### For Contributors

```bash
git clone https://github.com/YOUR_USERNAME/WilderThings.git
cd WilderThings
pip install -r requirements.txt
mkdocs serve
# Open http://localhost:8000
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for content standards and [STYLE_GUIDE.md](STYLE_GUIDE.md) for formatting rules.

## Tech Stack

| Layer | Tool |
|-------|------|
| Content | Markdown files in `docs/` |
| Site generator | [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) |
| Search | Built-in lunr.js (works offline) |
| Hosting | GitHub Pages (free) |
| CI/CD | GitHub Actions (auto-deploy on push) |

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

**89 guides total** | ~21,000 lines of content

## The Rule of Threes

Guides are prioritized around the survival rule of threes:

- **3 minutes** without air (medical/CPR)
- **3 hours** without shelter (in harsh conditions)
- **3 days** without water
- **3 weeks** without food

## Project Structure

```
WilderThings/
├── mkdocs.yml              # Site configuration and navigation
├── requirements.txt        # Python dependencies
├── docs/                   # All guide content (served as the site)
│   ├── index.md            # Homepage
│   ├── assets/             # CSS overrides, images
│   ├── medical/            # 10 guides
│   ├── water/              # 5 guides
│   ├── shelter/            # 6 guides
│   ├── fire/               # 7 guides
│   ├── food/               # 11 guides
│   ├── navigation/         # 5 guides
│   ├── wildlife/           # 9 guides
│   ├── tools-and-craft/    # 6 guides
│   ├── climate-specific/   # 6 guides
│   ├── preparedness/       # 6 guides
│   ├── psychology/         # 4 guides
│   ├── scenarios/          # 6 guides
│   └── references/         # Glossary, checklists, book list, sources
├── templates/              # Guide/checklist templates (for authors)
├── .github/workflows/      # CI/CD auto-deploy
├── CONTRIBUTING.md         # Content standards and dev workflow
├── STYLE_GUIDE.md          # Formatting rules
├── PROJECT_OUTLINE.md      # Roadmap and milestones
├── TASKS.md                # Work backlog
└── CLAUDE.md               # AI assistant context
```

## What's Next

**Milestone 4 (P3 — Polish):** All 89 guides are cross-linked across categories (496 links). Remaining: search keywords/tags in frontmatter, full review pass, spell-check, mobile UX audit. See [TASKS.md](TASKS.md) for the full backlog.

## Disclaimer

This collection is for **educational and reference purposes only**. It is not a substitute for professional medical advice, certified wilderness training, or hands-on practice. Always seek professional instruction for critical skills like CPR, wound care, and navigation. The authors assume no liability for actions taken based on this content.

## License

This project is unlicensed pending a decision on open-source licensing. Content is currently for personal use.
