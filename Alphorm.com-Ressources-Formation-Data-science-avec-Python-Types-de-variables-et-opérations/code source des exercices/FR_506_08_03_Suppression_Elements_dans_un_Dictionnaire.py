# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 12:18:41 2018

@author: danam
"""

# exemple de dictionnaire
d = {'rang': [1, 2], 'x' : 10, 'y' : 20, 'dic' : {1 : 'a', 2: 'b'}} 

# suppression d'élement connaissant la clé avec del
del d['x'] 
d

# suppression avec la méthode pop()
d.pop('y') # renvoie la valeur associée à la clé et supprime l'élément
d.pop('x', 'valeur défaut') # fournir une valeur par défaut pour une clé inexistante

# suppression avec la méthode popitem()
d.popitem()

# suppression avec la méthode clear()
d.clear()
# ou 
d = dict()
# ou 
d = {}
