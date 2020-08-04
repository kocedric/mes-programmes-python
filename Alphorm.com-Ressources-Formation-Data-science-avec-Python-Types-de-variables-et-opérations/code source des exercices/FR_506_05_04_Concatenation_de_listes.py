# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 12:18:41 2018

@author: danam
"""

# =============================================================================
#           concatener avec la méthode extend()
# =============================================================================
# créer des listes
x = [1, 2, 3]
y = [4, 5, 6]
x.extend(y) # concatener x et y et affecter x le résultat
# afficher x
x
x.extend([7])
x
# =============================================================================
#          concatener avec l'opérateur +
# =============================================================================
lettres = ['a','b','c']
chiffres = [1, 2, 3, 4]
# concatenation et affectation 
alphaNumeric = lettres + chiffres 
# afficher
alphaNumeric
# opération litérale
lettres = lettres + ['d', 'e', 'f']
lettres
# opération composée
lettres += ['g', 'h', 'i']
lettres

# =============================================================================
#         concatenation de n fois la même liste 
#                          ou 
#          répetition n fois de la même liste 
#                      avec *
# =============================================================================
n = [10]
rep5n = n * 5
rep5n
# ou 
[10] + [10] + [10] + [10] + [10]

x = [2]*3 + [3]*4 + [4]*5
x
