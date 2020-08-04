# Ce programme affiche la conversion du decimal en binaire, octal, hexadecimal.

continuer = "o"
while continuer == "o":
    nombre = input("Entrez le nombre à convertir ")
    try:
        nombre = int(nombre) 
        print("{} ---> oct({}), hex({}), bin({}) ".format(nombre, oct(nombre), hex(nombre), bin(nombre)))
    except:
        print("Entrez un entier svp !")
        continue
    continuer = input("Voulez vous continuer ? (o/N)")