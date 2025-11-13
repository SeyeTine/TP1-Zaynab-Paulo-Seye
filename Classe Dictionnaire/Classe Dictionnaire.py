class Dictionnaire(Volume):
    def __init__(self, titre, auteur, editeur):
        super().__init__(titre, auteur)
        self.editeur = editeur

    def __str__(self):
        return "Dictionnaire : " + super().__str__() + " - Éditeur : " + self.editeur

