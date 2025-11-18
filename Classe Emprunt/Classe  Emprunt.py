class Emprunt:
    def __init__(self, adherent, livre, date_emprunt=None, date_retour=None):
        self.adherent = adherent
        self.livre = livre
        self.date_emprunt = date_emprunt or datetime.now().strftime("%Y-%m-%d")
        self.date_retour = date_retour

    def __str__(self):
        retour = self.date_retour if self.date_retour else "Non rendu"
        return str(self.adherent) + " -> '" + self.livre.titre + "' (Emprunt : " + self.date_emprunt + ", Retour : " + retour + ")"

