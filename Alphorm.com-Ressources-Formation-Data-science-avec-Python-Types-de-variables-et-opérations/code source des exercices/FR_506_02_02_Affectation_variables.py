# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 12:18:41 2018

@author: danam
"""

### définitions de variables ####
x = 12
# identifiant de variable
id(x)
# réaffectation de variables
x = "Python"
id(x)

### affectation multiple
x = y = z = 10
id(x)
id(y)
id(z)

### affectations mutliples
nom, age, sexe = "Jean", 18, "M"
id(nom)
id(age)
id(sexe)

### affecation variable à variable
a = 12
b = a
id(a)
id(b)