class Journal(Document):
    def __init__(self, titre, date_parution):
        super().__init__(titre)
        self.date_parution = date_parution

    def __str__(self):
        return "Journal : " + self.titre + " - Paru le " + self.date_parution
