class TableauNoir:
    """Class permettant d'afficher un message a l'ecran ou de l'effacer.
        Elle dispose de trois méthodes:
        ---> ecrire
        ---> lire
        ---> effacer
    """

    def __init__(self):
        self.surface = ""

    def ecrire(self, message_a_ecrire):
        """Prend un message en parametre et le conserve dans la variable self.surface"""
        if self.surface != "":
            self.surface += "\n"
        self.surface += message_a_ecrire

    def lire(self):
        """Affiche le contenu de surface"""
        print(self.surface)

    def effacer(self):
        """Efface la surface du tableau"""
        self.surface = ""
