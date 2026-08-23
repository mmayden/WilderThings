# Contributing to WilderThings

## Content Safety — Read First

**This project contains medical, foraging, and emergency survival information. Inaccurate content can kill people.**

Before contributing:

1. Every factual claim must be traceable to a credible source (military field manuals, peer-reviewed medical literature, established wilderness training organizations).
2. If you are not certain something is accurate, do not include it. "I think this is right" is not a sufficient standard.
3. Safety warnings must come before procedures, not after.
4. Plant and mushroom identification must name dangerous look-alikes and state applicable regions.
5. Medical content must include a disclaimer that it does not replace professional training.
6. Regulated activities (hunting, trapping, firearms) must note that laws vary by jurisdiction.

To report inaccurate or dangerous content already in the project: open an issue tagged `content-safety`. See [SECURITY.md](SECURITY.md).

---

## Guide Standards

Every guide must meet these standards before being considered complete.

### Content Requirements

1. **Accuracy first.** Source from established survival literature, military field manuals, medical references, or verified expert knowledge. Cite your source.

2. **Actionable under stress.** Assume the reader is panicking, injured, or exhausted. Lead with the most critical action. Use numbered steps for procedures. Keep sentences short.

3. **No filler.** Every sentence must earn its place. Remove preamble, motivational padding, and obvious statements.

4. **Regional awareness.** When content varies by region (plants, animals, climate), state the applicable region explicitly.

5. **Safety warnings first.** If a technique has risks, lead with the warning before the instructions.

6. **Mobile-first.** Keep tables to 3-4 columns max. Avoid wide content that forces horizontal scrolling.

### Review Criteria

Before a guide is merged or marked complete, verify all of the following:

- [ ] Follows the guide template structure
- [ ] YAML frontmatter with `tags:` present
- [ ] "At a Glance" section is present and useful (3-5 bullets)
- [ ] "Common Mistakes" section is present
- [ ] "Quick Reference" section is present
- [ ] "See Also" has 3-8 cross-category links with em-dash descriptions
- [ ] Reciprocal links added in related guides
- [ ] No unsourced medical claims
- [ ] Safety warnings precede dangerous procedures
- [ ] Admonitions used (no raw `> **WARNING:**` blockquotes)
- [ ] Regional applicability stated where relevant
- [ ] Measurements include both metric and imperial
- [ ] Tables ≤4 columns
- [ ] No broken internal links
- [ ] Nav entry added in `mkdocs.yml`
- [ ] Passes `codespell docs/ --config .codespellrc --quiet-level=2`
- [ ] Passes `mkdocs build --strict`

