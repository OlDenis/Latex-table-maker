# Latex-table-maker
Créer un tableau LaTeX à partir de listes python imbriquées!

Pour utiliser :

1. Cloner le répertoire localement:
```
git clone git@github.com:OlDenis/Latex-table-maker.git
```
2. Copier Table.py dans le dossier de votre projet
3. Importer la class Table dans votre projet:
```
from Table import Table
```
4. Créer la table:
```
myTable = Table( rows, col_names, row_names=None, indent=3, title=None, diff_last_row=0)
```
```
rows : [[r,o,w,1],[r,o,w,2],...] : Liste de listes contenant les valeurs du tableau.
col_names : [col_name1, col_name2, ... ] : Liste contenant les noms des colonnes.
row_names : [row_name1, row_name2, ... ] : Liste contenant les noms des rangées.
indent    : int : Nombre d'indentation du tableau.
title     : str : Titre du tableau.
diff_last_row : int : Nombre de rangées séparées par une double ligne au bas du tableau.
```
