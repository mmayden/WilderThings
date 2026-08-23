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
import io
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


def collect_refs(html_files):
    """Map each page to its refs and its anchor ids, in one pass."""
    pages = {}
    for path in html_files:
        c = RefCollector()
        with io.open(path, encoding="utf-8", errors="replace") as f:
            c.feed(f.read())
        pages[path] = c
    return pages


def check_refs(root, html_files, label):
    """Resolve every local href/src, including its #fragment.

    Fragments used to be stripped and thrown away here, so a link into another
    guide's section kept passing after that heading was renamed. Cross-guide
    fragment links are how the corpus points at a canonical procedure instead of
    duplicating it, so an unchecked one is exactly the link that matters.
    """
    pages = collect_refs(html_files)
    ids = {path: set(c.ids) for path, c in pages.items()}
    broken, dangling = [], []
    total = frags = 0

    for path, c in pages.items():
        for ref in c.refs:
            if re.match(r'^(https?:|mailto:|data:|javascript:)', ref):
                continue
            head, _, frag = ref.partition("#")
            target = urllib.parse.unquote(head.split("?")[0])
            frag = urllib.parse.unquote(frag)

            if target:
                total += 1
                resolved = os.path.normpath(os.path.join(os.path.dirname(path), target))
                if not os.path.exists(resolved):
                    broken.append("%s -> %s" % (os.path.relpath(path, root), ref))
                    continue
                if os.path.isdir(resolved):
                    resolved = os.path.join(resolved, "index.html")
            else:
                resolved = path  # same-page fragment

            if not frag:
                continue
            frags += 1
            known = ids.get(resolved)
            if known is None:
                continue  # target outside the scanned set (asset, 404 page)
            if frag not in known:
                dangling.append("%s -> %s" % (os.path.relpath(path, root), ref))

    if broken:
        fail("%s has broken references" % label,
             "%d of %d; first: %s" % (len(broken), total, broken[0]))
    else:
        ok("%s references resolve" % label,
           "%d local refs across %d pages" % (total, len(html_files)))

    if dangling:
        fail("%s has links to headings that do not exist" % label,
             "%d of %d; first: %s" % (len(dangling), frags, dangling[0]))
    else:
        ok("%s anchors resolve" % label, "%d fragment links" % frags)


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
    check_refs(root, html_files, "offline build")

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
    check_refs(root, html_files, "site")



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
    # Only one guide states the milligram dose (elsewhere it is an auto-injector,
    # which is pre-dosed). Kept because it still catches the dose drifting between
    # the protocol and the quick reference inside that guide.
    "epinephrine adult dose":     r"(?:epinephrine|EpiPen)[^.]{0,60}?(0\.\d+)\s*mg",
    "tourniquet above wound":     r"tourniquet[^.]{0,60}?(\d+)-(\d+)\s*inches",
    # Added after each was found disagreeing across guides during the audit.
    # "mi" as well as "miles": signaling-for-rescue writes "100 mi / 160 km" and was
    # therefore never compared against the four guides saying roughly 10.
    "signal mirror range (mi)":   r"[Ss]ignal mirror[^.]{0,110}?(\d+)\s*(?:miles|mi)\b",
    "snow-to-water ratio":        r"(\d+):1\s*snow-to-water|snow-to-water ratio: approximately (\d+):1",
    # Both guides state the general range, but phrase it differently.
    "knot strength loss (range)": r"(?:reduces rope strength by|across knots generally the loss is)\s*(\d+)-(\d+)\s*%",
    "dry bite rate":              r"(\d+)[-\u2013](\d+)%\s*of (?:venomous )?snake bites are \"dry|dry bites?\"?[^.]{0,40}?(\d+)[-\u2013](\d+)%",
    # Pipes excluded from the gap would skip table rows, so allow them.
    "moose safe distance (ft)":   r"[Mm]oose[^.\n]{0,70}?(\d+)\s*ft\s*\(\d+\s*m\)",
    # Six guides gave a bleach dose and four disagreed with the canonical table in
    # purification.md, which is the only one that ties the dose to the concentration
    # on the bottle. The dose is meaningless without it: 8 drops is right at 6% and a
    # third too much at 8.25%.
    # The gap must exclude "%" itself. Guides that name both concentrations on one
    # line ("8 drops if 6%, 6 drops if 8.25%") otherwise let the 8.25% pattern reach
    # back past the 6% clause and pick up the wrong number — a checker bug that looked
    # exactly like a content disagreement until the matches were printed.
    "bleach drops per gallon at 6%":    r"(\d+)\s*drops?[^%.\n|]{0,30}?6%",
    "bleach drops per gallon at 8.25%": r"(\d+)\s*drops?[^%.\n|]{0,30}?8\.25%",
    # The 5-gallon row disagreed between purification.md and water-storage.md on the
    # teaspoon equivalent, and water-storage's 55-gallon row did not scale from its own
    # 5-gallon row. Table rows are the easiest place for arithmetic to rot unnoticed.
    "bleach 5 gallon, 6%":        r"5 gallons[^|\n]*\|\s*(\d+) drops \(([\d/]+) tsp\)",
    "bleach 5 gallon, 8.25%":     r"5 gallons[^|\n]*\|[^|\n]*\|\s*(\d+) drops \(([\d/]+) tsp\)",
}

