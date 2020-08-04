# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 12:18:41 2018

@author: danam
"""

# importation du module math
import math
# =============================================================================
#                 les fonctions arithmétiques
# =============================================================================
# somme avec la fonction fsum()
v = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
sum(v) # fonction native python
math.fsum(v)
# valeur absolue avec fabs()
math.fabs(-2.5)
# factoriel avec factorial()
math.factorial(4) 
1*2*3*4 # manuellement
# test d'approximation isclose()
x = 2.9999
y = 3
math.isclose(x,y)
math.isclose(x,y,rel_tol = 1e-3)
# test de dection de nombres finis isfinite()
val = 2.3
math.isfinite(val)
ival = float('inf')
math.isfinite(ival)

# =============================================================================
#                     fonctions de représentation ou arrondi 
# =============================================================================
# arrondir n chiffres après la virgule
round(x) 
round(x,2)
round(2.356)
round(2.356,2)
# arrondir à l'entier le plus grand(plafond) avec ceil()
math.ceil(val)
# arrondir à l'entier le plus plus petit(plancher) avec floor()
math.floor(val)
# arrondir à la valeur entière trunc()
math.trunc(val)
int(val)
