# Project Outline — WilderThings

## Vision

Build the most comprehensive, well-organized, and practically useful survival knowledge base — delivered as a mobile-first PWA that works offline. Every guide should be something you'd trust with your life: accurate, clear, searchable, and available without signal.

## Architecture

```
┌─────────────────────────────────────────────┐
│  Content Layer (Markdown in docs/)          │
│  ├── 13 category folders                   │
│  ├── 89 guides (P0–P2 complete)            │
│  └── Templates define structure             │
├─────────────────────────────────────────────┤
│  Build Layer (MkDocs Material 9.x)          │
│  ├── mkdocs.yml → nav, theme, plugins       │
│  ├── lunr.js → client-side search index     │
│  └── Service worker → offline caching       │
├─────────────────────────────────────────────┤
│  Deploy Layer (GitHub Actions → GH Pages)   │
│  ├── Auto-build on push to main             │
│  └── Static files served via CDN            │
├─────────────────────────────────────────────┤
│  Client Layer (PWA)                         │
│  ├── Mobile-responsive Material theme       │
│  ├── "Add to Home Screen" install           │
│  ├── Offline-first via service worker       │
│  └── Full-text search (offline-capable)     │
└─────────────────────────────────────────────┘
```

## Scope

### In Scope

- Wilderness survival across all major biomes (temperate, arctic, desert, tropical, mountain, ocean)
- Medical first aid and field medicine for emergencies
- Wildlife identification, behavior, and encounter protocols
- Bushcraft skills (fire, shelter, tools, cordage, navigation)
- Food acquisition (foraging, hunting, trapping, fishing, insect harvesting)
- Water sourcing, purification, and storage
- Urban and disaster survival
- Preparedness planning (EDC, bug-out bags, home prep, communications)
- Survival psychology and decision-making
- Real-world scenario walkthroughs
- Quick-reference checklists for field use
- Mobile-first PWA delivery with offline support
- Full-text search across all content

### Out of Scope (for now)

- Native mobile app (iOS/Android)
- User accounts or personalization
- Video or multimedia content
- Weapons and combat
- Long-term homesteading and agriculture (may revisit)
- Political or ideological content
- Backend/server/database

## Guide Inventory

### Medical (10 guides)

| # | Guide | Status | Priority |
|---|-------|--------|----------|
| 1 | first-aid-basics.md | **Done** | P0 |
| 2 | cpr-and-choking.md | **Done** | P0 |
| 3 | fractures-and-splints.md | **Done** | P0 |
| 4 | hypothermia-and-heatstroke.md | **Done** | P0 |
| 5 | trauma-and-triage.md | **Done** | P0 |
| 6 | bites-and-stings.md | **Done** | P1 |
| 7 | wound-infection.md | **Done** | P1 |
| 8 | dehydration-and-waterborne.md | **Done** | P1 |
| 9 | plant-poisoning.md | **Done** | P1 |
| 10 | improvised-medicine.md | **Done** | P2 |

### Water (5 guides)

| # | Guide | Status | Priority |
|---|-------|--------|----------|
| 1 | finding-water.md | **Done** | P0 |
| 2 | purification.md | **Done** | P0 |
| 3 | improvised-filters.md | **Done** | P1 |
| 4 | water-storage.md | **Done** | P1 |
| 5 | desert-and-sea-water.md | **Done** | P2 |

### Shelter (6 guides)

| # | Guide | Status | Priority |
|---|-------|--------|----------|
| 1 | shelter-principles.md | **Done** | P0 |
| 2 | debris-hut.md | **Done** | P0 |
| 3 | snow-shelters.md | **Done** | P1 |
| 4 | desert-shelter.md | **Done** | P1 |
| 5 | tarp-and-poncho.md | **Done** | P1 |
| 6 | long-term-structures.md | **Done** | P2 |

### Fire (7 guides)

| # | Guide | Status | Priority |
|---|-------|--------|----------|
| 1 | fire-principles.md | **Done** | P0 |
| 2 | friction-methods.md | **Done** | P0 |
| 3 | spark-methods.md | **Done** | P0 |
| 4 | fire-from-nothing.md | **Done** | P1 |
| 5 | fire-in-wet-conditions.md | **Done** | P1 |
| 6 | fire-types.md | **Done** | P1 |
| 7 | maintaining-fire.md | **Done** | P1 |

### Food (11 guides)

| # | Guide | Status | Priority |
|---|-------|--------|----------|
| 1 | foraging-basics.md | **Done** | P1 |
| 2 | edible-plants-temperate.md | **Done** | P1 |
| 3 | mushroom-identification.md | **Done** | P1 |
| 4 | hunting-basics.md | **Done** | P1 |
| 5 | trapping-and-snares.md | **Done** | P1 |
| 6 | fishing-improvised.md | **Done** | P1 |
| 7 | edible-plants-tropical.md | **Done** | P2 |
| 8 | insect-foraging.md | **Done** | P2 |
| 9 | field-butchering.md | **Done** | P2 |
| 10 | food-preservation.md | **Done** | P2 |
| 11 | cooking-without-gear.md | **Done** | P2 |

### Navigation (5 guides)

| # | Guide | Status | Priority |
|---|-------|--------|----------|
| 1 | map-and-compass.md | **Done** | P1 |
| 2 | natural-navigation.md | **Done** | P1 |
| 3 | signaling-for-rescue.md | **Done** | P0 |
| 4 | gps-and-electronics.md | **Done** | P2 |
| 5 | terrain-association.md | **Done** | P2 |

