# Hiérarchie des sources

Ce projet utilise plusieurs sources d'information. En cas de contradiction, la source la plus haute prévaut.

## Niveau 1 — Fiche officielle France Compétences RNCP40677

Source : https://www.francecompetences.fr/recherche/RNCP/40677
Statut : active au 1er avril 2026, échéance 23 mai 2028.

C'est le référentiel opposable. Il définit les blocs de compétences, les modalités d'évaluation par bloc, les types d'emplois accessibles et les voies d'accès. Si la fiche RNCP dit quelque chose que le kick-off ne dit pas, la fiche RNCP fait foi.

Fichier local : `reference/rncp40677-officiel.md`

## Niveau 2 — PDF Kick-Off Grand Oral Oreegami

Source : `Kick_Off_Grand_Oral_PBNC.pdf` (distribué par Oreegami aux apprenants)

C'est le document opérationnel qui détaille le format du passeport, le déroulé de la soutenance, la grille d'évaluation et les directives par slide. Le texte des directives et questions-guides est copié mot pour mot dans `reference/slides-referentiel.md`.

Fichier local : `reference/slides-referentiel.md`

**Attention :** Le kick-off omet C15 (Ishikawa/analyse causale). C15 existe dans la fiche RNCP et dans l'infographie Bloc 2 du kick-off lui-même, mais n'a pas de slide dédiée dans le PDF. Le projet reconstruit C15 à partir du RNCP et des cours — c'est signalé explicitement dans le référentiel des slides.

## Niveau 3 — Cours de formation e-learning (Teachup)

Source : plateforme Teachup, extraits en markdown dans `knowledge/`

Couvrent C1-C16 (Blocs 1-2). Les blocs 3-4 (C17-C31) ne sont pas couverts par le e-learning et s'appuient sur l'expérience terrain et les ateliers.

Fichier local : `knowledge/` + `knowledge/MAPPING-COMPETENCES.md`

## Niveau 4 — Enrichissements internes

Tout ce qui est produit par le projet mais qui ne vient pas directement des sources ci-dessus :
- Reconstruction de C15 (intitulé et questions-guides)
- Guide anti-patterns IA (`orion/anti-patterns-ia.md`)
- Guide diagrammes (`orion/generate/diagrams-SKILL.md`)
- Exemples et templates dans le YAML schema

Ces enrichissements sont toujours signalés comme tels et ne doivent jamais être présentés comme du contenu officiel.
