# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 12:18:41 2018

@author: danam
"""

# =============================================================================
#  remplacer le champ de formatage '... {nom ou position}...'.format() 
# =============================================================================
# remplacement par défaut
'langage {}, version {}'.format('Python', '3.6.0')
# remplacement par spécification de position 
'langage {0}, version {1}'.format('3.6.0','Python') 
# remplacement par spécification de nom
'langage {nom}, version {version}'.format(version = '3.6.0', nom = 'Python') 
# remplacement en utilisant une liste 
A = ['a', 'aa']
B = [1, 2]
txt = '{0[0]} = {1[0]} lettres de a\n{0[1]} = {1[1]} lettres de a'.format(A, B)
print(txt)

# =============================================================================
# la spécification de formatage  {nom ou position : format }
# =============================================================================
from math import pi as PI
# formater PI avec 2 chiffres après la virgule
'{0} vaut environ {1:.2f}'.format('PI', PI) 
'{0} vaut environ {1:+.2f}'.format('PI', PI) 
# formater PI avec 3 chiffres après la virgule sur 7 caractères
'{0} vaut environ {1:07.3f}'.format('PI', PI) 
# formater PI en notation scientifique 
'{0} vaut environ {1:e}'.format('PI', PI)
'{0} vaut environ {1:E}'.format('PI', PI)

# formter avec des séparateurs de milliers
'{0:,d} + {1:,d} = {2:,d}'.format(100000, 1285000, 1385000)
'{:,.3f}'.format(1555555.55263)
'{:+,.3f}'.format(1555555.55263)
'{:+,.3f}'.format(-1555555.55263)

# extraction de portion de chaîne de caractère
'{:.5}'.format('langage Python')

# justifier 
'{:>5}'.format(10) # justifier à droit
'{:<5}'.format(10) # justifier à gauche


