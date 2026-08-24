# Project Outline — WilderThings

## Vision

Build the most comprehensive, well-organized, and practically useful survival knowledge base — delivered primarily as a **self-contained offline copy you can hand to anyone**. Every guide should be something you'd trust with your life: accurate, clear, searchable, and available without signal.

The failure mode that matters is a survival guide that needs a connection at the moment you have none. So the product is a folder that opens from `index.html` with no internet, no server, and no install. The hosted site is a convenience mirror, not the deliverable.

**Accuracy is a life-safety matter.** Content quality and correctness are treated as security concerns — see [SECURITY.md](SECURITY.md).

## Architecture

```
┌─────────────────────────────────────────────┐
│  Content Layer (Markdown in docs/)          │
│  ├── 12 category folders                   │
│  ├── 60 guides (22 archived 2026-08-24)              │
│  ├── YAML frontmatter tags on every guide  │
│  └── Templates enforce structure            │
├─────────────────────────────────────────────┤
│  Build Layer (MkDocs Material 9.x)          │
│  ├── mkdocs.yml → nav, theme, plugins       │
│  ├── tags plugin → browseable tag index     │
│  ├── lunr.js → offline full-text search     │
│  └── minify plugin → smaller assets         │
├─────────────────────────────────────────────┤
│  Quality Gates (CI via GitHub Actions)      │
│  ├── lint.yml: codespell + build --strict  │
│  ├── deploy.yml: build then deploy          │
│  └── Dependabot: weekly dep updates         │
├─────────────────────────────────────────────┤
│  Deploy Layer (GitHub Actions → GH Pages)   │
│  ├── OIDC — no long-lived secrets           │
│  ├── Least-privilege: build=read,           │
│  │   deploy=pages:write only               │
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
- Full-text search and tag-based browsing across all content

### Out of Scope

- Native mobile app (iOS/Android)
- User accounts, personalization, or data collection
- Video or multimedia content
- Weapons and combat
- Long-term homesteading and agriculture (may revisit)
- Political or ideological content
- Backend, server, or database

## Guide Inventory

All 60 guides are complete. Scope is **someone stranded in the wilderness who needs to
survive** — if a guide would only matter to someone already safe, already settled, or
somewhere other than the wilderness, it does not belong.

All 60 guides are complete. A further 22 were archived on 2026-08-24 for falling outside the project's scope — see `archive/README.md`. Statuses are not repeated; this table serves as a reference index.

### Medical (10)

| Guide | Priority |
|-------|----------|
| first-aid-basics.md | P0 |
| cpr-and-choking.md | P0 |
| fractures-and-splints.md | P0 |
| hypothermia-and-heatstroke.md | P0 |
| trauma-and-triage.md | P0 |
| bites-and-stings.md | P1 |
| wound-infection.md | P1 |
| dehydration-and-waterborne.md | P1 |
| plant-poisoning.md | P1 |
| improvised-medicine.md | P2 |

### Water (4)

| Guide | Priority |
|-------|----------|
| finding-water.md | P0 |
| purification.md | P0 |
| improvised-filters.md | P1 |
| desert-and-sea-water.md | P2 |

### Shelter (5)

| Guide | Priority |
|-------|----------|
| shelter-principles.md | P0 |
| debris-hut.md | P0 |
| snow-shelters.md | P1 |
| desert-shelter.md | P1 |
| tarp-and-poncho.md | P1 |

### Fire (4)

| Guide | Priority |
|-------|----------|
| fire-principles.md | P0 |
| spark-methods.md | P0 |
| fire-in-wet-conditions.md | P1 |
| fire-types.md | P1 |

### Food (4)

| Guide | Priority |
|-------|----------|
| foraging-basics.md | P1 |
| trapping-and-snares.md | P1 |
| fishing-improvised.md | P1 |
| insect-foraging.md | P2 |

### Navigation (5)

| Guide | Priority |
|-------|----------|
| map-and-compass.md | P1 |
| natural-navigation.md | P1 |
| signaling-for-rescue.md | P0 |
| gps-and-electronics.md | P2 |
| terrain-association.md | P2 |

### Wildlife (9)

| Guide | Priority |
|-------|----------|
| bear-safety.md | P1 |
| big-cats.md | P1 |
| venomous-snakes.md | P1 |
| venomous-spiders.md | P1 |
| insect-threats.md | P1 |
| wolves-and-canids.md | P2 |
| marine-dangers.md | P2 |
| moose-and-ungulates.md | P2 |
| alligators-and-crocs.md | P2 |

### Tools and Craft (3)

| Guide | Priority |
|-------|----------|
| knife-use-and-care.md | P1 |
| knots-and-lashing.md | P1 |
| cordage.md | P1 |

### Psychology (2)

| Guide | Priority |
|-------|----------|
| survival-mindset.md | P0 |
| stress-management.md | P1 |

### Scenarios (5)

| Guide | Priority |
|-------|----------|
| lost-in-woods.md | P1 |
| animal-attack.md | P1 |
| injured-and-alone.md | P1 |
| vehicle-breakdown-remote.md | P2 |
| water-crossing.md | P2 |

### Climate-Specific (5)

| Guide | Priority |
|-------|----------|
| arctic-survival.md | P2 |
| desert-survival.md | P2 |
| jungle-survival.md | P2 |
| mountain-survival.md | P2 |
| ocean-survival.md | P2 |

### Preparedness (3)

| Guide | Priority |
|-------|----------|
| bug-out-bag.md | P2 |
| everyday-carry.md | P2 |
| vehicle-kit.md | P2 |

### References (8)

| Item | Type |
|------|------|
| glossary.md | Reference |
| book-list.md | Reference |
| sources.md | Reference |
| checklists/ (5 files) | Checklist |

## Milestones

### Milestone 0 — Platform ✓

MkDocs Material configured, content in `docs/`, GitHub Actions deploying, CSS mobile-first, all admonitions converted.

**Remaining:** PWA icons, PWA offline plugin, mobile install testing (iOS + Android)

### Milestone 1 — Foundation (P0) ✓

14 life-critical guides: core medical, water, shelter, fire, psychology, rescue signaling.

### Milestone 2 — Critical Skills (P1) ✓

36 guides covering food, wildlife, tools, scenarios, extended medical/shelter/fire/water/navigation/psychology.

### Milestone 3 — Advanced & Situational (P2) ✓

34 guides: climate-specific survival, preparedness, extended food, extended wildlife, tools, advanced navigation, advanced psychology, extended scenarios.

### Milestone 4 — Polish (P3) ✓

- Cross-linking: 347 cross-links, every one carrying a description of the relationship
- Search tags: YAML frontmatter tags on all 60 guides, tags index page
- Review pass: no broken links, no blockquote warnings, all required sections present
- Wide tables fixed: 16 files narrowed to ≤4 columns
- Spell-check: clean with `.codespellrc` suppressing valid domain words
- Mobile UX: table overflow scroll, larger font on narrow screens, nav tap targets

### Milestone 5 — PWA Completion (in progress)

**The primary deliverable now works.** `./scripts/build-offline.sh` produces a
self-contained copy — 12 MB unpacked, 2.8 MB zipped — that runs from the
filesystem with no network, no server, and no install.

Getting there required fixing three things the original plan did not account for:

| Problem | Why it broke offline | Fix |
|---------|----------------------|-----|
| Roboto webfont | Fetched from `fonts.googleapis.com` on every page load | `theme.font: false` — system font stack |
| `iframe-worker` shim | The `offline` plugin pulls it from `unpkg.com`; Chrome cannot start a Web Worker from `file://`, so search depends on it | Vendored to `docs/assets/javascripts/` and declared in `extra.polyfills` |
| Search index | Loaded via `fetch()`, which `file://` blocks | The `offline` plugin inlines it; Material detects `file:` at runtime and loads `search_index.js` |

