class Match(object) :
    def __init__(self, joueur1, score1, joueur2, score2):
        self.joueur1Score1 = tuple(joueur1, score1)
        self.joueur2Score2 = tuple(joueur2, score2)

