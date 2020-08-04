# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 12:18:41 2018

@author: danam
"""

# =============================================================================
#                         les entiers  int()
# =============================================================================
#%%
# base décimale 0 à 9
x = 10
y = 100
# base octale 0 à 7 doit être précédé de 0o
ox = 0o7
oy = 0o10
# base hexadecimale 0 à 9 et A à F doit être précédé de 0x
hx = 0xF
hy = 0x9
# base binaire 0 et 1 et précédé de 0b
bx = 0b1010
by = 0b100100
#%%
## conversion interne de base entre entiers
# convertir un decimal en binaire
bin(y)
# convertir un decimal en hexadecimal
hex(y)
# convertir un decimal en octal
oct(y) 
# convertir un hexadecimal en binaire
bin(hx)
#%% 
big_nombre = 1000**500
5000**3600
#%%
# =============================================================================
#            les réels ou nombres à virgules flottants float()
# =============================================================================
pi = 3.1415
# notation scientifique mantisse et exposant
nombre_flot = 15245.526
notation_scient = 15245526e-3
montant = 10e6

#%%
# =============================================================================
#            les nombres complexes complex()
# =============================================================================
nombre_complx = 12.5 + 0j
nombre_complx2 = 12j
#%%
# =============================================================================
#            la coercition 
# =============================================================================
# passer d'un entier à un nombre flottant
float(5)
# passer d'un entrier à un nombre complexe
complex(5)
# passer d'un nombre flottant à un entier
int(3.1415)
# passer d'un nombre flottant à un nombre entier
complex(3.1415)
