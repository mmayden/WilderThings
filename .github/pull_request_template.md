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
