def listing(iterable=range(0, 10), bullet="-"):
    '''Fonction qui prend un itérable en paramètre et retune une chaine
        de caractère d'éléments composant ce itérable'''

    liste = []
    for x in iterable:
        liste.append(f"{bullet} {x}")
    return "\n".join(liste)


print(listing())