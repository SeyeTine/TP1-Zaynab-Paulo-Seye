# À ajouter dans la classe Bibliotheque

def ajouter_adherent(self):
    print("\n--- Ajouter adhérent ---")
    nom = input("Nom : ")
    prenom = input("Prénom : ")
    email = input("Email (optionnel) : ")

    if not nom or not prenom:
        print("Saisie erronée !")
        return

    self.adherents.append(Adherent(nom, prenom, email))
    self.sauvegarder()
    print("Adhérent ajouté.")


def supprimer_adherent(self):
    print("\n--- Supprimer adhérent ---")
    nom = input("Nom : ")
    prenom = input("Prénom : ")

    adh = self.trouver_adherent(nom, prenom)
    if not adh:
        print("Adhérent introuvable.")
        return

        # Vérifier si l'adhérent a des emprunts actifs
    for e in self.emprunts:
        if e.adherent == adh and e.date_retour is None:
            print("Erreur : cet adhérent a des emprunts actifs.")
            return

    self.adherents.remove(adh)
    self.sauvegarder()
    print("Adhérent supprimé.")


def afficher_adherents(self):
    print("\n--- Adhérents ---")
    if not self.adherents:
        print("Aucun")
    for a in self.adherents:
        print(a)

