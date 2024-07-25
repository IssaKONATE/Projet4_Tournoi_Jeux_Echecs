from models.Tour import Tour
from models.Match import Match


class Tournoi(object):
    """
    Cette classe nommée Tournoi représente le modèle du tournoi

    Attributes:
        nom (string): nom du tour
        lieu (string): lieu du tournoi
        dateDeFin (string): date de fin
        dateDeDebut (string): date de fin
        nombreTours (int): nombre de tours au total
        numeroTourActuel (int): numero du tour actuel
    """

    joueurs = []
    tours = []
    nombreDeMatchParTour = -1

    # Ici on définit un constructeur de l'objet Tournoi
    def __init__(
        self, nom, lieu, dateDeDebut, dateDeFin, nombreTours, numeroTourActuel
    ):
        self.nom = nom
        self.lieu = lieu
        self.dateDeDebut = dateDeDebut
        self.dateDeFin = dateDeFin
        self.nombreTours = nombreTours
        self.numeroTourActuel = numeroTourActuel
        # self.initJoueursParFichierJson()

        while len(self.joueurs) % 2 != 0:
            print(
                "Nombre de joueurs est impair, veuillez inscrire un joueur de plus pour continuer !"
            )
            self.ajouterJoueurByTerminal(self.joueurs)

    def ajouterJoueur(self, joueur):
        """
        Cette méthode permet d'ajouter un joueur à la liste des joueurs
        Args:
           joueur (Joueur): le joueur à ajouter à la liste
        """

        found = any(
            x is not None and x.nom == joueur.nom and x.prenom == joueur.prenom
            for x in self.joueurs
        )
        if found:
            print(
                "Ce joueur est déjà enregistré ==> ",
                joueur.nom,
                " ",
                joueur.prenom,
                " ",
                "Date de naissance: ",
                joueur.dateDeNaissance,
            )
            return None
        else:
            # sinon ajouter le joueur
            print("joueur ajouté ....")
            self.joueurs.append(joueur)
            return joueur
