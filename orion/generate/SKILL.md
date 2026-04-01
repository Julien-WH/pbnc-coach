# Génération PDF du Passeport Certification

## Quand utiliser

Appelé par Orion (mode passeport) quand toutes les compétences sont couvertes et le contenu validé par l'apprenant. L'apprenant peut aussi demander directement : "génère le PDF", "exporte", "on finalise".

## Pré-requis

```bash
pip install -r orion/generate/requirements.txt
playwright install chromium
```

Si les dépendances ne sont pas installées, propose à l'apprenant de les installer et guide-le.

## Workflow

### 1. Construire le answers.yaml

À partir du contenu de `workspace/{prenom}/` (reponses.md, mapping.md, passeport/*.md), assemble un fichier `workspace/{prenom}/answers.yaml` conforme au schéma `orion/generate/answers.schema.json`.

Structure attendue :

```yaml
candidat:
  prenom: "..."
  nom: "..."
  date_naissance: "JJ/MM/AAAA"
  lieu_naissance: "..."

parcours:
  scolaire: "..."
  professionnel: "..."
  motivations: "..."
  projet_pro: "..."

radar:
  avant:
    C1: 2
    C2: 1
    # ... C1 à C31, valeurs 1-5
  apres:
    C1: 4
    C2: 3
    # ... C1 à C31, valeurs 1-5

activites:
  - titre: "..."
    contexte: "..."
    objectifs: "..."
    methodes: "..."
    ressources: "..."
    equipe: "..."
    deroulement: "..."
    difficultes: "..."
    reflexion: "..."
    axes_amelioration: "..."
    competences_couvertes: ["C1", "C3", "C6"]
  # 3 activités au total

competences:
  C1:
    titre: "Déterminer les besoins utilisateurs"
    exemple: "..."
    outils: "..."
    reflexion: "..."
  # ... C1 à C31

conclusion: "..."

ouverture:
  projet_pro: "..."
  poste_vise: "..."
  perspectives: "..."
```

### 2. Valider

Avant de générer, vérifie que le YAML est conforme :
```bash
python -c "
import yaml, json
from jsonschema import validate
data = yaml.safe_load(open('workspace/{prenom}/answers.yaml'))
schema = json.load(open('orion/generate/answers.schema.json'))
validate(data, schema)
print('OK')
"
```

### 3. Générer

```bash
python orion/generate/generate.py workspace/{prenom}/answers.yaml workspace/{prenom}/passeport.pdf
```

### 4. Annoncer

Affiche : "Ton Passeport est prêt ! Tu peux l'ouvrir avec `open workspace/{prenom}/passeport.pdf`"

## Fichiers

| Fichier | Rôle | Qui le modifie |
|---------|------|----------------|
| `answers.schema.json` | Valide la structure du YAML | Personne (sauf évolution du référentiel) |
| `passeport.html.j2` | Structure HTML du document | Un agent peut modifier la structure |
| `style.css` | Tout le visuel (couleurs, typo, layout) | Un agent peut modifier le style |
| `generate.py` | Orchestrateur (YAML → HTML → PDF) | Un agent peut améliorer le script |
| `requirements.txt` | Dépendances Python | Maintenu à jour avec le script |

## Séparation template / style

Le template Jinja2 et le CSS sont **intentionnellement séparés** pour qu'un agent puisse modifier l'apparence (style.css) sans toucher à la structure (passeport.html.j2) et vice-versa.
