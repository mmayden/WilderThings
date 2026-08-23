<!--
Thanks for contributing. Content accuracy here is a life-safety matter, so the
checklist below is about correctness first and formatting second.
-->

## What does this change?

<!-- One or two sentences. -->

## Type of change

- [ ] New guide
- [ ] Content correction (factual fix)
- [ ] Content update (expansion, clarification)
- [ ] Tooling / build / CI
- [ ] Documentation

## Sources

<!--
Required for any content change. Every claim must be traceable to a credible
source: field manuals, medical guidelines, established literature. Never
fabricated, never "generally known".
-->

## Accuracy review

See [CONTRIBUTING.md](../CONTRIBUTING.md#reviewing-content-for-accuracy).

**Triage first:** if a reader acts on this and it is wrong, what happens? Only
claims that could kill or seriously injure need the full four checks. Doses,
times, temperatures, thresholds, and any "never"/"always" always escalate.

For each escalated claim:

- [ ] **1. True, including the why?** Verified against a source. Anything computable has been recomputed
- [ ] **2. Current?** Checked the current guideline, not the traditional technique
- [ ] **3. False confidence?** It does not displace the thing that works, and any safety check given can actually detect the hazard
- [ ] **4. Missing?** Considered what will hurt this guide's reader that is not on the page

Mechanical (do not eyeball — grep or run the script):

- [ ] Grepped for this number/procedure elsewhere, **including the reference checklists**
- [ ] `python3 scripts/verify.py --offline site-offline --single wilderthings-mobile.html`

- [ ] Signal word severity is earned (DANGER = will kill; WARNING = could kill; CAUTION = lesser)
- [ ] Where evidence is thin, the text says so rather than sounding confident

## Checklist

Content changes:

- [ ] Every new or changed claim is backed by a cited source
- [ ] Safety warnings precede the dangerous procedure they describe
- [ ] Measurements give both metric and imperial
- [ ] Medical content carries a disclaimer and does not imply replacing professional care
- [ ] Plant/mushroom identification includes look-alike warnings and notes regional variation
- [ ] Regulated activities (hunting, trapping, fishing) note that rules vary by jurisdiction
- [ ] `## See Also` has 3–8 cross-category links, and reciprocal links were added to related guides
- [ ] Tables are 4 columns or fewer (mobile readability)

All changes:

- [ ] `mkdocs build --strict` passes
- [ ] `./scripts/build-offline.sh` passes (it fails if the offline copy starts making network requests)
- [ ] `python3 scripts/verify.py --offline site-offline --single wilderthings-mobile.html` passes
- [ ] `codespell docs/ --config .codespellrc --quiet-level=2` passes

<!--
Reminder: never add a webfont, CDN reference, or external image to guide content.
The offline copy must keep working with no network — CI enforces this.
-->
