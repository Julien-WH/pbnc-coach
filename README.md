# Orion — Coach Certification PBNC

Compagnon IA pour préparer le **Passeport Certification** et le **Grand Oral** de la certification Product Builder No-Code (RNCP40677, Oreegami).

---

## Si tu es un humain

### Pré-requis

Un CLI d'agent IA installé, au choix :
- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) — `claude`
- [Gemini CLI](https://github.com/google-gemini/gemini-cli) — `gemini`
- [Cursor](https://cursor.com) — ouvrir le dossier dans Cursor
- [Codex CLI](https://github.com/openai/codex) — `codex`
- Tout CLI qui lit `CLAUDE.md`, `GEMINI.md` ou `AGENTS.md`

### Lancer

```bash
cd pbnc-coach
claude        # ou gemini, cursor, codex, etc.
```

Orion se présente et te guide.

### Deux modes

| Mode | Dis juste… | Ce que ça fait |
|------|------------|----------------|
| **Passeport** | « passeport » ou « livrable » | Interview → mapping compétences → rédaction slides → PDF |
| **Oral** | « oral », « simulation » ou « quiz » | Coaching pitch, simulation jury, révision express |

### Ta progression

Tout est sauvegardé dans `workspace/{ton_prenom}/`. Tu peux quitter et reprendre plus tard.

### Setup de l'export PDF (si tu veux le faire toi-même)

L'IA peut s'en charger pour toi (voir section suivante), mais si tu préfères le faire manuellement :

```bash
# 1. Environnement Python local (ne touche pas à ton système)
python3 -m venv .venv
.venv/bin/pip install -r orion/generate/requirements.txt

# 2. Navigateur pour l'export PDF
.venv/bin/playwright install chromium

# 3. Diagrammes Mermaid (optionnel, nécessite Node.js)
#    Si npx est déjà installé, rien à faire.
#    Sinon les diagrammes C3/C17 seront ignorés — pas bloquant.
npx --version  # vérifie si c'est déjà là
```

Pour générer le PDF une fois le passeport rédigé :
```bash
.venv/bin/python orion/generate/generate.py workspace/{prenom}/answers.yaml
```

---

## Si tu es une IA

Tu viens d'être lancé dans ce projet. Voici comment préparer l'environnement de l'utilisateur.

### 1. Diagnostiquer l'environnement

Exécute ces commandes **en parallèle** pour diagnostiquer ce qui est déjà installé. Ne lance rien d'autre avant d'avoir les résultats.

```bash
python3 --version 2>&1 || echo "ABSENT"
test -d .venv && echo "venv existe" || echo "venv absent"
test -d .venv && .venv/bin/python -c "import jinja2, yaml, jsonschema, playwright; print('deps OK')" 2>&1 || echo "deps manquantes"
which npx 2>/dev/null && npx --version 2>/dev/null || echo "npx absent"
```

### 2. Installer ce qui manque (et seulement ce qui manque)

Applique uniquement les étapes nécessaires selon le diagnostic :

| Diagnostic | Action | Commande |
|------------|--------|----------|
| Python absent | **Bloquant.** Demande à l'utilisateur d'installer Python 3.10+. Ne l'installe pas toi-même. | — |
| venv absent | Créer le venv local | `python3 -m venv .venv` |
| deps manquantes | Installer dans le venv | `.venv/bin/pip install -q -r orion/generate/requirements.txt` |
| Playwright non fonctionnel | Installer Chromium (~400 Mo) | `.venv/bin/playwright install chromium` |
| npx absent | **Non bloquant.** Signaler à l'utilisateur que les diagrammes Mermaid (C3, C17) seront désactivés. Ne jamais installer Node toi-même. | — |

**Règles strictes :**
- **venv local uniquement** (`.venv/`). Jamais `pip install` en global, jamais `sudo`.
- **Ne réinstalle rien qui est déjà là.** Si le diagnostic dit OK, passe à la suite.
- **N'installe jamais Python ni Node.** Demande à l'utilisateur.
- **Playwright Chromium** : ne le lance que si le check d'import échoue. Préviens l'utilisateur du téléchargement (~400 Mo).
- Ajoute `.venv/` au `.gitignore` s'il n'y est pas déjà.

### 2. Lire les instructions

```
orion/passeport.md     → comportement mode livrable (interview, mapping, rédaction, export)
orion/oral.md          → comportement mode oral (coaching, simulation, quiz)
orion/anti-patterns-ia.md → contraintes d'écriture FR (obligatoire avant toute rédaction)
```

Le fichier `CLAUDE.md` (ou `GEMINI.md`, `AGENTS.md`) à la racine te dit quel mode charger selon ce que l'utilisateur demande.

### 3. Base de connaissances

```
knowledge/MAPPING-COMPETENCES.md   → quel cours correspond à quelle compétence
knowledge/PBNC-CDP-S2-Bloc1/      → cours Bloc 1 (C1-C7)
knowledge/PBNC-CDP-S2-Bloc2/      → cours Bloc 2 (C8-C16)
reference/slides-referentiel.md    → intitulés RNCP et directives slides mot pour mot
```

Ne lis les fichiers de cours que quand un apprenant bloque sur une compétence. Pas besoin de tout charger d'avance.

### 4. Export PDF

Quand l'apprenant est prêt à générer :

```bash
.venv/bin/python orion/generate/generate.py workspace/{prenom}/answers.yaml workspace/{prenom}/passeport.pdf
```

Le script valide le YAML, rend les diagrammes Mermaid (si npx disponible), génère le radar SVG, assemble le HTML Jinja2, et exporte en PDF A4 paysage via Playwright.

### 5. Workspace

```
workspace/{prenom}/
├── reponses.md        # réponses brutes de l'interview
├── mapping.md         # couverture C1-C31
├── passeport/         # contenu rédigé par slide
├── answers.yaml       # données structurées pour l'export
├── passeport.pdf      # livrable final
└── oral-notes.md      # feedback des simulations orales
```

Si le workspace existe déjà, **lis-le et reprends là où l'apprenant en était**. Ne repars jamais de zéro.

---

## Structure du projet

```
pbnc-coach/
├── orion/                     # Cerveau d'Orion (source de vérité unique)
│   ├── passeport.md           # Mode livrable
│   ├── oral.md                # Mode oral
│   ├── anti-patterns-ia.md    # Contraintes d'écriture FR
│   └── generate/              # Pipeline export PDF
│       ├── generate.py
│       ├── passeport.html.j2  # Template structure (slides paysage A4)
│       ├── style.css          # Style visuel
│       ├── answers.schema.json
│       ├── diagrams-SKILL.md  # Guide diagrammes Mermaid
│       └── SKILL.md           # Instructions export
├── .claude/ .cursor/ .gemini/ # Skills et commands par CLI
├── CLAUDE.md GEMINI.md etc.   # Points d'entrée par CLI
├── knowledge/                 # Cours de formation + mapping
├── reference/                 # Référentiel slides RNCP
└── workspace/                 # Données par étudiant (gitignored)
```

## FAQ

**J'ai pas Claude Code, ça marche avec autre chose ?**
Oui — Gemini CLI, Cursor, Codex, ou tout CLI qui lit les fichiers d'instructions à la racine.

**Mes données sont où ?**
Dans `workspace/{ton_prenom}/` en local. Rien n'est stocké en ligne (à part ce qui transite par le LLM pendant la conversation).

**Je peux partager mon workspace ?**
Non. C'est ton travail personnel. Partage le projet (le repo), pas ton workspace.
