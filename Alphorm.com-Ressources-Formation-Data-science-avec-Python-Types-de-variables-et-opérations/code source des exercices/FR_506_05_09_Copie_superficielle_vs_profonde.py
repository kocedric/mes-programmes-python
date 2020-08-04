# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 12:18:41 2018

@author: danam
"""

# cas de copie superficielle ou shallow copy
x = [1, 2, 3, 4, 5]
y = x  # affectation 
x[2] = 'Hey je suis un intrus' # altérer ou modifier un élément de x

# copie profonde ou deep copy
x = [1, 2, 3, 4, 5]
y =  x # affectation copie superficielle
y1 = x.copy()  # (1) avec la méthode copy()
y2 = list(x)   # (2) avec le constructeur list()
y3 = x[:]      # (3) avec affectation par valeur ou par extraction des valeurs
x[4] = 'Hey je suis un intrus !' # altérer ou modifier un élément de x
x # le 5ème élément de x est modifié
y # le 5ème élément de y également est modifié
y1 # n'est pas modifié
y2 # n'est pas modifié
y3 # n'est pas modifié
