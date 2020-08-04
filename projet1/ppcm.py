nombre1 = int (input("Entrez le premier nombre: "))
nombre2 = int (input("Entrez le deuxieme nombre:"))

if nombre1 > nombre2:
	plus_grand = nombre1

else:
	plus_grand = nombre2
i = nombre1 * nombre2

while plus_grand <= i:
	if plus_grand % nombre1 == 0 and plus_grand % nombre2 == 0:
		ppcm = plus_grand
		break
	plus_grand += 1

print("Le ppcm de %d et %d est: %d" %(nombre1, nombre2, ppcm))