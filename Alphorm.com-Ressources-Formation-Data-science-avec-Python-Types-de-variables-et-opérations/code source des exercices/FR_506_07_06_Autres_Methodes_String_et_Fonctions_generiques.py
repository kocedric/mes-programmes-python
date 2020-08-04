# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 12:18:41 2018

@author: danam
"""

# =============================================================================
#                     Quelques méthodes importantes
# =============================================================================
# replace() : pour remplacer des caractères dans une chaîne...
str0 = 'Python'
str0.replace('P', 'L')
# index() /rindex(): renvoie la position de la 1ère occurence d'une chaine de caractère dans une autre
str1 = 'L\'homme est un loup pour l\'homme, à l\'état de nature' 
str1.index('homme')
str1.index('homme',8)
str1.rindex('homme')
# count() : renvoie le nombre d'occurence d'une chaîne de caractère
str1.count('homme')
str1.count('e')
# endswith()/startswith() recherche suffixe/préfixe
str1.endswith('nature')        # True
str1.startswith('L\'homme')    # True
str1.startswith('l\'homme',25) # True
# find()/rfind() # fait la même chose que index()/rindex() 
# si le terme recherché n'existe pas find()/rfind() renvoie -1 alors que
# index()/rindex() renvoie une erreur
str1.find('est')
str1.find('homme') 
str1.find('terre')  
# encode()/decode() convertit les chaines de strings/bytes en chaîne de bytes/strings
str1_byte = str1.encode()
str1_byte
str1_byte.decode()
# strip()/lstrip()/rstrip() 
str1.strip('L\'homme')
'  Python   '.strip()
# capitalize(),lower(),upper(),title(),swapcase()
str0.capitalize()
str0.upper()
str0.swapcase()
# center()/just(), ljust(),rjust()
#isdigit(), isalpha, isalphanum
"ndjd".isdigit()
'1252'.isdigit()
int('1252')

# =============================================================================
#                           les fonctions génériques
# =============================================================================
# len()  # nombre de caractères dans une chaîne de caractères
len(str0)
len(str1)
# chr() vs ord()
chr(90) # équivalent en caractère 
chr(65)
ord('A') # équivalent en numerique
ord('î')
# une astuce pour ordonner des chaînes de caractère
''.join(sorted(str0))
