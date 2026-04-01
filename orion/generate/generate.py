#!/usr/bin/env python3
"""
Passeport Certification PBNC — PDF Generator
Charge answers.yaml → valide → rend Mermaid → rend Jinja2 → exporte PDF via Playwright.
"""

import json
import math
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml
from jsonschema import validate, ValidationError
from jinja2 import Environment, FileSystemLoader
from markupsafe import Markup


# ──────────────────────────── Radar SVG ────────────────────────────


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

    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {size} {size}">']

    # Grid
    for level in range(1, 6):
        r = (level / 5) * max_r
        svg.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="#DFE6E9" stroke-width="0.5"/>')
    for angle in angles:
        x, y = polar_to_xy(angle, 5)
        svg.append(f'<line x1="{cx}" y1="{cy}" x2="{x}" y2="{y}" stroke="#DFE6E9" stroke-width="0.5"/>')

    # Labels
    for i, (angle, label) in enumerate(zip(angles, labels)):
        lx, ly = polar_to_xy(angle, 5.6)
        anchor = "middle"
        if math.cos(angle) > 0.3:
            anchor = "start"
        elif math.cos(angle) < -0.3:
            anchor = "end"
        svg.append(
            f'<text x="{lx}" y="{ly}" text-anchor="{anchor}" '
            f'dominant-baseline="central" font-size="11" '
            f'font-family="Helvetica Neue, Arial" fill="#636E72">{label}</text>'
        )

    # Polygons
    for data, color, opacity, width in [
        (avant, "#667eea", "0.1", "1.5"),
        (apres, "#00B894", "0.15", "2.5"),
    ]:
        pts = " ".join(
            f"{polar_to_xy(angles[i], data.get(l, 1))[0]},{polar_to_xy(angles[i], data.get(l, 1))[1]}"
            for i, l in enumerate(labels)
        )
        svg.append(f'<polygon points="{pts}" fill="{color}" fill-opacity="{opacity}" stroke="{color}" stroke-width="{width}"/>')

    # Dots
    for i, label in enumerate(labels):
        x, y = polar_to_xy(angles[i], apres.get(label, 1))
        svg.append(f'<circle cx="{x}" cy="{y}" r="3" fill="#00B894"/>')

    svg.append("</svg>")
    return "\n".join(svg)


# ──────────────────────────── Mermaid → SVG ────────────────────────────


def render_mermaid_diagrams(competences: dict) -> dict[str, str]:
    """Rend les diagrammes Mermaid en SVG via npx mmdc. Retourne {Cx: svg_string}."""
    diagrams = {}

    for key, comp in competences.items():
        mermaid_code = comp.get("diagram_mermaid")
        if not mermaid_code:
            continue

        with tempfile.NamedTemporaryFile(mode="w", suffix=".mmd", delete=False) as f_in:
            f_in.write(mermaid_code)
            mmd_path = Path(f_in.name)

        svg_path = mmd_path.with_suffix(".svg")

        try:
            result = subprocess.run(
                [
                    "npx", "-y", "@mermaid-js/mermaid-cli",
                    "-i", str(mmd_path),
                    "-o", str(svg_path),
                    "-t", "neutral",
                    "--backgroundColor", "transparent",
                    "-q",
                ],
                capture_output=True,
                text=True,
                timeout=30,
            )

            if result.returncode != 0:
                print(f"  Attention: Mermaid a échoué pour {key}: {result.stderr[:200]}", file=sys.stderr)
                continue

            if svg_path.exists():
                svg_content = svg_path.read_text(encoding="utf-8")
                # Nettoyer les en-têtes XML si présents
                if "<svg" in svg_content:
                    svg_content = svg_content[svg_content.index("<svg"):]
                diagrams[key] = svg_content
                print(f"  {key} : diagramme rendu")
            else:
                print(f"  Attention: pas de SVG généré pour {key}", file=sys.stderr)

        finally:
            mmd_path.unlink(missing_ok=True)
            svg_path.unlink(missing_ok=True)

    return diagrams


# ──────────────────────────── Validation ────────────────────────────


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


# ──────────────────────────── Rendu HTML ────────────────────────────


def render_html(data: dict, template_dir: Path) -> str:
    """Rend le template Jinja2 avec les données + diagrammes."""
    env = Environment(
        loader=FileSystemLoader(str(template_dir)),
        autoescape=True,
    )
    template = env.get_template("passeport.html.j2")

    # Radar
    radar_svg = Markup(generate_radar_svg(data["radar"]["avant"], data["radar"]["apres"]))

    # Diagrammes Mermaid
    print("Rendu des diagrammes Mermaid...")
    raw_diagrams = render_mermaid_diagrams(data["competences"])
    diagrams_svg = {k: Markup(v) for k, v in raw_diagrams.items()}

    return template.render(radar_svg=radar_svg, diagrams_svg=diagrams_svg, **data)


# ──────────────────────────── Export PDF ────────────────────────────


async def export_pdf(html_content: str, css_path: Path, output_path: Path):
    """Exporte le HTML en PDF paysage A4 via Playwright."""
    from playwright.async_api import async_playwright

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        await page.set_content(html_content, wait_until="networkidle")

        css_content = css_path.read_text(encoding="utf-8")
        await page.add_style_tag(content=css_content)
        await page.wait_for_timeout(500)

        await page.pdf(
            path=str(output_path),
            landscape=True,
            format="A4",
            print_background=True,
            margin={"top": "0", "right": "0", "bottom": "0", "left": "0"},
        )

        await browser.close()

    print(f"PDF généré : {output_path}")


# ──────────────────────────── Preflight ────────────────────────────


def preflight():
    """Vérifie que toutes les dépendances sont disponibles."""
    missing = []
    for pkg in ["yaml", "jsonschema", "jinja2", "markupsafe"]:
        try:
            __import__(pkg)
        except ImportError:
            missing.append(pkg)
    try:
        from playwright.sync_api import sync_playwright  # noqa: F401
    except ImportError:
        missing.append("playwright")

    if missing:
        print("Dépendances manquantes :", ", ".join(missing), file=sys.stderr)
        print("  pip install -r orion/generate/requirements.txt", file=sys.stderr)
        if "playwright" in missing:
            print("  playwright install chromium", file=sys.stderr)
        sys.exit(1)

    # Vérifie npx (pour Mermaid)
    result = subprocess.run(["which", "npx"], capture_output=True)
    if result.returncode != 0:
        print("npx non trouvé. Installe Node.js pour le rendu des diagrammes Mermaid.", file=sys.stderr)
        print("Les diagrammes seront ignorés.", file=sys.stderr)


# ──────────────────────────── Main ────────────────────────────


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

    print(f"Chargement de {yaml_path}...")
    data = load_and_validate(yaml_path, schema_path)
    print("Validation OK")

    print("Rendu du template...")
    html = render_html(data, script_dir)

    print("Génération du PDF paysage A4 via Playwright...")
    asyncio.run(export_pdf(html, css_path, output_path))


if __name__ == "__main__":
    main()
