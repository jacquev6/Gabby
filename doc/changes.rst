Évolutions prévues
==================

Voir la `roadmap à jour dans Google Docs <https://docs.google.com/document/d/1DS8Rko0q3MCxfUUt0CijjdX41bBWy8J_3IV4rR0sOeA/edit?usp=sharing>`__.

Historique des versions
=======================

Cet historique ne concerne que les changements visibles par l'utilisateur : bugs, interface et fonctionnalités.
Les améliorations techniques ne figurent que dans le `log git <https://github.com/jacquev6/Gabby/commits/main/>`__.

Les titres des sections de ce document correspondent au champ ``Gabby version`` dans le "À propos".
Les versions sont nommées selon leur date de publication, au format ``YYYYMMDD-HHMMSS`` (année, mois, jour, tiret, heure, minute, seconde).

20240417-092715
---------------

- Corrections de bugs :

    - Détection des exercices déjà existants, ajout d'un bouton "Passer au suivant"

- Améliorations d'interface :

    - Ajout d'un lien "Accueil" dans la barre de navigation
    - Gain de place pour les champs "Indice" et "Exemple" quand les deux sont inutilisés
    - Possibilité de changer de page dans le PDF pendant la création d'un exercice
    - Remplacement de "Visualisation" par "Adaptation"
    - Affichage des rectangles englobant les exercices; ils deviennent obligatoires

- Déplacement de la description des évolutions prévues dans un Google Doc pour faciliter les commentaires (toujours accessible depuis l'aide)

- Support initial des adaptations :

    - Sélection du type d'adaptation (pour l'instant seulement parmi "Selection de mots" et "Remplissage par texte libre")
    - Prévisualisation de l'exercice adapté
    - Téléchargement de l'ensemble des exercices adaptés du projet, utilisable hors ligne

20240314-174534
---------------

- Ajout de la notion de "projet" et des exercices indépendants des manuels, adaptation de l'interface en conséquence
- Gestion des exercices ayant des "numéros" textuels
- Collecte des "événements d'extraction" pour l'équipe "machine learning"
- Enregistrement *dans le navigateur* des PDFs déjà ouverts
- Sauvegarde régulière de la base de données
- Ajout d'une section "Evolutions prévues" dans l'aide

20240228-163737
---------------

- Gestion de la correspondance entre les PDFs et les manuels, adaptation de l'interface en conséquence

20240221-075646
---------------

- Corrections de bugs :

    - Le PDF ne s'affiche plus à l'envers
    - Le champ de sélection de la page dans le PDF autorise n'importe quelle saisie

- Améliorations d'interface :

    - Le nom est maintenant "MALIN"
    - Le logo est celui du Cartable Fantastique
    - Le "À propos" n'est plus affiché systématiquement
    - Le numéro de l'exercice est enlevé automatiquement du texte sélectionné (expérimental, désactivable)
    - La hauteur des champs du formulaire est adaptée automatiquement à leur contenu
    - Les champs "Indice" et "Example" sont cachés par défaut
    - Le texte ajouté dans le formulaire depuis le PDF est surligné
    - Le changement de page se fait maintenant avec des boutons au dessus du PDF

- Ajout de la documentation utilisateur
- Ajout de l'historique des versions

20240125-162659
---------------

- Enregistrement des exercices extraits.

20240118-095444
---------------

Version initiale ; preuve de concept pour l'interface d'extraction depuis le PDF.
