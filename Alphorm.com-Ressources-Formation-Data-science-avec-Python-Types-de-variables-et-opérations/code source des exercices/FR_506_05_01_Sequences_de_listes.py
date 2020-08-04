# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 12:18:41 2018

@author: danam
"""

# créer la liste des n premiers nombres entiers
n = list(range(10)) # 0 ~ 9
print(n)
# créer la liste des nombres pairs compris entre 0 et 10
pairs = list(range(0, 11, 2))
print(pairs)
# créer la liste des nombres impairs compris entre 0 et 100
impairs = list(range(1, 100, 2)) # 1, 3, 5 ...
print(impairs)
# ou 
impairs1 = list(range(99, 0, - 2)) # 99, 97, 95 ...
print(impairs1)

