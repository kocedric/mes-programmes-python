continuer = "o"

while continuer == "o":

	table_nombre = int (input("Entrez le nombre a multiplier: "))
	valeur_max = int (input("Entrez la valeur de fin de la table: "))
	nombre_pas = int (input("Entrez le nombre de pas: "))


	print("voici la table de multiplication de %d\n\n" %table_nombre)

	for i in range(0, valeur_max+1, nombre_pas):
		print("%d * %d = %d" %(table_nombre, i, table_nombre * i))

	#while (continuer != "o" or continuer != "n"):
	continuer = str (input("Voulez vous continuer ?  (o/n): "))
	if continuer == "o":
		continue
	else:
		break

	
print("Fin du programme !")
