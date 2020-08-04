# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 22:45:41 2018

@author: danam
"""
# importer le package numpy
import numpy as np
# =============================================================================
#                       Broadcasting
# =============================================================================
a = np.matrix('2 2 3')
a.shape
b = np.matrix('5 2 7')
b.shape
# exemple d'opération : addition de a et b
a + b
# ou 
np.add(a,b)
# cas de Broadcasting  avec une matrice de 2D vs 1D
A = np.matrix('0 5 6; \
               5 2 8; \
              -5 7 3')
A + a
# cas de  Broadcasting avec une matrice de 1D vs scalaire
a + 5
A - 1
# cas de Broadcasting avec une matrice 3x1 vs 1x3
c = np.matrix('-2; 5; 9') # 3x 1
c.shape 
c + a

# cas d'exception
Z = np.matrix([1, 2, 3, 5])
Z + c # fonctionne
Z + a # erreur
Z + b # erreur 
Z + A # erreur

# =============================================================================
#          Opérations arithmétiques
# =============================================================================
# matrice et scalaire
A + 5 # addition 
# ou
np.add(A, 5)
A * 3 # multiplication
# ou
np.multiply(A, 3)
A / 2 # division 
np.divide(A, 2)
A - 10 # soustraction
np.subtract(A, 10)

# entre des matrices
X = b + c # addition
A + X 
# ou
np.add(A, X)
A / X
# ou
np.divide(A, X)
A * X
# ou
np.multiply(A, X)
A - X
np.subtract(A, X)

# =============================================================================
#            Autres opérations
# =============================================================================
np.log10(Z) # logarithme
np.absolute(c) # valeur absolue 
np.power(b, a) # puissance  5^2 2^2 7^3
