#!/usr/bin/env python3
"""Verify the built outputs actually work. Run by CI on every push.

These are the checks that catch the failures that matter for this project:
a copy that silently needs the network, links that go nowhere, or safety
warnings that render as raw markup. Each has been a real bug here.

    python3 scripts/verify.py --offline site-offline
    python3 scripts/verify.py --single  wilderthings-mobile.html
    python3 scripts/verify.py --site    site

Exits non-zero on any failure.
"""

import argparse
import collections
import datetime
import glob
import os
import re
import sys
import urllib.parse
from html.parser import HTMLParser

failures = []
notes = []


def fail(check, detail):
    failures.append(f"{check}: {detail}")


def ok(check, detail):
    notes.append(f"  PASS  {check} — {detail}")


# Resource-loading tags. Links in <a> are citations and may point anywhere;
# only fetched sub-resources determine whether a build is self-contained.
EXTERNAL_RESOURCE = re.compile(
    r'<(?:script|link|img|iframe|audio|video|source|embed)[^>]*'
    r'(?:src|href)\s*=\s*"?(?:https?:)?//[^\s>"]+', re.I)


class RefCollector(HTMLParser):
    """Collect href/src values and element ids from a document."""

    def __init__(self):
        super().__init__()
        self.refs = []
        self.ids = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get("id"):
            self.ids.append(a["id"])
        for key in ("href", "src"):
            if a.get(key):
                self.refs.append(a[key])


def check_no_external_requests(paths, label):
    leaks = set()
    for path in paths:
        with open(path, encoding="utf-8", errors="replace") as f:
            for m in EXTERNAL_RESOURCE.finditer(f.read()):
                leaks.add(m.group(0)[:120])
    if leaks:
        fail(f"{label} is not self-contained",
             f"{len(leaks)} external resource load(s); first: {sorted(leaks)[0]}")
    else:
        ok(f"{label} self-contained", "0 external resource loads")


def check_offline_dir(root):
    html_files = [os.path.join(dp, fn)
                  for dp, _, fns in os.walk(root)
                  for fn in fns if fn.endswith(".html")]
    if not html_files:
        fail("offline build", f"no HTML found under {root}")
        return

    check_no_external_requests(html_files, "offline build")

    # Every local reference must resolve to a real file, or the copy is broken
    # for someone with no network to fall back on.
    broken = []
    total = 0
    for path in html_files:
        p = RefCollector()
        with open(path, encoding="utf-8", errors="replace") as f:
            p.feed(f.read())
        for ref in p.refs:
            if re.match(r'^(https?:|mailto:|data:|#|javascript:)', ref):
                continue
            target = urllib.parse.unquote(ref.split("#")[0].split("?")[0])
            if not target:
                continue
            total += 1
            if not os.path.exists(os.path.normpath(os.path.join(os.path.dirname(path), target))):
                broken.append(f"{os.path.relpath(path, root)} -> {ref}")
    if broken:
        fail("offline build has broken references",
             f"{len(broken)} of {total}; first: {broken[0]}")
    else:
        ok("offline references resolve", f"{total} local refs across {len(html_files)} pages")

    # Search is inlined for file:// use; without it search silently does nothing.
    index = os.path.join(root, "search", "search_index.js")
    if os.path.getsize(index) > 0 if os.path.exists(index) else False:
        ok("offline search index", f"{os.path.getsize(index):,} bytes")
    else:
        fail("offline search index", "search/search_index.js missing or empty")

    for required in ("LICENSE.md", "START-HERE.txt"):
        if not os.path.exists(os.path.join(root, required)):
            fail("offline package", f"{required} missing — recipients need it")
    if not failures:
        ok("offline package", "LICENSE.md and START-HERE.txt bundled")


