class Joueur(object) :
    """
    Cette classe nommée Joueur modélise un joueur.
    Attributes:
        nom (string): nom du joueur
        prenom (string): prénom du joueur
        dateDeNaissance (string) sa date de naissance
        id (int): son identité numérique
    """

    def __init__(self, nom, prenom, dateDeNaissance, id):
        self.nom = nom
        self.prenom = prenom
        self.dateDeNaissance = dateDeNaissance
        self.id = id
        self.point = 0
