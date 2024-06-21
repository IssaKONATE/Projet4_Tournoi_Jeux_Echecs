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

        while (len(tournoi.tours[tournoi.numeroTourActuel].matchs) > 0):
            joueursQualifies = []
            print(" \n \n Debut du Tour : "+str(tournoi.numeroTourActuel+1))
            saveOrNot = input("Avant de passer au tour suivant, Voudriez vous faire une sauvegarde (Y/N)")
            if (saveOrNot == 'Y'):
                print("Sauvegarde en cours.....")
                with open('output/tournoi.pkl', 'wb') as out_file:
                    pickle.dump(tournoi, out_file)
                print("Sauvegarde terminée.....")
            for match in tournoi.tours[tournoi.numeroTourActuel].matchs:
                tournoiScreen.round(match)
                match.updateScore()
                tournoiScreen.afficherMatch(match)
                joueursQualifies.append(match.vainqueur)
            # Ici on recupère les joueurs qualifiés pour ce tour
            tournoi.joueursQualifies = joueursQualifies
            # Ici on teste si on a le vainqueur final du tournoi
            # Si oui nous sortons de la boucle sinon nous continuons
            # le deroulement du tour
            if (len(tournoi.joueursQualifies) == 1):
                tournoi.vainqueurFinal = tournoi.joueursQualifies[0]
                break
            debut = input("Entrer Date début prochain tour: ")
            fin = input("Entrer Date fin prochain tour:")
            nomTour = "Tour N° : "+str(tournoi.numeroTourActuel)
            tournoi.tours.append(Tour(dateDeDebut=debut, dateDeFin=fin, nomTour=nomTour, matchs=tournoi.tirage()))
            tournoi.numeroTourActuel += 1
# explication