def check_single_file(path):
    if not os.path.exists(path):
        fail("single-file build", f"{path} not found")
        return
    with open(path, encoding="utf-8", errors="replace") as f:
        html = f.read()

    check_no_external_requests([path], "single-file build")

    p = RefCollector()
    p.feed(html)

    # Concatenating 91 independently-rendered documents previously produced
    # duplicate ids, which silently merged content-tab radio groups.
    dupes = {k: v for k, v in collections.Counter(p.ids).items() if v > 1}
    if dupes:
        worst = sorted(dupes.items(), key=lambda kv: -kv[1])[:3]
        fail("single-file duplicate ids",
             f"{len(dupes)} duplicated; worst: {worst}")
    else:
        ok("single-file ids unique", f"{len(p.ids)} ids")

    targets = set(p.ids)
    frags = [r[1:] for r in p.refs if r.startswith("#") and len(r) > 1]
    broken = [f for f in frags if f not in targets]
    if broken:
        fail("single-file broken anchors",
             f"{len(broken)} of {len(frags)}; first: {broken[:3]}")
    else:
        ok("single-file anchors resolve", f"{len(frags)} internal links")

    # Admonition bodies were previously HTML-escaped instead of rendered, so
    # bold/links/tables inside safety warnings appeared as literal markup.
    literal = re.findall(r'>[^<>]*\*\*[^<>]*<', html)
    if literal:
        fail("single-file unrendered markdown",
             f"{len(literal)} text node(s) contain literal '**'; first: {literal[0][:80]}")
    else:
        ok("single-file markdown rendered", "no literal '**' in text nodes")

    if 'class="adm-body"' in html:
        fail("single-file admonitions",
             "hand-rolled adm-body markup present; should use the admonition extension")

    n_adm = len(re.findall(r'<div class="admonition', html))
    if n_adm < 100:
        fail("single-file admonitions", f"only {n_adm} rendered — expected 400+")
    else:
        ok("single-file admonitions", f"{n_adm} rendered")


def check_site(root):
    """The hosted build may reference external hosts (fonts); just check links."""
    html_files = [os.path.join(dp, fn)
                  for dp, _, fns in os.walk(root)
                  for fn in fns if fn.endswith(".html") and fn != "404.html"]
    broken, total = [], 0
    for path in html_files:
        p = RefCollector()
        with open(path, encoding="utf-8", errors="replace") as f:
            p.feed(f.read())
        for ref in p.refs:
            if re.match(r'^(https?:|mailto:|data:|#|javascript:)', ref):
                continue
            target = urllib.parse.unquote(ref.split("#")[0].split("?")[0])
            if not target:
                continue
            total += 1
            if not os.path.exists(os.path.normpath(os.path.join(os.path.dirname(path), target))):
                broken.append(f"{os.path.relpath(path, root)} -> {ref}")
    if broken:
        fail("site has broken references", f"{len(broken)} of {total}; first: {broken[0]}")
    else:
        ok("site references resolve", f"{total} local refs across {len(html_files)} pages")



# ---------------------------------------------------------------------------
# Content-consistency checks. These exist because CONTRIBUTING.md's review
# process says consistency is mechanical and should not consume judgment.
# Everything here was a real defect found by hand during the August 2026 audit.
# ---------------------------------------------------------------------------

IMPERIAL_TO_METRIC = {
    ("in", "cm"): 2.54, ("inch", "cm"): 2.54, ("inches", "cm"): 2.54,
    ("ft", "m"): 0.3048, ("feet", "m"): 0.3048,
    ("mi", "km"): 1.609344, ("miles", "km"): 1.609344,
    ("lb", "kg"): 0.453592, ("lbs", "kg"): 0.453592, ("pounds", "kg"): 0.453592,
    ("yd", "m"): 0.9144, ("yards", "m"): 0.9144,
    ("qt", "l"): 0.946353, ("quart", "l"): 0.946353, ("quarts", "l"): 0.946353,
    ("gal", "l"): 3.78541, ("gallon", "l"): 3.78541, ("gallons", "l"): 3.78541,
    ("oz", "g"): 28.3495,
}

