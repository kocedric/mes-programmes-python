# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 12:18:41 2018

@author: danam
"""

# créer des nombres complexes - littéral
c0 = 5.2 - 2j
print(c0)
type(c0)
isinstance(c0,complex)

# créer des nombres complexes avec le constructeur complex()
c1 = complex(5.2,-2)
print(c1)
type(c1)
isinstance(c1,complex)
c2 = complex("5.2-2j")
print(c2)
type(c2)
isinstance(c2,complex)

# extraire les différentes parties ou composants d'un nombre complexe
c0.real # extraire la partie réelle
c0.imag # extraire la partie imaginaire

# déterminer le conjugé d'un nombre complexe
c0.conjugate() # 5.2 + 2j
