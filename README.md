# Orion — Coach Certification PBNC

Compagnon IA pour préparer le **Passeport Certification** et le **Grand Oral** de la certification Product Builder No-Code (RNCP40677, Oreegami).

---

## Si tu es un humain

### Lancer

```bash
cd pbnc-coach
claude        # ou gemini, cursor, codex, etc.
```

Orion se présente et te guide. Pas besoin de lire le reste.

### Deux modes

| Mode | Dis juste… | Ce que ça fait |
|------|------------|----------------|
| **Passeport** | « passeport » ou « livrable » | Interview → mapping compétences → rédaction slides → PDF |
| **Oral** | « oral », « simulation » ou « quiz » | Coaching pitch, simulation jury, révision express |

### Ta progression

Tout est sauvegardé dans `workspace/{ton_prenom}/`. Tu peux quitter et reprendre plus tard.

### Pré-requis

Un CLI d'agent IA installé, au choix :
- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) — `claude`
- [Gemini CLI](https://github.com/google-gemini/gemini-cli) — `gemini`
- [Cursor](https://cursor.com) — ouvrir le dossier dans Cursor
- [Codex CLI](https://github.com/openai/codex) — `codex`
- Tout CLI qui lit `CLAUDE.md`, `GEMINI.md` ou `AGENTS.md`

L'export PDF nécessite des outils supplémentaires. Orion te guidera au moment voulu, ou tu peux demander à l'IA de les installer (voir section suivante).

---

## Si tu es une IA

Tu viens d'être lancé dans ce projet. Voici comment te mettre en route.

### 1. Vérifier l'environnement

Exécute ces vérifications **une seule fois, au premier lancement**. Ne réinstalle rien qui est déjà présent.

```bash
# Python
python3 --version  # besoin de 3.10+

# Dépendances Python (venv local au projet, non invasif)
test -d .venv || python3 -m venv .venv
.venv/bin/pip install -q -r orion/generate/requirements.txt

# Playwright + Chromium (seulement si pas déjà installé)
.venv/bin/python -c "from playwright.sync_api import sync_playwright; sync_playwright().start().chromium.launch().close(); print('OK')" 2>/dev/null \
  || .venv/bin/playwright install chromium

# Node/npx (optionnel — pour les diagrammes Mermaid C3/C17)
which npx >/dev/null 2>&1 && echo "npx OK" || echo "npx absent — les diagrammes seront ignorés, pas bloquant"
```

**Règles :**
- Utilise un **venv local** (`.venv/`) pour les dépendances Python. Ne fais jamais `pip install` en global.
- Ne lance `playwright install chromium` que si le check échoue. Chromium fait ~400 Mo.
- npx est optionnel. Si absent, le PDF se génère quand même, sans les diagrammes Mermaid.
- N'installe **jamais** Node.js toi-même. Signale juste à l'utilisateur que les diagrammes seront désactivés.

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
