# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 12:18:41 2018

@author: danam
"""

# importer le module
import fractions
# créer des fractions
fractions.Fraction(2,5)
# redefinir le constructeur
F = fractions.Fraction
# 
x = F(3,2)
x
y = F(10,4)
y
# extraire les composants
x.numerator
x.denominator
# opérations arithmétiques
x + y
x - y
x * y
x / y
# coercition 
float(x)
# (1)
fractions.Fraction.from_float(0.75)
fractions.Fraction.from_float(1/3)
# ou environ
(_.numerator)/(_.denominator)
# (2)
(0.75).as_integer_ratio()
# (3)
F(*(0.75).as_integer_ratio())
# Decimal à fraction 
from decimal import Decimal as D
d = D(1.1)
F.from_decimal(d)
d2 = D(1.1) + D(2.2)
F.from_decimal(d2)