The checklist above is **structural**. It tells you the guide is well-formed. It
does not tell you the guide is right. For that, see
[Reviewing Content for Accuracy](#reviewing-content-for-accuracy) below.

---

## Reviewing Content for Accuracy

Structural review catches malformed guides. Accuracy review catches guides that
are well-formed and wrong. This section is the second kind.

It is deliberately short at the point of use. **The operational part is one
triage question and four checks.** Everything after that is rationale you read
once, not a procedure you run every time.

---

### Stage 0 — Triage: does this claim need review at all?

Do not run the checks on everything. Reviewing "how to tie a bowline" with the
same rigor as an epinephrine dose wastes the attention that the dose needed.

Ask one question:

> **If a reader acts on this and it is wrong, what happens?**

| Answer | Treatment |
|---|---|
| They could die or be seriously injured | Full review — all four checks, verify against a source |
| They lose time, comfort, or resources | Check it is true and consistent. Move on |
| Nothing much | Normal editing. No review needed |

Most sentences are in the bottom row. Spend the effort where the first row is.

**Always escalate to full review**, regardless of topic: doses, times,
temperatures, thresholds, ratios, distances, and any sentence containing
"never" or "always."

---

### Stage 1 — The four checks

Run these only on claims Stage 0 escalated.

#### 1. Is it true — including the *why*?

Does the claim survive contact with a source? **Recompute anything computable.**

> A tarp's rain yield was understated 30x. Pine bark was listed above the
> calorie ceiling for a carbohydrate. A wind chill table was 9°F off. All three
> were arithmetic, and all three were found by doing the arithmetic.

The mechanism counts too. "Cold water closes your pores" was attached to correct
advice, but pores do not do that, and a reader who believes the model will apply
it wrongly somewhere else.

#### 2. Is it current?

Survival writing has a long tail. Techniques persist in print for decades after
the field drops them. **Check the current guideline, not what the technique has
always been.**

> Elevation and pressure points for bleeding; the 80/70/60 pulse rule; taping a
> flail chest; the lightning crouch. All were standard teaching. All are now
> withdrawn.

#### 3. Does it create false confidence?

The subtlest check and the most valuable. Two shapes, same failure — the reader
believes they are covered when they are not:

**(a) It displaces the thing that works.** Some advice is not false; it simply
consumes the window the effective action needed.

> The National Weather Service withdrew the lightning crouch in 2008. Their
> stated reason is the check itself: promoting it "gives people the false
> impression that crouching will provide safety... could cause people to become
> apathetic and not seek a safe shelter."

This is the same logic emergency medicine applies as **delay to definitive
care** — an intervention is judged not only on whether it helps but on what it
costs in time to real treatment.

Ask: **if this does not work, what does the reader lose by having tried it?**
Where the answer is "the minutes in which the real option was available," say so.
Never list a weak measure and a strong one as peers.

**(b) The safety check cannot detect the hazard.** A test that cannot find the
thing it tests for is worse than no test, because it manufactures certainty.

> "Discard the fermented fish if it smells foul." Botulinum toxin is odorless,
> and correctly fermented fish smells powerful. The test cannot separate safe
> from lethal.

When you write a check, state what it **cannot** catch.

#### 4. What is missing?

Absence is invisible. You have to go looking.

> The insect foraging guide never mentioned shellfish cross-allergy — and cited
> the arthropod relationship as encouragement. The disaster guide never
> mentioned carbon monoxide, which kills people after the storm.

Ask: **who reads this guide, and what will hurt them that is not on this page?**

---

### Stage 2 — Mechanical sweeps: script it, do not think about it

Consistency is not a judgment call, so it should not consume judgment. Anything
mechanical belongs in `scripts/verify.py` or a grep, run in CI.

| Sweep | Why it is mechanical |
|---|---|
| Unit conversions | Arithmetic. 689 pairs verified this way |
| Duplicated procedures and numbers | `grep` finds them; reading does not |
| Cross-guide contradictions | Extract each recurring claim, compare |
| Signal word severity | Rule-based (see below) |
| Broken links, missing sections | Already automated |

**Any procedure appearing in two places is a defect waiting to happen.**
Cross-link to one canonical copy. When you change a number, grep for it
everywhere — including the reference checklists, which are what people follow
under stress and which drifted from their parent guides during this audit.

---

### Stage 3 — Say how sure you are

The Wilderness Medical Society grades every recommendation on evidence quality
and notes plainly where trials do not exist and expert consensus is carrying the
weight. This project cites WMS constantly; it should adopt the same honesty.

Where a claim is not solidly established, mark it in the text:

| Tier | Means | Phrasing |
|---|---|---|
| **Established** | A current published guideline says this | State it plainly |
| **Consensus** | No trials, but expert bodies agree | "Standard practice is…" |
| **Field practice** | Traditional or anecdotal; unverified | "Traditionally… but this has not been well studied" |

Do not launder tier 3 into tier 1 by writing it confidently. A reader deciding
whether to risk something deserves to know which one they are holding.

---

### Scope of practice: separate "recognize" from "perform"

Some procedures in this collection are outside what an untrained person should
attempt. Teaching them is still correct — a reader needs to recognize a tension
pneumothorax to make an evacuation decision — but teaching them *without saying
who may perform them* is not.

NOLS and the Wilderness Medical Society publish Scope of Practice documents for
Wilderness First Aid and Wilderness First Responder. Needle decompression,
invasive airway adjuncts, and releasing a tourniquet in the field are explicitly
**excluded** from WFA scope.

Mark every procedure at one of three levels:

| Level | Meaning | Examples |
|---|---|---|
| **Anyone** | No training gate. Do it | Direct pressure, wound packing, applying a tourniquet, CPR, epinephrine auto-injector, splinting, hypothermia wrap |
| **Trained** | Requires hands-on certification and practice | Suturing, shoulder reduction, improvised traction splint |
| **Beyond wilderness first aid** | Provider-level. Here so you can **recognize** it, not perform it | Needle decompression, NPA/OPA insertion, abscess incision and drainage, rectal rehydration |

For anything in the third row, use this block verbatim so readers learn the
pattern and can spot it at a glance:

```markdown
!!! danger "Beyond wilderness first aid scope"
    This procedure is outside Wilderness First Aid scope and requires provider-level
    training. It is described here so you can **recognize the problem, understand
    what a provider will do, and make the evacuation decision** — not so you can
    perform it.

    Attempting it untrained is more likely to kill the patient than the condition is.
    [what specifically goes wrong]
```

**Why the wording matters.** "Only if you are confident" is the wrong gate: it
asks about *certainty*, not *competence*, and panic manufactures certainty.
Someone watching a friend struggle to breathe can be entirely certain and
entirely unqualified. Gate on training, and name the specific harm.

**Check the gating is not inverted.** Before this standard existed, suturing
(worst case: an infected wound) was gated with "use only if trained" while
needle decompression (worst case: you puncture the heart) said only "be
confident in the diagnosis."

---

### Keeping sources current

"Is it current?" is a check you run when you happen to be looking at a page.
This is what makes someone look. Without it, withdrawn guidance sits in the text
for years — this audit found four such techniques, one withdrawn in 2008.

**These bodies revise on cycles.** A citation to any of them is a citation to an
edition, and editions expire:

| Source | Revises |
|---|---|
| TCCC / Joint Trauma System | Roughly annually |
| AHA / ILCOR / Red Cross first aid | ~5 years, with focused updates between |
| Wilderness Medical Society practice guidelines | ~5 years per topic |
| ATLS, PHTLS | By edition |
| CDC, NWS, ANSI | Without announcement |

**Cadence.** Re-check the list above once a year and record the date in
TASKS.md. This is a check of roughly eight sources, not a re-read of 89 guides.
When a source has been revised, run check 2 (is it current?) against the guides
that cite it.

**Automated backstop.** `scripts/verify.py --content docs` flags any life-safety
guide whose newest cited source is older than the staleness threshold. It caught
that the altitude guide's newest clinical source was a 2001 paper while WMS had
published altitude guidelines in 2019 and again in 2024.

---

### Signal words: use ANSI Z535 severity

The project's admonitions are safety labels, and there is a standard for those.
Severity must be **earned**, not decorative:

| Use | When | Standard meaning |
|---|---|---|
| `!!! danger "DANGER"` | Acting wrongly here **will** kill or seriously injure | Imminent hazard |
| `!!! danger "WARNING"` | It **could** kill or seriously injure | Potential hazard |
| `!!! warning "CAUTION"` | Could cause moderate or minor injury, or make the situation worse | Lesser hazard |
| `!!! note` | Important but not a hazard | Notice |

A good safety message has four parts: **the hazard, the consequence, how to
avoid it, and the severity** (carried by the signal word). Most of this
project's warnings already do this — keep it.

**Warnings compete with each other for attention.** If every block is red, the
reader stops distinguishing them and the genuinely lethal ones lose their force.
Reserve DANGER for the small number of things that actually belong there:
amatoxins, botulism, water hemlock, paralytic shellfish poisoning, carbon
monoxide, drinking seawater, cassava cyanide, and the marine neurotoxins
(box jellyfish, cone snail, blue-ringed octopus).

`scripts/verify.py --content docs` fails if DANGER exceeds 15% of labelled
admonitions. It currently sits at 8% across 26 blocks. That ceiling is not a
target to fill — it is a tripwire against inflation.

---

### Stopping rules — how not to spiral

The review process has its own failure modes. These are the guards:

- **Sources disagree?** Do not adjudicate. Say so in the guide, give the safer
  option, cite both, and move on. One paragraph, not an afternoon.
- **Cannot verify a claim?** Downgrade it to its real tier (above) rather than
  deleting it or defending it.
- **Time-box each claim.** Checklist research finds attention degrades past
  roughly 60–90 seconds at a single checkpoint, after which people start
  skipping steps. If a claim is taking longer, it is a tier-3 claim — mark it
  and move on.
- **Do not re-review settled content** without a reason: a new source, a
  contradiction, or a report.
- **State scope when you claim something is reviewed.** "Reviewed" without scope
  is not a claim. Record what you checked *and what you did not* — see TASKS.md.

### Failure modes of this process

Watch for these in yourself:

| Failure | Looks like | Guard |
|---|---|---|
| Lens shopping | Arguing which check something falls under | The checks overlap by design; fix the defect, do not classify it |
| Warning inflation | Adding DANGER to be safe | Severity is earned. Inflation destroys the signal |
| Analysis paralysis | Re-litigating a thin claim | Stage 3 tiers exist so you can ship uncertainty honestly |
| Review theater | "Fully reviewed" with no scope | Record coverage and gaps |
| False precision | Inventing a number to replace a vague one | "Roughly" is better than a fabricated figure |

---

### Applying it

- **New guide:** Stage 0 on every claim, four checks on what escalates, all sweeps.
- **Content change:** four checks on the changed claim, plus the consistency grep.
- **Periodic audit:** work **by check, across the whole collection**, not guide by
  guide. Sweeping one check at a time is how the unit-conversion and duplicated-
  procedure problems surfaced; reading guide by guide would have missed both.
- **Prefer checking to recalling.** Every source check performed during the
  August 2026 audit changed something — including one that corrected an earlier
  correction.

---

## File Naming

- Lowercase kebab-case: `first-aid-basics.md`
- Descriptive and scannable — the filename should hint at content
- All guide content lives in `docs/` (MkDocs serves this as the site root)
- Checklists go in `docs/references/checklists/` with a `-checklist` suffix

## Guide Format

Every guide must follow `templates/guide-template.md`:

```markdown
---
tags:
  - category-tag
  - topic-tag
---
# Guide Title

> One-line summary of what this guide covers and when to use it.

## At a Glance
<!-- 3-5 critical bullet points -->

## [Main Content Sections]
<!-- H2 for major sections, H3 for subsections -->

## Common Mistakes
<!-- What people get wrong — this section saves lives -->

## Quick Reference
<!-- Condensed steps, measurements, or key facts. Tables ≤4 columns. -->

## See Also
<!-- 3-8 cross-category links with em-dash descriptions -->

## Sources
<!-- Citations -->
```

## Checklist Format

Quick-reference checklists follow `templates/checklist-template.md`:

```markdown
---
tags:
  - reference
  - checklist
  - topic
---
# Checklist Title

> When to use this checklist.

- [ ] Step or item
- [ ] Step or item
```

## Writing Style

- **Voice:** Direct, imperative. "Do this" not "You should consider doing this."
- **Tense:** Present tense for instructions. Past tense only for examples.
- **Person:** Second person ("you") for instructions. No first person.
- **Jargon:** Define technical terms on first use, or link to the glossary.
- **Measurements:** Both metric and imperial: `2 inches (5 cm)`.
- **Lists:** Numbered for sequential steps, bullets for non-ordered items.

## MkDocs-Specific Formatting

### Admonitions

```markdown
!!! danger "WARNING"
    Never attempt to suck venom from a snake bite.

!!! warning "CAUTION"
    Test only a small amount. Wait 8 hours before eating more.

!!! note
    This technique requires dry conditions.

!!! tip
    Birch bark ignites even when damp — look for it first.
```

Severity mapping:
- `!!! danger` — Risk of death or serious injury
- `!!! warning` — Risk of making the situation worse
- `!!! note` — Important context that affects the procedure
- `!!! tip` — Helpful technique or shortcut

### Content Tabs (for regional variations)

```markdown
=== "North America"
    Rattlesnake, copperhead, cottonmouth, coral snake.

=== "Australia"
    Eastern brown snake, taipan, death adder.
```

### Internal Links

```markdown
See [Shelter Principles](../shelter/shelter-principles.md) for site selection.
```

---

## Development Workflow

### Prerequisites

```bash
pip install -r requirements.txt
```

### Local Development

```bash
mkdocs serve          # hot-reload dev server at http://localhost:8000
mkdocs build --strict # production build — fails on warnings
codespell docs/ --config .codespellrc --quiet-level=2  # spell check
```

### Adding a New Guide

1. Create the `.md` file in the appropriate `docs/` subfolder
2. Add YAML frontmatter with `tags:`
3. Follow the guide template (all sections required)
4. Add a nav entry in `mkdocs.yml`
5. Add 3-8 cross-category See Also links
6. Add reciprocal links in related guides
7. Run `mkdocs serve` and verify it renders
8. Run spell-check and `mkdocs build --strict`
9. Commit: `content: add [guide-name]`

### Dependency Management

Dependencies are pinned in `requirements.txt`. To upgrade:

```bash
pip install --upgrade mkdocs-material mkdocs-minify-plugin
# note the new versions, then update requirements.txt manually
mkdocs build --strict  # verify nothing broke
```

Do not use `pip freeze > requirements.txt` — it captures transitive dependencies and creates noise.

Dependabot opens weekly PRs for updates. Review and merge those promptly to stay on patched versions.

### Deployment

The project uses the modern GitHub Pages Actions deployment (OIDC, no long-lived secrets):

- `lint.yml` runs on every push and PR: spell-check + `mkdocs build --strict`
- `deploy.yml` runs on push to `main`: build artifact → deploy to GitHub Pages

**One-time setup:** In GitHub Settings → Pages, set Source to **GitHub Actions**.

---

## Cross-Linking

Every guide has `## See Also` with links to related guides, prioritizing cross-category connections.

### Format

```markdown
## See Also

- [Guide Title](../category/guide-name.md) — brief description of why it's related.
- [Same-Category Guide](guide-name.md) — another relationship description.
```

### Rules

- Link across categories. A medical guide should link to relevant scenarios, tools, and psychology guides.
- Use relative paths from the current file.
- Include an em-dash description explaining the relationship.
- Target 3-8 links per guide.
- Add reciprocal links: if A links to B, B links back to A.
- Place See Also between Quick Reference and Sources.

---

## Commit Convention

```
content: add [guide-name]       — new guide
content: update [guide-name]    — revision to existing guide
docs: [description]             — project documentation changes
fix: [description]              — factual correction
chore: [description]            — structural/organizational changes
build: [description]            — MkDocs config, CI/CD, dependencies
style: [description]            — CSS, theme, layout
security: [description]         — security policy, CI hardening, content safety
```
