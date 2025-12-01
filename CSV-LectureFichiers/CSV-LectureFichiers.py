# À ajouter dans la classe Bibliotheque

def charger_donnees(self):
    """Charge les données des fichiers CSV"""

    # --- Adhérents ---
    try:
        with open(self.f_adherents, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for r in reader:
                self.adherents.append(Adherent(r["nom"], r["prenom"], r["email"]))
    except:
        pass

        # --- Documents ---
    try:
        with open(self.f_docs, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for r in reader:
                t = r["type"]
                if t == "Livre":
                    doc = Livre(r["titre"], r["auteur"])
                    doc.estDisponible = (r["dispo"] == "True")
                elif t == "BandeDessinee":
                    doc = BandeDessinee(r["titre"], r["auteur"], r["dessinateur"])
                elif t == "Dictionnaire":
                    doc = Dictionnaire(r["titre"], r["auteur"], r["editeur"])
                elif t == "Journal":
                    doc = Journal(r["titre"], r["date_parution"])
                else:
                    doc = Document(r["titre"])

                self.documents.append(doc)
    except:
        pass

        # --- Emprunts ---
    try:
        with open(self.f_emprunts, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for r in reader:
                adh = self.trouver_adherent(r["nom"], r["prenom"])
                livre = self.trouver_livre(r["titre"])
                if adh and livre:
                    emp = Emprunt(adh, livre, r["dateEmp"], r["dateRetour"] or None)
                    if r["dateRetour"] == "":
                        livre.estDisponible = False
                    self.emprunts.append(emp)
    except:
        pass