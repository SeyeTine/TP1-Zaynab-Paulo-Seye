class BandeDessinee(Volume):
    def __init__(self, titre, auteur, dessinateur):
        super().__init__(titre, auteur)
        self.dessinateur = dessinateur

    def __str__(self):
        return "BD : " + super().__str__() + " - Dessinateur : " + self.dessinateur