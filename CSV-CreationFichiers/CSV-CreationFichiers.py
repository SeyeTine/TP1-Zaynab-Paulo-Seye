# À ajouter dans la classe Bibliotheque

def creer_fichiers(self):
    """Crée les fichiers si absents."""
    if not os.path.exists(self.f_adherents):
        with open(self.f_adherents, "w", newline="", encoding="utf-8") as f:
            csv.writer(f).writerow(["nom", "prenom", "email"])

    if not os.path.exists(self.f_docs):
        with open(self.f_docs, "w", newline="", encoding="utf-8") as f:
            csv.writer(f).writerow(["type", "titre", "auteur", "dessinateur", "date_parution", "editeur", "dispo"])

    if not os.path.exists(self.f_emprunts):
        with open(self.f_emprunts, "w", newline="", encoding="utf-8") as f:
            csv.writer(f).writerow(["nom", "prenom", "titre", "dateEmp", "dateRetour"])