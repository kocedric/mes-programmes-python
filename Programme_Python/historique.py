import sys
import pathlib

try:
    dossier_de_profile = pathlib.Path(sys.argv[1])
except IndexError:
    sys.exit("Vous devez passer un dossier de profile en paramètre")

historique = dossier_de_profile / "places.sqlite"

if not historique.is_file():
    sys.exit(f"Impossible de trouver ce fichier: {historique}")