# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 12:18:41 2018

@author: danam
"""

# créer des variables
x, y = 10, 7
# opération d'addition (+)
#%%
x + y 
add = x + y 
# afficher le résultat
print("x + y =", add)
#%%
# opération de soustraction (-)
x - y 
y - x
sub1 = x - y
sub2 = y - x
# afficher le résultat
print("x - y =", sub1)
print("y - x =", sub2)
#%%
# opération de multiplication (*)
x * y
pdt = x * y
# afficher le résultat
print("x * y =", pdt)
#%%
# opération de division (/)
x/y
y/x
div1 = x/y
div2 = y/x
# afficher le résultat
print("x / y =", div1)
print("y / x =", div2)
#%%
# opération d'exposant (**)
x**y
y**x
x**2
y**2
exp1 = x**y
exp2 = y**x
# afficher le résultat
print("x ** y =", exp1)
print("y ** x =", exp2)
#%%
# opération modulaire (%)
x % y
y % x
# si un nombre est pair alors son modulo 2 est égal à 0
x % 2
y % 2
#%%
# opération de division entière (//)
x // y
y // x

## opérations d'affectation combinée à l'opération arithmétique
x = x + 1 # incrémentation 
print(x)
y = y - 1 # décrémentation
print(y)
# écriture compacte
x += 1
print(x)
y -= 1
print(y)
x **= 2
print(x)
y %= 2
print(y)
