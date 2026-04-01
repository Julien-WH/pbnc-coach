# Orion — Coach Certification PBNC

Compagnon IA pour préparer le **Passeport Certification** et le **Grand Oral** de la certification Product Builder No-Code (RNCP40677, Oreegami).

## Utilisation

### Pré-requis

Un CLI d'agent IA installé :
- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) (`claude`)
- [Gemini CLI](https://github.com/google-gemini/gemini-cli) (`gemini`)
- [GitHub Copilot CLI](https://githubnext.com/projects/copilot-cli) (`gh copilot`)
- [Codex CLI](https://github.com/openai/codex) (`codex`)
- Ou tout autre CLI qui lit `CLAUDE.md`, `GEMINI.md` ou `AGENTS.md`

### Lancer

```bash
cd pbnc-coach
claude        # ou gemini, ou codex, etc.
```

C'est tout. Orion se présente et te guide.

### Deux modes

| Mode | Commande | Ce que ça fait |
|------|----------|----------------|
| **Passeport** | "passeport", "livrable" | Interview structurée → mapping compétences → rédaction diapos → PDF |
| **Oral** | "oral", "simulation", "quiz" | Coaching pitch, simulation jury, révision express vocabulaire |

### Ta progression est sauvegardée

Tout est dans `workspace/{ton_prenom}/`. Tu peux quitter et reprendre plus tard, Orion reprend là où tu en étais.

## Structure

```
pbnc-coach/
├── orion/                     # Cerveau d'Orion (source de vérité unique)
│   ├── passeport.md           # Comportement mode Passeport
│   ├── oral.md                # Comportement mode Oral
│   └── generate/              # Pipeline de génération PDF
│       ├── generate.py        # YAML → Jinja2 → Playwright → PDF
│       ├── passeport.html.j2  # Template structure
│       ├── style.css          # Style visuel
│       └── answers.schema.json
├── .claude/skills/            # Skills projet-scoped (Claude Code)
├── .cursor/skills/            # Skills projet-scoped (Cursor)
├── .gemini/commands/          # Commands (Gemini CLI)
├── CLAUDE.md                  # Point d'entrée (+ GEMINI.md, AGENTS.md, etc.)
├── knowledge/                 # Cours de formation (ne pas modifier)
│   ├── MAPPING-COMPETENCES.md # Index cours → compétences C1-C31
│   ├── PBNC-CDP-S2-Bloc1/    # Bloc 1: Concevoir (C1-C7)
│   └── PBNC-CDP-S2-Bloc2/    # Bloc 2: Conduire (C8-C16)
├── reference/                 # Documents de référence
└── workspace/                 # Un dossier par étudiant (auto-créé)
```

## FAQ

**Q: J'ai pas Claude Code, ça marche avec autre chose ?**
Oui, n'importe quel CLI qui lit les fichiers d'instructions au root du projet (Gemini, Codex, Copilot CLI).

**Q: Mes données sont stockées où ?**
Dans `workspace/{ton_prenom}/` en local sur ta machine. Rien n'est envoyé nulle part (à part au LLM pendant la conversation).

**Q: Je peux partager mon workspace ?**
Oui, mais ne partage pas ton dossier workspace avec d'autres étudiants (c'est ton travail perso).
