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


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--offline", metavar="DIR")
    ap.add_argument("--single", metavar="FILE")
    ap.add_argument("--site", metavar="DIR")
    args = ap.parse_args()

    if not any([args.offline, args.single, args.site]):
        ap.error("nothing to verify — pass --offline, --single, and/or --site")

    if args.offline:
        check_offline_dir(args.offline)
    if args.single:
        check_single_file(args.single)
    if args.site:
        check_site(args.site)

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
