# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 12:18:41 2018

@author: danam
"""

# créer une chaîne de caractère 
lettres = 'abcdefghijklmnopqrstuvwxyz'

# indexer et extraire la première lettre
lettres[0]
# ou 
lettres[-26]

# indexer et extraire la dernière lettre
lettres[25]
# ou
lettres[-1]

# indexer et extraire xyz
lettres[23:]
# ou
lettres[-3:]

# indexer et extraire tous les éléments 
lettres[:]
# ou
lettres[0:]
# ou
lettres
# ou
lettres[::1]
# indexer et extraire les lettres de position paires
lettres[::2] # de 0 à 25 à pas de 2

# indexer et extraire de la 7ème lettre avant la fin et 4ème avant la fin
lettres[-7:-3]

# indexer et extraire les lettres en inversant l'ordre
lettres[::-1] 

# indexer et extraire les lettres en 10 et 20ème position pas de 3
lettres[10:21:3]
