# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 12:18:41 2018

@author: danam
"""

# importer les modules
import math
import cmath
# calcul de la racine carré de x
x = 4
math.sqrt(x) # renvoie un réel
cmath.sqrt(x) # renvoie un complexe
# 
y = -1
math.sqrt(y) # erreur
cmath.sqrt(y)
# 
math.nan
cmath.nanj
# ou
complex(0.0,float('nan'))
# 
math.inf
cmath.infj
# ou
complex(0.0,float('inf'))

