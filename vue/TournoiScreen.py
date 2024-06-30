from models.Match import Match
from models.joueur import Joueur


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
        print("******************** La liste des joueurs du tournoi est la suivante ********************")
        joueurs.sort(key=lambda joueur:joueur.nom+joueur.prenom)
        for joueur in joueurs:
            self.afficherJoueur(joueur=joueur)
        print("******************** ******************** ******************** ******************** ******")
