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
does not tell you the guide is right. For that, use the seven lenses below.

---

## The Seven Lenses — How to Review Content for Accuracy

Structural review catches malformed guides. Accuracy review catches guides that
are well-formed and wrong. Apply all seven lenses to any content change, and to
any guide being audited.

Each lens below exists because it caught a real defect in this repository. The
examples are actual findings, not hypotheticals.

### 1. Is it true?

The plain factual check. Does the claim survive contact with the source?

> **Found:** "Cook shellfish before eating to avoid paralytic shellfish
> poisoning." Saxitoxin is heat and acid stable — boiling, frying, canning, and
> freezing all leave it intact, and acid plus heat can make it *more* toxic.

Watch for numbers that are physically impossible. Pine inner bark was listed at
500-600 kcal/100 g; the ceiling for a carbohydrate food is 400. A wind chill
table understated cold by up to 9°F. A log's stated buoyancy was 2-3x what
Archimedes allows. **Recompute anything computable.**

### 2. Is it current?

Survival writing has a long tail. Techniques persist in print for decades after
the field abandons them. Check the guideline, not what the technique "has
always been."

> **Found:** elevation and pressure points in the bleeding ladder (dropped from
> ATLS/TCCC/Red Cross), the 80/70/60 pulse-to-blood-pressure rule (dropped from
> ATLS at the 8th edition), taping a flail chest (now contraindicated by PHTLS),
> and a ground-to-air signal code superseded by the current ICAO set.

### 3. Does believing this stop someone doing the thing that works?

**The displacement test.** This is the subtlest lens and the most valuable.

Some advice is not exactly false — it simply *substitutes* for the action that
actually saves the person. The harm is not the technique. The harm is the
confidence it creates.

> **Found:** the "lightning crouch." The National Weather Service withdrew it in
> 2008, and their stated reason is the lens itself:
>
> > "Promoting the crouch gives people the false impression that crouching will
> > provide safety... These beliefs could cause people to become apathetic and
> > not seek a safe shelter before the lightning threat becomes significant."
>
> The crouch is not dangerous in itself. It is dangerous because someone who
> believes they have a protective position stops running for shelter.

Ask of any protective measure: **if this does not work, what does the reader
lose by having tried it?** If the answer is "the minutes in which the real
option was available," say so explicitly. Do not present a weak measure and a
strong measure as though they are alternatives on a list.

Other instances found: "cook it to avoid PSP" (displaces avoidance, the only
real defense), and "animals drink here so the water is safe" (displaces
treating the water).

### 4. Can the stated check actually detect the hazard?

Related to lens 3, but distinct. Here the *verification method* is the defect.
A check that cannot detect the thing it is checking for is worse than no check,
because it manufactures certainty.

> **Found:** fermented fish, with "discard it if it smells foul" as the safety
> test. **Botulinum toxin is odorless and tasteless**, and correctly fermented
> fish is supposed to smell powerful. The test cannot separate safe from lethal.

> **Found:** the Universal Edibility Test as a general-purpose safety procedure.
> Water hemlock smells like parsnip, does not reliably burn the lips or tongue,
> and the final step has you eat a quarter cup.

When you write a check, state plainly what it **cannot** catch.

### 5. Does it agree with the rest of the collection?

A reader who follows two guides and gets two answers has lost confidence in
both, and may follow the wrong one.

> **Found:** vinegar prescribed for Portuguese man-of-war in one guide and
> contraindicated in another (the second was right). Cold-water survival times
> differing 3x at the same temperature. Signal fires spaced 25 ft in one guide
> and 100 ft in four others. Bleach re-dose waits of 15 vs 30 minutes.

**Any procedure that appears in two places is a defect waiting to happen.**
Cross-link to one canonical copy instead of duplicating. When a guide changes,
grep for every other place that number or procedure appears — including the
reference checklists, which are what people actually follow under stress.

### 6. Is it complete where the omission is dangerous?

Absence is invisible in review. You have to go looking for it.

> **Found:** the insect foraging guide had no mention of shellfish
> cross-allergy. Insect and shrimp tropomyosin are 75-80% identical, so
> shellfish-allergic people risk anaphylaxis from crickets — and cooking does
> not destroy the allergen. The guide even cited the arthropod relationship as
> *encouragement* to eat them.

> **Found:** the natural disaster guide never mentioned carbon monoxide.
> Generators and grills run indoors are a leading cause of death *after*
> hurricanes and winter storms.

Ask: **who reads this guide, and what will kill them that is not on this page?**

### 7. Is the reasoning sound, even when the advice is right?

A correct instruction supported by an invented mechanism is still a defect. It
teaches the reader a false model, which they will then apply somewhere else.

> **Found:** "wash urushiol off with cold water — cold closes your pores." Pores
> do not open and close with temperature. The advice (wash fast, use soap) was
> right; the explanation was fabricated, and a reader who believes the pore
> model will make bad decisions about burns, heat, and hygiene.

This project's first rule is that every claim is traceable. That applies to the
*why*, not only the *what*.

---

## Applying the Lenses

- **On a new guide:** all seven, before merge.
- **On a content change:** at minimum lenses 1, 2, and 5.
- **On a periodic audit:** work by lens rather than by guide. Sweeping the whole
  collection for one lens at a time surfaces patterns that guide-by-guide
  reading misses — that is how the duplicated-procedure and unit-conversion
  problems were found.
- **Prefer checking to recalling.** Every source check performed during the
  August 2026 audit changed something, including one that corrected an earlier
  correction. If a claim is checkable, check it.

Record what you verified and what you did not. "Reviewed" without scope is not
a useful claim — see TASKS.md for the current audit scope and its explicit gaps.

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
