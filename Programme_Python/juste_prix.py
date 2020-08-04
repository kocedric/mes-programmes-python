import random


jute_nombre = random.randint(0, 100)
nombre_choisi = None
historique_de_nombre = []

print("BIENVENU DANS LE JUSTE NOMBRE ---- VOUS DEVEZ TROUVER LE JUSTE NOMBRE ENTRE (0 ET 100).\n\n")
while nombre_choisi != jute_nombre:
	nombre_choisi = int(input("Quel est le juste nombre ?: "))
	historique_de_nombre.append(nombre_choisi)
	if nombre_choisi < jute_nombre:
		print("C'est plus !\n")
	elif nombre_choisi > jute_nombre:
		print("C'est moin !\n")
	else:
		print("Bravo vous avez gagné 💹 💵 👏 !")
		print(f"Vous avez gagné en = {len(historique_de_nombre)} coups.\n")

for historique in historique_de_nombre:
	print(f"- {historique}")