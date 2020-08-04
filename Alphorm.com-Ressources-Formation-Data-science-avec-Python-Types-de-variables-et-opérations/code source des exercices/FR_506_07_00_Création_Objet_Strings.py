# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 12:18:41 2018

@author: danam
"""

# =============================================================================
#         création littérale de chaîne de caractère
# =============================================================================
# création de chaîne de caractère entre  quote ('') simple
c0 = 'Python'
print(c0)
# création de chaîne de caractère entre quote ("") double
c1 = "Python"
print(c1)
# création de chaîne de caractère entre quote(""" """ ou ''' ''')  triple
c2 = """ Python """
c2
# ou 
c3 = ''' Python '''
c3
# cas de chaîne de caractère sur plusieurs lignes
str_long0 = """ Python 3.6.4 |Anaconda, Inc.| (default, Jan 16 2018, 10:22:32) [MSC v.1900 64 bit (AMD64)]
              Type "copyright", "credits" or "license" for more information.
              IPython 6.2.1 -- An enhanced Interactive Python. """
str_long0
print(str_long0)
# ou 
str_long1 = ''' Python 3.6.4 |Anaconda, Inc.| (default, Jan 16 2018, 10:22:32) [MSC v.1900 64 bit (AMD64)]
              Type "copyright", "credits" or "license" for more information.
              IPython 6.2.1 -- An enhanced Interactive Python. '''
print(str_long1)

# =============================================================================
#                                utiliser "" ou '' 
# =============================================================================
# utiliser les quotes double lorsque la chaîne de caractère contient '
c4 = "l'homme" 
c4
# utiliser les quotes simples lorsque la chaîne de caractère contient "
c5 = 'Type "copyright", "credits" or "license" for more information.'
c5 
# =============================================================================
#                utiliser \" ou \'
# =============================================================================
# utiliser \' pour faire paraître le symbole ' dans la chaîne de caractère
c6 = 'l\'homme'
c6
# utiliser \" pour faire paraître le symbole " dans la chaîne de caractère
c7 = "Type \"copyright\", \"credits\" or \"license\" for more information."
c7 
# utiliser \\ pour faire paraître le symbole \ dans la chaîne de caractère
c8 = "le symbole backslash \\"
print(c8)

# =============================================================================
#    coercition d'objets en chaîne de caractère avec le constructeur str()
# =============================================================================
c9 = str(125.624) # coercer un chiffre en chaîne de caractère
c9
c10 = str(1e-9)
c10
