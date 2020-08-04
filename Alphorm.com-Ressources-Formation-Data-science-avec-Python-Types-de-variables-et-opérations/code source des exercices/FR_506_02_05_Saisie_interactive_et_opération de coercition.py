# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 12:18:41 2018

@author: danam
"""

# =============================================================================
#             Saisie interactive
# =============================================================================
#%%
# demander à l'utilisateur de saisir son nom
nom = input("Quel est votre nom ? ")
# afficher le nom de l'utilisateur
print("Il s'appelle ", nom)
#%%
# demander à l'utilisateur de saisir sa taille
taille = input("Quelle est votre taille ?")
# afficher la taille de l'utilisateur 
print("Il mesure", taille, "m")

#%%
# =============================================================================
#              Opération de coercition
# =============================================================================
taille_numeric = float(taille)
#%%
# saisir une valeur numérique
x = int(input("saisir une première valeur numérique :"))
# saisir une autre valeur 
y = int(input("saisir une seconde valeur numérique :"))
# afficher la somme
x + y
#%%
# saisir des tableaux
lettres = list(input("Entrer des lettres : "))
print(lettres)
# cas de tuples
lettres = tuple(input("Entrer des lettres : "))
print(lettres)

