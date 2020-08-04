# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 12:18:41 2018

@author: danam
"""

# =============================================================================
#                          les tuples sont immutables
# =============================================================================
# les tuples implémentes mieux le concepts de constantes
xtuple = 'a', 'b','c' # tuple
xtuple[0] = 'b' # erreur
xliste = ['a', 'b','c'] # liste
xliste[0] = 'b' # fonctionne
xliste
# exceptionnellement on peut altérer 
# le contenu d'un objet mutable dans un tuple !!!
x = (2, 3, [2, 3], 6) 
x[2][0] = 'Python !' # fonctionne !

# =============================================================================
#                     les tuples consomment moins d'espace memoire(bytes)
# =============================================================================
import sys
tup = (1, 2, 3, 4, 5) 
lis = [1, 2, 3, 4, 5]
print('Taille memoire du tuple :', sys.getsizeof(tup))
print('Taille memoire de liste :', sys.getsizeof(lis))

# on peut créer des tuples nommés
# on peut utiliser les tuples comme clés dans un dictionnaire
# les arguments de fonctions sont passés sous forme de tuple