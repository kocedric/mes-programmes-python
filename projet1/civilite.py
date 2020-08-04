class Personne:
    """Class qui repectorie une personne et qui conserve ses informations
        ---> Nom
        ---> Prenom
        ---> Age
        ---> Sexe
        ---> Profession
        ---> Lieu de residence
    """

    def __init__(self, nom="Sans nom", prenom="Sans prenom"):
        self.nom = nom
        self.prenom = prenom
        self.age = 0
        self.sexe = 1 #1 pour homme 0 pour femme
        self.profession = "Sans emploi"
        self.residence = "pas definir"
