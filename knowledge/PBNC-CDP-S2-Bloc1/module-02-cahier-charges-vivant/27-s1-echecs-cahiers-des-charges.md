# S1 - Les échecs des cahiers des charges classiques

**Type :** E-learning
**Durée :** ~30 min
**Vimeo :** https://vimeo.com/1119923466 (~2:41)
**Statut :** ✅ Complété

## Structure de la leçon

Leçon avec vidéo quiz embarqué (quiz vidéo interactif).

---

## Contenu

Thème : "Les échecs récurrents des cahiers des charges classiques"

### Quiz (4 questions SwipeDeck + questions multiples)

1. Quelle est la cause fondamentale des échecs récurrents des projets de transformation digitale ?
2. Quelles sont les conséquences de la "spécification prématurée" ?
3. Quelles sont les conséquences de sur-détailler les cahiers des charges ?
4. Quel est le comportement contre-productif qui résulte de l'impuissance face aux changements ?

---

## Notes techniques (complétion)

- Leçon E-learning dans iframe play/element
- **Technique vidéo** : Chercher Vimeo frame → manipuler video.currentTime vers duration → postMessage depuis Vimeo frame vers parent
- **Auto-complétion** : Loop de validateAndNextOutput sur tous les outputs avec OutputState = 10
  - Fonctionne pour OutputForQuestion, OutputForInputProcess, OutputMessage, OutputForTheme
  - 12 itérations pour compléter
- IDs :
  - Element GUID : `e628f861-5d9a-46e3-8564-5305f0325d8b`
  - Learning ID : `MDVUR0J4NEw0Nis5b0RScVFGWlQ2dz09` (même que lesson 26 ?)


## Transcript vidéo (sous-titres auto-générés)

*Savez-vous que la majorité des projets Haïti échouent. Les études révèlent que deux tiers dépassent leur budget initial et que la majorité dépasse leurs délais. Où n'atteignent pas les objectifs. Le problème n'est pas technique. Il vient dans des défaut méthodologiques, les cahiers des charges classiques. Voyons d'abord le premier piège, la spécification prématurées.*

*Cette approche consiste à définir des fonctionnalités trop tôt avant de comprendre vraiment les besoins des utilisateurs et les contraintes de l'organisation. Résultat, plusieurs dysfonctionnements critiques apparaissent d'abord les faits tunnels. Quand les équipes s'enferment dans un document trop détaillé, il devient presque impossible de revenir en arrière.*

*Le cahier des charges se transforme en carcan et bloque toute adaptation. Ensuite, la déconnexion avec les utilisateurs quand les spécifications soient rédigées par des experts techniques ou des consultants externes sans implication réelle des utilisateurs finaux, le résultat alors peut sembler cohérent sur le papier, mais dans la pratique, il ne répond pas aux vrais besoins.*

*Enfin, l'escence rapide dans un environnement changeant, un document exhaustif prend tellement de temps à rédiger qu'il est déjà dépassé au moment où le développement commence. Un autre échec courant vient d'une croyance trompeuse. L'illusion de la complétude beaucoup pensent qu'un cahier des charges très détaillé garantit le succès.*

*En réalité, cette illusion génère du comportement qui aggrave les risques. La sûre spécification est le premier symptôme face à l'incertitude. Les équipes ajoutent toujours plus de détails pensant se protéger, mais plus le document est précis, plus le projet devient rigide et incapable d'apprendre en avançant.*

*Vient ensuite la fausse sécurité juridique, certaines organisations sur détails, leurs cahiers pour se protéger contractuellement. Mais ce crée une relation de méfiance avec les prestataires et bloque la collaboration créative nécessaire à l'innovation. Enfin, l'expertise à l'orienter.*

*Les efforts se concentrent sur des détails techniques alors même qu'on n'a pas validé si la fonctionnalité répond à un vrai besoin utilisateur, c'est comme peaufiner la peinture d'une maison avant de vérifier si les fondations tiennent. En résumé, les cahiers des charges classiques échouent parce qu'il enferme les projets dans une rigidité méthodologique.*

*La spécification prématurée et l'illusion de la complétude transforment un outil sans ses guir en un frein à l'innovation. Alors posez-vous la question comment pourriez-vous repenser vos spécifications pour rester agiles face au changement?*
