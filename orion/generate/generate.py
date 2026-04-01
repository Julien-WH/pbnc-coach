#!/usr/bin/env python3
"""
Passeport Certification PBNC — PDF Generator
Charge answers.yaml → valide → rend Jinja2 → exporte PDF via Playwright.
"""

import json
import math
import sys
from pathlib import Path

import yaml
from jsonschema import validate, ValidationError
from jinja2 import Environment, FileSystemLoader


def generate_radar_svg(avant: dict, apres: dict, size: int = 500) -> str:
    """Génère un radar chart SVG pour les 31 compétences."""
    labels = [f"C{i}" for i in range(1, 32)]
    n = len(labels)
    cx, cy = size // 2, size // 2
    max_r = size // 2 - 50

    angles = [2 * math.pi * i / n - math.pi / 2 for i in range(n)]

    def polar_to_xy(angle, value):
        r = (value / 5) * max_r
        return cx + r * math.cos(angle), cy + r * math.sin(angle)

    svg_parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {size} {size}">'
    ]

    # Grid circles
    for level in range(1, 6):
        r = (level / 5) * max_r
        svg_parts.append(
            f'<circle cx="{cx}" cy="{cy}" r="{r}" '
            f'fill="none" stroke="#DFE6E9" stroke-width="0.5"/>'
        )

    # Grid lines
    for angle in angles:
        x, y = polar_to_xy(angle, 5)
        svg_parts.append(
            f'<line x1="{cx}" y1="{cy}" x2="{x}" y2="{y}" '
            f'stroke="#DFE6E9" stroke-width="0.5"/>'
        )

    # Labels
    for i, (angle, label) in enumerate(zip(angles, labels)):
        lx, ly = polar_to_xy(angle, 5.6)
        anchor = "middle"
        if math.cos(angle) > 0.3:
            anchor = "start"
        elif math.cos(angle) < -0.3:
            anchor = "end"
        svg_parts.append(
            f'<text x="{lx}" y="{ly}" text-anchor="{anchor}" '
            f'dominant-baseline="central" font-size="11" '
            f'font-family="Helvetica Neue, Arial" fill="#636E72">{label}</text>'
        )

    # Data polygons
    for data, color, opacity, width in [
        (avant, "#667eea", "0.1", "1.5"),
        (apres, "#00B894", "0.15", "2.5"),
    ]:
        points = []
        for i, label in enumerate(labels):
            val = data.get(label, 1)
            x, y = polar_to_xy(angles[i], val)
            points.append(f"{x},{y}")
        pts = " ".join(points)
        svg_parts.append(
            f'<polygon points="{pts}" fill="{color}" '
            f'fill-opacity="{opacity}" stroke="{color}" stroke-width="{width}"/>'
        )

    # Dots for "après"
    for i, label in enumerate(labels):
        val = apres.get(label, 1)
        x, y = polar_to_xy(angles[i], val)
        svg_parts.append(
            f'<circle cx="{x}" cy="{y}" r="3" fill="#00B894"/>'
        )

    svg_parts.append("</svg>")
    return "\n".join(svg_parts)


def load_and_validate(yaml_path: Path, schema_path: Path) -> dict:
    """Charge le YAML et valide contre le schéma JSON."""
    with open(yaml_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    with open(schema_path, "r", encoding="utf-8") as f:
        schema = json.load(f)

    try:
        validate(instance=data, schema=schema)
    except ValidationError as e:
        print(f"Erreur de validation: {e.message}", file=sys.stderr)
        print(f"Chemin: {' → '.join(str(p) for p in e.absolute_path)}", file=sys.stderr)
        sys.exit(1)

    return data


def render_html(data: dict, template_dir: Path) -> str:
    """Rend le template Jinja2 avec les données."""
    env = Environment(
        loader=FileSystemLoader(str(template_dir)),
        autoescape=True,
    )
    template = env.get_template("passeport.html.j2")

    from markupsafe import Markup

    radar_svg = Markup(generate_radar_svg(data["radar"]["avant"], data["radar"]["apres"]))

    return template.render(radar_svg=radar_svg, **data)


async def export_pdf(html_content: str, css_path: Path, output_path: Path):
    """Exporte le HTML en PDF via Playwright (Chromium headless)."""
    from playwright.async_api import async_playwright

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        # Charge le HTML avec le CSS
        await page.set_content(html_content, wait_until="networkidle")

        # Injecte le CSS (puisque le fichier local n'est pas accessible via set_content)
        css_content = css_path.read_text(encoding="utf-8")
        await page.add_style_tag(content=css_content)

        # Attend un peu que les styles soient appliqués
        await page.wait_for_timeout(500)

        await page.pdf(
            path=str(output_path),
            format="A4",
            print_background=True,
            margin={"top": "0", "right": "0", "bottom": "0", "left": "0"},
        )

        await browser.close()

    print(f"PDF généré : {output_path}")


def preflight():
    """Vérifie que toutes les dépendances sont disponibles."""
    missing = []
    for pkg in ["yaml", "jsonschema", "jinja2", "markupsafe"]:
        try:
            __import__(pkg)
        except ImportError:
            missing.append(pkg)
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        missing.append("playwright")

    if missing:
        print("Dépendances manquantes :", ", ".join(missing), file=sys.stderr)
        print("Installe-les avec :", file=sys.stderr)
        print("  pip install -r orion/generate/requirements.txt", file=sys.stderr)
        if "playwright" not in missing:
            pass
        else:
            print("  playwright install chromium", file=sys.stderr)
        sys.exit(1)

    # Vérifie que Chromium est installé pour Playwright
    import subprocess
    result = subprocess.run(
        [sys.executable, "-m", "playwright", "install", "--dry-run", "chromium"],
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        print("Chromium n'est pas installé pour Playwright.", file=sys.stderr)
        print("Installe-le avec : playwright install chromium", file=sys.stderr)
        sys.exit(1)


def main():
    import asyncio

    if len(sys.argv) < 2:
        print("Usage: python generate.py <answers.yaml> [output.pdf]")
        sys.exit(1)

    preflight()

    yaml_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2]) if len(sys.argv) > 2 else yaml_path.with_suffix(".pdf")

    script_dir = Path(__file__).parent
    schema_path = script_dir / "answers.schema.json"
    css_path = script_dir / "style.css"

    # Load & validate
    print(f"Chargement de {yaml_path}...")
    data = load_and_validate(yaml_path, schema_path)
    print("Validation OK")

    # Render HTML
    print("Rendu du template...")
    html = render_html(data, script_dir)

    # Export PDF
    print("Génération du PDF via Playwright...")
    asyncio.run(export_pdf(html, css_path, output_path))


if __name__ == "__main__":
    main()
