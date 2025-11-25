class Bibliotheque:
    def __init__(self):
        self.adherents = []
        self.documents = []
        self.emprunts = []

        self.f_adherents = "Adherents.txt"
        self.f_docs = "Biblio.txt"
        self.f_emprunts = "Emprunts.txt"

        self.creer_fichiers()
        self.charger_donnees()

    # Méthodes utilitaires
    def trouver_adherent(self, nom, prenom):
        for a in self.adherents:
            if a.nom.lower() == nom.lower() and a.prenom.lower() == prenom.lower():
                return a
        return None

    def trouver_livre(self, titre):
        for d in self.documents:
            if isinstance(d, Livre) and d.titre.lower() == titre.lower():
                return d
        return None
