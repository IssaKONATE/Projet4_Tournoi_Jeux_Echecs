import json
from models.Tour import Tour
from models.Match import Match
from models.joueur import Joueur


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
        self.initJoueursParFichierJson()
        

        while len(self.joueurs) % 2 != 0:
            print(
                "Nombre de joueurs est impair, veuillez inscrire un joueur de plus pour continuer !"
            )
            self.ajouterJoueurByTerminal(self.joueurs)
