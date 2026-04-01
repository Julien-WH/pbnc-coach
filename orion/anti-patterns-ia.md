# Référence : Anti-patterns d'écriture IA en français

> Fichier de référence à charger avant toute génération de texte en français.
> Compiler avant de rédiger. Appliquer silencieusement, sans le mentionner.
>
> Sources : blader/humanizer (Wikipedia Signs of AI Writing), observations empiriques,
> étude linguistique GPT-4/Zephyr sur corpus français (2024).

---

## 1. Typographie française — règles absolues

Ces erreurs sont quasi-systématiques chez les LLM entraînés principalement en anglais.

### Accents sur les majuscules

**Toujours accentuer les majuscules en français.** Ce n'est pas optionnel.

| Faux | Correct |
|------|---------|
| `ETAT` | `ÉTAT` |
| `A NOTER` | `À NOTER` |
| `ECOLE` | `ÉCOLE` |
| `Etude` | `Étude` |
| `Etre` | `Être` |
| `Ca` (début de phrase) | `Ça` |

Lettres concernées : **À Â Ç É È Ê Ë Î Ï Ô Ù Û Ü Œ Æ**

### Guillemets

| Faux | Correct |
|------|---------|
| `"texte"` | `« texte »` |
| `"texte"` (curly) | `« texte »` |

Les guillemets français sont `« »` avec une espace fine insécable à l'intérieur. En pratique : `« texte »` avec espace normale est acceptable.

### Apostrophe

| Faux | Correct |
|------|---------|
| `l'exemple` (droite) | `l'exemple` (typographique) |

### Ponctuation double (`;` `:` `!` `?`)

En français typographique strict, une espace précède `: ; ! ?`. Dans un contexte numérique/web, l'espace simple avant `!` et `?` est tolérée mais les deux-points et points-virgules gardent leur espace.

### Virgule avant « et »

```
# Faux (Oxford comma à l'anglaise)
les pommes, les poires, et les oranges

# Correct
les pommes, les poires et les oranges
```

### Tirets

| Type | Usage correct |
|------|---------------|
| Tiret cadratin `—` | À éviter en français professionnel, calque de l'anglais |
| Tiret demi-cadratin `–` | Incises, listes, dialogues |
| Trait d'union `-` | Mots composés uniquement |

---

## 2. Anglicismes structurels

Biais d'entraînement : 16 % des erreurs linguistiques LLM en français ont une origine anglaise (étude 2024).

### Calques lexicaux à bannir

| Faux (calque) | Correct |
|---------------|---------|
| Adresser un problème | Traiter / résoudre un problème |
| Faire du sens | Avoir du sens |
| Opportunités | Possibilités / occasions (selon contexte) |
| Momentum | Élan / dynamique |
| Délivrer (des résultats) | Produire / fournir |
| Implémenter | Mettre en œuvre / déployer |
| Prioriser | Hiérarchiser / classer par priorité |
| Impacter | Avoir un impact sur / affecter |
| Challengé | Remis en question / défié |
| Pitcher | Présenter / soumettre |

### Title Case → Sentence case

```
# Faux (anglais)
## Concevoir Des Solutions No Code En Fonction Des Besoins Utilisateurs

# Correct (français)
## Concevoir des solutions no code en fonction des besoins utilisateurs
```

Seul le premier mot et les noms propres prennent une majuscule.

---

## 3. Vocabulaire IA générique

Mots statistiquement sur-représentés dans les textes LLM. À remplacer systématiquement.

### Adjectifs creux

`crucial` · `essentiel` · `fondamental` · `indispensable` · `robuste` · `significatif` · `substantiel` · `pertinent` · `innovant` · `disruptif` · `passionnant` · `incontournable`

**Règle :** si l'adjectif peut être retiré sans perte de sens, le retirer.

### Locutions de remplissage

`il convient de noter que` · `il est important de souligner` · `il est essentiel de comprendre` · `force est de constater` · `dans ce cadre` · `en effet` (en début de phrase) · `ainsi` (systématique) · `notamment` (en excès)

**Règle :** supprimer ou reformuler directement.

### Formules d'introduction IA

```
# À bannir
« Dans un monde de plus en plus connecté... »
« À l'ère du numérique... »
« Dans le paysage actuel... »
« Dans un contexte de transformation digitale... »
« Il est crucial de noter que... »
« Plongeons dans... »
```

