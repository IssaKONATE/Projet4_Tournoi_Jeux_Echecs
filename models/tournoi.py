import json
from models.Tour import Tour
from models.Match import Match
from models.joueur import Joueur

# Choisis de manière aléatoire un élément dans une liste
from random import choice


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

    joueursJson = []
    joueursQualifies = []
    vainqueurFinal = None

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
        self.joueurs = self.joueursJson
        self.joueursQualifies = self.joueursJson
        self.tours = [Tour("", "", "", self.tirage())]

    def ajouterJoueur(self, joueur):
        """
        Cette méthode permet d'ajouter un joueur à la liste des joueurs
        Args:
           joueur (Joueur): le joueur à ajouter à la liste
        """

        found = any(
            x.nom == joueur.nom and x.prenom == joueur.prenom for x in self.joueursJson
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
        else:
            # sinon ajouter le joueur
            self.joueursJson.append(joueur)

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

    # Tirage au sort des joueurs et établit la liste des matchs pour ce tour
    def tirage(self):
        """
        Cette méthode permet de faire le tirage de façon aléatoire à partir de la liste des joueurs.
        Args:
        Aucun

        Returns:
        Match[]: return une liste de matchs qui opposent les joueurs deux à deux
        """

        joueursQualifies = self.joueursQualifies
        matchs = []
        while joueursQualifies:
            p = []
            for i in range(2):
                e = choice(joueursQualifies)
                p.append(e)
                joueursQualifies.remove(e)
            matchs.append(Match(p[0], p[1]))
        return matchs
