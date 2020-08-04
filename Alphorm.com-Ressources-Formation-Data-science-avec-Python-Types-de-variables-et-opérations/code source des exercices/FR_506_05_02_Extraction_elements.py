# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 12:18:41 2018

@author: danam
"""

# créer une liste pour illustrer les opérations
jours = ['Lundi','Mardi','Mercredi','Jeudi','Vendredi','Samedi','Dimanche']
# positive : 0      1          2       3       4            5        6
# negative : -7     -6        -5       -4      -3          -2        -1
# =============================================================================
#                     Extraction d'un élément [n]
# =============================================================================
# extraire lundi 
jours[0]
# ou 
jours[-7]
# extraire Samedi
jours[5]
# ou
jours[-2]
# extraire Dimanche 
jours[6]
# ou 
jours[-1]
# =============================================================================
#    Extraction d'élements [debut:fin] avec debut inclus  et fin exclus
# =============================================================================
# extraire les élements allant de Mardi à Vendredi 
jours[1:5]
# ou
jours[-6:-2]
# extraire les élements à partir de debut
jours[2:] # à partir de Mercredi jusqu'à la fin de la liste
# extraire les élements jusqu'à fin 
jours[:4] # de debut de la liste jusqu'à Jeudi

# =============================================================================
#    Extraction d'élements [debut:fin:pas] avec debut inclus  et fin exclus
# =============================================================================
# extraire les élements d'indexe pair
jours[::2]
# extraire les élements de Mardi jusqu'à samedi (inclus) pas de 2
jours[1:6:2]
# ou 
jours[-6:-1:2]
# inverser l'ordre des élements d'une liste
jours[::-1]
