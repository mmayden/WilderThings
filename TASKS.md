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
- [ ] Line-by-line pass on the **12 guides never given a full read**. Everything
      hazard-bearing has now been read; what remains is the lower-consequence tail:

      | Guide | Why it was deprioritised |
      |---|---|
      | `references/glossary.md` | Definitions, no procedures |
      | `references/book-list.md` | Bibliography — but see the citation finding below |
      | `references/sources.md` | Same |
      | `psychology/group-dynamics.md` | No physical procedure to get wrong |
      | `psychology/solo-survival.md` | Same |
      | `navigation/map-and-compass.md` | Errors cost time, not life, and are self-correcting |
      | `navigation/natural-navigation.md` | Same |
      | `navigation/terrain-association.md` | Same |
      | `preparedness/financial-preparedness.md` | Financial loss, not injury |
      | `tools-and-craft/containers-and-vessels.md` | Scanned; food-contact and heating are the risks |
      | `food/cooking-without-gear.md` | Reviewed in the earlier audit; not re-read |
      | `food/insect-foraging.md` | Reviewed in the earlier audit; not re-read |

      Two of these deserve a second look despite the ranking. `book-list.md` and
      `sources.md` are pure bibliography, and three fabricated citations have now been
      found elsewhere — they are the most likely place for more.
- [ ] Verify cited sources actually say what guides attribute to them. See the citation-verification section below — three fabricated citations found so far, and the checker cannot detect this class.

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

- [x] **Built out to 16 entries** (2026-08-24), grouped into five sections: getting
      found, medical, water and food, shelter and weather, vehicles. Every entry is a
      bold one-liner plus one or two sentences and a link, with the one long explanation
      collapsed. Roughly 1,100 words including chrome.

- [ ] **Entries considered and left out**, so the reasoning is visible: botulinum toxin
      being odourless, saxitoxin being heat-stable, solar retinopathy being painless, and
      "do not eat snow." All true and all in the guides. They lost to the page's own bar —
      each is a fact you would meet *while already reading about that hazard*, rather than
      something you would never think to look for. The page works by being short.

- [ ] **Presentation.** First draft was far too text-heavy. The page has to be scannable,
      not read. Two ideas to carry forward: collapsible sections (`??? note "..."`) so a
      long page is not a wall of text — one is already in use here — and applying the
      same treatment to the guides themselves, which have the same problem in places.

- [ ] Consider a `verify.py` check that every claim on the page still exists in the
      guide it links to, so the page cannot drift from its sources — and a hard cap on
      the number of entries, since selectivity is the whole value and cannot be
      enforced by judgement alone across many sessions.

### Citation verification — OPEN, and now known to be needed

**Eight wrong citations found so far**, across eight different guides. Five of the
works do not appear to exist at all:

| Cited as | Actually | Where |
|---|---|---|
| Hume, Ed. *Primitive Fire: Mastering the Bow Drill*, 2016 | No such book. Daniel Hume, *Fire Making*, 2017 | friction-methods |
| Hennessy, Tom. *Hammock Camping*, 2008 | Ed Speer, Speer Hammocks, 2003 | tarp-and-poncho |
| Gregory, Joy. *Water in the Wilderness*, WMS, 2019 | No such work. Backer, Derlet & Hill (2019, rev. 2024) | finding-water |
| Herring, William. *The Book of Fire* | No such book | book-list |
| Johnson, Mark. *The Complete Guide to Water Filtration in the Backcountry*, WMS, 2021 | No such book | purification |
| Eiben, Patrick. *The Complete Guide to Everyday Carry*, 2021 | No evidence it exists | everyday-carry |
| Hurd, Richard. *Primitive Fire Lighting Methods*, SPT Bulletin, 1998 | No evidence it exists | fire-from-nothing |
| Knight, Michael Finkel. *The Stranger in the Woods* | Author is Michael Finkel; Christopher Knight is the subject | solo-survival |

Plus two factual errors about Army publications: FM 21-76's successor is ATP 3-50.21
(via FM 3-05.70), not ATP 3-50.3, and ATP 3-50.21 is titled *Survival*, not *Survival,
Evasion, and Recovery*.

Every one was found by opening the source, not by scanning the bibliography. Every one
looked entirely plausible — right subject, plausible author, plausible publisher,
plausible year. Three shared a tell worth knowing: a generic title of the form "The
Complete Guide to X" attached to a common surname.

