Évolutions prévues
==================

Voir la `roadmap à jour dans le code source <https://github.com/jacquev6/Gabby/blob/develop/roadmap.md>`__.

Historique des versions
=======================

Cet historique ne concerne que les changements visibles par l'utilisateur : bugs, interface et fonctionnalités.
Les améliorations techniques ne figurent que dans le `log git <https://github.com/jacquev6/Gabby/commits/main/>`__.

Les titres des sections de ce document correspondent au champ ``Gabby version`` dans le "À propos".
Les versions sont nommées selon leur date de publication, au format ``YYYYMMDD-HHMMSS`` (année, mois, jour, tiret, heure, minute, seconde).

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

- Correction de bugs:

    - Le PDF ne s'affiche plus à l'envers
    - Le champ de sélection de la page dans le PDF autorise n'importe quelle saisie

- Amélioration d'interface:

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
