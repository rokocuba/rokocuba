#!/usr/bin/env python3
"""Generate the profile timeline as one clickable SVG strip per entry.

A single SVG referenced by <img> is inert, so links inside it never fire.
Slicing the timeline into one file per entry lets each strip be wrapped in an
<a>, which is the only way to make a timeline navigable on GitHub.
"""

import os
from xml.sax.saxutils import escape

W = 880
DATE_X = 138
RAIL_X = 166
TEXT_X = 194
TYPE_X = 846

FONT = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"

# height, title size, dot radius
SIZES = {
    "xl": (124, 17.0, 7.0),
    "l":  (104, 15.5, 6.0),
    "m":  (88, 14.5, 5.5),
    "s":  (72, 13.5, 4.5),
}

THEMES = {
    "light": {
        "title": "#1F2328", "desc": "#59636E", "date": "#6E7781", "rail": "#D1D9E0",
        "accent": {"education": "#3B6FD4", "research": "#7C5CD1", "thesis": "#7C5CD1",
                   "competition": "#BE8A1E", "award": "#BE8A1E", "industry": "#1F8A6E"},
    },
    "dark": {
        "title": "#E6EDF3", "desc": "#9198A1", "date": "#7D8590", "rail": "#30363D",
        "accent": {"education": "#58A6FF", "research": "#A277FF", "thesis": "#A277FF",
                   "competition": "#E3B341", "award": "#E3B341", "industry": "#3FB950"},
    },
}

# slug, size, date, title, [description lines], category, label, anchor, marker, ring
ENTRIES = [
    ("eth", "xl", "09.2026", "ETH Zürich",
     ["MSc Computer Science, starting September 2026.",
      "Machine Intelligence major, Theoretical Computer Science minor."],
     "education", "EDUCATION", None, "circle", True),

    ("cern", "l", "Summer 2026", "CERN",
     ["Summer Student in Geneva."],
     "research", "RESEARCH", "#cern-summer-student", "circle", False),

    ("bsc", "xl", "06.2026", "BSc in Computing, FER",
     ["University of Zagreb, Faculty of Electrical Engineering and Computing.",
      "Graduated with high honours."],
     "education", "EDUCATION", None, "circle", True),

    ("thesis", "l", "03–06.2026", "Shapley-Guided VAE",
     ["Bachelor thesis. Letting a model work out during training how much",
      "each of its secondary objectives should count."],
     "thesis", "THESIS", "#shapley-guided-vae", "circle", False),

    ("stem26", "m", "05.2026", "STEM Games 2026, Mathematics Arena",
     ["Telling AI-written Reddit comments from human ones, from the text alone."],
     "competition", "COMPETITION", "#stem-games-2026-mathematics-arena", "circle", False),

    ("cmc25", "l", "11.2025", "AVL Computational Modeling Challenge 2025",
     ["1st place, EUR 1,000. Covering a stage with patches cut from a single sheet,",
      "at the lowest possible cutting and travel cost."],
     "award", "1ST PLACE", "#avl-computational-modeling-challenge-2025", "diamond", True),

    ("gaussvae", "m", "10.2025–02.2026", "GaussVAE",
     ["Compressing images through their Gaussian splatting parameters, not their pixels."],
     "research", "RESEARCH", "#gaussvae", "circle", False),

    ("abysalto", "l", "Summer 2025", "Abysalto",
     ["AI Academy internship. Retrieval and agent infrastructure for a",
      "document-processing platform."],
     "industry", "INDUSTRY", "#abysalto-ai-agent-factory", "circle", False),

    ("stem25", "m", "05.2025", "STEM Games 2025, Mathematics Arena",
     ["1st place. Designing codes that survive a noisy communication channel."],
     "competition", "COMPETITION", "#stem-games-2025-mathematics-arena", "circle", False),

    ("loncar", "m", "11.2024", "Josip Lončar Award",
     ["FER's award for academic excellence, top 1.5% of the first year."],
     "award", "AWARD", None, "diamond", False),

    ("cmc24", "s", "11.2024", "Computational Modeling Challenge 2024",
     ["Placing mirrors to light as much of a dark room as possible."],
     "competition", "COMPETITION", "#computational-modeling-challenge-2024", "circle", False),

    ("scholarships", "s", "2023–2026", "Scholarships",
     ["Zagreb Excellence scholarship, and the national STEM stipend."],
     "award", "SCHOLARSHIP", None, "diamond", False),

    ("fer-start", "m", "09.2023", "University of Zagreb, FER",
     ["Started the BSc in Computing, with FER's entrance award for placing",
      "in the top 6% of candidates on the faculty ranking."],
     "education", "EDUCATION", None, "circle", False),
]