The five nonexistent works were removed rather than replaced. Each guide already had
real sources, and inventing a substitute only creates something else to verify.

- [ ] **A systematic pass over all 504 citations is warranted.** Roughly 141 distinct
      book-form works are cited. Eight errors have been found in the subset checked so
      far, which is a high enough rate that the remainder should be assumed unverified
      rather than assumed correct.

#### Verification ledger

So the next pass does not redo this work. Three states, kept separate on purpose.

**Corrected dates and attributions** (the work is real; the citation was not):

| Cited as | Corrected to |
|---|---|
| WMS *Practice Guidelines for Wilderness Emergency Care*, 5th ed., **2014** | Forgey, ed., Falcon Guides, **2006** — and superseded in practice by the per-topic WMS guidelines |
| FM 31-70, **2011** | **1968** |
| SAS Survival Handbook, William **Morrow** (in sources.md) | William **Collins**, matching the other 32 citations |
| Halcon, Linda and **Milisa, Kelly** — tea tree oil review | Halcón, Linda, and Kelly **Milkus** |
| Langley, "**Alligator Attacks in the United States: 1928-2009**" | "**Adverse Encounters With Alligators in the United States: An Update**" — journal, volume, year and pages were all correct |

The Langley entry is the most instructive error found so far. Volume 21, issue 2, 2010,
pages 156-163 are exactly right; only the title is invented, and it reads like a
plausible summary of what the paper contains. Nothing about it looks wrong, and a reader
following the page numbers lands on the real article. Only someone checking the title
against the journal would notice.

**Confirmed real** (checked against the literature or the publisher this session):
Daniel Hume *Fire Making* · Ed Speer *Hammock Camping* · Backer, Derlet & Hill (WMS
water, 2019 rev. 2024) · Kochanski *Bushcraft* (1987, Lone Pine) · ATP 3-50.21
*Survival* (2018) · Bilsborough & Mann 2006 · Vetter *The Brown Recluse Spider* ·
Isbister & Fan *Lancet* 2011 · Dart et al. *Toxins* 2017 · HSE RR708 · ANZCOR 9.1.5 ·
Fredston & Fesler *Snow Sense* · Ashley *Book of Knots* · Koester *Lost Person Behavior*.

**Confirmed wrong** — the eight in the table above, now fixed.

**Could not verify — left in place, flagged.** Searched without result, but each is
plausibly a niche agency or small-press item that is simply not indexed. Removing a real
citation is as much a defect as keeping a fabricated one, so these stay until someone can
check a catalogue rather than a search engine:

| Citation | Guide |
|---|---|
| Crellin, Dawn and Dennis. *Twist It: Making Cordage from Natural Fibers.* Backcountry Publishing | cordage |
| Stoffel, Robert C. *Emergency Signaling.* US National Park Service | signaling-for-rescue |
| NASA Technical Report, *Solar Distillation for Survival Water* (1965) | desert-and-sea-water |
| U.S. Navy SERE Manual, *Water Procurement at Sea* | desert-and-sea-water |
| Hellweg, Paul. *Flintknapping: The Art of Making Stone Tools.* Canyon Publishing, 1984 | improvised-tools (now archived) |
| NASA Technical Report, *Solar Distillation for Survival Water* (1965) | desert-and-sea-water |
| U.S. Navy SERE Manual, *Water Procurement at Sea* | desert-and-sea-water |

**Removed** after searching without result, where the claim did not need the citation:
Baer, "Ferrocerium: History and Metallurgy," *Journal of Chemical Education* 72 (1995).
No such article appears in that journal, and the ferrocerium history is well documented
elsewhere — the citation was doing no work that a patent reference cannot do.

Three military publications resolved rather than flagged, since the numbering systems
are documented and checkable:

| Cited as | Corrected to | Why |
|---|---|---|
| FM 31-70, 2011 | FM 31-70, **1968** | No 2011 edition; 1968 supersedes a 1959 printing |
| *USAF Survival Training* (AFPAM 36-2211), 2008 | **AFR 64-4** *Survival Training*, 1985 | The 36-22xx series is education and training, not survival. AFR 64-4 is the documented USAF survival manual, and the corpus already cites the current SERE publication (AFH 10-644) correctly |
| *U.S. Navy Survival Manual* (NAVPERS 16083) | **Craighead & Craighead**, *How to Survive on Land and Sea*, Naval Institute Press | NAVPERS is the Naval Personnel series. The Navy's actual survival reference is the Craighead volume, prepared for the US Naval Institute Education Series |

