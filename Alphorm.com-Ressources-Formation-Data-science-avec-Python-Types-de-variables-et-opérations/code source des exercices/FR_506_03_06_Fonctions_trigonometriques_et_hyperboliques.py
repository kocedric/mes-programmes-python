# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 12:18:41 2018

@author: danam
"""

# importer le module
import math
# =============================================================================
#             fonctions trigonometriques (circulaire x^2 + y^2 = 1)
# =============================================================================
# définition de PI
PI = 3.1415
#(1) la fonction cosinus
math.cos(PI/3) # ~ 1/2
# réciproque arc cosinus
math.acos(1/2) # ~ PI/3
#(2) la fonction sinus
math.sin(PI/6) # ~ 1/2
# réciproque arc sinus
math.asin(1/2) # ~ PI/6
#(3) la tangente
math.tan(PI/4) # ~ 1
# réciproque arc tangente
math.atan(1) # ~ PI/4
# la fonction de calcul de la norme eucludienne sqrt(x^2 + y^2)
math.hypot(1,1)
# =============================================================================
#                    les fonctions hyperboliques ( x^2 - y^2 = 1)
# =============================================================================
math.cosh() # cosinus hyperbolique
math.acosh() # arc cosinus hyperbolique 