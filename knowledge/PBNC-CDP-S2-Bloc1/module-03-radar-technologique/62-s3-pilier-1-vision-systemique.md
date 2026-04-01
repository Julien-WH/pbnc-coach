# S3 - Les trois piliers du Solution Crafting : 1. La vision systémique

**Type :** E-learning
**Durée :** ~1h
**Vimeo :** https://vimeo.com/1131312787 + https://vimeo.com/1131327011 + https://vimeo.com/1131362858
**Statut :** ✅ Complété

## Structure de la leçon

Leçon en 3 vidéos avec quiz avancés (études de cas).

---

## Contenu

Thème : "Vision systémique : interdépendances fonctionnelles, cohérence, évolutivité, résilience"

### Quiz (11 questions)

1. D'après l'exemple de la chaîne e-commerce, quelles sont les conséquences d'un échec de l'automatisation qui met à jour l'inventaire ? (Plusieurs réponses possibles)
2. Quel est le concept clé que la vidéo recommande d'adopter pour bien gérer l'interdépendance fonctionnelle ?
3. Selon la vidéo, qu'est-ce qui fait la différence entre un système no-code fragile et un système robuste ?
4. Quels sont les trois niveaux de cohérence à maîtriser pour garantir une architecture no-code harmonieuse ? (Plusieurs réponses possibles)
5. Qu'est-ce qui est inclus dans le niveau de la 'cohérence d'expérience' ? (Plusieurs réponses possibles)
6. Quelles sont les pratiques recommandées pour assurer une bonne 'évolutivité' de l'architecture no-code ? (Plusieurs réponses possibles)
7. D'après l'exemple du changement d'outil de formulaire, qu'est-ce qui caractérise une architecture no-code évolutive par rapport à une architecture non évolutive ?
8. [Étude de cas] En cas de défaillance de l'API de paiement, quelle(s) action(s) correspondrai(en)t à une stratégie de dégradation progressive efficace ? (Plusieurs réponses possibles)
9. [Étude de cas] Pour un taux d'échec de 0,5 % sur un scénario Make synchronisant des données sensibles, quelle(s) stratégie(s) de résilience implémenter en priorité ? (Plusieurs réponses possibles)
10. [Étude de cas] Si vous modélisez un système de recommandation no-code basé sur les boucles de feedback, quels seraient les bénéfices stratégiques découlant de cette propriété émergente ?
11. [Étude de cas] Pour un système Airtable + Make + Google Drive de facturation, quelle est la propriété émergente créée par cet assemblage ?

---

## Notes techniques (complétion)

- Leçon E-learning dans iframe play/element
- 3 vidéos Vimeo + 11 questions quiz (dont études de cas avancées)
- Auto-complétion : Loop de validateAndNextOutput
- IDs :
  - Element GUID : `9b09be7b-cc61-4137-9f6a-66f5608b32be`
  - Learning ID : `Mkh5MGxXNjY0OHdCTE9yNXhiSktGZz09`


## Transcript vidéo (sous-titres auto-générés)

**Vidéo 1131312787:**

*Lorsqu'on construit une architecture, nos codes, il faut toujours garder une chose en tête. Rayon n'existe de manière isolée chaque outil, chaque automatisation, chaque base de données dépend des autres. Et si vous modifie une seule pièce de puzzle, c'est tout le système qui peut bouger. C'est ce qu'on appelle l'interdépendance fonctionnelle. La question à se poser est simple.*

*Si je change quelque chose dans l'outil a, qu'est-ce qui doit aussi changer dans l' TI b? Autrement dit, quelles sont les conséquences en cascade de ce que je fais dans une architecture? Nos codes, tout est relié. Une petite modification apparemment anodine peut déclencher une série d'effets inattendue dans le reste du système. Prenons un exemple très concret en système de ecommerce en client.*

*Passe commande automatiquement le stock doit diminuer animal de confirmation par aux clients, une facture régénérée et un fin, le système comptable et né à jour tout ça, c'est un enchaînement logique, mais surtout, c'est une interdépendance totale entre les outils fier. Un maillon de cette chaîne casse.*

*Par exemple, si l'automatisation TI met à jour, l'inventaire échoue, le reste du processus se dérègle, le stock reste faux, les confirmations partent en retard et la comptabilité devient incohérente. Une seule erreur et tout l'écosystème s'en trouve empaqueté. Comme vous pouvez le comprendre, cette dimension est essentielle pour garantir la fiabilité de votre stack.*

*Ce n'est pas juste une question de connexion technique. C'est une question de logique métier global. Chaque outil doit savoir à quel moment intervenir, quelle donnée il reçoit et qui donner l'envoi. C'est cette coordination presque chorégraphique qui fait la différence entre entre un système fragile et un système robuste.*

*Pour bien gérer l'interdépendance fonctionnelle, il faut apprendre à raisonner en chaîne d'effets avant de modifier un champ en scénario ou en paramètre. Posez vous toujours la question qu'est-ce que cette modification va entraîner ailleurs? C'est un réflexe à adopter parce que dans le no code, tout est vivant.*

