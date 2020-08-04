# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 12:18:41 2018

@author: danam
"""

# créer un dictionnaire pour illustration
produits = {'A': 12.5, 'B': 20.5, 'C' : 30, 'D' : 40 }
# dictionnaire de dictionnaires
table  = {'Dave' : { 'Math' : 15, 'Fr' : 13, 'Geo' : 15},
          'Alice' : { 'Math' : 16, 'Fr' : 15, 'Geo' : 12},
          'Berny' : { 'Math' : 10, 'Fr' : 12.5, 'Geo' : 15},
          'Cavani' : { 'Math' : 9.5, 'Fr' : 16, 'Geo' : 11.5}}

# test d'existence de clé avec  in
'A' in produits # True
'E' in produits # False
'a' in produits # False

# extraire un élément(valeur) connaissant sa clé avec ['cle'] 
produits['A'] # extraire le prix du produit A
produits['D'] # extraire le prix du produit D
table['Dave'] # extraire les notes de Dave
table['Dave']['Math'] # extraire la note de Math de Dave
table['Alice']['Fr']  # extraire la note de Français de Alice

# extraire un élement(valeur) connaissant sa clé avec get()
produits.get('A') # extraire le prix du produit A
produits.get('D') # extraire le prix du produit D
table.get('Dave') # extraire les notes de Dave
table.get('Dave').get('Math') # extraire la note de Math de Dave
table.get('Alice').get('Fr')  # extraire la note de Français de Alice

# extraire tous les éléments ou valeurs avec values()
produits.values()  
list(produits.values()) # obtenir les valeurs sous forme de liste 
table.values()
list(table.values())  # obtenir les valeurs sous forme de liste 

# extraire toutes les clés avec keys()
produits.keys()
list(produits.keys())
table.keys()
list(table.keys())

# extraire les pairs clés - valeurs avec items()
produits.items()
list(produits.items())
table.items()
list(table.items())
