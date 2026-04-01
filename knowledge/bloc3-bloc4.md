# Fiches compétences C17-C31 (Blocs 3-4)

Les cours e-learning ne couvrent pas ces blocs. Ce fichier fournit le contexte métier pour chaque compétence afin qu'Orion puisse aider l'apprenant à structurer ses réponses, même sans cours de référence.

---

## Bloc 3 — Personnaliser et déployer des technologies no-code et IA générative

### C17 — Architecture des informations / modèle de données

**Ce que c'est :** Concevoir le schéma de données (MCD/ERD) d'une application no-code — quelles entités, quelles relations, quels champs — en respectant les normes de sécurité (RGPD).

**Concepts clés :**
- MCD (Modèle Conceptuel de Données) : entités, attributs, relations, cardinalités
- ERD (Entity-Relationship Diagram) : représentation visuelle du MCD
- Normalisation : éviter la redondance, garantir la cohérence
- Sécurité RGPD dans l'architecture : minimisation des données, chiffrement, droits d'accès, logs d'audit

**Outils courants :** dbdiagram.io, Lucidchart, Miro, les vues de structure d'Airtable/Notion

**Piège fréquent :** Créer un modèle de données sans penser à la sécurité dès la conception (privacy by design).

### C18 — Agents IA

**Ce que c'est :** Concevoir un agent IA en configurant le contexte, les instructions (prompts) et le choix du LLM pour automatiser un traitement de données.

**Concepts clés :**
- Prompt engineering : system prompt, few-shot examples, chain-of-thought, contraintes de format
- Choix du LLM : GPT-4o (polyvalent, écosystème large), Claude (raisonnement long, documents), Mistral (souveraineté FR, coût), modèles open-source
- Critères de choix : coût par token, latence, taille du contexte, confidentialité des données, qualité sur la tâche
- RAG (Retrieval-Augmented Generation) : enrichir le prompt avec des données métier
- Évaluation : tester sur des cas réels, mesurer la qualité (précision, hallucinations, pertinence)

**Outils courants :** API OpenAI/Anthropic/Mistral, plateformes comme Relevance AI, Dust, Flowise

**Piège fréquent :** Utiliser un LLM sans justifier le choix, ou sans itérer sur les prompts.

### C19 — Implémentation no-code

**Ce que c'est :** Configurer les applications no-code (bases de données, règles métier, permissions) conformément au modèle de données défini.

**Concepts clés :**
- Configuration BDD : tables/collections, champs (types, validations), vues filtrées
- Règles métier : automations internes (ex : quand statut = "terminé", notifier le manager), formules, rollups
- Permissions : qui voit quoi, qui modifie quoi (row-level security dans Supabase, vues partagées dans Airtable)
- Vérification : l'implémentation doit correspondre fidèlement au MCD défini en C17

**Outils courants :** Airtable, Notion (databases), Supabase (PostgreSQL managé), Xano, NocoDB

**Piège fréquent :** Configurer « à la main » sans plan, puis découvrir que le modèle ne tient pas à l'échelle.

### C20 — Workflows d'automatisation

**Ce que c'est :** Créer des séquences d'exécution dans des outils d'automatisation en connectant des applications et des API IA.

**Concepts clés :**
- Scénario/Zap/Workflow : déclencheur → filtre → actions → gestion d'erreurs
- Connexion API : authentification (API key, OAuth), endpoints, format des données (JSON)
- Gestion d'erreurs : routes d'erreur dans Make, retry logic, alertes (Slack, email)
- MCP (Model Context Protocol) : connecter des LLM à des outils externes
- Orchestration complexe : scénarios chaînés, webhooks, files d'attente

**Outils courants :** Make (Integromat), Zapier, N8n (self-hosted), Activepieces

**Piège fréquent :** Construire un scénario complexe sans gestion d'erreurs ni documentation.

### C21 — Tests

**Ce que c'est :** Concevoir une procédure de tests systématique en simulant des parcours utilisateurs inclusifs.

