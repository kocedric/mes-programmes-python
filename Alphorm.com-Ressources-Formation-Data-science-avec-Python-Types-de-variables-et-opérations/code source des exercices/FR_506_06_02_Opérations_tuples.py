# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 12:18:41 2018

@author: danam
"""

# =============================================================================
#                 extraction des éléments d'un tuple
# =============================================================================
# création d'un tuple
xtuple = ('a', 2, [2, 3, 5])
# extraction avec l'opérateur [:]
xtuple[0] # extraire le premier élément
# ou 
xtuple[-3] 
xtuple[1:3] # extraire une séquence 
xtuple[::-1] # inverser l'ordre des éléments dans la liste
# extraction par déballage ou tuple unpacking
lettre, chiffre, liste = xtuple
lettre
chiffre
liste
# échanger des objets entre variables
a = 5
b = 6
b, a = a, b
a
b
# =============================================================================
#                   les méthodes de tuple
# =============================================================================
x = (2, 0, 3, 4, 6, -2, 0, 5, 0)
# la méthode count()
x.count(0) # compter le nombre d'occurence de 0
# la méthode index()
x.index(0) 
x.index(4)

# =============================================================================
#                  les fonctions génériques 
# =============================================================================
# la fonction len() : renvoie le nombre d'élément d'un tuple
len(x)
# la fonction sum(), max() et min()
sum(x)
max(x)
min(x)
# la fonction sorted() pour le tri
sorted(x)
sorted(x, reverse = True)

# =============================================================================
#                         autres opérations 
# =============================================================================
# concatenation (+)
(0, 2, 4) + (6, 8, 10)
(lettre,) + (chiffre,) + (liste,)  # ça donne xtuple 
# repetion ou concatenation n fois le même tuple avec *
(0, 2, 4) * 3
# ou 
(0, 2, 4)  + (0, 2, 4) + (0, 2, 4) 
