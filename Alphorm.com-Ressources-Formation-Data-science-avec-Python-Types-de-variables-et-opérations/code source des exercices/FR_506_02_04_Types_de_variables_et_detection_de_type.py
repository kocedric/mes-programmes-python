# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 12:18:41 2018

@author: danam
"""

# Créer des variables numériques
x = 5
y = 6
# Créer des variables Strings
a = "Python"
b = "b"
# Créer des variables booléennes
estNombre = True
# Créer des variables itérables
tableau = [2, 3, 5]
tableau2 = 2,3,5

### Détection de type de variables
# avec type()
type(a)
type(x)
type(estNombre)
# avec isinstance()
isinstance(x,int)
isinstance(a,int)
isinstance(a,str)
isinstance(tableau,list)
a = 3.5
type(a)
isinstance(a,float)
