# Task Backlog — WilderThings

Active work backlog organized by milestone. Completed work is collapsed at the bottom.

---

## Up Next — Milestone 5 (PWA Completion + Infrastructure)

### Documentation and Security

- [x] Add SECURITY.md (content accuracy policy + CI security)
- [x] Harden CI/CD: split build/deploy jobs, least-privilege permissions (OIDC)
- [x] Add lint.yml workflow (codespell + mkdocs build --strict on every push/PR)
- [x] Add dependabot.yml (weekly pip + Actions updates)
- [x] Pin requirements.txt to exact versions
- [x] Harden .gitignore (secrets, env files, credentials)
- [x] Update README, PROJECT_OUTLINE, CONTRIBUTING, STYLE_GUIDE, CLAUDE.md

### PWA Completion

- [ ] Generate PWA icons (favicon 16/32px, apple-touch-icon 180px, manifest icons 192/512px)
- [ ] Create `docs/manifest.webmanifest` with name, icons, display, theme_color
- [ ] Enable MkDocs Material offline plugin in `mkdocs.yml`
- [ ] Configure `extra.manifest` in `mkdocs.yml`
- [ ] Push to GitHub remote (`git remote add origin ...`)
- [ ] Set GitHub Pages Source to "GitHub Actions" (Settings → Pages)
- [ ] Verify GitHub Actions deploy.yml runs clean
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
