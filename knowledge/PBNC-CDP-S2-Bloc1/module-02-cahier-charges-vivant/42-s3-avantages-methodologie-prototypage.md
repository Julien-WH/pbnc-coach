# S3 - Avantages et méthodologie du prototypage précoce

**Type :** E-learning
**Durée :** ~30 min
**Vimeo :** https://vimeo.com/1124769068 + https://vimeo.com/1124775176 + https://vimeo.com/1124783156
**Statut :** ✅ Complété

## Structure de la leçon

Leçon en 3 vidéos avec quiz intercalés + textes libres.

---

## Contenu

Thème : "Avantages du prototypage précoce, niveaux de fidélité, cycles d'itération"

### Quiz (6 questions)

1. Pourquoi les besoins cachés des utilisateurs apparaissent-ils souvent seulement après avoir testé un prototype ?
2. Pourquoi le prototypage réduit-il fortement les risques de développement ?
3. Quel est l'objectif principal du prototypage basse fidélité ?
4. Qu'apporte le prototypage haute fidélité par rapport aux autres niveaux ?
5. Quel est le principe d'un cycle d'itération en prototypage ?
6. Pourquoi vaut-il mieux plusieurs prototypes imparfaits qu'un seul parfait ?

---

## Notes techniques (complétion)

- Leçon E-learning dans iframe play/element
- Contient 3 OutputForInputMedia (vidéos) + 6 OutputForQuestion + OutputForInputText
- Auto-complétion : Loop de validateAndNextOutput (22 outputs)
- IDs :
  - Element GUID : `caa9db13-1830-496f-82b7-43d9d3dff4bc`
  - Learning ID : `aXBLQ1JLVFdBM3JOZHBvM1lCQ3gvZz09`


## Transcript vidéo (sous-titres auto-générés)

**Vidéo 1124769068:**

*Souvent, les utilisateurs découvrent leurs vrais besoins seulement quand ils manipulent une solution concrète. Prenons un exemple simple, une application de planning d'équipe. Au départ, lors des interviews, tout le monde disait nous avons juste besoin d'un calendrier partagé.*

*On crée donc un premier prototype pré basique avec des créneaux, des participants, rien de plus, mais lors du test, les retours fusent, c'est bien, mais est ce qu'on pourrait voir la charge de travail de chacun.*

*Et si on avait un aperçu des compétences disponibles selon les créneaux, il faudrait aussi pouvoir proposer des alternatives quand quelqu'un n'est pas libre, ce qui n'était qu'un simple calendrier s'est transformé en véritable outil de gestion de ressources avec un algorithme d'optimisation. Autrement dit, le besoin réel n'apparaît que quand l'utilisateur se confronte au concret.*

*Un autre révélateur puissant c'est le test dans le contexte réel. Une application de maintenance industrielle, par exemple, fonctionne parfaitement laboratoire. La tablette répond bien, la navigation est fuite. Tout semble l'idéal. Mais dès qu'on l'atteste sur le terrain, la réalité rattrape le projet avec des mains sales ou comptés.*

*Les boutons deviennent impossible à cliquer dans le bruit ambiant. Le feedback son nord ne suffit plus en plein soleil. Les crome manquent de contraste avec les vibrations des machines. Tapées du texte est compliqué et en situation d'urgence, le workflow est tout simplement trop long. Résultat l'application doit évoluer.*

*Il faut des interfaces adaptées aux gonds, des feedback visuels renforcés, un mode plein soleil, la saisie vocale et un workflow simplifié pour les quatre critiques, les utilisateurs, enfin, s'approprient toujours les outils de manière créative, parfois bien au delà de ce qui était prévu. Un outil de gestion de projet conçu poursuivre les tâches de manière linéaire et vite détourné.*

*Les commentaires deviennent un chat informel. Certains traits de fausse tâches, juste pour se souvenir d'idée, d'autres manipulent l'état pour prioriser visuellement. Et le partage d'écran sert à organiser des réunions improviss face à ces usages inattendus, le produit s'adapte. On intègre un vrai chat, un système de notes, une priorisation visuelle et même un mode de présentation.*

*Autrement dit, ce sont les détournements qui révèlent les vraies attentes. Corriger un défaut n'a pas le même coup selon le moment où l'on le découvre en phase prototype, changer une maquette prend quelques heures. Une fois que le code est écrit, c'est déjà 10 fois plus cher en face de tests 100 fois plus en production 1000 fois plus et Une fois le produit adopté, la facture peut être décuplée.*

*Prenons un site ecommerce bit en face prototype. L'équipe a réalisé que le work de validation des commandes était bien trop complexe pour les acheteurs occasionnels. La correction a demandé deux jours de redesign.*

*Si ce problème avait été découvert après le développement, cela aurait coûté trois semaines de refactoring plus une semaine de test et un accompagnement au changement pour les utilisateurs. Ici, une semaine investie dans le prototypage a permis d'éviter quatre semaines de perte.*

*Chaque fonctionnalité repose sur une hypothèse sans la valider au risque d'investir lourdement dans une mauvaise direction. Imaginer qu'une équipe part de l'idée que les utilisateurs préfèrent un menu horizontal. On con soit trois prototypes, un horizontal, un vertical et contextuel. On les fait tester par 20 utilisateurs.*

