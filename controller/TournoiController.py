from datetime import date
import pickle
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
                with open("sauvegarde/tournoi.pkl", "wb") as out_file:
                    pickle.dump(tournoi, out_file)
                print("Sauvegarde terminée.....")
            for match in tournoi.tours[tournoi.numeroTourActuel].matchs:
                tournoiScreen.round(match)
                match.updateScore()
                tournoiScreen.afficherMatch(match)
                print(
                    "----------------------------------------------------------------"
                )

            tournoiScreen.afficherJoueurParPointDecroissant(tournoi.joueurs)
            tournoi.numeroTourActuel += 1
        tournoi.dateDeFin = date.today().strftime("%d/%m/%Y")
        print("Fin de tournoi au : ***************")

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

    def ajouterJoueurByTerminal(self, listeJoueur):
        nom = input("Entrer nom : ")
        prenom = input("Entrer prenom : ")
        dateNaissance = input("Entrer date de naissance : ")
        id = input("Entrer Id: ")
        joueur = Joueur(nom=nom, prenom=prenom, dateDeNaissance=dateNaissance, id=id)
        self.ajouterJoueur(joueur=joueur)

    def initJoueursParFichierJson(self):
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
                self.ajouterJoueur(
                    Joueur(nom=nom, prenom=prenom, dateDeNaissance=dateNaissance, id=id)
                )

    def tirage(self):
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
        for joueur in self.joueurs:
            joueursTirage.append(joueur)
        matchs = []
        size = len(joueursTirage)
        for i in range(size):
            for j in range(i + 1, size):
                matchs.append(Match(self.joueurs[i], self.joueurs[j]))
        return matchs

    def process(self, matchs):
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
        self.nombreDeMatchParTour = len(self.joueurs) / 2
        self.nombreTours = len(self.joueurs) - 1
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
                    if len(intermediaire) < self.nombreDeMatchParTour:
                        intermediaire.append(matchChoice)
                if len(intermediaire) >= self.nombreDeMatchParTour:
                    listeTours.append(
                        Tour(
                            dateDeDebut="",
                            dateDeFin="",
                            nomTour="Tour XX",
                            matchs=intermediaire,
                        )
                    )
                    intermediaire = []
        self.tours = listeTours
        return listeTours