# A pattern that matches nothing is worse than no pattern: it reports PASS and
# implies the claim is covered. Solar-still yield was tried here and dropped —
# the figure sits several lines below its heading, so a line-based matcher
# cannot tie the two together.
#
# Retried later with a pattern that does match, and dropped again for a better
# reason worth recording so nobody attempts it a third time: the corpus states
# three different still yields and all three are correct. A single ground still
# gives 0.5-1 qt/day, an inflatable gives 1-2.5, and three to five ground stills
# together give 1.5-5. A checker comparing those numbers reports a contradiction
# that is not one. Some claims are only comparable with the context a human reads
# and a regex does not, and forcing them produces false alarms — which cost more
# trust than the missing check does.
#
# A pattern matching only ONE place is nearly as weak: with a single instance
# there is nothing to compare it against, so it can never report a disagreement.
# Crocodilian land speed was tried and dropped for that reason — it appears in
# exactly one guide. Before adding a pattern, confirm it matches every place the
# claim is made, and at least two.

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
    # Both "95\u00b0F (35\u00b0C)" and "95\u00b0F / 35\u00b0C" are used; the slash form was
    # unmatched, leaving 5 more pairs unchecked in four guides.
    # The degree marker is optional: 11 pairs written as bare "145 F (63 C)" were
    # silently skipped, so the corpus had unchecked conversions in four guides. Those
    # are normalized now, but leaving the marker required would let the next one
    # through unnoticed.
    pat = re.compile(
        r"(-?\d+(?:\.\d+)?)\s*(?:\u00b0\s*|deg\s*)?F\b"
        r"(?:[^()]{0,12}\(\s*~?\s*|\s*/\s*)"
        r"(-?\d+(?:\.\d+)?)\s*(?:\u00b0\s*|deg\s*)?C\b")
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
                    # Patterns with alternation yield None for the branch that did
                    # not match, so the same value can produce different tuples.
                    # Normalise before comparing, or the checker reports a
                    # disagreement between a guide and itself.
                    key = tuple(g for g in m.groups() if g is not None)
                    seen[key].add(os.path.relpath(path, root))
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
        return

    # Severity has to be earned. DANGER means "will kill or maim" and is reserved
    # for a short list — amatoxins, botulism, water hemlock, PSP, carbon monoxide,
    # seawater, the handful of marine neurotoxins. If everything becomes DANGER the
    # genuinely lethal warnings stop registering, which is the failure this tier
    # exists to prevent.
    total = sum(counts.values())
    n_danger = counts.get("DANGER", 0)
    share = n_danger / total if total else 0
    if share > DANGER_SHARE_CEILING:
        fail("DANGER label inflation",
             f"{n_danger} of {total} labelled admonitions ({share:.0%}) are DANGER, "
             f"above the {DANGER_SHARE_CEILING:.0%} ceiling. Warnings compete for "
             f"attention — demote any that are 'could kill' rather than 'will kill'")
    else:
        ok("signal word severity",
           f"{total} labelled admonitions consistent; DANGER reserved to {n_danger} ({share:.0%})")


