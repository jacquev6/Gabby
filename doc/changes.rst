Évolutions prévues
==================

Voir la `roadmap à jour dans Google Docs <https://docs.google.com/document/d/1DS8Rko0q3MCxfUUt0CijjdX41bBWy8J_3IV4rR0sOeA/edit?usp=sharing>`__.

Historique des versions
=======================

Cet historique ne concerne que les changements visibles par l'utilisateur : bugs, interface et fonctionnalités.
Les améliorations techniques ne figurent que dans le `log git <https://github.com/jacquev6/Gabby/commits/main/>`__.

Les titres des sections de ce document correspondent au champ ``Gabby version`` dans le "À propos".
Les versions sont nommées selon leur date de publication, au format ``YYYYMMDD-HHMMSS`` (année, mois, jour, tiret, heure, minute, seconde).

20241031-160526
---------------

- Interface d'adaptation :
    - refonte de la création de QCM : implémentation du flow décrit par Léa
        - le type "Choix multiples (dans l'énoncé)" a été supprimé
        - le type "Choix multiples (dans la consigne)" n'est plus utilisable pour de nouveaux exercices
        - le type "Choix multiples" a été ajouté couvrant les deux cas
        - il maintenant possible d'avoir plusieurs QCMs dans un seul exercice
    - la colonne de prévisualisation contient maintenant une version réduite de l'exercice, avec la possibilité de passer en plein écran

- Exercices adaptés :
    - dans les QCM, les choix ne recouvrent plus jamais la phrase du dessous

20241014-090349
---------------

- Correction de bugs:
    - il est à nouveau possible de télécharger le HTML exporté
    - il est à nouveau possible de modifier un exercice ayant été crée avec une adaptation avant la version 20241003-153035

20241003-153035
---------------

- Expérience utilisateur:
    - le numéro de page de l'exercice est affiché dans un champ dédié
        - un message de confirmation est affiché si l'utilisateur a changé de page et que l'exercice va être créé sur une autre page que celle affichée actuellement
        - cela explicite un comportement fortement contre-intuitif où l'exercice était toujours créé sur la page affichée, même si l'utilisateur avait changé de page de puis le début de la création de l'exercice
    - un message est affiché si l'utilisateur charge un PDF qui n'est pas exactement identique au PDF utilisé lors de la création du manuel
    - un message de confirmation est affiché lors de la suppression d'un exercice

- Adaptation :
    - le nombre de lignes d'énoncé par page d'exercice adapté est maintenant paramétré lors de l'adaptation
    - un nouveau type d'adaptation "Items et effets (essai n°1)" a été ajouté pour expérimenter avec les sections "Items" et "Effets" de la colonne "Outils"
        - ce type d'adaptation est temporaire; tous les types d'adaptation actuels seront bientôt unifiés
        - ce type d'adaptation permet déjà de faire tout ce que fait "Selection de mots"
        - et ajoute la possibilité d'ajouter un effet "cadre" aux items
        - et ajoute la possibilité de sélectionner manuellement les items

- Exercices adaptés:
    - QCM: la réponse "...." a été enlevée. Il n'est plus possible de vider un champ qui a été rempli
    - le document "CSS.pdf" du 24/09 a été appliqué autant que faire se peut. En particulier:
        - QCM: les choix sont affichés sur deux lignes, en colonnes alignées à gauche
        - mots cochables: les "1 clic", "2 clics", etc. ont été enlevés de la consigne
        - les couleurs alternées des lignes de l'énoncé ont été mise à jour
        - les couleurs alternées des choix de QCM également

20240829-151537
---------------

- l'éditeur WYSIWYG est utilisable sur tous les champs
- l'éditeur WYSIWYG est utilisable sur les exercices de type "Remplissage par texte libre", "Sélection de mots" et "Choix multiples (dans la consigne)"
- un PDF contenant des examples d'exercices est utilisé pour les tests automatisés
- pour les "Sélection de mots":
    - le nombre de couleurs utilisables est choisi visuellement en cliquant sur la dernière couleur
    - les couleurs peuvent être personnalisées avec un clic droit

