# Ce programme affiche le chiffre correspondant a un caractere conformement au model ASCII

continuer = "o"
while continuer == "o":
    caractere = input("Entrez le caractere dont vous voulez le numero correspondant: ")
    try:
        chiffre = ord(caractere) #conversion de caractere en chiffre et on l'affecte a la variable chiffre
        #on affiche le caractere en decimal, hexadecimal, et binaire
        print("{} ---> {}, hex({}), bin({}) ".format(caractere, chiffre, hex(chiffre), bin(chiffre)))
    except:
        print("Vous avez entrez plus d'un caractere, reprenez.")
        continue
    continuer = input("Voulez vous continuer ? (o/N)")