# Claims that recur across guides. A disagreement here is a contradiction the
# reader can actually hit by following two pages.
#
# LIMITATION: this check is only as good as the patterns below. It proves the
# listed claims agree; it does not prove the corpus is free of contradictions.
# When you find a new contradiction by hand, add a pattern for it here so the
# same class cannot come back.
RECURRING_CLAIMS = {
    # Matches prose ("above 6,500 ft ... boil 3 minutes") and table rows. The
    # sea-level row of an altitude table also mentions 6,500 and says 1 minute,
    # which is correct and must not be read as a disagreement — hence EXCLUDE.
    "boil time above 6,500 ft":   r"6,500[^\n]{0,80}?(\d+)\s*min",
    "signal fire triangle spacing": r"triangle[^.]{0,60}?(\d+)\s*(?:ft|feet)",
    "bleach re-dose wait":        r"repeat the dose and wait another (\d+)\s*minutes",
    "epinephrine adult dose":     r"(?:epinephrine|EpiPen)[^.]{0,60}?(0\.\d+)\s*mg",
    "tourniquet above wound":     r"tourniquet[^.]{0,60}?(\d+)-(\d+)\s*inches",
}

# Lines matching these are legitimately different claims, not contradictions.
CLAIM_EXCLUSIONS = {
    "boil time above 6,500 ft": r"sea level|below 6,500|0[\u2013-]2,000",
}

# ANSI Z535: DANGER = will kill/maim, WARNING = could, CAUTION = lesser harm.
ALLOWED_TITLES = {
    "danger": {"DANGER", "WARNING"},
    "warning": {"CAUTION", "DISCLAIMER", "NOTICE"},
}


def _md_files(root):
    return [os.path.join(dp, fn)
            for dp, _, fns in os.walk(root)
            for fn in fns if fn.endswith(".md")]


def check_unit_conversions(root):
    num = r"(\d+(?:,\d{3})*(?:\.\d+)?)"
    rng = num + r"\s*(?:[-\u2013\u2014]\s*" + num + r")?"
    pat = re.compile(
        rng + r"\s*(in|inch|inches|ft|feet|mi|miles|lb|lbs|pounds|yd|yards|"
              r"qt|quart|quarts|gal|gallon|gallons|oz)\b\s*\(\s*~?" + rng +
        r"\s*(cm|m|km|kg|l|g)\b", re.I)
    bad, checked = [], 0
    for path in _md_files(root):
        for ln, line in enumerate(open(path, encoding="utf-8"), 1):
            # Fractions like "1/2 in" confuse the parser; skip those spans.
            if re.search(r"\d/\d", line):
                continue
            for m in pat.finditer(line):
                a1, a2, u1, b1, b2, u2 = m.groups()
                k = IMPERIAL_TO_METRIC.get((u1.lower(), u2.lower()))
                if not k:
                    continue
                checked += 1
                # Ranges may be written "800 to 1,500 lbs (360-680 kg)", where the
                # regex sees only the upper imperial value. Accept a match against
                # either metric endpoint rather than reporting a false positive —
                # a check that cries wolf is a check people learn to ignore.
                metric_vals = [float(v.replace(",", "")) for v in (b1, b2) if v]
                imperial_vals = [float(v.replace(",", "")) for v in (a1, a2) if v]
                for src in imperial_vals:
                    exp = src * k
                    if not exp:
                        continue
                    tol = 0.13 if exp >= 10 else 0.30
                    if not any(abs(dst - exp) / exp <= tol for dst in metric_vals):
                        bad.append(f"{path}:{ln} {m.group(0)[:50]!r} ({src}{u1}={exp:.1f}{u2})")
    if bad:
        fail("unit conversions", f"{len(bad)} suspicious; first: {bad[0]}")
    else:
        ok("unit conversions", f"{checked} dual measurements verified")


