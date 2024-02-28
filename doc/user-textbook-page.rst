Vue d'extraction
================

Structure générale
------------------

La vue d'extraction est divisée en trois colonnes :

- le PDF du manuel scolaire en entrée
- la zone d'édition
- la zone de pré-visualisation

Ces colonnes correspondent aux deux principales étapes de l'adaptation d'exercices depuis un manuel scolaire :

- la première consiste à extraire du PDF les textes et images (pas encore implémentée) des exercices, de la première à la deuxième colonne
- la seconde, à décrire comment adapter les exercices extraits, de la deuxième colonne à la troisième (pas encore implémentée)


.. image:: user/three-columns.png
   :alt: Screenshot
   :align: center

Décalage des pages entre PDF et manuel
--------------------------------------

Un bouton en forme d'engrenage à proximité des boutons de navigation dans le PDF permet de régler cet éventuel décalage.

.. image:: user/textbook-page-section-editor.png
   :alt: Screenshot
   :align: center

Liste des exercices existants
-----------------------------

Après avoir navigué jusqu'à une page d'un PDF, la liste des exercices déjà extraits est affichée dans la deuxième colonne.
Vous pouvez alors ajouter un exercices avec le bouton "Nouvel exercice" en bas de cette liste, ou modifier ou supprimer les exercices existants.

.. image:: user/existing-exercises.png
    :alt: Screenshot
    :align: center

Ajout d'un nouvel exercice
--------------------------

Lorsqu'on clique sur le bouton "Nouvel exercice", un formulaire d'édition apparaît dans la deuxième colonne.

Les contrôles permettant de changer de PDF ou de page de la première colonne sont désactivés.

Le bouton "Annuler" permet de retourner à la liste des exercices existant sans enregistrer le nouvel exercice.

Le bouton "Enregistrer puis créer le suivant" est désactivé jusqu'à ce que le numéro de l'exercice soit renseigné.
Ce bouton permet ensuite d'enregistrer l'exercice et de vider le formulaire pour en créer un autre.
Le numéro de l'exercice suivant est automatiquement incrémenté, mais peut être modifié.

.. image:: user/create-exercise.png
    :alt: Screenshot
    :align: center

Extraction du texte du PDF
~~~~~~~~~~~~~~~~~~~~~~~~~~

L'extraction du texte du PDF se fait en dessinant à la souris un rectangle autour du texte souhaité.
Le texte trouvé à l'intérieur de ce rectangle est mis en surbrillance.

.. image:: user/selecting-in-pdf.png
    :alt: Screenshot
    :align: center

Lorsqu'on relâche le bouton de la souris, le texte est extrait et affiché dans une boite de dialogue,
à proximité immédiate du pointeur pour limiter les déplacements de souris.

.. image:: user/selected-in-pdf.png
    :alt: Screenshot
    :align: center

On peut alors cliquer sur un des boutons de ce dialogue pour ajouter le texte dans le champ correspondant du formulaire d'édition.

Modification d'un exercices existant
------------------------------------

Le numéro d'un exercice existant n'est pas modifiable pour éviter les confusions.
Vous pouvez toutefois supprimer un exercice mal numéroté et le recréer avec le bon numéro.

Les fonctionnalités d'extraction depuis le PDF sont les mêmes que lors de l'ajout d'un nouvel exercice.

Le bouton "Annuler" permet de retourner à la liste des exercices existant sans enregistrer les modifications.

Le bouton "Enregistrer" permet de sauvegarder les modifications apportées à l'exercice et de retourner à la liste des exercices existant.

.. image:: user/modify-exercise.png
    :alt: Screenshot
    :align: center
