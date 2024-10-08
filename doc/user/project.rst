Vue projet
==========

La vue projet est constituée de plusieurs zones:

- un en-tête rappelant le titre et la description du projet
- une colonne permettant d'associer un nouveau manuel au projet
- une colonne permettant de créer un exercice indépendant dans le projet
- une colonne listant les manuels et exercices existant dans le projet

.. image:: project/project.png
   :alt: Screenshot
   :align: center

Téléchargement des exercices adaptés
------------------------------------

Un lien permet de télécharger les exercices adaptés contenus dans le projet.
Le fichier HTML téléchargé est nommé en fonction du titre du projet.
Il est autonome et peut être ouvert dans un navigateur web même sur un ordinateur sans connexion internet.

Modification du titre et de la description
------------------------------------------

Le bouton "Modifier" à coté du titre affiche un formulaire permettant de modifier le titre et la description du projet.

.. image:: project/edit.png
   :alt: Screenshot
   :align: center

Ajout d'un manuel
-----------------

Note: un projet peut contenir des exercices de plusieurs manuels, ainsi que des exercices indépendants sans restriction.
Le formulaire d'ajout de manuel reste donc accessible même si le projet contient déjà un manuel.

Après avoir ouvert un PDF, vous pouvez en parcourir les pages.
Tous les champs du formulaire sont optionnels sauf le PDF et le titre.

.. image:: project/new-textbook.png
   :alt: Screenshot
   :align: center

Une fois le manuel créé, la :doc:`vue d'extraction (Manuel) <project-textbook-page>` est affichée.

Extraction depuis un manuel existant
------------------------------------

Les liens dans la colonne de droite mènent également à les vues d'extraction
(:doc:`Manuel <project-textbook-page>` ou :doc:`Exercice <project-textbook-page-exercise>` selon les liens).

Ajout d'un exercice indépendant
-------------------------------

Cette fonctionnalité n'est pas finalisée.
