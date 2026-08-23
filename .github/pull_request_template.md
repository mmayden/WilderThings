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

## Accuracy review — the seven lenses

See [CONTRIBUTING.md](../CONTRIBUTING.md#the-seven-lenses--how-to-review-content-for-accuracy).
Structural checks tell you a guide is well-formed; these tell you it is right.

- [ ] **1. True?** Claim survives contact with the source. Anything computable has been recomputed
- [ ] **2. Current?** Checked against the current guideline, not the traditional technique
- [ ] **3. Displacement?** Believing this does not stop the reader doing the thing that actually works
- [ ] **4. Detectable?** Any safety check given can actually detect the hazard it is checking for
- [ ] **5. Consistent?** Grepped for this procedure/number elsewhere, including the reference checklists
- [ ] **6. Complete?** Considered what will hurt this guide's reader that is not on the page
- [ ] **7. Sound reasoning?** The stated mechanism is real, not a plausible-sounding invention

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
