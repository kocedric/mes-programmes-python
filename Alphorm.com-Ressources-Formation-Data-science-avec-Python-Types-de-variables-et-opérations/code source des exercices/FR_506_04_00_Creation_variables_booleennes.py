# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 12:18:41 2018

@author: danam
"""

# création de variables booléennes
x = True
y = False
# coercition d'un type spécifique en booléen bool()
# type numerique en booléen renvoie toujours True
bool(1)
bool(3.5)
True + 1
# sauf 0 ou 0.0 ou 0j qui renvoie False
bool(0)
bool(0.0)
bool(0j)
# tout objet convertit en booléen renvoie True sauf :
# - l'objet None
bool(None)
# - les objets itérables vides
l = [] # liste vide
t = () # tuple vide
c = "" # chaîne de caractère vide
bool(l)
bool(t)
bool(c)