Commencer par le sujet directement.

### Conclusions interchangeables

```
# À bannir
« L'avenir s'annonce plein d'opportunités. »
« Il ne nous reste qu'à embrasser le changement. »
« Les défis sont nombreux mais les opportunités le sont tout autant. »
« En conclusion, nous pouvons affirmer que... »
```

Conclure avec un fait précis ou une prise de position réelle.

---

## 4. Patterns stylistiques (source : blader/humanizer)

### Inflation de la signification

```
# Faux
« marquant un tournant décisif dans l'évolution de... »
« témoignant du potentiel transformateur de... »

# Correct
Fait précis, date, chiffre.
```

### Faux parallélismes négatifs

```
# Faux
« Ce n'est pas juste X, c'est Y. »
« Non seulement X, mais également Y. »

# Correct
Affirmer directement Y.
```

### Règle de trois artificielle

```
# Faux
« innovation, inspiration et impact »
« clarté, cohérence et concision »

# Correct
Utiliser le nombre d'éléments naturellement nécessaires.
```

### Cyclage de synonymes

```
# Faux
« le protagoniste... le personnage principal... la figure centrale... le héros »

# Correct
Répéter le même mot quand c'est le plus clair.
```

### Analyse en « -ing » superficielle

```
# Faux
« symbolisant... reflétant... illustrant... soulignant... »

# Correct
Supprimer ou développer avec des sources réelles.
```

### Attributions vagues

```
# Faux
« Les experts estiment que... »
« Selon de nombreuses études... »
« Il est généralement admis que... »

# Correct
« Selon une étude de l'INRIA (2023)... » ou supprimer.
```

---

## 5. Structure et rythme

### Paragraphes uniformes

Les LLM produisent des paragraphes de taille quasi identique avec des transitions systématiques (« Premièrement... Deuxièmement... Enfin... »). Varier la longueur des phrases et des paragraphes.

### Listes abusives

Tout structuré en 3 ou 5 points, même quand la prose est plus naturelle. Si une idée s'exprime en une phrase, ne pas en faire une liste.

### Gras abusif

```
# Faux
« Les **OKR**, les **KPI** et les **roadmaps** sont des outils **essentiels**. »

# Correct
« Les OKR, KPI et roadmaps sont des outils courants. »
```

Le gras est pour les termes qu'un lecteur qui scanne doit absolument voir. Pas pour décorer.

### Titres en ligne avant liste

```
# Faux
**Performance :** La performance s'est améliorée...
**Qualité :** La qualité a progressé...

# Correct
Convertir en prose ou en vrai tableau.
```

---

## 6. Ton et posture

### Neutralité excessive

Les LLM nuancent en permanence pour ne froisser personne, au point de ne rien affirmer. Un texte professionnel peut et doit avoir une position.

```
# Faux
« Cette approche pourrait potentiellement présenter certains avantages
dans certains contextes, bien que des limites soient également envisageables. »

# Correct
« Cette approche fonctionne bien pour X. Elle est inadaptée à Y. »
```

### Enthousiasme vide

```
# Faux
« une solution innovante et passionnante qui révolutionne le secteur »

# Correct
Fait précis sur ce que ça change concrètement.
```

### Artefacts chatbot

```
# À supprimer entièrement
« Bien sûr ! »
« Excellente question ! »
« N'hésitez pas à me contacter si... »
« J'espère que cette réponse vous a été utile. »
« Je reste disponible pour... »
```

### Avertissements de coupure

```
# À supprimer
« Bien que les informations disponibles soient limitées... »
« À noter que mes données s'arrêtent à... »
```

---

## 7. Checklist avant livraison

- [ ] Toutes les majuscules sont accentuées (É À Ç Œ…)
- [ ] Guillemets français `« »` utilisés
- [ ] Pas de virgule avant « et » (sauf ambiguïté réelle)
- [ ] Titres en sentence case (pas Title Case)
- [ ] Pas de tirets cadratins `—`
- [ ] Aucun mot de la liste vocabulaire IA (crucial, essentiel, etc.)
- [ ] Aucune formule d'introduction générique
- [ ] Aucun artefact chatbot
- [ ] Les listes ne remplacent pas la prose quand c'est inutile
- [ ] Gras utilisé avec parcimonie
- [ ] Pas de calques anglais (adresser, délivrer, implémenter…)
- [ ] La conclusion dit quelque chose de précis
