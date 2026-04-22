# Style Guide — WilderThings

Consistent formatting makes guides faster to read under stress. Follow these rules for all content.

## Document Structure

Every guide uses this skeleton:

```markdown
# Title

> One-line summary: what this covers and when to use it.

## At a Glance
- Most critical point 1
- Most critical point 2
- Most critical point 3

## [Body Sections — H2 headers]

### [Subsections — H3 headers]

## Common Mistakes

## Quick Reference

## See Also
- [Related Guide](../category/related-guide.md)

## Sources
```

### Required Sections

| Section | Purpose | Required? |
|---------|---------|-----------|
| Title (H1) | Clear, descriptive name | Yes |
| Blockquote summary | One-line "what and when" | Yes |
| At a Glance | 3-5 bullet critical takeaways | Yes |
| Body sections | Main content | Yes |
| Common Mistakes | What people get wrong | Yes |
| Quick Reference | Condensed lookup | Yes |
| See Also | Links to related guides | Yes (if related guides exist) |
| Sources | Citations | Yes |

## Writing Rules

### Voice and Tone
- **Imperative mood.** "Apply pressure" not "You should apply pressure."
- **Present tense.** "The bow drill creates friction" not "The bow drill will create friction."
- **Second person** for instructions. "Hold the knife at 20 degrees."
- **Active voice.** "Pack the wound with gauze" not "The wound should be packed with gauze."
- **No hedging.** "This works in temperatures above freezing" not "This might possibly work in some conditions."

### Clarity
- One idea per sentence.
- One procedure per numbered list.
- Define jargon on first use: "Apply a tourniquet (a tight band that stops blood flow to a limb)."
- If a term appears often, define it once and link to the glossary for subsequent uses.

### Measurements
Always provide both systems. Imperial first for North American context:

- `3 inches (7.5 cm)`
- `2 quarts (1.9 liters)`
- `98.6°F (37°C)`

### Lists

**Numbered lists** for sequential steps (order matters):
```markdown
1. Clear the area of debris.
2. Lay a base of dry bark.
3. Build a teepee of kindling over the tinder.
```

**Bullet lists** for non-ordered items:
```markdown
- Birch bark
- Dried grass
- Cedar shavings
```

## Admonitions

Use MkDocs Material admonitions for all warnings, cautions, notes, and tips. These render as styled callout boxes on the site and remain readable as raw Markdown.

### Syntax

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

### Severity Levels

| Admonition | Use When | Color |
|------------|----------|-------|
| `!!! danger` | Risk of death or serious injury | Red |
| `!!! warning` | Risk of making the situation worse | Orange |
| `!!! note` | Important context that affects the procedure | Blue |
| `!!! tip` | Helpful technique or shortcut | Green |
| `!!! example` | Real-world illustration or case study | Purple |

### Collapsible Admonitions

For long warnings that shouldn't dominate the page:

```markdown
??? danger "Full list of toxic look-alikes"
    Content here is collapsed by default. Reader clicks to expand.
```

### Legacy Format (fully converted)

All guides now use MkDocs admonitions. If you encounter a stray blockquote warning, convert it:

```markdown
<!-- Blockquote (old) → Admonition (current) -->
!!! danger "WARNING"
    Do not do this.
```

## Content Tabs

Use for regional variations, alternative methods, or side-by-side comparisons:

```markdown
=== "Method A: Boiling"
    Bring water to a rolling boil for 1 minute (3 minutes above 6,500 ft / 2,000 m).

=== "Method B: Chemical"
    Add 2 drops of household bleach per quart (liter). Wait 30 minutes.

=== "Method C: UV (SODIS)"
    Fill a clear PET bottle. Place in direct sunlight for 6 hours (2 days if cloudy).
```

## Internal Links

Link to other guides using relative paths from the current file's location:

```markdown
See [Shelter Principles](../shelter/shelter-principles.md) for site selection.
```

For links within the same category:
```markdown
See [Friction Methods](friction-methods.md) for the bow drill technique.
```

## See Also Section

Every guide ends with a `## See Also` section linking to related guides across categories. This is the primary cross-navigation mechanism.

### Format

```markdown
## See Also

- [Guide Title](../category/guide-name.md) — brief description of the relationship.
- [Same-Category Guide](guide-name.md) — why this is relevant.
```

### Rules

- Place between `## Quick Reference` and `## Sources`.
- **Prioritize cross-category links** over same-category links. The nav sidebar handles within-category browsing; See Also should connect across categories.
- Include an em-dash (`—`) description after each link explaining the relationship.
- Target **3-8 links** per guide.
- When adding a link from guide A to guide B, add a reciprocal link from B to A.

### Example (from `docs/fire/friction-methods.md`)

```markdown
## See Also

- [Fire Principles](fire-principles.md) — the fire triangle, fire lays, tinder and kindling selection.
- [Spark and Lens Methods](spark-methods.md) — alternative ignition when friction fails.
- [Cordage](../tools-and-craft/cordage.md) — bow drill string from natural or improvised rope.
- [Knife Use and Care](../tools-and-craft/knife-use-and-care.md) — carving fire sets, notches, and spindles.
```

## Headers

- **H1 (`#`)** — Document title only. One per file.
- **H2 (`##`)** — Major sections.
- **H3 (`###`)** — Subsections within an H2.
- **H4 (`####`)** — Rarely needed. If you need H4, consider restructuring.

## Tables

Use for comparison data, species identification, or quick-lookup. Keep tables mobile-friendly:

- **3-4 columns maximum.** Wider tables cause horizontal scrolling on phones.
- Short cell content. If a cell needs a paragraph, restructure as a list instead.

```markdown
| Snake Feature | Venomous | Non-Venomous |
|---------------|----------|--------------|
| Head shape | Triangular | Rounded |
| Pupils | Vertical slits | Round |
| Neck | Distinct narrow neck | Gradual taper |
```

## Code Blocks

Not typically used in survival guides, but if needed for measurements, formulas, or diagrams:
```
Wind Chill = 35.74 + 0.6215T - 35.75(V^0.16) + 0.4275T(V^0.16)
```

## Mobile Considerations

- Test all content at 375px width (standard phone).
- Avoid images wider than 600px without responsive sizing.
- Keep "Quick Reference" sections scannable — a reader glancing at their phone in rain or cold.
- Prefer short paragraphs (2-3 sentences) over long blocks.

## File Conventions

- **Encoding:** UTF-8
- **Line endings:** LF (Unix-style)
- **Max line length:** No hard wrap. Let the renderer handle it.
- **Trailing newline:** Yes. Every file ends with a single newline.
- **No trailing whitespace.**
- **File location:** All content in `docs/`. Templates in `templates/` (not served).
