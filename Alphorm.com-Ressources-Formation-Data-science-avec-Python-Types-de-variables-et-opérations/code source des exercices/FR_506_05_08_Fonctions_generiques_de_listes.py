# la fonction len(x) : renvoie la taille d'un objet iterable x
x = [1, 2, 3, 'a', 'b']
len(x)

# la fonction sorted(x) : renvoie une liste ordonné de x
y = [2, 3.5, -6, 7, 9.5, 8]
sorted(y)     # tri croissant 
sorted(y, reverse = True) # tri décroissant 

# les fonctions sum(), max() et min()
notes = [10.5, 12, 8.9, 11]
sum(notes)  # somme des notes
max(notes)  # note maximale
min(notes)  # note minimale

# la commande in 
11 in notes # True
'a' in x   # True
