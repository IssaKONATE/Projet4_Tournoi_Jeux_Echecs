from datetime import date
import json
import pickle
from models.Match import Match
from models.Tour import Tour
from models.joueur import Joueur
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
            for match in tournoi.tours[tournoi.numeroTourActuel].matchs:
                tournoiScreen.round(match)
                match.updateScore()
                tournoiScreen.afficherMatch(match)
                print(
                    "----------------------------------------------------------------"
                )
            yesOrNo = input("Voudriez-vous sauvegarder le tournoi ... (Y/N)")
            if yesOrNo == "Y":
                self.saveTournoi(tournoi=tournoi)
            tournoiScreen.afficherJoueurParPointDecroissant(tournoi.joueurs)
            tournoi.numeroTourActuel += 1
        tournoi.dateDeFin = date.today().strftime("%d/%m/%Y")
        print("Fin de tournoi au : ", tournoi.dateDeFin)

    def saveTournoi(self, tournoi: Tournoi):
        print("Sauvegarde en cours.....")
        fileName = tournoi.nom + "_" + tournoi.lieu + "_tournoi.pkl"
        with open("sauvegarde/" + fileName, "wb") as out_file:
            pickle.dump(tournoi, out_file)
        print("Sauvegarde terminée.....")

    def ajouterJoueurByTerminal(self, tournoi):
        nom = input("Entrer nom : ")
        prenom = input("Entrer prenom : ")
        dateNaissance = input("Entrer date de naissance : ")
        id = input("Entrer Id: ")
        joueur = Joueur(nom=nom, prenom=prenom, dateDeNaissance=dateNaissance, id=id)
        tournoi.ajouterJoueur(joueur=joueur)

    def initJoueursParFichierJson(self, tournoi):
        """
        Cette méthode permet d'initialiser la liste des joueurs à partir d'un fichier json
        Args:
        Aucun
        """

        dataJoueurs = []
        # Chargement du fichier json contenant les joueurs
        with open("data/tournaments/joueurs.json") as f:
            dataJoueurs = json.load(f)
            # parcours de la liste des joueurs
            for joueur in dataJoueurs:
                # Ajout des données json(joueurs) dans la liste des joueurs
                nom = joueur["nom"]
                prenom = joueur["prenom"]
                dateNaissance = joueur["dateDeNaissance"]
                id = joueur["id"]
                tournoi.ajouterJoueur(
                    Joueur(nom=nom, prenom=prenom, dateDeNaissance=dateNaissance, id=id)
                )

    def tirage(self, tournoi):
        """
        Cette méthode permet de faire le tirage de façon aléatoire à partir de la liste des joueurs.
        Chaque tour ou round est constitué de plusieurs matchs
        La confrontation joueur à joueur est unique
        Args:
        Aucun

        Returns:
        Match[]: return une liste de matchs qui opposent les joueurs deux à deux
        """

        joueursTirage = []
        for joueur in tournoi.joueurs:
            joueursTirage.append(joueur)
        matchs = []
        size = len(joueursTirage)
        for i in range(size):
            for j in range(i + 1, size):
                matchs.append(Match(tournoi.joueurs[i], tournoi.joueurs[j]))
        return matchs

    def process(self, matchs, tournoi):
        """
        Cette méthode permet de faire le tirage de façon aléatoire à partir de la liste des joueurs.
        Chaque tour ou round est constitué de plusieurs matchs
        La confrontation joueur à joueur est unique
        Args:
        Aucun

        Returns:
        list Match: return une liste de matchs qui opposent les joueurs deux à deux
        """

        listeTours = []
        matchTmp = []
        intermediaire = []
        tournoi.nombreDeMatchParTour = len(tournoi.joueurs) / 2
        tournoi.nombreTours = len(tournoi.joueurs) - 1
        for match in matchs:
            matchTmp.append(match)

        while matchTmp:
            for matchChoice in matchTmp:
                found = any(
                    x.scoring1.joueur.id == matchChoice.scoring1.joueur.id
                    or x.scoring1.joueur.id == matchChoice.scoring2.joueur.id
                    or x.scoring2.joueur.id == matchChoice.scoring1.joueur.id
                    or x.scoring2.joueur.id == matchChoice.scoring2.joueur.id
                    for x in intermediaire
                )
                if not found:
                    matchTmp.remove(matchChoice)
                    if len(intermediaire) < tournoi.nombreDeMatchParTour:
                        intermediaire.append(matchChoice)
                if len(intermediaire) >= tournoi.nombreDeMatchParTour:
                    listeTours.append(
                        Tour(
                            dateDeDebut="",
                            dateDeFin="",
                            nomTour="Tour XX",
                            matchs=intermediaire,
                        )
                    )
                    intermediaire = []
        tournoi.tours = listeTours
        return listeTours

    def genererRapport(self, tournoi: Tournoi):
        # Convertir l'objet tournoi en objet JSON
        tournoiJson = json.dumps(
            tournoi, default=lambda o: o.__dict__, sort_keys=True, indent=4
        )
        nomFichier = "output/" + tournoi.nom + "_" + tournoi.lieu + "_" + "tournoi.json"
        f = open(nomFichier, "w")
        f.write(tournoiJson)
        f.close()