def check_temperature_conversions(root):
    # The corpus writes temperatures both as "95°F (35°C)" and "95 degF (35 degC)".
    # An earlier version of this check only matched the degree symbol and silently
    # skipped every "degF" pair — found by negative-testing the check itself.
    pat = re.compile(
        r"(-?\d+(?:\.\d+)?)\s*(?:\u00b0\s*|deg\s*)F\b"
        r"[^()]{0,12}\(\s*~?\s*(-?\d+(?:\.\d+)?)\s*(?:\u00b0\s*|deg\s*)C\b")
    bad, checked = [], 0
    for path in _md_files(root):
        for ln, line in enumerate(open(path, encoding="utf-8"), 1):
            # Temperature *differences* convert by ratio, not offset — skip them.
            if re.search(r"drops?\s+of|drop of|difference|colder than|below ambient", line, re.I):
                continue
            for m in pat.finditer(line):
                f, c = float(m.group(1)), float(m.group(2))
                checked += 1
                exp = (f - 32) * 5 / 9
                if abs(c - exp) > max(1.5, abs(exp) * 0.05):
                    bad.append(f"{path}:{ln} {m.group(0)} (should be {exp:.0f}C)")
    if bad:
        fail("temperature conversions", f"{len(bad)} suspicious; first: {bad[0]}")
    else:
        ok("temperature conversions", f"{checked} F/C pairs verified")


def check_recurring_claims(root):
    disagreements = []
    for name, pat in RECURRING_CLAIMS.items():
        seen = collections.defaultdict(set)
        excl = CLAIM_EXCLUSIONS.get(name)
        for path in _md_files(root):
            for line in open(path, encoding="utf-8"):
                if excl and re.search(excl, line, re.I):
                    continue
                for m in re.finditer(pat, line, re.I):
                    seen[m.groups()].add(os.path.relpath(path, root))
        if len(seen) > 1:
            disagreements.append(f"{name}: " + " vs ".join(
                f"{k} in {sorted(v)[:2]}" for k, v in seen.items()))
    if disagreements:
        fail("guides disagree on a recurring claim",
             f"{len(disagreements)}; first: {disagreements[0]}")
    else:
        ok("recurring claims agree", f"{len(RECURRING_CLAIMS)} claims checked across guides")


def check_signal_words(root):
    """ANSI Z535 severity. Severity must be earned or the lethal warnings lose force."""
    bad = []
    counts = collections.Counter()
    for path in _md_files(root):
        for ln, line in enumerate(open(path, encoding="utf-8"), 1):
            m = re.match(r'\s*!!!\s+(danger|warning)\s+"([^"]*)"', line)
            if not m:
                continue
            kind, title = m.group(1), m.group(2)
            head = title.split(":")[0].strip().upper()
            counts[head] += 1
            allowed = ALLOWED_TITLES[kind]
            # A descriptive title (a sentence) is fine; a wrong signal word is not.
            if head in {"DANGER", "WARNING", "CAUTION", "NOTICE"} and head not in allowed:
                bad.append(f"{os.path.relpath(path, root)}:{ln} !!! {kind} \"{head}\"")
    if bad:
        fail("signal word severity (ANSI Z535)",
             f"{len(bad)} mismatched; first: {bad[0]}")
    else:
        ok("signal word severity", f"{sum(counts.values())} labelled admonitions consistent")


def check_content(root):
    check_clinical_sources(root)
    check_source_currency()
    check_unit_conversions(root)
    check_temperature_conversions(root)
    check_recurring_claims(root)
    check_signal_words(root)



# ---------------------------------------------------------------------------
# Source currency. "Is it current?" only happens if something makes someone
# look. AGREE II rates the updating procedure as the strongest predictor of
# guideline quality, and this project previously had none — four withdrawn
# techniques sat in the text, one withdrawn in 2008.
# ---------------------------------------------------------------------------

# Bodies that publish living clinical guidance. A guide covering a clinical
# topic should cite at least one, or it is working from textbooks and tradition.
CLINICAL_BODIES = [
    (r"\bWilderness Medical Society\b", False), (r"\bWMS\b", True),
    (r"\bTCCC\b", True), (r"\bILCOR\b", True), (r"\bATLS\b", True),
    (r"\bPHTLS\b", True), (r"\bANZCOR\b", True), (r"\bNAEMSP\b", True),
    (r"\bCDC\b", True), (r"\bAmerican Heart Association\b", False),
    (r"\bRed Cross\b", False), (r"\bCenters for Disease Control\b", False),
    (r"\bAustralian Resuscitation Council\b", False),
    (r"\bAmerican College of Surgeons\b", False),
    (r"\bSurviving Sepsis\b", False), (r"\bUpToDate\b", False),
    (r"\bSanford Guide\b", False),
]

