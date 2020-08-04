# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 12:18:41 2018

@author: danam
"""

# charger le module re
import re
# importer une chaîne de caractère de python
from string import printable
printable

# search() retrouve une occurence d'un motif dans une chaîne de caractère
num = re.search(r'\d', printable) # retrouver un caractère numérique
num.group(0)
num = re.search(r'\d+', printable) # retrouver un groupe de caractère numérique
num.group(0)
char = re.search(r'[a-z]+',printable)
char.group()

# match() retrouve une occurence d'un motif en debut de chaîne de caractère
num = re.match(r'\d', printable) # retrouver un caractère numérique
num.group(0)
char = re.match(r'[a-z]+',printable) # extraire les lettres de a-z
char.group()
num = re.match(r'\d+', printable) # retrouver un groupe de caractère numérique
num.group(0)

# findall() retrouve toutes les occurrences d'un motif
num = re.findall(r'\d', printable) # retrouver un caractère numérique
num
txt = 'il est 10 h 30 mins'
re.findall(r'\d', txt)
re.findall(r'\d+',txt)

# sub(), qui substitue les occurences d'un motif par une chaines de caractères
re.sub(r'\D','',txt)

# split(), décompose une chaîne de caractère en ces occurences de motif donné
re.split(r'\D',txt)

# compile(), compiler les expressions regulières pour les plus performantes
motif_num = re.compile(r'\d')
motif_num.findall(printable)

# retrouver des occurences de dates 
txt0 = 'il viendra le 12/12/2012 ou le 10/01/2013'
motif_date = re.compile(r'\d+/\d+/\d+')
motif_date.findall(txt0)
txt1 = txt0 + ' ou 123/253/2013'
txt1
motif_date.findall(txt1)
motif_date = re.compile(r'\d{2}/\d{2}/\d{4}')
motif_date.findall(txt1)

# retrouver les adresses mails 
msg = 'voici mon email : addbc@gmail.com ou add-bc@gamil.fr ou add.bc@gmail.com'
motif_mail = re.compile(r'[\w]+@[\w]+')
motif_mail.findall(msg)
  # prise en compte des symboles . et -
motif_mail = re.compile(r'[\w.-]+@[\w.-]+')
motif_mail.findall(msg)
msg2 = 'voici mon email : addbc@gmail.com ou add-bc@gamil.fr ou add.bc@gmail.com \
       et mon nom utilisateur addbc@1252'
motif_mail.findall(msg2)
motif_mail = re.compile(r'[\w.-]+@[\w.-]+\.[\w]+')
motif_mail.findall(msg2)
