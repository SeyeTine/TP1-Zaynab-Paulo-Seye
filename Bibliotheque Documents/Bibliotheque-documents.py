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