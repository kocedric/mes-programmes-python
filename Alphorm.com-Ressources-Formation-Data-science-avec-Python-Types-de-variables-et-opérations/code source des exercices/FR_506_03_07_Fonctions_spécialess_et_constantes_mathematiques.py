# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 12:18:41 2018

@author: danam
"""

# importer le module
import math
# =============================================================================
#                fonctions spéciales
# =============================================================================
#(1) la fonction d'erreur 
math.erf(0.5)
# la fonction d'erreur complémentaire
math.erfc(0.5)
# ou
1 - math.erf(0.5)
# la fonction cumulative de distribution normale standard
def normCDF(x):
    val = 0.5*(1 + math.erf(x/math.sqrt(2)))
    return val
# P(x < 0)
normCDF(0) # ~ 0.5
# P( -1.96 < x < 1.96)
normCDF(1.96) - normCDF(-1.96) # ~ 0.95

# (2) la fonction gamma
math.factorial(2)  # 1*2
# erreur factoriel d'un nombre non entier
math.factorial(2.5) 
# factoriel d'un réel ou complex
math.gamma(2.5)
# gamma() vs factorial()
math.factorial(3) # 3*2*1
math.gamma(3) # 2*1
math.gamma(4) # équivaut à math.factorial(3)
# log de la valeur absolue de gamma
math.lgamma(3)
# ou 
math.log(math.gamma(3))

# =============================================================================
#                  les constantes mathématiques
# =============================================================================
# la valeur de pi
math.pi # ~ 3.14159
# la nombre euler
math.e # ~ 2.718
# le ratio tau : circ = 2*Pi*r=> 2P = circ/r
math.tau
# ou
math.pi*2
###  l'infini
float('inf')
# ou avec math
math.inf
val_inf = - float('inf')
# tester si c'est une valeur finie
math.isfinite(val_inf)
# ou tester si c'est une valeur infinie
math.isinf(val_inf)
### les NAN Not A Number
float('nan')
# ou avec math
math.nan
val_nan = float('nan')
# tester si c'est une valeur finie
math.isfinite(val_nan)
# ou tester si c'est une valeur NAN
math.isnan(val_nan)

