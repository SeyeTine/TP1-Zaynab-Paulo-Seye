class Livre(Volume):
    def __init__(self, titre, auteur):
        super().__init__(titre, auteur)
        self.estDisponible = True

    def __str__(self):
        statut = "Disponible" if self.estDisponible else "Emprunté"
        return "Livre : " + super().__str__() + " (" + statut + ")"

    def emprunter(self):
        if self.estDisponible:
            self.estDisponible = False
            return True
        return False

    def retourner(self):
        self.estDisponible = True
