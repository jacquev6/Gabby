Évolutions prévues
==================

Voir la `roadmap à jour dans Google Docs <https://docs.google.com/document/d/1DS8Rko0q3MCxfUUt0CijjdX41bBWy8J_3IV4rR0sOeA/edit?usp=sharing>`__.

Historique des versions
=======================

Cet historique ne concerne que les changements visibles par l'utilisateur : bugs, interface et fonctionnalités.
Les améliorations techniques ne figurent que dans le `log git <https://github.com/jacquev6/Gabby/commits/main/>`__.

Les titres des sections de ce document correspondent au champ ``Gabby version`` dans le "À propos".
Les versions sont nommées selon leur date de publication, au format ``YYYYMMDD-HHMMSS`` (année, mois, jour, tiret, heure, minute, seconde).

20240701-062228
---------------

- les lenteurs de l'application ont été fortement réduites
- les accès sans identification sont impossibles, même en lecture, même pour un utilisateur technicien
- l'ordre des exercices est correct sur la vue "projet"

20240620-140702
---------------

- Il est nécessaire de s'identifier pour accéder à l'application. Attention, à cause d'une limitation technique, il est encore possible pour un utilisateur technicien de voir les données sans s'identifier. Cela sera corrigé dans une prochaine version. Il est cependant impossible de modifier ces données sans être identifié.
    - Il est possible de demander l'envoi par e-mail d'un lien de réinitialisation du mot de passe
    - Il faut saisir ses identifiants après 16 heures d'utilisation
    - Pour chaque donnée en base, l'utilisateur qui l'a créée et celui qui l'a modifiée en dernier sont enregistrés. Ces informations ne sont pas affichées pour l'instant mais peuvent servir si un audit est nécessaire.

- Adaptation :
    - Nouveaux type : choix multiples avec les choix dans l'énoncé
    - Les choix multiples sont affichés dans un cadre (plutôt que dans une liste déroulante)
    - L'exemple et l'indice sont affichés dans l'exercice adapté
    - Les exercices adaptés sont affichés sur plusieurs pages

- Interface :
    - Sélectionner du texte dans le PDF ne remplit plus le champ "Rechercher" des outils
    - Le bouton "Annuler" est désactivé lors du chargement ou de la création d'un exercice
    - Ctrl+Z et Ctrl+Y sont utilisables pour annuler et refaire

20240516-130222
---------------

- Corrections de bugs :
    - Affichage des exercices dans l'ordre correct sur la vue projet et dans le HTML téléchargeable

- Améliorations d'interface :
    - Possibilité de changer la largeur des colonnes de la vue d'extraction :
        - Possibilité de les cacher entièrement
        - Positions conservées entre les utilisations
        - Barre de défilement verticale dans chaque colonne
        - Amélioration de l'efficacité du changement de taille de l'affichage du PDF

    - Désambiguïsation de vocabulaire entre "adapté" et "adaptation" : le formulaire d'édition permet de choisir un type d'**adaptation** et ses options, pour produire un exercice **adapté**. L'adaptation est un processus, dont l'exercice adapté est le résultat.

    - Amélioration du délai de mise à jour de la pre-visualisation de l'exercice adapté

    - Ajout de liens directs vers les exercices dans la vue projet

- Fonctionnalités d'édition :
    - Ajout des outils "Annuler"/"Refaire" et "Remplacer"

    - Choix d'une convention pour les fins de lignes et de paragraphes

- Support des adaptations :
    - "Sélection de mots"
        - Ajout d'une option "Sélectionner aussi la ponctuation"
        - Possibilité d'afficher du texte coloré (comme s'il était sélectionné) dans la consigne
        - Affichage systématique des couleurs disponibles à la fin de la consigne

    - Support initial des adaptations "Choix multiples" (uniquement avec les choix dans la consigne)

- Affichage des exercices adaptés :
    - Augmentation de l'interligne dans les exercices adaptés

    - Affichage de la consigne en noir, et de l'énoncé en lignes de couleurs alternées

    - Sauvegarde des réponses de l'élève dans le HTML téléchargeable
        - Avec un bouton "Effacer les réponses" pour les réinitialiser

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
