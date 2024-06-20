class Joueur(object) :
    point = 0
    couleur = None

    def __init__(self, nom, prenom, dateDeNaissance, id):
        self.nom = nom
        self.prenom = prenom
        self.dateDeNaissance = dateDeNaissance
        self.id = id

    def afficher(self):
        print("Id: ", self.id, ", Nom : ", self.nom, ",Prenom : ", self.prenom, ", Date de naissance : "
              , self.dateDeNaissance, ", Point : ", self.point)
