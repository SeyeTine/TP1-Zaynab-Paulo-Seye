def sauvegarder(self):
    with open(self.f_adherents, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["nom", "prenom", "email"])
        for a in self.adherents:
            w.writerow([a.nom, a.prenom, a.email])

    with open(self.f_docs, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["type", "titre", "auteur", "dessinateur", "date_parution", "editeur", "dispo"])

        for d in self.documents:
            t = d.__class__.__name__
            if isinstance(d, Livre):
                w.writerow([t, d.titre, d.auteur, "", "", "", d.estDisponible])


            elif isinstance(d, BandeDessinee):
                w.writerow([t, d.titre, d.auteur, d.dessinateur, "", "", ""])
                elif isinstance(d, Dictionnaire):
                w.writerow([t, d.titre, d.auteur, "", "", d.editeur, ""])
                elif isinstance(d, Journal):
                w.writerow([t, d.titre, "", "", d.date_parution, "", ""])
                else:
                w.writerow(["Document", d.titre, "", "", "", "", ""])

        with open(self.f_emprunts, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["nom", "prenom", "titre", "dateEmp", "dateRetour"])
            for e in self.emprunts:
                w.writerow([e.adherent.nom, e.adherent.prenom, e.livre.titre, e.date_emprunt, e.date_retour or ""])