# À ajouter dans la classe Bibliotheque

def ajouter_emprunt(self):
    print("\n--- Emprunt ---")
    nom = input("Nom adhérent : ")
    prenom = input("Prénom adhérent : ")
    adh = self.trouver_adherent(nom, prenom)

    if not adh:
        print("Adhérent introuvable.")
        return

    titre = input("Titre du livre : ")
    livre = self.trouver_livre(titre)

    if not livre:
        print("Livre introuvable.")
        return

    if not livre.emprunter():
        print("Livre déjà emprunté.")
        return

    emp = Emprunt(adh, livre)
    self.emprunts.append(emp)
    self.sauvegarder()
    print("Emprunt enregistré.")


def retour_emprunt(self):
    print("\n--- Retour ---")
    nom = input("Nom adhérent : ")
    prenom = input("Prénom adhérent : ")
    titre = input("Titre du livre : ")

    for e in self.emprunts:
        if e.adherent.nom == nom and e.adherent.prenom == prenom and e.livre.titre == titre and e.date_retour is None:
            e.date_retour = datetime.now().strftime("%Y-%m-%d")
            e.livre.retourner()
            self.sauvegarder()
            print("Retour enregistré.")
            return

    print("Emprunt non trouvé.")


def afficher_emprunts(self):
    print("\n--- Emprunts ---")
    if not self.emprunts:
        print("Aucun")
    for e in self.emprunts:
        print(e)