### Wildlife (9 guides)

| # | Guide | Status | Priority |
|---|-------|--------|----------|
| 1 | bear-safety.md | **Done** | P1 |
| 2 | big-cats.md | **Done** | P1 |
| 3 | venomous-snakes.md | **Done** | P1 |
| 4 | venomous-spiders.md | **Done** | P1 |
| 5 | insect-threats.md | **Done** | P1 |
| 6 | wolves-and-canids.md | **Done** | P2 |
| 7 | marine-dangers.md | **Done** | P2 |
| 8 | moose-and-ungulates.md | **Done** | P2 |
| 9 | alligators-and-crocs.md | **Done** | P2 |

### Tools and Craft (6 guides)

| # | Guide | Status | Priority |
|---|-------|--------|----------|
| 1 | knife-use-and-care.md | **Done** | P1 |
| 2 | knots-and-lashing.md | **Done** | P1 |
| 3 | cordage.md | **Done** | P1 |
| 4 | improvised-tools.md | **Done** | P2 |
| 5 | containers-and-vessels.md | **Done** | P2 |
| 6 | clothing-and-insulation.md | **Done** | P2 |

### Psychology (4 guides)

| # | Guide | Status | Priority |
|---|-------|--------|----------|
| 1 | survival-mindset.md | **Done** | P0 |
| 2 | stress-management.md | **Done** | P1 |
| 3 | group-dynamics.md | **Done** | P2 |
| 4 | solo-survival.md | **Done** | P2 |

### Scenarios (6 guides)

| # | Guide | Status | Priority |
|---|-------|--------|----------|
| 1 | lost-in-woods.md | **Done** | P1 |
| 2 | animal-attack.md | **Done** | P1 |
| 3 | injured-and-alone.md | **Done** | P1 |
| 4 | vehicle-breakdown-remote.md | **Done** | P2 |
| 5 | natural-disaster.md | **Done** | P2 |
| 6 | water-crossing.md | **Done** | P2 |

### Climate-Specific (6 guides)

| # | Guide | Status | Priority |
|---|-------|--------|----------|
| 1 | arctic-survival.md | **Done** | P2 |
| 2 | desert-survival.md | **Done** | P2 |
| 3 | jungle-survival.md | **Done** | P2 |
| 4 | mountain-survival.md | **Done** | P2 |
| 5 | ocean-survival.md | **Done** | P2 |
| 6 | urban-survival.md | **Done** | P2 |

### Preparedness (6 guides)

| # | Guide | Status | Priority |
|---|-------|--------|----------|
| 1 | bug-out-bag.md | **Done** | P2 |
| 2 | everyday-carry.md | **Done** | P2 |
| 3 | vehicle-kit.md | **Done** | P2 |
| 4 | home-preparedness.md | **Done** | P2 |
| 5 | communication-plans.md | **Done** | P2 |
| 6 | financial-preparedness.md | **Done** | P2 |

### References (8 items)

| # | Item | Status | Priority |
|---|------|--------|----------|
| 1 | glossary.md | **Done** | P3 |
| 2 | book-list.md | **Done** | P3 |
| 3 | sources.md | **Done** | P3 |
| 4 | checklists/ (5 checklists) | **Done** | P3 |

## Milestones

### Milestone 0 — Platform Setup ✓

MkDocs Material configured, content migrated to `docs/`, GitHub Actions deploying.

- MkDocs config with full nav tree (89+ entries)
- Material theme with dark/light toggle (slate + deep orange)
- GitHub Actions CI/CD pipeline
- Content migrated from root to `docs/`
- All admonitions converted from blockquote format (131 conversions)
- Custom CSS for mobile readability
- Internal cross-links verified

**Status:** Complete — remaining: PWA icons, PWA offline plugin, GitHub remote setup, mobile install testing

### Milestone 1 — Foundation (P0) ✓

All life-or-death basics: core medical, water, shelter, fire, psychology, rescue signaling.

**14 guides** | **Status:** Complete

### Milestone 2 — Critical Skills (P1) ✓

Food, wildlife, tools, scenarios + extended medical, shelter, fire, water, navigation, psychology.

**36 guides** | **Status:** Complete

### Milestone 3 — Advanced & Situational (P2) ✓

Climate-specific survival (arctic, desert, jungle, mountain, ocean, urban), preparedness (bug-out bag, EDC, vehicle kit, home, comms, financial), extended food (tropical plants, insects, butchering, preservation, no-gear cooking), extended wildlife (wolves, marine, moose, gators/crocs), extended tools (improvised tools, containers, clothing), advanced navigation (GPS, terrain association), advanced psychology (group dynamics, solo survival), extended scenarios (vehicle breakdown, natural disaster, water crossing), plus improvised medicine, desert/sea water, and long-term shelter.

**34 guides** | **Status:** Complete

### Milestone 4 — Polish (P3)

Cross-linking, review pass, search optimization, mobile UX audit.

- [x] Cross-link related guides across categories (496 links across all 89 guides)
- [ ] Add search keywords/tags to guide frontmatter
- [ ] Full review pass against CONTRIBUTING.md criteria
- [ ] Spell-check and grammar pass on all guides
- [ ] Mobile UX review (tables, readability, navigation)

**Status:** In progress — cross-linking complete, remaining tasks queued

## Quality Gates

A guide moves through these states:

- **Planned:** Scoped in the inventory, not yet written
- **Draft:** Content written, follows template structure, admonitions used
- **Done:** Passes all review criteria in CONTRIBUTING.md, cross-linked, verified