def check_link_labels(root):
    """One guide, one name — and never a bare filename as the link text.

    The single-file build has no sidebar and no search box: Ctrl+F is the whole
    navigation system. A reader looking for "Water Purification" there will not find
    the two entries that called it "Purification", and "fishing-improvised.md" as
    visible link text tells them nothing at all about whether to follow it.
    """
    import collections
    labels = collections.defaultdict(collections.Counter)
    bare = []
    for path in _md_files(root):
        with io.open(path, encoding="utf-8") as f:
            for ln, line in enumerate(f, 1):
                m = re.match(r"- \[([^\]]+)\]\(([^)]+\.md)(?:#[^)]*)?\)", line)
                if not m:
                    continue
                text, href = m.group(1), m.group(2)
                if text.endswith(".md"):
                    bare.append("%s:%d %s" % (os.path.relpath(path, root), ln, text))
                    continue
                target = os.path.normpath(os.path.join(os.path.dirname(path), href))
                labels[target][text] += 1

    if bare:
        fail("link text is a bare filename",
             "%d; first: %s" % (len(bare), bare[0]))
    else:
        ok("link text", "no bare filenames used as link text")

    clashes = ["%s: %s" % (os.path.relpath(t, root), " vs ".join(sorted(c)))
               for t, c in sorted(labels.items()) if len(c) > 1]
    if clashes:
        fail("guides referred to by more than one name",
             "%d; first: %s" % (len(clashes), clashes[0]))
    else:
        ok("link labels consistent", "%d guides, one name each" % len(labels))


# Skip anything naming a specific article or chapter: many share a container title
# legitimately, and their page ranges look like years to any naive scan (pp. 2039-2047).
# The quoted-title test needs three or more words. Excluding every citation with a
# quote mark also excluded every author with a quoted nickname — John "Lofty"
# Wiseman among them — which silently skipped the SAS Handbook, one of the works
# this check was written to catch. Found by negative-testing, not by reading.
JOURNAL_MARKERS = re.compile(
    r"\bvol\.|\bpp\.|\bno\.|\bdoi|;\d+\(|\bch\.\s*\d"
    r"|[\u201c\"][^\u201d\"]*\s\S+\s[^\u201d\"]*[\u201d\"]")


def check_citation_consistency(root):
    """One work, one citation.

    Sources listed a book under two different years or two different publishers in
    six cases — Kochanski as both 1987 and 2014, FM 21-76 as both 1992 and 2002, the
    SAS Handbook under two publishers. A source cited two ways is a source nobody
    checked, and this project's own policy is that every claim must be traceable.

    Journal articles are skipped: many articles share a journal title legitimately,
    and their page ranges look like years to any naive scan (pp. 2039-2047).
    """
    import collections
    works = collections.defaultdict(dict)
    for path in _md_files(root):
        with io.open(path, encoding="utf-8") as f:
            body = f.read()
        m = re.search(r"^## Sources\s*$(.*)", body, re.M | re.S)
        if not m:
            continue
        for line in m.group(1).splitlines():
            line = line.strip()
            if not line.startswith("- "):
                continue
            cite = line[2:].strip()
            if JOURNAL_MARKERS.search(cite):
                continue
            titles = re.findall(r"\*([^*]{6,})\*", cite)
            if not titles:
                continue
            # Key on author plus main title, ignoring any subtitle. A subtitle is the
            # same work — "Bushcraft 101" and "Bushcraft 101: A Field Guide to the Art
            # of Wilderness Survival" were counted separately, so one book cited two
            # ways passed silently. The author has to stay in the key: two different
            # works share a main title here (FEMA and FDIC both wrote "Financial
            # Preparedness"; Auerbach's "Wilderness Medicine" is not Forgey's
            # "Wilderness Medicine: Beyond First Aid"), and folding on title alone
            # reports those as contradictions.
            title = max(titles, key=len).split(":")[0]
            author = cite.split("*")[0]
            key = (re.sub(r"[^a-z0-9]", "", author.lower())[:24]
                   + "|" + re.sub(r"[^a-z0-9]", "", title.lower()))
            works[key][cite] = os.path.relpath(path, root)

    clashes = []
    for key, variants in sorted(works.items()):
        if len(variants) > 1:
            first = sorted(variants)[0]
            clashes.append("%s cited %d ways (e.g. %s in %s)"
                           % (key[:32], len(variants), first[:60], variants[first]))
    if clashes:
        fail("the same work cited more than one way",
             "%d; first: %s" % (len(clashes), clashes[0]))
    else:
        ok("citations consistent", "%d works, one citation each" % len(works))


def check_content(root):
    check_clinical_sources(root)
    check_source_currency()
    check_unit_conversions(root)
    check_temperature_conversions(root)
    check_recurring_claims(root)
    check_signal_words(root)
    check_link_labels(root)
    check_citation_consistency(root)



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
DANGER_SHARE_CEILING = 0.15  # DANGER must stay a clear minority to keep its force


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
