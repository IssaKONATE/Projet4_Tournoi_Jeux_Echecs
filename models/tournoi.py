import json

from models.Tour import Tour
from models.Match import Match
from models.joueur import Joueur

#Choisis de manière aléatoire un élément dans une liste
from random import choice


class Tournoi(object) :
    joueursJson = []
    joueursQualifies=[]
    vainqueurFinal = None
    
    # Ici on définit un constructeur de l'objet Tournoi
    def __init__(self, nom, lieu, dateDeDebut, dateDeFin, nombreTours, numeroTourActuel):
        self.nom = nom
        self.lieu = lieu
        self.dateDeDebut = dateDeDebut
        self.dateDeFin = dateDeFin
        self.nombreTours = nombreTours
        self.numeroTourActuel = numeroTourActuel
        self.initJoueursParFichierJson()
        self.joueurs = self.joueursJson
        self.joueursQualifies= self.joueursJson
        self.tours  = [Tour("", "", "", self.tirage())]


    def ajouterJoueur(self, joueur):
        found = any(x.nom == joueur.nom and x.prenom == joueur.prenom for x in self.joueursJson)
        if(found):
            print("Ce joueur est déjà enregistré ==> ", joueur.nom," ", joueur.prenom," ", "Date de naissance: ", joueur.dateDeNaissance)
        else:
            #sinon ajouter le joueur
            self.joueursJson.append(joueur)

    def initJoueursParFichierJson(self):
        dataJoueurs = []
        # Chargement du fichier json contenant les joueurs
        with open("data/tournaments/joueurs.json") as f:
            dataJoueurs = json.load(f)
            # parcours de la liste des joueurs
            for joueur in dataJoueurs:
                # Ajout des données json(joueurs) dans la liste des joueurs 
                self.ajouterJoueur(Joueur(nom=joueur['nom'], prenom=joueur['prenom'], dateDeNaissance=joueur['dateDeNaissance'], id=joueur['id']))


    def afficherJoueursDuTournoi(self):
        for joueur in self.joueursJson:
            joueur.afficher()

    #Tirage au sort des joueurs et établit la liste des matchs pour ce tour
    def tirage(self):
        l = self.joueursQualifies
        matchs = []
        while l:
            p = []
            for i in range(2):
                e = choice(l)
                p.append(e)
                l.remove(e)
            matchs.append(Match(p[0], p[1]))
        
        return matchs