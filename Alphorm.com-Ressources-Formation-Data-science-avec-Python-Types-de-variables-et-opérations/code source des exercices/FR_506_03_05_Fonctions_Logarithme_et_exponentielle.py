# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 12:18:41 2018

@author: danam
"""

# importer le module math
import math
# =============================================================================
# # les fonctions logarithmes
# =============================================================================
# log base e
math.log(2) 
# log base 10
math.log(2, 10)
# ou
math.log10(2)
# log base 2
math.log2(10)
# ou
math.log(10, 2)
# log(1 + x) pour x ~ zéro
xplus1 = 1.0029
math.log(xplus1)
# avec meilleure précision
math.log1p(0.0029)

# =============================================================================
# # les fonctions exponentielles
# =============================================================================
# exponentiel
math.exp(0) # 1
math.exp(1) # e
math.exp(-1) # 1/e
# exponentiel de x
x = math.log(2) 
math.exp(x) # 2
# ou 
math.exp(1)**x
# e(x) - 1 pour x ~ zéro
math.exp(0.005) - 1
# ou pour une meilleure précision  
math.expm1(0.005)

# puissance  avec pow()
math.pow(2,10)
# ou
2**10
# racine carrée
math.sqrt(4)
# ou
4**0.5