def strip(entry, theme_name, first=False, last=False):
    slug, size, date, title, desc, cat, label, anchor, marker, ring = entry
    t = THEMES[theme_name]
    H, title_size, r = SIZES[size]
    a = t["accent"][cat]

    # centre the text block, so a taller strip reads as more breathing room
    if len(desc) == 2:
        ty, dys = H / 2 - 11, [H / 2 + 6, H / 2 + 23]
    else:
        ty, dys = H / 2 - 2, [H / 2 + 17]
    cy = ty - 5

    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" '
         f'height="{H}" font-family="{FONT}" role="img" '
         f'aria-label="{escape(date)}. {escape(title)}. {escape(" ".join(desc))}">']

    # fade the rail towards each edge so the seam between strips reads as a dip, not a break
    o.append(
        '<defs><linearGradient id="r" gradientUnits="userSpaceOnUse" '
        f'x1="0" y1="0" x2="0" y2="{H}">'
        f'<stop offset="0" stop-color="{t["rail"]}" stop-opacity="{0 if first else 0.55}"/>'
        f'<stop offset="0.14" stop-color="{t["rail"]}" stop-opacity="1"/>'
        f'<stop offset="0.86" stop-color="{t["rail"]}" stop-opacity="1"/>'
        f'<stop offset="1" stop-color="{t["rail"]}" stop-opacity="{0 if last else 0.55}"/>'
        '</linearGradient></defs>'
    )

    if first:
        o.append(f'<line x1="{RAIL_X}" y1="1" x2="{RAIL_X}" y2="{cy - r - 6:.1f}" '
                 f'stroke="{a}" stroke-width="2.5" stroke-dasharray="1 6" '
                 'stroke-linecap="round" opacity="0.55"/>')
        o.append(f'<rect x="{RAIL_X - 1.25}" y="{cy:.1f}" width="2.5" height="{H - cy:.1f}" '
                 'fill="url(#r)"/>')
    elif last:
        o.append(f'<rect x="{RAIL_X - 1.25}" y="0" width="2.5" height="{cy:.1f}" fill="url(#r)"/>')
    else:
        o.append(f'<rect x="{RAIL_X - 1.25}" y="0" width="2.5" height="{H}" fill="url(#r)"/>')

    if ring:
        o.append(f'<circle cx="{RAIL_X}" cy="{cy:.1f}" r="{r + 4.5:.1f}" fill="none" '
                 f'stroke="{a}" stroke-width="1.5" opacity="0.3"/>')
    if marker == "diamond":
        s = r * 1.75
        o.append(f'<rect x="{RAIL_X - s/2:.1f}" y="{cy - s/2:.1f}" width="{s:.1f}" '
                 f'height="{s:.1f}" rx="1.5" fill="{a}" '
                 f'transform="rotate(45 {RAIL_X} {cy:.1f})"/>')
    else:
        o.append(f'<circle cx="{RAIL_X}" cy="{cy:.1f}" r="{r}" fill="{a}"/>')

    o.append(f'<text x="{DATE_X}" y="{ty:.1f}" text-anchor="end" font-size="12.5" '
             f'font-weight="600" fill="{t["date"]}" letter-spacing="0.2">{escape(date)}</text>')
    o.append(f'<text x="{TEXT_X}" y="{ty:.1f}" font-size="{title_size}" font-weight="650" '
             f'fill="{t["title"]}" letter-spacing="-0.1">{escape(title)}</text>')
    for line, dy in zip(desc, dys):
        o.append(f'<text x="{TEXT_X}" y="{dy:.1f}" font-size="13" '
                 f'fill="{t["desc"]}">{escape(line)}</text>')
    o.append(f'<text x="{TYPE_X}" y="{ty:.1f}" text-anchor="end" font-size="9.5" '
             f'font-weight="700" fill="{a}" letter-spacing="1.3" opacity="0.9">{label}</text>')

    o.append("</svg>")
    return "\n".join(o)


def main(outdir):
    os.makedirs(outdir, exist_ok=True)
    n = len(ENTRIES)
    for i, e in enumerate(ENTRIES):
        for theme in ("light", "dark"):
            path = os.path.join(outdir, f"{i:02d}-{e[0]}-{theme}.svg")
            with open(path, "w", encoding="utf-8") as f:
                f.write(strip(e, theme, first=(i == 0), last=(i == n - 1)))
    print(f"wrote {n * 2} strips to {outdir}")


def markdown_block(assets="assets/timeline"):
    rows = []
    for i, e in enumerate(ENTRIES):
        slug, _, date, title, desc, _, _, anchor, _, _ = e
        alt = escape(f"{date}. {title}. {' '.join(desc)}", {'"': "&quot;"})
        img = (f'<picture><source media="(prefers-color-scheme: dark)" '
               f'srcset="{assets}/{i:02d}-{slug}-dark.svg">'
               f'<img src="{assets}/{i:02d}-{slug}-light.svg" width="100%" '
               f'alt="{alt}"></picture>')
        rows.append(f'<a href="{anchor}">{img}</a>' if anchor else img)
    return "\n".join(rows)


if __name__ == "__main__":
    main("/mnt/user-data/outputs/assets/timeline")
    with open("/home/claude/timeline_block.html", "w") as f:
        f.write(markdown_block())
    print("wrote markdown block")
