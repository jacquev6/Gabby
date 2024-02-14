# Documentation utilisateur

## Structure générale

La vue principale est divisée en trois colonnes :

- le PDF du manuel scolaire en entrée
- la zone d'édition
- la zone de pré-visualisation

Ces colonnes correspondent aux deux principales étapes de l'adaptation d'exercices depuis un manuel scolaire :

- la première consiste à extraire du PDF les textes et images (pas encore implémentée) des exercices, de la première à la deuxième colonne
- la seconde, à décrire comment adapter les exercices extraits, de la deuxième colonne à la troisième (pas encore implémentée)

![Screenshot](/help/three-columns.png)

## Extraction du texte du PDF

L'extraction du texte du PDF se fait en dessinant à la souris un rectangle autour du texte souhaité.
Le texte trouvé à l'intérieur de ce rectangle est mis en surbrillance:

![Screenshot](/help/selecting-in-pdf.png)

Lorsqu'on relâche le click de la souris, le texte est extrait et affiché dans une boite de dialogue,
à proximité immédiate du pointeur pour limiter les déplacements de souris:

![Screenshot](/help/selected-in-pdf.png)

On peut alors cliquer sur un des boutons de ce dialogue pour ajouter le texte dans le champ correspondant du formulaire d'édition.
