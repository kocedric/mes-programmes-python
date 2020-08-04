import os
import json

base = "/home/cedric/Bureau/structure"
chemin_json = base + "/structure.json"


def print_hierachie(chemin_json):
	with open(chemin_json, "r") as f:
		structure = json.load(f)
	print("Les dossiers existent deja")
	print("voici la hierachie des dossiers")
	for key, values in structure.items():
		print("%s/" %key)
		for value in values:
			print("---> %s" %value)
		print("="*25)



def creer_dossier(dossier_a_creer):
	for key, values in dossier_a_creer.items():
		for value in values:
			dossier = "%s/%s/%s" %(base, key, value)
			os.makedirs(dossier)
			print("creation du dossier ---> %s" %dossier)



def ecrire_json(chemin_json, dictionnaire):
	with open(chemin_json, "w") as f:
		json.dump(dictionnaire, f, indent=5)


structure = {
				"Musiques": ["Religieuse", "Rap", "Pop", "Clasique"],
				"Documents": ["Travail", "Maison", "Facture"],
				"Universite": ["UVCI", "Cerco"],
				"Video": ["Film", "Clip"],
				"images": ["Personnel", "Professionnel", "Souvenir", "Publique"]
			}

if os.path.isfile(chemin_json):
	print_hierachie(chemin_json)

else:
	creer_dossier(structure)
	ecrire_json(chemin_json, structure)