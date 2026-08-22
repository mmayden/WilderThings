#!/usr/bin/env bash
# Build the shareable offline copy of WilderThings.
#
#   ./scripts/build-offline.sh
#
# Produces:
#   site-offline/               — open index.html in any browser, no server needed
#   wilderthings-offline.zip    — the single file to hand to someone
#
# The result is fully self-contained: no network requests, no install, no server.
# See mkdocs.offline.yml for how that is guaranteed, and the verify step below
# for how it is checked.

set -euo pipefail
cd "$(dirname "$0")/.."

OUT_DIR="site-offline"
PKG_NAME="WilderThings-Offline"
ZIP_NAME="wilderthings-offline.zip"

echo "==> Building offline site"
mkdocs build -f mkdocs.offline.yml --strict

# 404.html is a web-server error page. It references assets by absolute path,
# which cannot resolve on a filesystem copy, so it is dead weight here.
rm -f "$OUT_DIR/404.html"

echo "==> Bundling licenses (recipients need to know their rights)"
cp LICENSE "$OUT_DIR/LICENSE.md"
cp LICENSE-CONTENT.txt LICENSE-CODE.txt "$OUT_DIR/"

echo "==> Adding START-HERE for recipients"
cat > "$OUT_DIR/START-HERE.txt" <<'EOF'
WilderThings — Offline Survival Guide Collection
================================================

TO READ IT:  open the file named  index.html  in this folder.
             Any web browser will do. Double-clicking usually works.

You do NOT need internet. You do NOT need to install anything.
Everything works with no signal — that is the point.

Use the search box at the top to search all 89 guides.

Copy this whole folder anywhere you like: a phone, a USB stick,
an SD card, another computer. Keep the folder together — the
guides live in the subfolders next to index.html.

--------------------------------------------------------------
SHARE THIS FREELY

The guides are licensed CC BY-SA 4.0. You may copy, print,
translate, adapt, and redistribute them — commercially too.
Credit "WilderThings Contributors" and keep any derivative
under the same free license. Full terms: LICENSE.md

--------------------------------------------------------------
IMPORTANT — READ THIS

This collection is reference material, not a substitute for
training, professional medical care, or emergency services.
Get to real help whenever that is possible.

Plant and mushroom identification carries a risk of death from
misidentification. Never eat anything you cannot positively
identify. Look-alike warnings are included but are not a
substitute for expert, region-specific knowledge.

Hunting, trapping, and fishing are legally regulated and the
rules vary by jurisdiction.
--------------------------------------------------------------
EOF

echo "==> Verifying the build is genuinely offline"
# Any external resource load (script/link/img) means the copy is not self-contained.
# Content links in <a> tags are citations and are expected/allowed.
LEAKS=$(grep -rhoE '<(script|link|img)[^>]*(src|href)=("?)(https?:)?//[^ >"]+' \
          "$OUT_DIR" --include=*.html | sort -u || true)
if [ -n "$LEAKS" ]; then
  echo "FAIL: build makes external requests, so it is not offline-safe:" >&2
  echo "$LEAKS" >&2
  exit 1
fi

# The inlined search index is what makes search work without a server.
if [ ! -s "$OUT_DIR/search/search_index.js" ]; then
  echo "FAIL: search/search_index.js missing — offline search would be broken." >&2
  exit 1
fi
echo "    no external requests; offline search index present"

echo "==> Packaging $ZIP_NAME"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT
mkdir -p "$TMP/$PKG_NAME"
cp -r "$OUT_DIR"/. "$TMP/$PKG_NAME/"
rm -f "$ZIP_NAME"
(cd "$TMP" && zip -qr - "$PKG_NAME") > "$ZIP_NAME"

echo
echo "Done."
echo "  folder : $OUT_DIR/index.html"
echo "  archive: $ZIP_NAME  ($(du -h "$ZIP_NAME" | cut -f1))"
