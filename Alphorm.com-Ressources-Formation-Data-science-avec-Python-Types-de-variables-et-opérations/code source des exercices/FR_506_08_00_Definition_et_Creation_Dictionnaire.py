# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 12:18:41 2018

@author: danam
"""

# =============================================================================
#         création de dictionnaire avec {}
# =============================================================================
# créer un dictionnaire vide 
dict_vide = {}
dict_vide
# créer un dictionnaire
description = {'nom' : 'Python', 'version' : [2.7, 3.5, 3.6, 3.7]}
description
type(description)
data = {'x' : [12, 23, 25, 23, 58],
        'y' : [15, 23, 25, 20, 40],
        'z' : [25, float('nan'), 20, 36, 30]}
data
liste = {1 : 'C', 2 : 'C++', 3 : 'Java', 4: 'C#', 5: 'Python' }
liste
# =============================================================================
#             créer des dictionnaire avec dict()
# =============================================================================
# créer un dictionnaire vide
dict_vide1 = dict()
dict_vide1
# créer un dictionnaire par coercition de liste de listes
list_de_list  = [[1 , 'C'], [2 ,'C++'], 
                 [3 , 'Java'], [4 , 'C#'], [5, 'Python']]
d0 = dict(list_de_list)
d0
type(d0)
# créer un dictionnaire par coercition de liste de tuples
list_de_tuples = [('a', 1), ('b', 2), ('c', 3)]
d1 = dict(list_de_tuples)
d1
# créer un dictionnaire par coercition de liste de chaîne de caractères
list_de_str = ['12', '52', '22', 'aa', 'bb']
d2 = dict(list_de_str)
d2
# créer un dictionnaire par coercition de tuple de listes
tuple_de_list  = ([1 , 'C'], [2 ,'C++'], 
                 [3 , 'Java'], [4 , 'C#'], [5, 'Python'])
d3 = dict(tuple_de_list)
d3
# créer un dictionnaire par coercition de tuple de chaîne de caractères
tuple_de_str = ('12', '52', '22', 'aa', 'bb')
d4 = dict(tuple_de_str)
d4

# =============================================================================
#    créer des dictionnaires à partir de clés avec dict.fromkeys()
# =============================================================================
d5 = dict.fromkeys(['Nom', 'Age', 'Ville', 'taille'])
d5
d6 = dict.fromkeys((1, 2, 3, 4))
d6
