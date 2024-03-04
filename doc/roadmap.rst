Evolutions prévues
==================

Ces prévisions ne concernent que les changements visibles par l'utilisateur : bugs, interface et fonctionnalités.
Les améliorations techniques prévues se trouvent avec ``git grep @todo``.

Les titres des sections de ce document correspondent à la data de publication prévue pour la version contenant les changements listés.

Correction des bugs connus
--------------------------

Aucun pour le moment.

20240314
--------

Ajouter cette roadmap à l'aide
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Logger les actions de l'utilisateur dans le PDF
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pour chaque rectangle cliqué: le texte détecté, le champ auquel il a été ajouté, etc.

Autoriser les numéros d'exercices en texte libre
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*E.g.* "Défi langue".

Attacher les exercices à un "projet"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Au lieu d'un manuel.
Et certains projet contiendront une liste d'extraits de manuels.

Ajouter une vue de projet
~~~~~~~~~~~~~~~~~~~~~~~~~

Avec la liste des exercices extraits, et une mise en valeur des exercices pas encore extraits.

Afficher les informations de projet et de manuel dans la barre de navigation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sur la page d'extraction.

20240404
--------

Gérer les utilisateurs, les organismes et les permissions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Les utilisateurs appartiennent à un organisme (ou plusieurs à terme).

Tous les membres d'un organisme peuvent voir la liste des projets de cet organisme.
Seuls les membres autorisés peuvent voir le contenu des projets, par projet.
Seuls les membres autorisés peuvent modifier les projets, par projet.
Les administrateurs de l'organisme peuvent accorder et retirer des permissions.

Conserver un historique de qui modifie quoi
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Versions ultérieures
--------------------

En franglais pour le moment.

Ensure concurrent use is safe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

How can Gabby help coordinating several people working on the same textbook? Locks? Merging? Conflict resolution? Simple flags saying "[Name] is working on this page"? Continuous save and update in other's view?

Ensure safety of DB
~~~~~~~~~~~~~~~~~~~

Extracted exercises are copyrighted material. We should ensure their safety.

Keep formatting
~~~~~~~~~~~~~~~

    Est-ce qu'il y a un moyen de garder les caractéristiques typographiques genre souligné ou gras facilement ? Parce que parfois, il faut remplacer le mot en gras par exemple.

It's difficult in general because the PDF does not contain the information:

- https://github.com/mozilla/pdf.js/issues/7372#issuecomment-222665266
- https://github.com/mozilla/pdf.js/issues/7297#issuecomment-217627918
- https://stackoverflow.com/a/28068493/905845

A few ideas:

- Grouped by fontName, on the whole page:
    - Measure the average darkness of rendered text rectangles. The darker, the more likely it is bold.
    - Measure the amount of slanted transitions between black and white pixels in the rendered text (*i.e.* detect slanted line in the gradient). The more slanted, the more likely it is italic.
- The same idea, but on the glyphs in the fonts.
- Try to render the text with a bold font and compare the result with the original rendering. If the result is similar, it's bold. This approach could also work for italic text, and bold italic text.
- Use the relative number of chars in each font. We could assume that the most used font is the normal one, the second most used is the bold one, and the third most used is the italic one.

Ensure usability
~~~~~~~~~~~~~~~~

Gabby must be usable with screen readers and similar technologies.

    Pour l'ergonomie, Jérôme demande si tu veux interagir avec lui maintenant ou si on attend que tu aies implémenté plus de fonctionnalités avant de se pencher sur l'ergonomie ?

Automate
~~~~~~~~

    Du côté de l'automatisation : Olivier me dit qu'Elise et lui ont beaucoup travaillé récemment sur l'extraction à partir de la visualisation et donc qu'il y aurait la possibilité de rentrer à gauche des fichiers avec des cadres déjà faits qu'il n'y aurait donc plus qu'à valider ou à retracer si ce ne sont pas les bons. Est-ce envisageable ? Et que faudrait-il faire pour que ce soit implémentable à terme ?

Allow images in exercices
~~~~~~~~~~~~~~~~~~~~~~~~~

    On a besoin de pouvoir inclure les images des exercices

Make sure they are included in the DB backups.

Customize the floating modal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    En termes d'ergonomie de la fenêtre qui s'ouvre quand on sélectionne, il faudrait qu'on puisse l'agrandir et la déplacer. Pour la police, il faudrait mettre de l'arial par défaut. Idéalement, il faudrait que ce soit paramétrable pour chaque adaptateur (taille de la fenêtre, emplacement, police, taille de la police, interligne).

Handle multiple choice questions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Il se pose la question des choix qui sont un champ spécifique dans l'adaptation pour les exercices à choix multiples type Cartable. Les choix peuvent être dans la consigne, sous la consigne, dans l'énoncé et ils sont un élément spécifique de l'adaptation. Il faut qu'on voit qu'elle est la meilleure option. Je te mets en PJ les différents types d'exercices à Choix Multiples. Est-ce que tu veux qu'on échange en visio sur ce point ?

Handle columns
~~~~~~~~~~~~~~

(Maybe never, if integrating Olivier and Elise's automation is enough.)

    Quand le texte est en 2 colonnes, on est obligé de sélectionner la première colonne puis la seconde si on veut que ça se mette dans l'ordre. Je ne sais pas si c'est arrangeable.

Adapt exercises
~~~~~~~~~~~~~~~

Implement the third column.

    Types d'exos à adapter en priorité:

    - mots à cocher
    - remplir au clavier
    - QCM

Export adapted exercises
~~~~~~~~~~~~~~~~~~~~~~~~

Exporting as a .zip file is error-prone.

It should be possible to export as a single html file, with all the exercises in it. Let's explore that.
