# Cette fonction permet a l'utilisateur d'entrer manuellement la structure de dossier a creer
def info_de_dossier():
    continuer = True
    while continuer:
        try:
            nombre_dossier = int(input("Entrer le nombre de dossier(s) parent(s): "))
            liste_donnee = []
            break
        except ValueError:
            print("Vous devez entrer imperativement un nombre entier.")
            continue

    for i in range(0, nombre_dossier):
        nom_dossier = input("Entrer le nom du dossier parent {}: ".format(i+1))
        liste_donnee.append(nom_dossier)

    structure = {}
    structure = structure.fromkeys(liste_donnee)

    for key in structure.keys():
        while continuer:
            try:
                nombre_sous_dosssier = int(input("Combien de sous dossier(s) voulez-vous pour {}\\: ".format(key)))
                liste_sous_dossier = []
                break
            except ValueError:
                print("Vous devez entrer imperativement un nombre entier.")
                continue

        for j in range(0, nombre_sous_dosssier):
            while continuer:
                try:
                    sous_dossier = input("Entrez le nom du sous dossier {} de {}\\".format(j+1,key))
                    liste_sous_dossier.append(sous_dossier)
                    break
                except ValueError:
                    print("Vous devez entrer imperativement un nombre entier.")
                    continue
        structure[key] = liste_sous_dossier

    print(structure)

info_de_dossier()
