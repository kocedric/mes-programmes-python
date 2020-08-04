# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 12:18:41 2018

@author: danam
"""

# =============================================================================
#                      décomposition ou partitionnement
# =============================================================================
# la méthode partition(separateur) : renvoie un 3-tuple
phrase = "Python est un langage très interessant !"
phrase.partition("est")
phrase.partition("un langage")

# la méthode rpartition(separateur) : 
# partion en 3-tuple en commençant par la fin
phrase.rpartition("est") # même resultat que  phrase.partition("est")
phrase.rpartition("an") # différent de phrase.partition("an")

# la méthode split(sep, maxsplit) : décompose une chaine de caractère 
# en une liste de n éléments découpés à chaque occurence de separateur
phrase.split(sep = " ")
phrase.split(sep = " ", maxsplit = 3)
table = "|1000|2000|3200|\n |3000|3000|2300|\n|5000|3200|5600|"""
print(table)
table.split(sep = "|") # découper au niveau des barres
table.split(sep = "|\n")
table.split(sep = "\n")

# la méthode rsplit(sep, maxsplit)
phrase.rsplit(sep = " ")
phrase.rsplit(sep = " ", maxsplit = 3)

# la méthode splitlines()
table.splitlines()
# ou 
table.split(sep = "\n")
# avec conservation du séparateur à la fin de chaque élément
table.splitlines(keepends = True)

# =============================================================================
#           combinaison ou concatenation avec join()
# =============================================================================
liste = ['Python', 'est','un', 'langage', 'très', 'interessant', '!']
# joindre ou combiner par espace
' '.join(liste)
' '.join(phrase.split(' '))
# joindre ou combiner par ,
','.join(liste)
# joindre ou combiner \n
'\n'.join(liste)
print('\n'.join(liste))
# joindre ou
x = ('1','2','3')
','.join(x)
'+'.join(x)
