voyelle = ["a", "o", "i", "u", "e", "y", "A", "O", "I", "U", "E", "Y"]

caractere_entree = input("Entrer un caractere svp: ")

if caractere_entree in voyelle:
	print("%s est une voyelle" %caractere_entree)

else:
	print("%s est une consonne" %caractere_entree)