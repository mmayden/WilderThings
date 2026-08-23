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

- [ ] Decide distribution — GitHub Release asset vs. committed to repo (deferred; CI uploads both artifacts on every run in the meantime)

### Single-file build — DONE

- [x] Adopt the same markdown extension set as `mkdocs.yml` — admonition bodies were HTML-escaped, so **bold, links and tables inside safety warnings rendered as literal markup**
- [x] Namespace generated ids per guide — 148 duplicate ids across the 91 concatenated documents, which merged every content-tab radio group and left all tabs unselected
- [x] Fix cross-guide fragment links emitting malformed `#guide#heading`
- [x] Add license + disclaimer footer to the distributed file
- [x] Stop committing the generated file — it had gone 4 months stale in the repo; CI builds it fresh instead

### Licensing — DONE

- [x] `LICENSE` — CC BY-SA 4.0 for guides, MIT for tooling, © WilderThings Contributors
- [x] Bundle licenses into the offline zip and the single file so recipients know their rights
- [x] Footer notice on the hosted site

### Content accuracy review — DONE (highest-risk guides)

Reviewed the 14 guides where an error is lethal (medical, mushroom/plant ID,
water, snakes, bears, food preservation) against current clinical and
wilderness-medicine standards, plus mechanical checks across all 89.

- [x] **Bleeding control** — removed elevation and pressure points from the ladder (dropped from ATLS/TCCC/Red Cross; they delay packing and tourniquet on a 3-5 minute bleed)
- [x] **Fermented fish** — was presented as safe; it is the leading cause of foodborne botulism in North America, and the guide's smell test cannot detect an odorless toxin
- [x] **Universal Edibility Test** — existed as two contradictory protocols; consolidated to one, with the plants that defeat it named explicitly
- [x] Pulse-to-BP correlation removed (discredited, dropped from ATLS)
- [x] Flail chest taping removed (restricts ventilation, contraindicated)
- [x] Third-degree burn cooling corrected (risk is burn size, not depth)
- [x] CPR no longer requires a pulse check before compressions
- [x] Smoking temperatures corrected; cold smoking tied to its required salt cure
- [x] Consistency: dry-bite rate, bear-hang dimensions, bleach dosing, pine bark calories
- [x] "Cold water closes pores" myth removed; garbled briquette warning restored
- [x] 4 medical disclaimers converted from blockquotes to admonitions so they render as warning boxes
- [x] Verified 689 dual measurements convert correctly across all 89 guides — no errors found

**Round 2 (all high-risk guides now read in full — 25 of 89):**

- [x] Man-of-war vs box jellyfish — vinegar is contraindicated for *Physalia*; two guides disagreed
- [x] Shellfish/insect cross-allergy (tropomyosin) — anaphylaxis risk was entirely unmentioned
- [x] Sandstone recommended for rock boiling despite being porous — it spalls in fire
- [x] Wind chill table understated cold by 5-9°F; added NWS frostbite times
- [x] Log buoyancy overstated 2-3x (physics checked)
- [x] Biphasic anaphylaxis timing conflated with the second-dose window
- [x] "Snow conducts heat 25x faster than air" — snow is an insulator; that figure is water's
- [x] Butane lighter failure temperature; mountain lion fatality rate stated three ways
- [x] Verified corpus-wide: 689 dual measurements and 91 °F/°C pairs all convert correctly

**Rounds 4-6 (36 of 89 guides now read in full):**

- [x] **Lightning crouch** — taught as protective; NWS withdrew it in 2008 and warns it delays people seeking real shelter
- [x] **Paralytic shellfish poisoning** — "cook before eating to avoid PSP" was false; saxitoxin survives boiling, frying, canning and freezing
- [x] **Post-disaster carbon monoxide** — generators/grills indoors kill after storms; absent from the disaster guide
- [x] Reference checklists had drifted from their parent guides (first-aid still had the removed elevation step)
- [x] Ground-to-air code corrected to the current ICAO five (V/X/N/Y/arrow); "I — need supplies" was wrong in every code
- [x] Signal fire spacing 25 ft vs 100 ft — at 25 ft three fires read as one from the air
- [x] Lyme attachment time corrected to CDC's 36-48 hours, with the caveat that RMSF transmits faster
- [x] Bleach re-dose wait harmonized (one guide said 15 min, three said 30)
- [x] Cold-water survival times at 70°F disagreed 3x between two guides
- [x] "Animals use clean water" removed — animals are the source of Giardia and Crypto
- [x] Moose run/zigzag advice reconciled; jungle rainwater exception vs "purify without exception"
- [x] Removed a freediving book cited as a source in the jungle guide

**Still open — not a substitute for expert review:**

- [ ] Independent review of medical guides by a licensed clinician
- [ ] Independent review of plant/mushroom ID by a regional botanist/mycologist
- [ ] Line-by-line pass on the remaining 53 guides (most fire technique, shelter construction, navigation, tools, psychology, preparedness, references) — these have had automated checks and targeted scans, but not a full read
- [ ] Verify cited sources actually say what guides attribute to them (only a handful spot-checked against the literature so far)

### Engineering standards — DONE

