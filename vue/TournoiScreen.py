import glob
import json
from models.Match import Match
from models.joueur import Joueur
from models.tournoi import Tournoi


class TournoiScreen(object):
    """
    Cette classe nommée TournoiScreen représente la vue

    Attributes:
        Aucun attribut
    """

    def __init__(self):
        pass

    def round(self, match: Match):
        """
        cette méthode round permet lancer un round
        Args:
            match (Match): l'instance d'un objet Match.
        """

        print("Veuillez enregistrer le score du joueur :")
        self.afficherJoueur(match.scoring1.joueur)
        match.scoring1.score = self.readInput()
        print("Veuillez enregistrer le score du joueur ")
        self.afficherJoueur(match.scoring2.joueur)
        match.scoring2.score = self.readInput()

    def readInput(self):
        """
        cette méthode permet de lire un entier depuis le terminal
        Args:
            Aucun
        Returns:
        int : l'entier retourné représente le score de ce joueur
        """

        loop = True
        inputVar = -1
        while loop:
            try:
                inputVar = int(input("Enter a score : "))
                loop = False
            except ValueError:
                print("Veuillez entrer un entier")
        return inputVar

    # permet de lire les données sur la sorties?
    def afficherMatch(self, match: Match):
        """
        cette méthode permet d'afficher les joueurs avec leur score
        Args:
            Aucun
        """
        self.afficherJoueur(match.scoring1.joueur)
        self.afficherJoueur(match.scoring2.joueur)

    # explication classread input

    def afficherJoueur(self, joueur: Joueur):
        """
        cette méthode permet d'afficher les infos d'un joueur
        Args:
            Aucun
        """
        print(
            "** Id: ",
            joueur.id,
            ", Nom : ",
            joueur.nom,
            ",Prenom : ",
            joueur.prenom,
            ", Date de naissance : ",
            joueur.dateDeNaissance,
            ", Point : ",
            joueur.point,
        )

    def trierParNom(listeDico):
        return listeDico.nom

    def afficherJoueurs(self, joueurs):
        print(
            "******************** Liste des joueurs déjà inscrits ********************"
        )
        joueurs.sort(key=lambda joueur: joueur.nom + joueur.prenom)
        for joueur in joueurs:
            self.afficherJoueur(joueur=joueur)
        print(
            "******************** ******************** ******************** ******************** ******"
        )

    def afficherJoueurParPointDecroissant(self, joueurs):
        """
        cette méthode permet d'afficher les joueurs par ordre de points decroissant
        Args:
            joueurs: list Joueur
        """
        print(
            "******************** Classement des joueurs par point ********************"
        )
        joueurs.sort(key=lambda joueur: joueur.point, reverse=True)
        for joueur in joueurs:
            self.afficherJoueurParPoint(joueur=joueur)
        print(
            "******************** ******************** ******************** ******************** ******"
        )

    def afficherJoueurParPoint(self, joueur: Joueur):
        """
        cette méthode permet d'afficher joueur avec son point
        Args:
            joueur: Joueur
        """
        print(
            joueur.prenom
            + "  "
            + joueur.nom
            + "........................"
            + str(joueur.point)
        )

    def initTournoi(self):
        print(
            "\nA ==> Initialiser un tournoi\n",
            "B ==> Lancer la sauvegarde \n",
            "C ==> Generer rapport \n",
            "D ==> Afficher rapport\n" "E ==> Quitter",
        )
        return input()

    def afficherRapport(self, tournoi: Tournoi):
        print(glob.glob("output/*.json"))
        fileName = input("Entrer le nom du rapport que vous voudriez afficher : ")
        f = open("output/" + fileName, "r")
        print(f.read())
