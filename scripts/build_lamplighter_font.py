#!/usr/bin/env python3
"""Build the self-hosted Lamplighter Display headline face.

Lamplighter Display is a deliberately condensed, renamed derivative of the
72pt optical-size Newsreader ExtraBold source. Newsreader is distributed under
the SIL Open Font License 1.1; the resulting font remains under that license.

The transformation is intentionally conservative: the display cut already has
the open counters, wedge serifs, and editorial contrast this project needs. We
condense outlines and advances independently to create a tighter 1920s headline
rhythm without turning the face into a generic geometric condensed serif.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from fontTools.pens.recordingPen import DecomposingRecordingPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.ttLib import TTFont


FAMILY = "Lamplighter Display"
STYLE = "ExtraBold"
POSTSCRIPT_NAME = "LamplighterDisplay-ExtraBold"
VERSION = "Version 1.000"
OUTLINE_SCALE = 0.89
ADVANCE_SCALE = 0.92


def set_font_names(font: TTFont) -> None:
    name = font["name"]
    for name_id in (1, 2, 3, 4, 5, 6, 16, 17):
        name.removeNames(nameID=name_id)

    records = {
        1: FAMILY,
        2: STYLE,
        3: f"{FAMILY} {STYLE} 1.000",
        4: f"{FAMILY} {STYLE}",
        5: VERSION,
        6: POSTSCRIPT_NAME,
        16: FAMILY,
        17: STYLE,
        13: (
            "This Font Software is licensed under the SIL Open Font License, "
            "Version 1.1. It is a modified version of Newsreader."
        ),
        14: "https://scripts.sil.org/OFL",
    }
    for name_id, value in records.items():
        name.setName(value, name_id, 3, 1, 0x409)
        name.setName(value, name_id, 1, 0, 0)


def condense_glyphs(font: TTFont) -> None:
    glyph_order = font.getGlyphOrder()
    source_glyphs = font.getGlyphSet()
    old_metrics = dict(font["hmtx"].metrics)
    transformed = {}
    advances = {}

    # Record every source outline before replacing the glyf table so composite
    # glyphs are decomposed from the untouched source rather than double-scaled.
    for glyph_name in glyph_order:
        advance, _ = old_metrics[glyph_name]
        new_advance = max(1, round(advance * ADVANCE_SCALE))
        offset_x = round((new_advance - advance * OUTLINE_SCALE) / 2)

        recording = DecomposingRecordingPen(source_glyphs)
        source_glyphs[glyph_name].draw(recording)
        pen = TTGlyphPen(None)
        recording.replay(
            TransformPen(pen, (OUTLINE_SCALE, 0, 0, 1, offset_x, 0))
        )
        transformed[glyph_name] = pen.glyph()
        advances[glyph_name] = new_advance

    glyf = font["glyf"]
    for glyph_name, glyph in transformed.items():
        glyf[glyph_name] = glyph

    metrics = {}
    for glyph_name in glyph_order:
        glyph = glyf[glyph_name]
        glyph.recalcBounds(glyf)
        left_side_bearing = getattr(glyph, "xMin", 0)
        metrics[glyph_name] = (advances[glyph_name], left_side_bearing)
    font["hmtx"].metrics = metrics

    hhea = font["hhea"]
    widths = []
    for glyph_name in glyph_order:
        glyph = glyf[glyph_name]
        advance, lsb = metrics[glyph_name]
        x_min = getattr(glyph, "xMin", 0)
        x_max = getattr(glyph, "xMax", 0)
        glyph_width = x_max - x_min
        widths.append((advance, lsb, advance - lsb - glyph_width, lsb + glyph_width))
    hhea.advanceWidthMax = max(row[0] for row in widths)
    hhea.minLeftSideBearing = min(row[1] for row in widths)
    hhea.minRightSideBearing = min(row[2] for row in widths)
    hhea.xMaxExtent = max(row[3] for row in widths)


def set_style_metadata(font: TTFont) -> None:
    os2 = font["OS/2"]
    os2.usWeightClass = 800
    os2.usWidthClass = 4  # semi-condensed
    # Bold and Regular are mutually exclusive in OS/2.fsSelection.
    os2.fsSelection = (os2.fsSelection | (1 << 5)) & ~(1 << 0) & ~(1 << 6)
    font["head"].macStyle = (font["head"].macStyle | 1) & ~2

    for table_tag in ("cvt ", "fpgm", "prep", "hdmx", "LTSH", "VDMX"):
        if table_tag in font:
            del font[table_tag]


def build(source: Path, output: Path) -> None:
    font = TTFont(source, recalcBBoxes=True, recalcTimestamp=False)
    if "glyf" not in font:
        raise SystemExit("Lamplighter builder expects a TrueType glyf source font")

    condense_glyphs(font)
    set_style_metadata(font)
    set_font_names(font)
    font.flavor = "woff2"
    output.parent.mkdir(parents=True, exist_ok=True)
    font.save(output)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path, help="Newsreader72pt-ExtraBold.ttf")
    parser.add_argument("output", type=Path, help="lamplighter-display.woff2")
    args = parser.parse_args()
    build(args.source, args.output)


if __name__ == "__main__":
    main()
