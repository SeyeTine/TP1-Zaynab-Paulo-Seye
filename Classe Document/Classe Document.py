class Document:
    def __init__(self, titre):
        self.titre = titre

    def __str__(self):
        return "Document : " + self.titre
