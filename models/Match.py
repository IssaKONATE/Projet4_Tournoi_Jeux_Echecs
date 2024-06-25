from models.MatchScoring import MatchScoring


class Match(object):
    """
    Cette classe nommée Match représente un match qui oppose deux joueurs.
    Attributes:
        scoring1 (MatcScoring): représente le joueur 1 et son score'
        scoring2 (MatcScoring): représente le joueur 2 et son score'
    """

    def __init__(self, joueur1, joueur2):
        self.scoring1 = MatchScoring(joueur=joueur1, score=0, qualifier=0)
        self.scoring2 = MatchScoring(joueur=joueur2, score=0, qualifier=0)
        self.vainqueur = None

    # Elle permet de déterminer lequel des joueurs a gagné et attribuer les points aux joueurs
    def updateScore(self):
        """
        Cette méthode permet de mettre à jour le point des joueurs après la fin de ce match
        Args:
            Aucun argument
        """
        if self.scoring1.score > self.scoring2.score:
            self.scoring1.joueur.point = self.scoring1.joueur.point + 1
            self.scoring1.qualifier = 1
            self.scoring2.qualifier = -1
            self.vainqueur = self.scoring1.joueur
        elif self.scoring1.score < self.scoring2.score:
            self.scoring2.joueur.point = self.scoring2.joueur.point + 1
            self.scoring1.qualifier = -1
            self.scoring2.qualifier = 1
            self.vainqueur = self.scoring2.joueur
        else:
            self.scoring1.joueur.point = self.scoring1.joueur.point + 0.5
            self.scoring2.joueur.point = self.scoring2.joueur.point + 0.5
