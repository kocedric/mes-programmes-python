# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 12:18:41 2018

@author: danam
"""

# opération concatenation avec + 
str0 = "Hello" + "World" + "!"
print(str0)
# ou 
str1 = "Hello"   "World"   "!"
print(str1)

# opération de répétition avec *
str2 = str0 * 3
print(str2)
str3 = 'a'*4 + ' ' + 'b'*2
print(str3)
# ou \n signifie retour à la ligne
str4 = 'Python\n'*3 
print(str4)
# ou \t signifie tabulation
str5 = 'Python\t'*3
print(str5)

# la fonction générique len() : renvoie le nombre de caractères
len(str0)
len(str4)

# l'opérateur d'appartenance in et not in
'y' in str5 # True
'y' not in str5 # False

# l'opérateur d'identité également 
'y' is 'Y'  # False
"Python" is 'Python' # True
'True' is not True   # True