*Changer une donnée ici, c'est influencer une automatisation là qui elle-même va modifier un rapport ou déclencher une action dans un autre outil. C'est une mécanique d'une grande précision.*
**Vidéo 1131327011:**

*Règle d'or. Tous vos outils doivent parler le même langage parce que si chaque outil fait les choses à sa manière, vous allez vite vous retrouver dans un chaos complet. Imaginez un instant votre maison dans les cuisines, vous avez des prises européennes dans la chambre des prix américaines et dans le salon des prises britanniques.*

*Résultat pour brancher en simple appareil, il vous faut trois adaptateurs différents, un cauchemar arna eh bien, c'est exactement ce qui fasse quand vos outils n'ont aucune cohérence architecturale.*

*Prenons un exemple très courant les dates vous collecter les dates de naissance, mais chaque outil, les steppes différemment dans RT, bol jour moins année dans Google sheet, mois, jour année et dans votre formulaire année, mois jour. Et là, c'est le drame. Quand vous transférez automatiquement les données, le janvier devient le er mars catastrophe garantie. La solution est les simple dès le départ.*

*Choisissez un standard unique. Par exemple, ce format i o configurer tous vos outils de la même façon. Résultat zéro confusion, zéro conversion, zéro bu pour garantir une architecture harmonieuse. Il y a trois niveaux de cohérence à maîtriser. Niveau un, la cohérence des données, c'est le socle.*

*Toutes vos données doivent parler le même langage, même format pour les dates, même capitalisation et surtout les mêmes listes de choix. Une seule version, pas deux. Cette cohérence évite les erreurs et rend les automatisation beaucoup plus fiable. Niveau deux la cohérence de sécurité.*

*Si un utilisateur a accès à des données dans l' a, doit-il automatiquement et avoir accès dans l tibe et inversement, vos sont-ils cohérents dans un outil à l'autre admis utilisateur à inviter? Ces statuts doivent avoir le même sens partout.*

*C'est ce qui garantit en contrôle clair et homogène ni vos trois la cohérence d'expérience parce qu'un système cohérent, c'est aussi un système agréable à utiliser. Utiliser les mêmes mots partout, par exemple le rendez-vous ou r d ou appointment.*

*Choisissez en termes unique et gardez le et pensez à la cohérence visuelle si annulée et toujours un rouge dans un outil, garder ce code couleur dans les autres, votre cerveau lui vous dira merci. Faites le test. Maintenant, prenez deux de vos outils actuels. Les dates sont dès le même format. Oui, parfait, non.*

*Alors notez le, c'est une petite incohérence aujourd'hui qui peut devenir un vrai problème de nom.*
**Vidéo 1131362858:**

*Question centrale. Votre système peut il s'adapter aux changements futurs sans tout casser, parce que dans le code comme dans l'architecture d'une maison, tout est une question de conception. Prenons un exemple simple. Vous voulez remplacer votre outil de formulaire dans une architecture non évolutive. Vous avez quelque chose comme type forme script personnalisé. R est belle. Le problème.*

*Toute la logique métier est dans le script. Alors si vous changez typeform pour Google forms, vous devez réécrire tout le code des heures, voir des jours de travail. Maintenant, imaginons une architecture évolutive. Vous avez formulaire au choix web standard make ici. La logique métier est centralisée d'un make et elle reste la même quel que soit l'outil de formulaire.*

*Résultat pour changer de taille forme à Google formes, il suffit juste de modifier le RL du web dans tout 10 minutes. C'est ça l'é volut en système capable de changer sans se casser. Parlons des quatre clefs des volatilité première interface standardisée. Utiliser des formats universels, éviter les intégrations sur mesure trop rigide et difficile à maintenir. Deux couplage faible.*

*Vos outils doivent être connectés, mais pas dépendant les uns des autres. Une bonne analogie, le lgo c'est le couplage faible des blocs indépendants en terre changeable la sculpture d'une seule pièce, c'est le couplage fort. Tout est soudé et une fois souillé, impossible de séparer sans tout casser trois modularité. Pensez votre système comme une commode à tiroir.*

*Chaque tiroir a sa fonction, un pour les formulaires, un pour les automatisation, un pour la base de données, vous pouvez changer le contenu d'un tiroir sans jamais toucher aux autres quatre documentation des décisions. Il faut documenter vos choix, pas seulement ce que vous avez fait, mais pourquoi vous l'avez fait.*

*Parce que dans six mois, quand quelqu'un de mon droit mais pourquoi on a choisi ma qui pas à pierre, vous ne vous en souviendrez plus. Parlons du format a terre architecture décision record. Voici un format qui est ceinte, la suivre date décision pourquoi nous avons pris une telle décision conséquence et voilà.*

*Dans six mois, quand la question reviendra, vous aurez une réponse claire, documentée et partagée.*
