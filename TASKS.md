# Task Backlog — WilderThings

Active work backlog organized by milestone. Completed work is collapsed at the bottom.

---

> [!IMPORTANT]
> **The shareable offline copy is the primary deliverable.** A folder that opens
> from `index.html` with no internet, no server, and no install. The hosted
> GitHub Pages site is an online convenience mirror, not the product.

## Up Next — Milestone 5 (Delivery)

### Offline copy — DONE

- [x] Add `mkdocs.offline.yml` (Material `offline` plugin, `use_directory_urls=false`, inlined search index)
- [x] Disable the Google Fonts webfont (`theme.font: false`) — was the one real network dependency
- [x] Vendor the `iframe-worker` shim locally so the offline plugin does not pull it from unpkg.com
- [x] Add `scripts/build-offline.sh` — builds, **verifies zero external requests**, and zips
- [x] Ship a `START-HERE.txt` in the package for non-technical recipients
- [x] Verify: 0 external resource loads, 0 broken internal links across 91 pages, search index of 2,777 docs loads under `file://`

Result: 12 MB folder / 2.8 MB zip.

- [ ] Decide distribution — release asset vs. committed to repo (deliberately deferred)

### Hosted site (secondary)

### Documentation and Security

- [x] Add SECURITY.md (content accuracy policy + CI security)
- [x] Harden CI/CD: split build/deploy jobs, least-privilege permissions (OIDC)
- [x] Add lint.yml workflow (codespell + mkdocs build --strict on every push/PR)
- [x] Add dependabot.yml (weekly pip + Actions updates)
- [x] Pin requirements.txt to exact versions
- [x] Harden .gitignore (secrets, env files, credentials)
- [x] Update README, PROJECT_OUTLINE, CONTRIBUTING, STYLE_GUIDE, CLAUDE.md

### PWA Completion

- [x] Generate PWA icons (favicon 16/32/.ico, apple-touch-icon 180px, manifest icons 192/512 + 512 maskable)
- [x] Create `docs/manifest.webmanifest` with name, icons, display, theme_color
- [x] Emit `<link rel="manifest">` + apple-touch/`apple-mobile-web-app-*` tags via `overrides/main.html`
- [x] Set `site_url` (enables canonical URLs)
- [x] Correct the homepage, which claimed content "is cached for offline access" — it was not, and on a life-safety project a false offline promise is a defect
- [ ] Test "Add to Home Screen" on iOS Safari (needs real hardware)
- [ ] Test "Add to Home Screen" on Android Chrome (needs real hardware)
- [ ] Decide: does the *hosted* site also need to work offline? Needs a service worker

