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
