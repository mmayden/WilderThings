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
