# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 12:18:41 2018

@author: danam
"""

# créer un dictionnaire 
fiche = dict.fromkeys(['Nom', 'Age', 'Poids'])
table = {}
produits = {'A' : 12.5, 'B' : 20,  'C': 30, 'D' : 40}

# modification d'éléments(valeurs) en affectant des valeurs
# connaissant sa clé avec ['clé'] 
fiche['Nom'] = ['Dave', 'Alice']
fiche['Age'] = [19, 18]
fiche['Poids'] = [70, 65]
fiche
fiche.values()

# ajouter des élements(clés-valeurs) dans un dictionnaire avec update()
table.update({'ProduitA': {'Qte' : 1000, 'Pu'  : 20.75},
              'ProduitB': {'Qte' : 2000, 'Pu'  : 30.50},
              'ProduitC': {'Qte' : 2500, 'Pu'  : 40.00}})
table.values() # extraire les valeurs uniquement
table.keys() # extraire les clés uniquement
# ajouter un élément à table
table.update({'ProduitD' : {'Qte' : 3000, 'Pu'  : 45.50}})
table.items() # extraire les pairs clés-valeurs
table.keys() # extraire les clés uniquement

# ajouter un élement clé -valeur mais dont la clé existe déja
autres_produits = {'E' : 25, 'D' : 30}
# afficher les clé -valeurs de produits 
produits.items()
# mettre à jour avec autres_produits
produits.update(autres_produits)
# afficher les clé -valeurs de produits après ajout de autres_produits
produits.items()
