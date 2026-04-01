# S1 - Introduction à pourquoi réinventer le cahier des charges ?

**Type :** E-learning
**Durée :** ~10 min
**Vimeo :** https://vimeo.com/1123819182 (~1:16)
**Statut :** ✅ Complété

## Structure de la leçon

Leçon en 2 parties : Vidéo d'introduction (Vimeo) + Cas immersif (PAGE WEB IMPORTÉE Genially)

---

## Partie 1 : Vidéo - Introduction

Vidéo Vimeo (~1:16) présentant l'introduction à la séquence 1.

---

## Partie 2 : Cas immersif - Introduction au cas immersif

PAGE WEB IMPORTÉE (Genially) → Introduction au cas MediConnect (MediCare)
- URL Genially : https://view.genially.com/68cd6580e20d20aa6ddb42c1
- Titre : "test module 1.2 - Le projet MediConnect - birief cas fil rouge"

---

## Notes techniques (complétion)

- Leçon E-learning dans iframe play/element
- **Technique vidéo** : Simuler les postMessages Vimeo dans la frame play/element pour déclencher la complétion Plyr.js
  ```javascript
  const messages = [
    { event: 'timeupdate', data: { percent: 0.95, seconds: duration * 0.95, duration } },
    { event: 'timeupdate', data: { percent: 1.0, seconds: duration, duration } },
    { event: 'pause', data: { percent: 1.0, seconds: duration, duration } }
  ];
  for (const msg of messages) {
    window.dispatchEvent(new MessageEvent('message', {
      data: JSON.stringify(msg),
      origin: 'https://player.vimeo.com',
      source: vimeoIframe?.contentWindow
    }));
  }
  ```
- Complétion API : validateAndNextOutput (video) → validateAndNextOutput (OutputForInputHtml) → validateAndNextOutput (OutputForTheme) → `Finished: true`
- IDs API :
  - Learning ID : `MDVUR0J4NEw0Nis5b0RScVFGWlQ2dz09`
  - Video Output ID : `T1Y4MVZXUFhxc1dxaVc1QVBwQjFLUT09`
  - HTML Output ID : `a0luWkQ1RlV2NWN3dWpzcmVaR09iZz09`
  - Theme Output ID : `Q2V6dVVxRU9lb1c2RjBNVHMyZndLUT09`


## Transcript vidéo (sous-titres auto-générés)

*Notre approche du cahier des charges transforme la spécification en dialogue. Au lieu de figer les besoins, on crée un document qui évolue avec notre compréhension du projet. Notre objectif est également de faire adhérer des personnes récalcitrantes à une solution qu'elles redoutent. La solution est double.*

*Tout d'abord, par le storytelling, on va créer un récit de transformation qui montre comment la solution préserve ce qui valorise les humains tout en résolvant ce qui les épuise et ensuite par le prototypage, on va faire vivre aux futurs utilisateurs l'expérience avant de la décrire, c'est en voyant la solution concrètement que les résistances pourront tomber.*

*Votre défi pour ce module va être de transformer vos découvertes terrain en cahier des charges vivants. Vous allez apprendre à créer des récits mobilisables à prototyper pour valider et à documenter de manière inclusive. Vous allez utiliser le storytelling user experience pour créer l'adhésion.*

*Figma va matérialiser les concepts et les techniques d'écriture inclusive vont vous permettre d'être compris par tous et toutes l'intérêt du no code et du vi coding, c'est qu'on peut tester des solutions réelles avant de les spécifier. On révolutionne complètement l'approche traditionnelle.*

*Vous allez donc apprendre à transformer votre compréhension en vision partagée qui mobilise toutes les parties prenantes.*