20240821-114939
---------------

- l'identification est valide pendant 1 an (sera réduit pour la production)
- les identifiants d'un utilisateur de démo sont affichés dans le dialogue d'identificaiton

20240808-133707
---------------

- Correction de bugs:
    - préservation des espaces après les champs "texte libre" dans les exercices adaptés (cet espace disparaissait sous Chrome)
    - le caret est maintenant correctement centré verticalement les champs "texte libre" (il était décalé vers le bas sous Chrome)
    - choisir "Annuler" après avoir ouvert un PDF sous Chrome ne cause plus de crash

- Améliorations d'interface:
    - il est possible de changer la page affichée du PDF même lors de l'édition d'un exercice. Cela ne modifie pas la page de l'exercice lui-même
    - un lien vers la liste des exercices de la page a été ajouté aux "breadcrumbs" (liens séparés par des chevrons en haut de la page) sur les pages d'ajout et d'édition d'exercice
    - l'outil "Remplacer" a été supprimé. Je l'avais implémenté avant de comprendre la volonté "WYSIWYG"

- Suppression de la notion de rectangle englobant:
    - plus besoin de le tracer au début de la création d'un exercice
    - les exercices existants sont grisés dans le PDF en fonction des rectangles utilisés pour en extraire les différents champs

- Éditeur WYSIWYG:
    - disponible **exclusivement** pour le champs "instructions" pour les exercices de type "Choix multiples (dans la consigne)"
    - désactivable par une case à cocher (n'apparaissant que dans ce cas)
    - permet l'ajout de gras, italique et de choix pour le QCM
    - les formatages sont exclusifs les uns des autres
    - conserve les fonctionnalités existantes :
        - annuler / refaire
        - mise en surbrillance du texte ajouté depuis le PDF
        - *etc.*

20240711-155526
---------------

- Correction de bugs:
    - la navigation dans le PDF fonctionne lors de l'ajout d'un manuel à un projet
    - la popup "Text sélectionné" ne sort plus jamais de l'écran

- Une popup peut maintenant apparaître en cas de bug dans l'interface. Elle comporte des détails à transmettre à Vincent

- Améliorations d'interface:
    - la popup "Text sélectionné" se ferme avec la touche Echap
    - les boutons du formulaire d'ajout d'exercise ont évolué
        - ils ont été renommés plus explicitement
        - des boutons "précédent" et "suivant" ont été ajoutés
    - les listes d'exercices affichent le type d'adaptation
    - la colonne "Edition" de la vue listant les exercices d'une page a été renommée "Exercices existants"
    - le bouton "Nouvel exercice" a été déplacé en haut de la colonne
    - le type d'adaptation a été déplacé en haut du formulaire d'ajout d'exercice
    - les détails de l'adaptation ont été déplacés dans la colonne "Outils"
    - l'exercise adapté est toujours affiché, même quand aucun type d'adaptation n'a été sélectionné
    - Selection de mots: la case "sélectionner la ponctuation" est désactivée par défaut
    - Selection de mots: il est possible d'utiliser la balise `{sel1|*texte*}` même quand il n'y a qu'une couleur
    - les exercices déjà extraits sont grisés dans le PDF au lieux d'être mis en surbrillance
    - les exercices déjà extraits restent grisés lors de la création d'un exercice

- Amélioration de l'affichage des exercices adaptés:
    - Trous à remplir: les trous sont plus petits par défaut et s'élargissent quand on y tape du texte
    - les retours à la ligne des énoncés sont tous conservéS
    - les retours à la ligne des consignes, examples et indices sont ignorés au milieu des phrases
    - dans les consignes, examples et indices, si des phrases sont reconnues, elles sont séparées par des retour à la ligne
        - la reconnaissance des phrases est assez strict, dans le but d'éviter des retours à la ligne non souhaitables
    - Selection de mots: les 5 couleurs fixes de la plateforme précédente sont utilisée
    - Trous à remplir: la CSS correspond mieux à la plateforme précédente
    - QCM: la CSS correspond mieux à la plateforme précédente

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
