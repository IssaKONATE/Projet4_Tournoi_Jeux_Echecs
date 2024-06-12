import json

from models.Tour import Tour
from models.Match import Match
from models.joueur import Joueur
from random import choice


class Tournoi(object) :
    joueurs = []
    joueursQualifies=[]
    vainqueurFinal = None
    
    def __init__(self, nom, lieu, dateDeDebut, dateDeFin, nombreTours, numeroTourActuel):
        self.nom = nom
        self.lieu = lieu
        self.dateDeDebut = dateDeDebut
        self.dateDeFin = dateDeFin
        self.nombreTours = nombreTours
        self.numeroTourActuel = numeroTourActuel
        self.initJoueursParFichierJson()
        self.joueursQualifies= self.joueurs
        self.tours  = [Tour("", "", "", self.tirage())]


    def ajouterJoueur(self, joueur):
        found = any(x.nom == joueur.nom and x.prenom == joueur.prenom for x in self.joueurs)
        if(found):
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

    def tirage(self):
        l = self.joueursQualifies
        o = []
        while l:
            p = []
            for i in range(2):
                e = choice(l)
                p.append(e)
                l.remove(e)
            o.append(Match(p[0], p[1]))
        
        return o
    
    #explication tirage