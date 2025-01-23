Évolutions prévues
==================

Voir la `roadmap sur GitHub <https://github.com/jacquev6/Gabby/issues>`__.

Historique des versions
=======================

Cet historique ne concerne que les changements visibles par l'utilisateur : bugs, interface et fonctionnalités.
Les améliorations techniques ne figurent que dans le `log git <https://github.com/jacquev6/Gabby/commits/main/>`__.

Les titres des sections de ce document correspondent au champ ``Gabby version`` dans le "À propos".
Les versions sont nommées selon leur date de publication, au format ``YYYYMMDD-HHMMSS`` (année, mois, jour, tiret, heure, minute, seconde).

20250123-100544
---------------

(La `milestone GitHub avec les issues traitées <https://github.com/jacquev6/Gabby/milestone/2>`__.)

- Le caractère "…" (points de suspension) est maintenant remplacé par trois caractères "." (points) lors de l'extraction depuis le PDF. **Il ne sera plus nécessaire de le copier-coller** pour l'utiliser comme trou à remplir (QCM ou texte libre). Les données existantes ont été corrigées de la même manière (`#29 <https://github.com/jacquev6/Gabby/issues/29>`__)

- Items et effets :
    - suppression du type d'items par défaut : l'utilisateur doit le choisir explicitement (`#44 <https://github.com/jacquev6/Gabby/issues/44>`__)
    - ajout des types d'items "Phrases" (`#46 <https://github.com/jacquev6/Gabby/issues/46>`__) et "Lettres" (`#47 <https://github.com/jacquev6/Gabby/issues/47>`__)
    - possibilité de choisir le type d'items "Ponctuations" sans avoir choisi "Mots" (`#51 <https://github.com/jacquev6/Gabby/issues/51>`__)
    - détection des en-têtes de listes, pour ne pas leur appliquer les effets (`#43 <https://github.com/jacquev6/Gabby/issues/43>`__)
    - possibilité d'utiliser l'effet "Cadre" sans l'effet "Cochable" (`#6 <https://github.com/jacquev6/Gabby/issues/6>`__)
    - l'apostrophe est maintenant reconnue comme un caractère en fin de mot (`#50 <https://github.com/jacquev6/Gabby/issues/50>`__)
    - remplacement de la palette continue par une liste de couleurs prédéfinies pour la personnalisation des couleurs de l'effet "Cochable" (`#10 <https://github.com/jacquev6/Gabby/issues/10>`__)
    - l'activation des effets "Cadre" et "Cochable" ne change plus l'espacement entre les mots (`#48 <https://github.com/jacquev6/Gabby/issues/48>`__, `#53 <https://github.com/jacquev6/Gabby/issues/53>`__)
    - la largeur des cadres a été réduite (`#49 <https://github.com/jacquev6/Gabby/issues/49>`__)
    - suppression du padding horizontal sur les items cochables (`#3 <https://github.com/jacquev6/Gabby/issues/3>`__, `#48 <https://github.com/jacquev6/Gabby/issues/48>`__)

- Choix multiples :
    - taper du texte à une extrémité d'un choix multiple dans la colonne "Édition" ajoute ce texte dans le choix. Cela a demandé d'en changer le formatage (traits noirs en haut et en bas, et fond gris) pour que le curseur de texte soit affiché à la bonne position (`#82 <https://github.com/jacquev6/Gabby/issues/82>`__)
    - les choix dans la consigne sont toujours affichés de la même manière dans l'exercice adapté, indépendamment des séparateurs utilisé dans la colonne "Édition" : séparés par des virgules et les deux derniers par un "ou" (`#74 <https://github.com/jacquev6/Gabby/issues/74>`__)
    - la détection automatique du séparateur a été améliorée :
        - suppression de la détection du mot anglais "or" (`#75 <https://github.com/jacquev6/Gabby/issues/75>`__)
        - ajout des tirets (`#77 <https://github.com/jacquev6/Gabby/issues/77>`__)
        - ajout des losanges "◆" et ronds "●" (`#78 <https://github.com/jacquev6/Gabby/issues/78>`__)
        - la détection du mot "ou" ne s'active maintenant que s'il est entouré d'espaces (`#79 <https://github.com/jacquev6/Gabby/issues/79>`__)
    - les choix sont maintenant affichés espacés relativement à la fin du choix précédent, et plus sous forme de tableau (`#60 <https://github.com/jacquev6/Gabby/issues/60>`__)
    - les choix ne sont toujours affichés que sur 2 lignes même près du bord droit de l'écran (`#61 <https://github.com/jacquev6/Gabby/issues/61>`__)
    - suppression d'un espace accidentel après les champs "Choix multiples" (`#3 <https://github.com/jacquev6/Gabby/issues/3>`__)