**Concepts clés :**
- Plan de tests : matrice fonctionnalités × cas de test × résultat attendu
- Parcours utilisateurs : happy path + edge cases + parcours inclusifs (lecteur d'écran, navigation clavier, daltonisme)
- Types de tests : fonctionnel, intégration (les automatisations fonctionnent-elles bout en bout ?), UAT (validation par l'utilisateur final)
- Documentation des bugs : description, étapes de reproduction, sévérité, statut

**Outils courants :** Tableur/Notion pour le plan, navigateur pour les tests manuels, Playwright pour l'automatisation

**Piège fréquent :** Tester seulement le happy path, oublier les cas limites et les profils inclusifs.

### C22 — Maquette fonctionnelle

**Ce que c'est :** Concevoir une maquette inclusive de l'interface avec un outil de design pour valider l'ergonomie avant le développement.

**Concepts clés :**
- Wireframe → Mockup → Prototype interactif
- Accessibilité : WCAG 2.1 (contraste 4.5:1 minimum, cibles cliquables 44px, navigation clavier, textes alternatifs)
- Test utilisateur : faire tester la maquette par des utilisateurs réels avant de construire
- Design system : composants réutilisables, cohérence visuelle

**Outils courants :** Figma (standard), Sketch, Adobe XD, Penpot (open-source)

**Piège fréquent :** Maquetter sans tester avec des utilisateurs, ou ignorer les critères d'accessibilité.

### C23 — Déploiement front-office

**Ce que c'est :** Reproduire la maquette validée dans l'outil no-code front-office pour déployer l'interface réelle.

**Concepts clés :**
- Fidélité maquette → intégration : compromis entre le design idéal et les contraintes de l'outil
- Responsive : l'interface fonctionne sur desktop, tablette, mobile
- Performance : temps de chargement, optimisation des images
- Déploiement : domaine personnalisé, DNS, SSL

**Outils courants :** Softr, Bubble, Webflow, Glide, Framer

**Piège fréquent :** Se battre contre les limites de l'outil au lieu de les intégrer dès le design.

---

## Bloc 4 — Pérennité du produit no-code

### C24 — Guide utilisateur inclusif

**Ce que c'est :** Créer un guide compréhensible par tous les publics, y compris les personnes en situation de handicap.

**Concepts clés :**
- FALC (Facile À Lire et à Comprendre) : phrases courtes (15 mots max), mots courants, une idée par phrase
- Structure : sommaire, captures annotées, pas-à-pas, glossaire
- Formats multiples : texte + visuels + vidéo si possible
- Test de lisibilité : faire relire par une personne non technique

**Piège fréquent :** Écrire un guide technique déguisé en guide utilisateur.

### C25 — Documentation technique

**Ce que c'est :** Rédiger une documentation suffisamment complète pour qu'un autre builder puisse reprendre le projet.

**Concepts clés :**
- Contenu minimal : architecture (MCD), workflows d'automatisation, règles métier, permissions, API utilisées, paramétrages spécifiques
- Format : README de projet, wiki, Notion partagé
- Sécurité : documenter les accès, les clés API (sans les exposer), les politiques de sauvegarde

**Piège fréquent :** Documentation qui décrit ce que fait l'outil en général au lieu de ce qui a été configuré spécifiquement.

### C26 — Formation

**Ce que c'est :** Animer des sessions de formation adaptées aux différents publics pour garantir l'appropriation de l'outil.

**Concepts clés :**
- Adaptation : profil technique → atelier pratique, profil manager → démo orientée résultats, profil handicap → format adapté
- Vérification : quiz, mise en pratique supervisée, feedback post-formation
- Support post-formation : FAQ, permanence, référent

**Piège fréquent :** Format unique pour tous, sans vérification de l'acquisition.

### C27 — Collecte de données / retours utilisateurs

**Ce que c'est :** Mettre en place les outils pour collecter les bugs et les feedbacks des utilisateurs.

**Concepts clés :**
- Outils : formulaire intégré (Tally, Typeform), ticketing (Linear, Freshdesk, Notion), analytics (Hotjar, PostHog, Mixpanel)
- Processus : collecte → triage → priorisation → action → communication retour
- Boucle de feedback : les utilisateurs doivent savoir que leur retour a été pris en compte

**Piège fréquent :** Collecter des données sans processus de traitement ni de retour vers les utilisateurs.

### C28 — Qualité / feuille de route

**Ce que c'est :** Appliquer des méthodes de gestion de la qualité et structurer l'évolution du produit.

**Concepts clés :**
- Lean : éliminer le gaspillage, amélioration continue (Kaizen)
- Six Sigma : réduire la variabilité, DMAIC (Define, Measure, Analyze, Improve, Control)
- Feuille de route : V2/V3 avec jalons, priorisation par valeur utilisateur
- Priorisation : RICE (Reach, Impact, Confidence, Effort), Kano model, simple effort/impact

**Piège fréquent :** Lister des fonctionnalités futures sans méthode de priorisation ni critères clairs.

### C29 — Support utilisateur

**Ce que c'est :** Définir les canaux et modalités de support adaptés au public cible.

**Concepts clés :**
- Canaux : chat (Intercom, Crisp), email, visio, FAQ/base de connaissances
- SLA (Service Level Agreement) : temps de première réponse, temps de résolution, par niveau de sévérité
- Arbres de décision : « si le problème est X, alors escalader à Y »
- Accessibilité : le support doit être utilisable par tous (pas uniquement par téléphone si public malentendant)

**Piège fréquent :** Proposer un seul canal sans considérer les besoins variés du public.

### C30 — Équipe support

**Ce que c'est :** Dimensionner et structurer l'équipe de support post-déploiement.

**Concepts clés :**
- Rôles : L1 (premier contact, FAQ), L2 (technique, configuration), L3 (développeur/builder)
- Dimensionnement : ratio tickets/agent, plages horaires, montée en charge prévue
- Formation : l'équipe support doit connaître l'outil aussi bien que les builders
- Inclusivité : diversité dans l'équipe, compétences en accessibilité

**Piège fréquent :** Ne pas anticiper la montée en charge après le lancement.

### C31 — Tableaux de bord support

**Ce que c'est :** Concevoir un dashboard de suivi de la performance du support pour piloter l'amélioration continue.

**Concepts clés :**
- KPIs quantitatifs : temps de première réponse, temps de résolution, volume de tickets, taux de résolution au premier contact
- KPIs qualitatifs : CSAT (satisfaction client), NPS, verbatims
- Dashboard : Notion, Metabase, Google Data Studio, le built-in de l'outil de ticketing
- Amélioration continue : revue hebdo/mensuelle des KPIs, identification des tendances, actions correctives

**Piège fréquent :** Mesurer le volume sans mesurer la qualité.
