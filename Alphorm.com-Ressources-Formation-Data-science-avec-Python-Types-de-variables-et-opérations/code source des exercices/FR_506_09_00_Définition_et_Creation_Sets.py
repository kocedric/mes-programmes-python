# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 12:18:41 2018

@author: danam
"""

# =============================================================================
#                     Création de Set ou ensembles avec set() ou {}
# =============================================================================
# créer un vide set avec set()
set_vide = set()
set_vide
# créer des sets avec {}
entier = {1, 0, 2, 3, 5}
entier
pairs = {2, 4, 6, 8, 10}
pairs 
# type 
type(entier)

# sets sont des objets mutables mais d'admettent pas de doublons
x = {0,0,1,2,2,2}
x

# sets sont des objets mutables mais d'admettent pas d'élements mutables
set_valide = {1, 'a', 2, 3, (1, 2,3)}
set_valide
set_invalide = {1, 'a', 2, 3, [1, 2,3]} # erreur 

# coercition : list en set 
#%%%
liste = ['a', 'b', 'c', 'y', 'j']
set_de_list = set(liste)
set_de_list
# coercition : tuple en set
#%%
tupl = (2, 3, 5, 6, 8) 
set_de_tuple = set(tupl)
set_de_tuple
# coercition : string en set
#%%
char = 'Python est interessant !'
set_de_string = set(char)
set_de_string
# coercition : dictionnaire en set
#%%
dic = {'a' : 12, 'b' : 25, 'c' : [2, 3, 5]}
set_de_dict = set(dic)
set_de_dict
#%%
# =============================================================================
#                      Frozenset ou Ensemble immutable  
# =============================================================================
# les sets sont mutables
x.add(3)
x
# les sets immutables
set_const = frozenset([2, 3, 5, 6])
set_const
type(set_const)
