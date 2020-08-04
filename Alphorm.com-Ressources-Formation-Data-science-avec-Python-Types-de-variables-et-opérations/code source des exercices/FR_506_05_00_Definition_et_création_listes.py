# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 12:18:41 2018

@author: danam
"""

# =============================================================================
#      création de liste avec [item1, item2, ..., itemN]
# =============================================================================
# création de liste vie
list_vide = []
# affichage de liste
print(list_vide)
# création de listes avec des éléments
jours = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi','Vendredi']
print(jours)
notes = [12.5, 15, 16, 13, 10]
print(notes)
mixtes = ['Python', 12.5, 7, True, '12/09/2017',
         10 - 2j, float('inf')] 
print(mixtes)

# =============================================================================
#                 constructeur de liste avec list()
# =============================================================================
# créer une liste 
liste_vide1 = list()
print(liste_vide1)
# créer une liste à partir d'un autre objet
lettres = list('Python 3.6.4')
print(lettres)
# à partir de tuple
tuple_nombres = 1,2,3,4
list(tuple_nombres)