- [x] `scripts/verify.py` — test suite (no external requests, link integrity, id uniqueness, render correctness); negative-tested to confirm it actually catches regressions
- [x] CI `offline-check` job builds both offline artifacts, verifies them, and uploads them
- [x] Declare direct dependencies (`Markdown`, `PyYAML`, `pymdown-extensions`) instead of relying on transitive installs
- [x] `CODE_OF_CONDUCT.md`, content-accuracy issue template, PR template
- [x] Remove the "field-tested" claim — the content is well-sourced, which is a different claim

### "Critical" page — STARTED, decisions pinned

`docs/critical.md`. Started with one entry (phone satellite SOS) to see the
shape. Two decisions deliberately deferred until it can be looked at:

- [ ] **Entry bar.** Currently the strictest option: only facts where the belief most
      people hold makes the situation *worse*. The alternative was a broader
      ~30-item "critical must-knows" grouped by category. The strict bar keeps it
      readable in one sitting; the broad one is more complete but easier to skim past.
      Length is the thing that makes this page work, so whatever the bar is, it needs
      to be written down and enforced — otherwise every future review adds its
      favourite fact and it becomes a second index.

- [ ] **Placement.** Currently second in the nav, after Home. The stronger option is
      making it the landing page of the offline copy, so someone who opens the folder
      hits it before anything else. That best serves the problem it exists for and is
      the more disruptive choice for people who know what they want.

- [ ] **Candidates already found and not yet written up:** rabies treatment has no
      deadline; lean meat alone is worse than eating nothing; cooking does not defeat
      ciguatera; antihistamines do not stop anaphylaxis; bleach does not kill
      cryptosporidium; bat contact counts as rabies exposure with no visible bite; the
      NWS withdrew the lightning crouch; botulinum toxin is odourless; saxitoxin is
      heat-stable; solar retinopathy is painless while it happens; ground insulation
      matters more than the roof; do not eat snow.

- [ ] **Presentation.** First draft was far too text-heavy. The page has to be scannable,
      not read. Two ideas to carry forward: collapsible sections (`??? note "..."`) so a
      long page is not a wall of text — one is already in use here — and applying the
      same treatment to the guides themselves, which have the same problem in places.

- [ ] Consider a `verify.py` check that every claim on the page still exists in the
      guide it links to, so the page cannot drift from its sources — and a hard cap on
      the number of entries, since selectivity is the whole value and cannot be
      enforced by judgement alone across many sessions.

### Cross-linking polish — OPEN

- [ ] **124 See Also entries have no description.** `CLAUDE.md` requires an em-dash
      description after every cross-link explaining the relationship; roughly a third
      of them are a bare title. Concentrated in the reference checklists, glossary,
      navigation, and medical guides.

      Deliberately not mass-generated. Writing 124 in one pass produces filler
      ("— related information") that is worse than the gap, because it looks answered.
      Each needs someone who knows both guides to say why a reader would follow the
      link. Do it a category at a time, alongside reviewing that category's content.

      The two mechanical halves of this are already fixed and enforced by
      `scripts/verify.py`: no bare filenames as link text, and one name per guide.

- [ ] Five guides fall outside the 3-8 See Also range (`book-list` and `sources` have
      2; `injured-and-alone`, `lost-in-woods`, and `shelter-principles` have 9). Minor,
      and the two references guides may be legitimate exceptions.

### Dependency risk — WATCH

- [ ] **MkDocs 2.0 removes the plugin system with no migration path.** Material for
      MkDocs now prints this warning on every build. This project depends on the
      Material theme, the `offline` plugin, the `tags` plugin, and `minify` — the
      offline copy, the primary deliverable, is built entirely on that plugin stack.

      Nothing to do today: the pinned versions in `requirements.txt` keep building.
      But the single-file build (`build_single_file.py`) is worth noting as the
      hedge — it depends only on `Markdown` plus `pymdown-extensions`, not on MkDocs
      at all, so the most portable artifact survives whatever happens upstream.
      Re-evaluate before any Material major-version bump. See
      https://squidfunk.github.io/mkdocs-material/blog/2026/02/18/mkdocs-2.0/

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

---

## Source Currency

These bodies revise on cycles, so a citation to any of them is a citation to an
edition. Re-check each against its publisher annually and update the date below.
`scripts/verify.py --content docs` fails once a row passes 400 days.

<!-- source-currency -->

| Source | Last verified | Revises |
|---|---|---|
| TCCC / Joint Trauma System | 2026-08-23 | ~annually |
| Wilderness Medical Society practice guidelines | 2026-08-23 | ~5 yr per topic |
| AHA / ILCOR / Red Cross first aid | 2026-08-23 | ~5 yr + focused updates |
| ATLS (American College of Surgeons) | 2026-08-23 | by edition |
| PHTLS (NAEMT) | 2026-08-23 | by edition |
| ANZCOR guidelines | 2026-08-23 | rolling |
| CDC (tick-borne, waterborne, botulism) | 2026-08-23 | without announcement |
| NWS / NOAA (lightning, wind chill, rip currents) | 2026-08-23 | without announcement |

<!-- /source-currency -->

**What "verified" means here:** someone checked whether the body has published a
newer edition than the one cited, and if so ran check 2 (is it current?) against
the guides citing it. It does not mean every claim was re-read.


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
