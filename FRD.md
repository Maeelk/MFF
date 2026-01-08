# Document de besoins (FRD) — Recherche terrain

## 1. Rôles et permissions

### Créateur/Superviseur
- **Création & configuration** : créer une recherche, définir l’objectif, la zone, les dates, les règles de collecte.
- **Gestion des créneaux** : ouvrir/fermer des créneaux, inviter/assigner des participants, ajuster les quotas.
- **Pilotage** : lancer/mettre en pause/arrêter la recherche, suivre la progression globale.
- **Qualité & conformité** : valider les soumissions, demander des corrections, signaler des anomalies.
- **Clôture & export** : clôturer la recherche, générer/exporter les résultats et rapports.
- **Accès aux données** : accès complet aux données de la recherche (y compris logs et événements).

### Participants
- **Inscription** : s’inscrire à un créneau disponible ou accepter une assignation.
- **Exécution** : collecter et soumettre des observations selon le protocole.
- **Édition limitée** : modifier ses propres soumissions tant qu’elles ne sont pas validées.
- **Signalement** : signaler des incidents ou contraintes terrain.
- **Visibilité** : voir son propre statut et la progression de son créneau.

### Observateurs
- **Consultation** : accès en lecture seule aux données agrégées et indicateurs.
- **Suivi** : visualiser l’avancement et les signalements.
- **Restrictions** : aucun accès aux données personnelles sensibles, pas de modification ni de soumission.

## 2. Cycle de vie d’une recherche

1. **Création**
   - Définition du périmètre (zone, objectifs, protocole, critères de qualité).
   - Définition des rôles, des critères d’éligibilité et des niveaux d’accès.
2. **Planification des créneaux**
   - Découpage en créneaux (dates, zones, quotas, ressources).
   - Ouverture des inscriptions/assignations.
3. **Lancement**
   - Validation de la préparation (briefing, matériel, check réseau/GPS).
   - Activation officielle de la collecte.
4. **Tracking (suivi)**
   - Collecte en cours, suivi temps réel/ différé.
   - Contrôles qualité, relances, corrections.
5. **Signalement**
   - Enregistrement des incidents (sécurité, accès, données manquantes, GPS).
   - Escalade et décisions (ajustement protocole, re-planification).
6. **Clôture**
   - Arrêt de la collecte, validation finale.
   - Consolidation des données, export et archivage.

## 3. Contraintes terrain

- **Couverture réseau** : zones sans 3G/4G/5G, nécessité de synchronisation différée.
- **Précision GPS** : variabilité selon l’environnement (urbain dense, forêt, intérieur).
- **Sécurité** : risques liés au terrain, respect des protocoles de sécurité et du RGPD.
- **Fonctionnement offline** : collecte et stockage local, synchronisation lorsque la connectivité revient.

## 4. User stories prioritaires

### MVP
- En tant que **créateur**, je veux créer une recherche avec une zone et un protocole pour cadrer la collecte.
- En tant que **créateur**, je veux planifier des créneaux et limiter le nombre de participants pour gérer les ressources.
- En tant que **participant**, je veux m’inscrire à un créneau et recevoir les consignes pour réaliser la collecte.
- En tant que **participant**, je veux soumettre une observation même hors ligne pour continuer la mission.
- En tant que **superviseur**, je veux suivre la progression globale en temps réel pour réagir rapidement.
- En tant que **superviseur**, je veux clôturer la recherche et exporter un rapport pour partager les résultats.

### Futur
- En tant qu’**observateur**, je veux accéder à des tableaux de bord détaillés pour analyser les tendances.
- En tant que **superviseur**, je veux configurer des alertes automatiques sur les anomalies.
- En tant que **participant**, je veux recevoir des suggestions de zones à couvrir basées sur le GPS.
- En tant que **superviseur**, je veux intégrer des sources externes (cartes, météo) pour améliorer le suivi.
- En tant que **créateur**, je veux versionner les protocoles pour garder une traçabilité complète.
