class Adherent:
    def __init__(self, nom, prenom, email=""):
        self.nom = nom
        self.prenom = prenom
        self.email = email

    def __str__(self):
        if self.email:
            return self.prenom + " " + self.nom + " (" + self.email + ")"
        return self.prenom + " " + self.nom