WorldCat, the Library of Congress catalogue, and the agencies' own publication indexes
are the right tools for these — not a web search.

- [ ] The master source list is **not covered by the citation check** at all.
      `scripts/verify.py` scans `## Sources` sections, and `references/sources.md` keeps
      its bibliography under `## Key Textbooks`. That is how it came to cite the SAS
      Handbook to a different publisher than the other 32 citations of the same book.

**`scripts/verify.py` cannot do this and never will.** The citation check compares the
corpus against itself — it catches one work cited two ways, and a fabricated citation
stated consistently passes clean. Every one of the three above would have passed. This
is a limitation to state plainly rather than design around: internal consistency is not
accuracy, and the check reports the former.

CLAUDE.md already says citations have not been verified against the originals. That was
written as a caveat; it is now a measured finding.

### Cross-linking polish — OPEN

- [x] **All See Also entries now carry a description** (2026-08-24). There were 124;
      41 were fixed incidentally while reviewing their guides, and the remaining 83 were
      written once the whole corpus had been read.

      That order mattered. The reason not to mass-generate them at the start was that a
      description is a claim about what a reader will find, and writing 124 without having
      read the targets produces filler that looks answered. Written afterwards, each one
      says something specific — "why pressure immobilisation depends on the species",
      "the slow killer once the immediate danger has passed".

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

The table records **which edition the corpus cites**, not merely when someone last
glanced at it. The previous version tracked only a date, which is how eight guides came
to cite TCCC 2023 and five to cite the 2021 Red Cross manual while the table read
"verified" — the tracker was measuring my attention, not the corpus.

| Source | Edition cited | Confirmed current | Revises |
|---|---|---|---|
| TCCC / Joint Trauma System | 1 May 2026 | 2026-08-24 | frequently; check jts.health.mil |
| AHA / Red Cross CPR & ECC | 2025 Guidelines | 2026-08-24 | ~5 yr (2015, 2020, 2025) |
| American Red Cross manual | Revision 2025 (r.25) | 2026-08-24 | with the guideline cycle |
| European Resuscitation Council | Guidelines 2025 | 2026-08-24 | ~5 yr, with ILCOR |
| ILCOR CoSTR | 2025 | 2026-08-24 | annual reviews, 5-yr consensus |
| WMS — water treatment | 2024 update | 2026-08-24 | ~5 yr per topic |
| WMS — frostbite | 2024 update | 2026-08-24 | ~5 yr per topic |
| WMS — heat illness | 2024 update | 2026-08-24 | ~5 yr per topic |
| WMS — spinal cord protection | 2024 update | 2026-08-24 | ~5 yr per topic |
| WMS — tick-borne illness | 2021 update | 2026-08-24 | ~5 yr per topic |
| WMS — accidental hypothermia | 2019 update | 2026-08-24 (still current) | ~5 yr per topic |
| Auerbach *Wilderness Medicine* | 7th ed., 2017 | 2026-08-24 (8th due 2028) | by edition |
| Tintinalli's | 9th ed., 2020 | 2026-08-24 | by edition |
| WMS — acute altitude illness | 2024 update | 2026-08-24 | ~5 yr per topic |
| WMS — pit viper envenomation | 2026 update | 2026-08-24 | ~5 yr per topic |
| Surviving Sepsis Campaign | 2026 | 2026-08-24 | ~3-5 yr |
| ATLS | 11th ed., 2025 | 2026-08-24 | by edition |
| PHTLS | 10th ed. | 2026-08-24 (still current) | by edition |
| Sanford Guide | 2026 ed. | 2026-08-24 | annual |
| ANZCOR | rolling | 2026-08-23 | rolling |
| CDC / EPA / NOAA / NWS | web resources | 2026-08-23 | without announcement |

**Every medical source in the corpus is now on its current edition** (checked
2026-08-24). Three clinical corrections came out of the pass, all found by asking what
version a source was on rather than whether it existed:

| Found | Because |
|---|---|
| Tourniquet reassessment at 2 hours was missing | TCCC 2023 → 1 May 2026 |
| Improvised backboards taught as good practice | WMS spine 2019 → 2024 |
| MARCH and ABCDE framed as competing orders | ATLS 10th → 11th (xABCDE) |

- [ ] Re-run this pass periodically. The tracker records the edition cited, so drift is
      visible — but nothing checks it automatically, and TCCC alone revises several times
      a year. A source cited to a fixed year will eventually be wrong again.

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
