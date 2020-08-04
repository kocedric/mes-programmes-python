# Ce programme affiche la table ASCII

print("{}VOICI LA TABLE ASCII{}".format("="*5, "="*5))
for i in range(0, 256):
    print("{} ---> {}".format(i, chr(i)))
