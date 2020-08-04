# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 12:18:41 2018

@author: danam
"""

# =============================================================================
#                  opérateurs et opérations de comparaison
# =============================================================================
# test de supériorité avec >
5 > 4   # True
3 > 10  # False 
# test d'infériorité avec <
5 < 4  # False
3 < 10 # True
# test d'égalité avec ==
5 == 4 # False
5 == 5 # True 
5.0 == 5 # True
# test d'inégalité avec !=
5 != 4 # True
True != False # True
(5 > 4) != True # False
# test de supériorité ou égale >=
True >= False # True
(5 - 3) >= 0 # True
-float('inf') >= 1 # False
# test d'infériorité ou égale <=
True <= False # False
(5 - 3) <= 0 # False
-float('inf') <= 1 # True
# =============================================================================
#                 opérateurs et opérations logiques
# =============================================================================
vrai = True
faux = False
# l'opérateur "or" ( "OU" en français )
vrai or faux  # True
faux or faux  # False
vrai or vrai  # True
faux or vrai  # True  
# l'opérateur "and" ( "ET" en français )
vrai and vrai # True
vrai and faux # False
faux and faux # False
faux and vrai # False
# l'opérateur "not" ( "NON" en français )
not vrai  # False
not faux  # True
# les combinaisons or , and et not
(vrai or faux) and (faux and faux) # False
# combiner avec les opérateurs de comparaison
(5 > 4) or (10 == 10.5) # True
(5 != 6) and (7 > 5) or not (10 < 11) # True
# =============================================================================
#          opérateurs et opérations d'indentité ou identity operator
# =============================================================================
# l'opérateur "is" 
1 is 1 # True
1 is 1.0 # False
a = 5
b = 5
a is b # True 
noteS1 = [10,15,20]
noteS2 = [10,15,20]
noteS1 is noteS2 # False 
# l'opérateur "is not"
1 is not 1 # False
vrai is not faux # True
a is not b # False
noteS1 is not noteS2 # True

# =============================================================================
#          opérateurs ou opérations d'inclusions ou d' appartenance
# =============================================================================
# l'opérateur "in"
'a' in 'Python' # False
'y' in 'Python' # True
10 in noteS1   # True
# l'opérateur "not in"
'a' not in 'Python' # True
'y' not in 'Python' # False
10  not in noteS1   # False
