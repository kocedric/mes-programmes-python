# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 12:18:41 2018

@author: danam
"""

# =============================================================================
#        ajout d'élements avec append()
# =============================================================================
noms = ['Python']
# ajout simple d'élément avec append() 
noms.append('R')
noms
noms.append('Java')
# ajout simple d'objet (listes) avec append()
noms.append(['C','C++'])
noms
noms.append(noms)
noms
noms[4] # les noms
# =============================================================================
#      ajout d'élements avec insert()
# =============================================================================
x = [1, 3, 5, 8]
# inserer 2 entre 1 et 3
x.insert(1,2)
x
# inserer 0 avant 1 ou en début de liste
x.insert(0,0)
x
# inserer 6 et 7  entre 5 et 8
x.insert(5,[6, 7]) 
x
