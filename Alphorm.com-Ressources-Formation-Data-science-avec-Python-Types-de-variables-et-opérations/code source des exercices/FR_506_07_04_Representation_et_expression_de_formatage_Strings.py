# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 12:18:41 2018

@author: danam
"""

# =============================================================================
#                Représentation de chaîne de caractères
# =============================================================================
txt = 'Python est un langage \n- Orienté objet\n- Scientifique'
# affichage implicite
txt
# affiche explicite (avec évaluation du contenu)
print(txt)
# representation avec str() evalue le contenu de la chaîne de caractère
print(str(txt))
# representation avec repr() retourne le contenu tel quel
print(repr(txt))

# =============================================================================
#            les expressions de formatage avec %
# =============================================================================
# formatage de chaîne de caractère %s
nom = 'Python'
'%s est un langage'%nom
'%s  est un %s'%(nom,'langage')

# formatage de nombre %d  (entiers relatifs)
from math import pi as PI
'%d est le ratio ...'%PI
'%03d est le ratio ...'%PI

# formatage de nombre avec %f (nombres à virgule flottante)
'%.3f est le ratio ...'%PI # 3 chiffres après la virgules
'%s = %.3f est le ratio ...'%('PI', PI)
'%s = %07.3f est le ratio ...'%('PI', PI)

# formatage de nombre avec %E ou %e (notation scientifique)
'%s = %E est le ratio ...'%('PI', PI)
# ou
'%s = %e est le ratio ...'%('PI', PI)


