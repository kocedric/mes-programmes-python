# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 12:18:41 2018

@author: danam
"""

# =============================================================================
#                          la méthode count(x)
#   renvoie le nombre d'occurence d'un élément dans une liste
# =============================================================================
x = ['a', 1, 'b', 1, '1', 'c', 'a', 'b', 1 ]
x.count(1) # le nombre d'occurence de 1 dans x
x.count('b') # le nombre d'occurence de 'b' dans x

# =============================================================================
#                         la méthode index() 
#           renvoie la position d'élement dans une liste 
# =============================================================================
x.index('1') # position de '1'
x.index(1) # par défaut position de la première occurence
x.index(1, 2, 8) #  position de 1 entre le 2ème et le 8ème élément
x.index(1, 4, 9) # position de 1 entre le 4ème et le 8ème élément

# =============================================================================
#                       la methode reverse() 
#               inverse l'ordre des éléments d'une liste
# =============================================================================
x.reverse()
x
x[::-1] # inverser à nouveau pour revenir dans l'ordre initial

# =============================================================================
#                            la methode sort()
#    renvoie la trier par ordre croissant/ decroissant des éléments
# =============================================================================
A = ['b', 'd', 'z', 'i', 'c']
A.sort() # par défaut ordre croissant 
A
A.sort(reverse = True) # ordonner dans l'ordre décroissant
A
Y = [0, -float('inf'), 2, -5, 10, float('inf')]
Y
Y.sort()
Y
Y.sort(reverse = True)
Y
