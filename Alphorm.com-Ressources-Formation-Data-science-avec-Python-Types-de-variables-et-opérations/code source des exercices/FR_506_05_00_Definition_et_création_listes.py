# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 12:18:41 2018

@author: danam
"""

# =============================================================================
#      cr�ation de liste avec [item1, item2, ..., itemN]
# =============================================================================
# cr�ation de liste vie
list_vide = []
# affichage de liste
print(list_vide)
# cr�ation de listes avec des �l�ments
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
# cr�er une liste 
liste_vide1 = list()
print(liste_vide1)
# cr�er une liste � partir d'un autre objet
lettres = list('Python 3.6.4')
print(lettres)
# � partir de tuple
tuple_nombres = 1,2,3,4
list(tuple_nombres)