# Clinical topics that live outside docs/medical/. Listed explicitly rather than
# guessed: a heuristic over the whole corpus produced 20 flags, nearly all false
# (bear-safety citing the National Park Service is correct, not a gap).
CLINICAL_ELSEWHERE = [
    "climate-specific/mountain-survival.md",   # altitude illness — WMS topic
    "climate-specific/arctic-survival.md",     # hypothermia, frostbite — WMS topics
    "wildlife/marine-dangers.md",
    "wildlife/insect-threats.md",
    "wildlife/venomous-snakes.md",
    "wildlife/venomous-spiders.md",
]

STALE_AFTER_DAYS = 400  # annual cadence, with grace


def _cites_clinical_body(text):
    return any(re.search(pat, text, 0 if cs else re.I) for pat, cs in CLINICAL_BODIES)


def check_clinical_sources(root):
    """Clinical guides must cite a body that revises, not only textbooks."""
    targets = sorted(glob.glob(os.path.join(root, "medical", "*.md")))
    targets += [os.path.join(root, rel) for rel in CLINICAL_ELSEWHERE]
    missing = []
    for path in targets:
        if not os.path.exists(path):
            continue
        m = re.search(r"^## Sources\s*$(.*)", open(path, encoding="utf-8").read(), re.M | re.S)
        if not m or not _cites_clinical_body(m.group(1)):
            missing.append(os.path.relpath(path, root))
    if missing:
        fail("clinical guides citing no living guideline body",
             f"{len(missing)}: {', '.join(missing)}")
    else:
        ok("clinical guides cite a living body", f"{len(targets)} checked")


def check_source_currency(tasks_path="TASKS.md"):
    """Living sources get re-checked annually; the dates live in TASKS.md."""
    if not os.path.exists(tasks_path):
        return
    text = open(tasks_path, encoding="utf-8").read()
    block = re.search(r"<!-- source-currency -->(.*?)<!-- /source-currency -->", text, re.S)
    if not block:
        return
    rows = re.findall(r"\|\s*([^|]+?)\s*\|\s*(\d{4}-\d{2}-\d{2})\s*\|", block.group(1))
    if not rows:
        fail("source currency", "no dated rows found in the source-currency block")
        return
    today = datetime.date.today()
    overdue = []
    for name, datestr in rows:
        age = (today - datetime.date.fromisoformat(datestr)).days
        if age > STALE_AFTER_DAYS:
            overdue.append(f"{name} ({age} days)")
    if overdue:
        fail("living sources overdue for re-check",
             f"{len(overdue)} of {len(rows)}: {'; '.join(overdue)}. "
             f"Re-check each against its publisher, then update the date in TASKS.md")
    else:
        oldest = max((today - datetime.date.fromisoformat(d)).days for _, d in rows)
        ok("living sources current", f"{len(rows)} tracked, oldest checked {oldest} days ago")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--offline", metavar="DIR")
    ap.add_argument("--single", metavar="FILE")
    ap.add_argument("--site", metavar="DIR")
    ap.add_argument("--content", metavar="DOCS_DIR",
                    help="consistency checks over the markdown source")
    args = ap.parse_args()

    if not any([args.offline, args.single, args.site, args.content]):
        ap.error("nothing to verify — pass --offline, --single, --site, and/or --content")

    if args.offline:
        check_offline_dir(args.offline)
    if args.single:
        check_single_file(args.single)
    if args.site:
        check_site(args.site)
    if args.content:
        check_content(args.content)

    print("\n".join(notes))
    if failures:
        print("\nFAILED:")
        for f in failures:
            print(f"  {f}")
        return 1
    print("\nAll checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