> [!NOTE]
> **Two different things both called "offline".**
>
> The Material `offline` plugin (now used, and working) produces a `file://`
> copy. It installs **no service worker** and cannot make the hosted site work
> without a connection — that is a separate problem needing a hand-written
> `sw.js` precaching pages plus the lunr index, registered from
> `overrides/main.html`. It would be the project's first custom application code.
>
> Since the offline copy now fully covers the no-signal use case, this is
> optional convenience rather than a gap in the product.
- [x] Push to GitHub remote (live at https://mmayden.github.io/WilderThings/)
- [x] Set GitHub Pages Source to "GitHub Actions" (Settings → Pages)
- [x] Verify GitHub Actions deploy.yml runs clean
- [ ] Test "Add to Home Screen" on iOS Safari
- [ ] Test "Add to Home Screen" on Android Chrome

---

## Completed

<details>
<summary>Milestone 0 — Platform Setup (click to expand)</summary>

- [x] Create `requirements.txt`
- [x] Create `mkdocs.yml` with full configuration (theme, nav, plugins, extensions)
- [x] Create `docs/index.md` (site homepage)
- [x] Create `docs/assets/css/custom.css`
- [x] Create `.github/workflows/deploy.yml` (GitHub Actions CI/CD)
- [x] Move all guide folders into `docs/`
- [x] Verify all internal links (294 checked, 0 broken)
- [x] Convert blockquote warnings to MkDocs admonitions (131 across 37 files)
- [x] Test local build with `mkdocs serve`

</details>

<details>
<summary>Milestone 1 — Foundation / P0 (14 guides)</summary>

- [x] `medical/first-aid-basics.md`
- [x] `medical/cpr-and-choking.md`
- [x] `medical/fractures-and-splints.md`
- [x] `medical/hypothermia-and-heatstroke.md`
- [x] `medical/trauma-and-triage.md`
- [x] `water/finding-water.md`
- [x] `water/purification.md`
- [x] `shelter/shelter-principles.md`
- [x] `shelter/debris-hut.md`
- [x] `fire/fire-principles.md`
- [x] `fire/friction-methods.md`
- [x] `fire/spark-methods.md`
- [x] `psychology/survival-mindset.md`
- [x] `navigation/signaling-for-rescue.md`

</details>

<details>
<summary>Milestone 2 — Critical Skills / P1 (36 guides)</summary>

- [x] `food/foraging-basics.md`
- [x] `food/edible-plants-temperate.md`
- [x] `food/mushroom-identification.md`
- [x] `food/hunting-basics.md`
- [x] `food/trapping-and-snares.md`
- [x] `food/fishing-improvised.md`
- [x] `wildlife/bear-safety.md`
- [x] `wildlife/big-cats.md`
- [x] `wildlife/venomous-snakes.md`
- [x] `wildlife/venomous-spiders.md`
- [x] `wildlife/insect-threats.md`
- [x] `tools-and-craft/knife-use-and-care.md`
- [x] `tools-and-craft/knots-and-lashing.md`
- [x] `tools-and-craft/cordage.md`
- [x] `scenarios/lost-in-woods.md`
- [x] `scenarios/animal-attack.md`
- [x] `scenarios/injured-and-alone.md`
- [x] `references/glossary.md`
- [x] `references/book-list.md`
- [x] `references/sources.md`
- [x] `references/checklists/first-aid-checklist.md`
- [x] `references/checklists/fire-starting-checklist.md`
- [x] `references/checklists/signal-checklist.md`
- [x] `references/checklists/water-purification-checklist.md`
- [x] `references/checklists/shelter-checklist.md`
- [x] `medical/bites-and-stings.md`
- [x] `medical/wound-infection.md`
- [x] `medical/dehydration-and-waterborne.md`
- [x] `medical/plant-poisoning.md`
- [x] `water/improvised-filters.md`
- [x] `water/water-storage.md`
- [x] `shelter/snow-shelters.md`
- [x] `shelter/desert-shelter.md`
- [x] `shelter/tarp-and-poncho.md`
- [x] `fire/fire-from-nothing.md`
- [x] `fire/fire-in-wet-conditions.md`
- [x] `fire/fire-types.md`
- [x] `fire/maintaining-fire.md`
- [x] `navigation/map-and-compass.md`
- [x] `navigation/natural-navigation.md`
- [x] `psychology/stress-management.md`

</details>

<details>
<summary>Milestone 3 — P2 Advanced (34 guides)</summary>

- [x] `medical/improvised-medicine.md`
- [x] `water/desert-and-sea-water.md`
- [x] `shelter/long-term-structures.md`
- [x] `food/edible-plants-tropical.md`
- [x] `food/insect-foraging.md`
- [x] `food/field-butchering.md`
- [x] `food/food-preservation.md`
- [x] `food/cooking-without-gear.md`
- [x] `navigation/gps-and-electronics.md`
- [x] `navigation/terrain-association.md`
- [x] `wildlife/wolves-and-canids.md`
- [x] `wildlife/marine-dangers.md`
- [x] `wildlife/moose-and-ungulates.md`
- [x] `wildlife/alligators-and-crocs.md`
- [x] `climate-specific/arctic-survival.md`
- [x] `climate-specific/desert-survival.md`
- [x] `climate-specific/jungle-survival.md`
- [x] `climate-specific/mountain-survival.md`
- [x] `climate-specific/ocean-survival.md`
- [x] `climate-specific/urban-survival.md`
- [x] `preparedness/bug-out-bag.md`
- [x] `preparedness/everyday-carry.md`
- [x] `preparedness/vehicle-kit.md`
- [x] `preparedness/home-preparedness.md`
- [x] `preparedness/communication-plans.md`
- [x] `preparedness/financial-preparedness.md`
- [x] `tools-and-craft/improvised-tools.md`
- [x] `tools-and-craft/containers-and-vessels.md`
- [x] `tools-and-craft/clothing-and-insulation.md`
- [x] `psychology/group-dynamics.md`
- [x] `psychology/solo-survival.md`
- [x] `scenarios/vehicle-breakdown-remote.md`
- [x] `scenarios/natural-disaster.md`
- [x] `scenarios/water-crossing.md`

</details>
