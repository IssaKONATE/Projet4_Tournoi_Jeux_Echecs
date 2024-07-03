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
