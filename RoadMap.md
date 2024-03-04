The project stakeholders are French and roadmap items are (hopefully) short-lived so it's not worth translating them.
But as French as I am, my brain has been rewired to think in English when I make software.
So this document is partly in French and partly in English, thank you for your understanding.

> Text like this is a direct quote from a stakeholder.

Other text is mine.

# Known bugs

None at the moment.

# Functional roadmap

## 20240314

### Add this roadmap to the help page

### Log user actions on the PDF

Olivier Pons would love to know which rectangles were used to extract which text.

### Display textbook title on extraction page

> Il manque le nom du manuel en haut.

### Allow textual exercice identifiers

> Il manque un champ numéro d'exercice, indispensable pour nous. Il faudrait réduire le champ page en longueur et mettre à côté un champ numéro d'exercice. Attention certains exercices sont indiqués non pas par un numéro mais par un nom (par exemple Défi Langue). Il faut donc pouvoir mettre Defi Langue dans le champ du numéro de l'exercice.

### Attach exercises to a project

Instead of a textbook.

### Add a view for a project

> Centraliser les exercices d'un manuel. Avec mise en valeur des exos pas extraits.

## 20240404

### Add users and profiles

"Users" belong to "organisations".
All users can list all their organisation's projects and none from other organisations.
"Viewers" can with a few selected projects.
"Editors" can edit a few selected projects.
"Admins" can edit all projects and grant viewer and editor role to some users.

### Keep a history of who does what

## Later

### Ensure concurrent use is safe

How can Gabby help coordinating several people working on the same textbook? Locks? Merging? Conflict resolution? Simple flags saying "[Name] is working on this page"? Continuous save and update in other's view?

### Ensure safety of DB

Extracted exercises are copyrighted material. We should ensure their safety.

### Keep formatting

> Est-ce qu'il y a un moyen de garder les caractéristiques typographiques genre souligné ou gras facilement ? Parce que parfois, il faut remplacer le mot en gras par exemple.

It's difficult in general because the PDF does not contain the information:

- https://github.com/mozilla/pdf.js/issues/7372#issuecomment-222665266
- https://github.com/mozilla/pdf.js/issues/7297#issuecomment-217627918
- https://stackoverflow.com/a/28068493/905845

A few ideas:

- Grouped by fontName, on the whole page:
    - Measure the average darkness of rendered text rectangles. The darker, the more likely it is bold.
    - Measure the amount of slanted transitions between black and white pixels in the rendered text (i.e. detect slanted line in the gradient). The more slanted, the more likely it is italic.
- The same idea, but on the glyphs in the fonts.
- Try to render the text with a bold font and compare the result with the original rendering. If the result is similar, it's bold. This approach could also work for italic text, and bold italic text.
- Use the relative number of chars in each font. We could assume that the most used font is the normal one, the second most used is the bold one, and the third most used is the italic one.

### Ensure usability

Gabby must be usable with screen readers and similar technologies.

> Pour l'ergonomie, Jérôme demande si tu veux interagir avec lui maintenant ou si on attend que tu aies implémenté plus de fonctionnalités avant de se pencher sur l'ergonomie ?

### Automate

> Du côté de l'automatisation : Olivier me dit qu'Elise et lui ont beaucoup travaillé récemment sur l'extraction à partir de la visualisation et donc qu'il y aurait la possibilité de rentrer à gauche des fichiers avec des cadres déjà faits qu'il n'y aurait donc plus qu'à valider ou à retracer si ce ne sont pas les bons. Est-ce envisageable ? Et que faudrait-il faire pour que ce soit implémentable à terme ?

### Allow images in exercices

> On a besoin de pouvoir inclure les images des exercices

Make sure they are included in the DB backups.

### Customize the floating modal

> En termes d'ergonomie de la fenêtre qui s'ouvre quand on sélectionne, il faudrait qu'on puisse l'agrandir et la déplacer. Pour la police, il faudrait mettre de l'arial par défaut. Idéalement, il faudrait que ce soit paramétrable pour chaque adaptateur (taille de la fenêtre, emplacement, police, taille de la police, interligne).

### Handle multiple choice questions

> Il se pose la question des choix qui sont un champ spécifique dans l'adaptation pour les exercices à choix multiples type Cartable. Les choix peuvent être dans la consigne, sous la consigne, dans l'énoncé et ils sont un élément spécifique de l'adaptation. Il faut qu'on voit qu'elle est la meilleure option. Je te mets en PJ les différents types d'exercices à Choix Multiples. Est-ce que tu veux qu'on échange en visio sur ce point ?

### Handle columns

(Maybe never, if integrating Olivier and Elise's automation is enough.)

> Quand le texte est en 2 colonnes, on est obligé de sélectionner la première colonne puis la seconde si on veut que ça se mette dans l'ordre. Je ne sais pas si c'est arrangeable.

### Adapt exercises

Implement the third column.

> Types d'exos à adapter en priorité:
> - mots à cocher
> - remplir au clavier
> - QCM

### Export adapted exercises

Exporting as a .zip file is error-prone.

It should be possible to export as a single html file, with all the exercises in it. Let's explore that.

# Technical roadmap

See `git grep '@todo'`.
