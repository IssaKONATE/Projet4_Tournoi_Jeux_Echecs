from datetime import date
import pickle
from models.Tour import Tour
from models.tournoi import Tournoi
from vue.TournoiScreen import TournoiScreen


class TournoiController(object):
    """
    Cette classe nommée TournoiController représente le controller
    Attributes:
        Aucun attribut
    """

    def __init__(self):
        pass

    def deroulerTour(self, tournoi: Tournoi, tournoiScreen: TournoiScreen):
        """
        cette méthode du controller permet de faire derouler tous les tours du tournoi.
        Args:
            tournoi (Tournoi): l'instance d'un objet Tournoi.
            tournoiScreen (TournoiScreen): l'instance d'un objet TournoiScreen
        """

        print("Debut du tournoi au :", tournoi.dateDeDebut)
        while tournoi.numeroTourActuel < tournoi.nombreTours:
            print(" \n \nDebut du Tour : " + str(tournoi.numeroTourActuel + 1))
            saveOrNot = input(
                "Avant de passer au tour suivant, Voudriez vous faire une sauvegarde (Y/N) ? "
            )
            if saveOrNot == "Y":
                print("Sauvegarde en cours.....")
                with open("bin/tournoi.pkl", "wb") as out_file:
                    pickle.dump(tournoi, out_file)
                print("Sauvegarde terminée.....")
            for match in tournoi.tours[tournoi.numeroTourActuel].matchs:
                tournoiScreen.round(match)
                match.updateScore()
                tournoiScreen.afficherMatch(match)
                print("----------------------------------------------------------------")
            tournoi.numeroTourActuel += 1
        tournoi.dateDeFin = date.today().strftime("%d/%m/%Y")
        print("Fin de tournoi au : ***************")
