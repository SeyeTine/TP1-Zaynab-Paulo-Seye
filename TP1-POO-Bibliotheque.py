import csv
from datetime import datetime
import os

# ---------------- CLASSES ----------------
class Document:
    def __init__(self, titre):
        self.titre = titre

    def __str__(self):
        return "Document : " + self.titre


class Volume(Document):
    def __init__(self, titre, auteur):
        super().__init__(titre)
        self.auteur = auteur

    def __str__(self):
        return self.titre + " - Auteur : " + self.auteur


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


class BandeDessinee(Volume):
    def __init__(self, titre, auteur, dessinateur):
        super().__init__(titre, auteur)
        self.dessinateur = dessinateur

    def __str__(self):
        return "BD : " + super().__str__() + " - Dessinateur : " + self.dessinateur


class Dictionnaire(Volume):
    def __init__(self, titre, auteur, editeur):
        super().__init__(titre, auteur)
        self.editeur = editeur

    def __str__(self):
        return "Dictionnaire : " + super().__str__() + " - Éditeur : " + self.editeur


class Journal(Document):
    def __init__(self, titre, date_parution):
        super().__init__(titre)
        self.date_parution = date_parution

    def __str__(self):
        return "Journal : " + self.titre + " - Paru le " + self.date_parution


class Adherent:
    def __init__(self, nom, prenom, email=""):
        self.nom = nom
        self.prenom = prenom
        self.email = email

    def __str__(self):
        if self.email:
            return self.prenom + " " + self.nom + " (" + self.email + ")"
        return self.prenom + " " + self.nom


class Emprunt:
    def __init__(self, adherent, livre, date_emprunt=None, date_retour=None):
        self.adherent = adherent
        self.livre = livre
        self.date_emprunt = date_emprunt or datetime.now().strftime("%Y-%m-%d")
        self.date_retour = date_retour

    def __str__(self):
        retour = self.date_retour if self.date_retour else "Non rendu"
        return str(self.adherent) + " -> '" + self.livre.titre + "' (Emprunt : " + self.date_emprunt + ", Retour : " + retour + ")"


# ------------------ BIBLIOTHÈQUE ------------------

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

    # ---------- Méthodes utilitaires ----------

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

    # ---------- Opérations ----------

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

    def ajouter_document(self):
        print("\n--- Ajouter document ---")
        print("1 Livre - 2 BD - 3 Dictionnaire - 4 Journal")
        choix = input("Choix : ")

        titre = input("Titre : ")

        if choix == "1":
            auteur = input("Auteur : ")
            self.documents.append(Livre(titre, auteur))

        elif choix == "2":
            auteur = input("Auteur : ")
            dess = input("Dessinateur : ")
            self.documents.append(BandeDessinee(titre, auteur, dess))

        elif choix == "3":
            auteur = input("Auteur : ")
            ed = input("Éditeur : ")
            self.documents.append(Dictionnaire(titre, auteur, ed))

        elif choix == "4":
            date = input("Date de parution (YYYY-MM-DD) : ")
            self.documents.append(Journal(titre, date))

        else:
            print("Choix erroné!")
            return

        self.sauvegarder()
        print("Document ajouté.")

    def supprimer_document(self):
        print("\n--- Supprimer document ---")
        titre = input("Titre du document : ")

        doc = None
        for d in self.documents:
            if d.titre.lower() == titre.lower():
                doc = d
                break

        if not doc:
            print("Document introuvable.")
            return

        # Vérifier si c'est un livre emprunté
        if isinstance(doc, Livre) and not doc.estDisponible:
            print("Erreur : ce livre est actuellement emprunté.")
            return

        self.documents.remove(doc)
        self.sauvegarder()
        print("Document supprimé.")

    def afficher_documents(self):
        print("\n--- Documents ---")
        if not self.documents:
            print("Aucun")
        for d in self.documents:
            print(d)

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

    # ---------- Sauvegarde ----------

    def sauvegarder(self):
        # Adhérents
        with open(self.f_adherents, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["nom", "prenom", "email"])
            for a in self.adherents:
                w.writerow([a.nom, a.prenom, a.email])

        # Documents
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

        # Emprunts
        with open(self.f_emprunts, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["nom", "prenom", "titre", "dateEmp", "dateRetour"])
            for e in self.emprunts:
                w.writerow([e.adherent.nom, e.adherent.prenom, e.livre.titre, e.date_emprunt, e.date_retour or ""])


# ------------------ MENU PRINCIPAL ------------------

def afficher_menu():
    b = Bibliotheque()

    while True:
        print("\n" + "*"*50)
        print("         Bienvenue à votre bibliothèque")
        print("       Faites un choix :")
        print("*"*50)
        print("    1 - Ajouter adhérent")
        print("    2 - Supprimer adhérent")
        print("    3 - Afficher tous les adhérents")
        print("    4 - Ajouter Document")
        print("    5 - Supprimer Document")
        print("    6 - Afficher tous les Documents")
        print("    7 - Ajouter Emprunt")
        print("    8 - Retour d'un Emprunt")
        print("    9 - Afficher tous les Emprunts")
        print("    Q - Quitter")
        print("*"*50)

        choix = input("Choisissez une action : ").upper()

        if choix == "1":
            b.ajouter_adherent()
        elif choix == "2":
            b.supprimer_adherent()
        elif choix == "3":
            b.afficher_adherents()
        elif choix == "4":
            b.ajouter_document()
        elif choix == "5":
            b.supprimer_document()
        elif choix == "6":
            b.afficher_documents()
        elif choix == "7":
            b.ajouter_emprunt()
        elif choix == "8":
            b.retour_emprunt()
        elif choix == "9":
            b.afficher_emprunts()
        elif choix == "Q":
            print("Au revoir !")
            break
        else:
            print("Choix erroné !")


# ---------- EXECUTION ----------
if __name__ == "__main__":
    afficher_menu()
