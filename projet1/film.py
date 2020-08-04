continuer = "o"
liste_films = []

while continuer == "o":
	titre_film = input("\nEntrez le titre d'un film: ")

	if titre_film.lower() in [film[0].lower() for film in liste_films]:
		print("%s est deja present dans la liste" %(titre_film.capitalize()))
	else:
		note = input("Entrez une note pour ce film: ")
		liste_films.append((titre_film, note))

	continuer = input("Voulez-vous continuer ? (o/n): ")

liste_films.sort()
print(liste_films)
