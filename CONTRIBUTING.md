# Contributing to WilderThings

## Guide Standards

Every guide in this collection must meet these standards before being considered complete.

### Content Requirements

1. **Accuracy first.** All information must be sourced from established survival literature, military field manuals, medical references, or verified expert knowledge. When in doubt, cite your source.

2. **Actionable under stress.** Assume the reader is panicking, injured, or exhausted. Lead with the most critical action. Use numbered steps for procedures. Keep sentences short.

3. **No filler.** Every sentence must earn its place. Remove preamble, motivational padding, and obvious statements. "Water is important for survival" adds nothing.

4. **Regional awareness.** When content varies by region (plants, animals, climate), state the applicable region explicitly. Do not write "this plant is edible" without specifying where it grows.

5. **Safety warnings first.** If a technique has risks (e.g., eating wild mushrooms, crossing rivers), lead with the warning before the instructions.

6. **Mobile-first.** Keep tables narrow (3-4 columns max). Avoid wide content that forces horizontal scrolling. Test readability at phone width.

## File Naming

- Use lowercase kebab-case: `first-aid-basics.md`
- Names should be descriptive and scannable: a reader should know what's inside without opening the file
- All guide content lives in `docs/` (MkDocs serves this as the site root)
- Checklists go in `docs/references/checklists/` with a `-checklist` suffix

## Guide Format

Every guide must follow the template in [templates/guide-template.md](templates/guide-template.md). Key sections:

```markdown
# Guide Title

> One-line summary of what this guide covers and when to use it.

## At a Glance
<!-- Bullet-point summary of the most critical takeaways — 3 to 5 points max -->

## [Main Content Sections]
<!-- Varies by guide. Use H2 for major sections, H3 for subsections -->

## Common Mistakes
<!-- What people get wrong — this section saves lives -->

## Quick Reference
<!-- Condensed version: steps, measurements, or key facts for fast lookup -->

## See Also
<!-- Cross-category links to related guides — see Cross-Linking section below -->

## Sources
<!-- Where the information came from -->
```

## Checklist Format

Quick-reference checklists follow [templates/checklist-template.md](templates/checklist-template.md):

```markdown
# Checklist Title

> When to use this checklist.

- [ ] Step or item
- [ ] Step or item
- [ ] Step or item
```

## Writing Style

- **Voice:** Direct, imperative. "Do this" not "You should consider doing this."
- **Tense:** Present tense for instructions. Past tense only for examples.
- **Person:** Second person ("you") for instructions. Avoid first person.
- **Jargon:** Define technical terms on first use, or link to the glossary.
- **Measurements:** Use both metric and imperial: `2 inches (5 cm)`.
- **Lists:** Use numbered lists for sequential steps, bullets for non-ordered items.

## MkDocs-Specific Formatting

### Admonitions (use instead of blockquote warnings)

```markdown
!!! danger "WARNING"
    Never attempt to suck venom from a snake bite. This does not work and risks infection.

!!! warning "CAUTION"
    Test only a small amount. Wait 8 hours before eating more.

!!! note
    This technique requires dry conditions. See fire-in-wet-conditions.md for alternatives.

!!! tip
    Birch bark ignites even when damp — look for it first.
```

Severity mapping:
- `!!! danger` — Risk of death or serious injury (replaces `> **WARNING:**`)
- `!!! warning` — Risk of making the situation worse (replaces `> **CAUTION:**`)
- `!!! note` — Important context that affects the procedure (replaces `> **NOTE:**`)
- `!!! tip` — Helpful technique or shortcut

### Content Tabs (for regional variations)

```markdown
=== "North America"
    Rattlesnake, copperhead, cottonmouth, coral snake.

=== "Australia"
    Eastern brown snake, taipan, death adder.

=== "Central/South America"
    Fer-de-lance, bushmaster, coral snake.
```

### Internal Links

Link to other guides using relative paths from the current file:

```markdown
See [Shelter Principles](../shelter/shelter-principles.md) for site selection.
```

## Development Workflow

### Prerequisites

```bash
pip install -r requirements.txt
```

### Local Development

```bash
# Serve with hot reload at http://localhost:8000
mkdocs serve

# Build static site to site/ directory
mkdocs build
```

### Adding a New Guide

1. Create the `.md` file in the appropriate `docs/` subfolder
2. Follow the guide template
3. Add a nav entry in `mkdocs.yml` under the correct category
4. Add a `## See Also` section with 3-8 cross-category links (see Cross-Linking below)
5. Add reciprocal links in the related guides' See Also sections
6. Run `mkdocs serve` and verify it renders correctly
7. Check that internal links resolve
8. Commit with `content: add [guide-name]`

### Deployment

Pushing to `main` triggers GitHub Actions, which builds and deploys to GitHub Pages automatically. No manual deploy needed.

## Cross-Linking

Every guide has a `## See Also` section with links to related guides, prioritizing **cross-category** connections. This is a core navigation feature — readers should be able to discover related knowledge across the entire collection.

### Format

```markdown
## See Also

- [Guide Title](../category/guide-name.md) — brief description of why it's related.
- [Another Guide](same-category-guide.md) — another relationship description.
```

### Rules

- **Link across categories, not just within.** A medical guide should link to relevant scenarios, tools, and psychology — not only other medical guides.
- **Use relative paths** from the current file: `../category/guide.md` for cross-category, `guide.md` for same-category.
- **Include an em-dash description** explaining the relationship, not just the title.
- **Target 3-8 links per guide.** Enough to be useful, not so many it's noise.
- **Add reciprocal links.** When guide A links to guide B, guide B should link back to guide A.
- **Place See Also between Quick Reference and Sources.**

### Choosing Links

Prioritize connections that help a reader in context:

- A reader of "Fractures and Splints" benefits from knowing about "Cordage" (splint lashing) and "Injured and Alone" (self-splinting scenario).
- A reader of "Fire Principles" benefits from knowing about "Shelter Principles" (fire placement relative to shelter) and "Signaling for Rescue" (signal fires).
- A reader of "Bear Safety" benefits from knowing about "First Aid Basics" (treating wounds after an encounter) and "Animal Attack" (step-by-step response).

## Review Criteria

Before a guide is merged or marked complete, verify:

- [ ] Follows the guide template structure
- [ ] "At a Glance" section is present and useful
- [ ] "Common Mistakes" section is present
- [ ] "Quick Reference" section is present
- [ ] "See Also" section has 3-8 cross-category links with descriptions
- [ ] Reciprocal links added in related guides
- [ ] No unsourced medical claims
- [ ] Safety warnings precede dangerous procedures
- [ ] Admonitions used (not raw blockquote warnings)
- [ ] Regional applicability is stated where relevant
- [ ] Measurements include both metric and imperial
- [ ] No broken internal links
- [ ] Tables are mobile-friendly (3-4 columns max)
- [ ] Nav entry added in `mkdocs.yml`
- [ ] Renders correctly in `mkdocs serve`
- [ ] Spell-checked and grammar-checked