- Corrections diverses :
    - les lignes de l'exercice adapté sont maintenant toujours colorées en alternance. Il peut y avoir retard d'une seconde dans de rares cas (`#76 <https://github.com/jacquev6/Gabby/issues/76>`__)
    - la flèche pour changer de page dans l'exercice adapté est maintenant correcte sous tous les OS (`#38 <https://github.com/jacquev6/Gabby/issues/38>`__)
    - suppression de la barre de défilement apparaissant inutilement dans la colonne "Exercice adapté" sous Firefox (`#36 <https://github.com/jacquev6/Gabby/issues/36>`__)
    - changer manuellement la page d'un exercice (champ "Page" dans la colonne "Edition") est maintenant pris en compte dans l'avertissement "Pas [la page] affichée" (`#81 <https://github.com/jacquev6/Gabby/issues/81>`__)

20241128-161450
---------------

(La `milestone GitHub avec les issues traitées <https://github.com/jacquev6/Gabby/milestone/>`__.)

- Homogénéisation du comportement relativement au type d'adaptation (`#33 <https://github.com/jacquev6/Gabby/issues/33>`__)
    - les données existantes ont été migrées au nouveau format
    - le type d'adaptation n'a plus aucun impact fonctionnel; tous les types sont équivalents, le type d'adaptation est purement informatif
    - tous les exercices sont maintenant inclus dans le HTML exporté (précédemment, seuls les exercices ayant un type d'adaptation défini l'étaient)
    - les mêmes outils sont affichés quel que soit le type d'adaptation

- Amélioration de la gestion des fins de lignes (`#1 <https://github.com/jacquev6/Gabby/issues/1>`__)
    - lors de l'extraction depuis le PDF, des retours à la ligne ne sont ajoutés automatiquement que dans les cas suivants :
        - si une liste est détectée : chaque item est terminé par un retour à la ligne
        - si du texte justifié est détecté : les ligne plus courtes que les autres sont terminées par un retour à la ligne
        - si des interlignes plus grands sont détectés parmi des interlignes réguliers : les lignes avant ces grands interlignes sont terminées par un retour à la ligne
    - une option a été ajoutée au dialogue d'extraction pour conserver tous les retours à la ligne du PDF (utile pour les poèmes par exemple)
    - une option a été ajoutée au dialogue d'extraction pour désactiver la détection des listes. Cette option sera retirée quand on aura confiance que cette détection fonctionne correctement
    - les exercices pré-existants ne bénéficient pas de cette amélioration, et devront être corrigés à la main (car ce changement intervient avant l'enregistrement de l'exercice)

- la création des exercices indépendants a été (temporairement) retirée. Cette fonctionnalité était inutilisable en l'état, en l'absence de prévisualisation et de possibilité de modification

- la case à cocher "WYSIWYG" a été retirée. Toute l'édition se fait maintenant en WYSIWYG

- Répartition des lignes (`#5 <https://github.com/jacquev6/Gabby/issues/5>`__)
    - une typo a été corrigée ("1 lignes par page" devient "1 ligne par page")
    - la répartition automatique est devenu optionnelle (décochable)
    - il est maintenant possible de forcer un passage à la page suivante dans l'exercices adapté en insérant deux lignes blanches consécutives dans l'énoncé

- la détection des phrases dans la consigne (pour les mettre chacune sur une ligne) a été rendue plus souple
    - il est vraisemblable que cela donne lieu à des cas où la consigne est affichée sur trop de lignes; l'issue `#39 <https://github.com/jacquev6/Gabby/issues/39>`__ a été ouverte pour recenser ces cas

- Création de choix multiples (`#34 <https://github.com/jacquev6/Gabby/issues/34>`__)
    - les réglages ("Début", "Fin", "Séparateurs") sont détectés automatiquement :
        - si le texte est encadré par des parenthèses ou crochets droits, ces caractères sont utilisés comme "Début" et "Fin"
        - si le texte contient au moins un caractère comme "," ou "/", il est utilisé comme premier séparateur
        - si le texte contient le mot "ou", il est utilisé comme deuxième séparateur

- un champs "Référence" a été ajouté pour les références de texte. Elles sont affichées seules sur la dernière page de l'exercice adapté (`#2 <https://github.com/jacquev6/Gabby/issues/2>`__)

- un `PDF de demo <https://github.com/jacquev6/Gabby/blob/main/pdf-examples/demo.pdf>`__ et un `PDF focalisant sur l'extraction de texte <https://github.com/jacquev6/Gabby/blob/main/pdf-examples/text-extraction.pdf>`__, correspondant à une infime parte des tests automatisés, ont été ajoutés. Ils peuvent servir de base au discussions concernant l'extraction et l'adaptation

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
