class Volume(Document):
    def __init__(self, titre, auteur):
        super().__init__(titre)
        self.auteur = auteur

    def __str__(self):
        return self.titre + " - Auteur : " + self.auteur
