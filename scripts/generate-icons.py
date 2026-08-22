#!/usr/bin/env python3
"""Generate WilderThings PWA icon set: a compass rose matching theme.icon.logo
(material/compass-rose) on the Material deep-orange primary."""

import math
import os
from PIL import Image, ImageDraw

BG = (255, 87, 34, 255)      # Material deep orange 500 — matches theme palette primary
FG = (255, 255, 255, 255)    # white glyph
SS = 8                       # supersample factor for anti-aliasing

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "..", "..", "..")
OUT = os.environ.get("ICON_OUT", "docs/assets/images")


def star_point(cx, cy, angle_deg, outer, inner):
    """One kite-shaped compass point: tip -> side -> center -> side."""
    a = math.radians(angle_deg)
    tip = (cx + outer * math.cos(a), cy + outer * math.sin(a))
    left = (cx + inner * math.cos(a + math.pi / 2), cy + inner * math.sin(a + math.pi / 2))
    right = (cx + inner * math.cos(a - math.pi / 2), cy + inner * math.sin(a - math.pi / 2))
    return [tip, left, (cx, cy), right]


def draw_icon(size, glyph_scale=0.78, corner=0.18, ring=True, minor_points=True, waist=0.15):
    """Render one icon. glyph_scale is the glyph diameter as a fraction of canvas.
    waist is the half-width of each point as a fraction of R — raise it at small
    sizes so the star stays legible instead of thinning out to hairlines."""
    S = size * SS
    img = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)

    # Background plate
    r = int(S * corner)
    if r > 0:
        d.rounded_rectangle([0, 0, S - 1, S - 1], radius=r, fill=BG)
    else:
        d.rectangle([0, 0, S - 1, S - 1], fill=BG)

    cx = cy = S / 2.0
    R = S * glyph_scale / 2.0

    if ring:
        w = max(1, int(R * 0.055))
        d.ellipse([cx - R, cy - R, cx + R, cy + R], outline=FG, width=w)
        R *= 0.86  # keep points inside the ring

    if minor_points:
        for ang in (45, 135, 225, 315):
            d.polygon(star_point(cx, cy, ang, R * 0.60, R * waist * 0.73), fill=FG)

    for ang in (0, 90, 180, 270):
        d.polygon(star_point(cx, cy, ang, R, R * waist), fill=FG)

    return img.resize((size, size), Image.LANCZOS)


def save(img, name):
    path = os.path.join(OUT, name)
    img.save(path, "PNG", optimize=True)
    print(f"  {name:28s} {img.size[0]}x{img.size[1]}  {os.path.getsize(path):>6,} B")


os.makedirs(OUT, exist_ok=True)
print(f"Writing to {OUT}/")

# Small sizes: drop the ring and diagonal points — they turn to mush under ~48px.
save(draw_icon(16, glyph_scale=0.92, corner=0.10, ring=False, minor_points=False, waist=0.34), "favicon-16.png")
save(draw_icon(32, glyph_scale=0.90, corner=0.12, ring=False, minor_points=False, waist=0.30), "favicon-32.png")
save(draw_icon(180, glyph_scale=0.76, corner=0.0), "apple-touch-icon.png")  # iOS applies its own mask
save(draw_icon(192, glyph_scale=0.78), "icon-192.png")
save(draw_icon(512, glyph_scale=0.78), "icon-512.png")
# Maskable: glyph inside the 80% safe zone, full-bleed square so any mask shape works.
save(draw_icon(512, glyph_scale=0.56, corner=0.0), "icon-512-maskable.png")

# Multi-resolution .ico for legacy /favicon.ico requests
ico = draw_icon(64, glyph_scale=0.90, corner=0.14, ring=False, minor_points=False, waist=0.28)
ico_path = os.path.join(OUT, "favicon.ico")
ico.save(ico_path, "ICO", sizes=[(16, 16), (32, 32), (48, 48)])
print(f"  {'favicon.ico':28s} 16/32/48    {os.path.getsize(ico_path):>6,} B")
