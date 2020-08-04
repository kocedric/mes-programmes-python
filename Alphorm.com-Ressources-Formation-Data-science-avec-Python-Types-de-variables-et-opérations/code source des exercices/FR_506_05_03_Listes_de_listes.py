# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 12:18:41 2018

@author: danam
"""

# créer une liste de listes 2 D
tableau = [['A', 'B', 'C', 'D'],
           ['a', 'b', 'c', 'd'],
          [1, 2, 3, 4, 5, 6, 7]]
# afficher 
tableau
# extraire la liste des lettres miniscules
tableau[1]
# ou
tableau[-2]
# extraire la liste des chiffres
tableau[2]
# ou 
tableau[-1]
# extraire la lettre B
tableau[0][1]
# ou
tableau[-3][-3]
# extraire le chiffre 7
tableau[-1][-1]
# ou 
tableau[2][6]

# liste de listes en 3D
fiche = [['Python',[0.0, 2.7, 3.6]],
        ['R',      [0.0,3.3,3.5]]]
# extraire la première ligne ou celle où se trouve Python
fiche[0]
# extraire le nom d'un langage 
fiche[0][0] # extraire 'Python'
# ou 
fiche[1][0] # extraire 'R'
# extraire une version
fiche[0][1][1] # extraire 2.7
fiche[1][1][2] # extraire 3.5
fiche[1][1][1:] # extraire 3.3 et 3.5
