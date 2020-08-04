nombre1 = int (input("Entrez le premier nombre: "))
nombre2 = int (input("Entrez le deuxieme nombre:"))

a = nombre1
b = nombre2

while (nombre1 != nombre2):
	if nombre1 > nombre2:
		nombre1 -= nombre2

	else:
		nombre2 -= nombre1

print("Le PGCD de %d et %d est: %d" %(a, b, nombre1))
	