*Résultat, le menu horizontal plaît à 35 d'entre eux, le vertical à 60 et le contextuel à 80. Sans ce test, l'équipe pourrait développer la première option en pensant bien faire, mais n'aurait convaincu qu'un tiers des utilisateurs.*
**Vidéo 1124775176:**

*On peut comparer les niveaux de fidélité du prototypage à l'architecture. La basse fidélité, c'est le croquis griffonner sur une serviette, la moyenne fidélité, ce sont les plans techniques et la haute fidélité. C'est la maquette d réaliste, très proche du bâtiment final.*

*L'objectif de cette étape est simple, générer rapidement un maximum d'idées, valider les grands principes et favoriser les échanges créatifs sans tomber dans le piège de s'attacher trop vite à une solution. Les outils sont rudimentaires papier. Si l'eau postit, voire une petite maquette en carton, prenons une application de livraison en seulement deux heures.*

*Un simple prototype papier permet déjà de simuler la navigation. On peut le tester avec quelques utilisateurs dans un café et identifier une douzaine de problèmes majeurs. Trois concepts totalement différents peuvent même immerger. L'avantage est évident. Un coup quasi nul, une rapidité immédiate, une flexibilité totale et une créativité libérée. Bien sûr, il y a des limites.*

*On ne teste pas des interactions complexes ni l'esthétique finale, mais ce n'est pas le but. Une fois les grandes lignes à l'idée, on passe à des prototypes plus aboutis. Ici, l'enjeu est d'évaluer les workflows complètes de tester l'ergonomie et la logique de navigation. Des outils comme Figma sketches ou ado big day permettent de simuler la navigation et même quelques micro interactions.*

*Imaginons un CRM. Un prototype interactif peut inclure les principaux écrans des données réalistes et des scénarios de navigation. On peut alors organiser un test utilisateur d'une demi-heure et mesurer les éléments précis, le temps nécessaire pour accomplir une tâche, le taux d'erreur, les points de friction ou encore la satisfaction ressentie.*

*On apprend ainsi le workflow et intuitif si l'information est hiérarchisée correctement et où se situent les décrochages. À ce stade, le but est de tester l'expérience émotionnelle complète. On ne parle plus seulement d'efficacité, mais aussi d'ambiance d'identité visuelle et sonore et de qualité perçue.*

*Le prototype est pixel perfect avec des animations fluides, des contenus réalistes et des performances proches du produit final. Prenant une application de méditation, le prototype inclut déjà les vraies couleurs, les typographie finales, les illustrations des transitions soignées et même les enregistrements audio.*

*On peut faire vivre à un utilisateur une vraie session de 10 minutes et mesurer son ressenti. On évalue alors l'atmosphère, l'impact émotionnel, la qualité perçue et même l'intention d'achat.*
**Vidéo 1124783156:**

*Le prototypage n'est pas un processus linéaire. C'est une boucle. Construire, mesurer, apprendre. On crée un prototype minimal pour tester une hypothèse. On mesure avec des données objectives et l'observation des comportements. Puis on apprend en comparant les attentes à la réalité, en identifiant les causes des problèmes et en formulant de nouvelles hypothèses.*

*Un cycle peut tenir en une semaine le lundi et le mardi ont construit, par exemple, unboarding d'idées en cinq écrans le mercredi et le jeudi, on teste avec 10 utilisateurs. On mesure le temps de complétion, les abandons, les hésitations le vendredi, on analyse ces 30 des gens abandonnent au troisième écran, c'est que le tutoriel est trop long ou trop technique.*

*La semaine suivante, on reform l'hypothèse et on teste une nouvelle version en prototypage. Il vaut mieux 10 prototypes imparfait qu'un seul prototype parfait. Multiplier les itérations, c'est accélérer l'apprentissage, réduire les risques et garder une dynamique d'avancées constantes. Pour réussir, il faut poser des limites de temps courtes, se concentrer sur une hypothèse à la fois.*

*Viser une qualité suffisante pour tester et documenter l'essentiel sans noyer l'équipe dans des rapports. Le danger, c'est de tomber dans trois pièges, le perfectionnisme qui bloque la livraison, libération infinie où l'on tourne en rond et la fausse itération qui ne change rien de fondamental. Adopter une approche prototypage first, c'est changer de paradigme.*

*On remplace la certitude par l'expérimentation. On préfère l'empirique o théorique. On choisit libération plutôt que la planification parfaite et on valorise l'apprentissage plutôt que l'exécution immédiate.*

*Les résultats sont mesurables, moins de défauts en production, moins de changements tardif, moins de rea, une meilleure satisfaction des utilisateurs, une adoption accélérée et moins de formation nécessaire pour l'organisation. C'est aussi des délais réduits, des réunions allégées et une équipe mieux alignée. Le prototypage first n'est pas juste une méthode.*

*C'est une philosophie à prendre en faisant valider, en testant, réussir en interrompant votre prochain projet ne devrait pas commencer par 50 pages de spécifications, mais par un prototype testable dès la première semaine. La vraie question n'est plus. Est-ce que le prototypage fonctionne? Les biens? Pouvez vous encore vous permettre de ne pas prototyper.*
