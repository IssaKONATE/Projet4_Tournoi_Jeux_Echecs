import json

from models.joueur import Joueur


class Tournoi(object) :
    tours = []
    joueurs = []
    def __init__(self, nom, lieu, dateDeDebut, dateDeFin, nombreTours, numeroTourActuel):
        self.nom = nom
        self.lieu = lieu
        self.dateDeDebut = dateDeDebut
        self.dateDeFin = dateDeFin
        self.nombreTours = nombreTours
        self.numeroTourActuel = numeroTourActuel


    def ajouterJoueur(self, joueur):
        if(self.joueurs.__contains__(joueur)):
            print("Ce joueur est déjà enregistré ==> ", joueur.nom," ", joueur.prenom," ", "Date de naissance: ", joueur.dateDeNaissance)
        else:
            self.joueurs.append(joueur)

    def initJoueursParFichierJson(self):
        dataJoueurs = []
        # Chargement du fichier json contenant les joueurs
        with open("data/tournaments/joueurs.json") as f:
            dataJoueurs = json.load(f)
            # parcours de la liste des joueurs
            for joueur in dataJoueurs:
                self.ajouterJoueur(Joueur(nom=joueur['nom'], prenom=joueur['prenom'], dateDeNaissance=joueur['dateDeNaissance'], id=joueur['id']))


    def afficherJoueursDuTournoi(self):
        for joueur in self.joueurs:
            joueur.afficher()