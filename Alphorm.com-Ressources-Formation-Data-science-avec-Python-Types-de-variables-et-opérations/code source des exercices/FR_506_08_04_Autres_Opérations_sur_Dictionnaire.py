# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 12:18:41 2018

@author: danam
"""

# exemple de dictionnaire
d = {1 : 'a', 2 : 'b',  3 : 'c', 4 : 'd'}

# la fonction générique len()
len(d) # renvoie le nombre d'élément(clé-valeur) contenu dans un dictionnaire

# les autres méthodes de la classe dictionnaire

# la méthode copy() # le deep copy ou la copie profonde
d1 = d # une copie superficielle
d2 = d.copy() # une copie profonde 
d.update({5: 'e'}) # une fois d modifé
d1 # sera modifié
d2 # ne sera pas affecté

# la méthode setdefault()
v6 =  d.setdefault(6)
print(v6)
v7 = d.setdefault(7, 'g')
print(v7)
