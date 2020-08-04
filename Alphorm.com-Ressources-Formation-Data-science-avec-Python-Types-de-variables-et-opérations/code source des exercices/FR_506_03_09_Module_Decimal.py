# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 12:18:41 2018

@author: danam
"""

import decimal
# simple opération
decimal.Decimal(1.1) + decimal.Decimal(2.2)
# manager de contexte 
decimal.getcontext().prec = 3 # fixer la précision à 3
decimal.Decimal(1.1) + decimal.Decimal(2.2)
# créer des objets Decimal()
D = decimal.Decimal  # renommer le constructeur
x = D(1.1)
y = D(100)
z = D('1.1')
v = D('100')
# opérations arithmétiques
x*y
y + v
div = z/v
div
y%2
# méthodes mathématiques
y.sqrt()
x.log10()
x.ln()
v.exp()
decimal.getcontext().prec = 10 # fixer la précision à 10
y.sqrt()
x.log10()
x.ln()
v.exp()
# les constantes
D('inf')
D('nan')
# coecition de Decimal à float
float(x + y)
float(decimal.Decimal(1.1) + decimal.Decimal(2.2))
