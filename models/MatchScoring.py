
class MatchScoring(object) :

    """
    Cette classe nommée MatchScoring représente le score du joueur pendant le match
    Attributes:
        joueur (Joueur): représente le joueur
        score (int): représente son score'
        qualifier (int): -1 non qualifié, 1 qualifié
    """

    def __init__(self, joueur, score, qualifier):
        self.joueur = joueur
        self.score = score
        self.qualifier = qualifier