Verified: 0 external resource loads, 0 broken internal links across 91 pages,
and a 2,777-document search index that loads under `file://`. The build script
re-checks the first two on every run and fails if a network request reappears.

Also done: icon set (favicons, apple-touch-icon, 192/512 manifest icons plus a
maskable variant), `docs/manifest.webmanifest`, and the install metadata
Material does not emit on its own (`overrides/main.html`).

Corrected along the way: the homepage claimed content "is cached for offline
access." It was not. On a project that treats accuracy as life-safety, a false
offline promise is a defect, and it is now fixed.

**Remaining:**

- Test "Add to Home Screen" on real iOS Safari and Android Chrome hardware
- Decide distribution for the zip (release asset vs. committed) — deferred
- Optional: a service worker so the *hosted* site also survives losing signal

#### Note on the hosted site and "offline"

The `offline` plugin installs no service worker, so it does nothing for the
hosted site. Making *that* work without a connection is a separate problem
requiring a hand-written `sw.js`, which would be this project's first custom
application code and would break the "zero custom application code" property.

Because the offline copy already covers the no-signal case completely, this is
now optional convenience rather than a gap in the product — a materially
smaller decision than it was when the hosted PWA was the only plan.

## Quality Gates

Every guide passes these checks before merge:

1. Follows `templates/guide-template.md` structure
2. Has all required sections: At a Glance, Common Mistakes, Quick Reference, See Also, Sources
3. YAML frontmatter with `tags:` present
4. Has 3-8 cross-category See Also links with em-dash descriptions
5. Admonitions used (no raw blockquote warnings)
6. Tables ≤4 columns
7. Measurements in both metric and imperial
8. Safety warnings precede dangerous procedures
9. Passes `codespell` with `.codespellrc`
10. Passes `mkdocs build --strict`

## Security Principles

1. **Content accuracy** is a life-safety concern — treat inaccurate advice as a defect
2. **CI pipeline** runs with least-privilege permissions (OIDC, no stored secrets)
3. **Dependencies** are pinned and auto-updated by Dependabot
4. **No user data** — the site is static, no tracking, no cookies, no accounts
