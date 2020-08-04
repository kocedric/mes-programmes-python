# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 12:18:41 2018

@author: danam
"""

# créer une liste 
x = ['a', 1, 'b', 2, 'c', float('inf'),'d', 0, 'e', 'f',8, 'g', 'z']

# suppresion avec la commande del 
del x[3]  # supprimer le chiffre 2
x
del x[-11] # supprimer le chiffre 1
x
# suppression avec la méthode pop(n), où n est la position de l'élement
x.pop() # sans argument supprime le dernier élément de la liste
x
x.pop(5) # supprimer le chiffre 0 de la liste 
x
# suppression avec la méthode remove(x), où x est l'élément
# et si x à plusieurs occurence dans la liste 
# c'est la première qui est supprimée
x.remove(float('inf')) # supprimer inf
x
x.remove(8) # supprimer l'élement 8
x
x.remove('g') # supprimer l'élemnt 'g'
x
# ajouter l'élément 'c' à x
x.append('c')
x 
x.remove('c') # supprime la première occurence de c
x

# la commande del à l'avantage toutefois de permettre la suppression
# de plusieurs élément à la fois 
del x[2:4] # supprime d et e
y = list(range(11))
del y[::2] # supprimer tous les nombres pairs
y

