class Match(object) :
    def __init__(self, joueur1, score1, joueur2, score2):
        self.joueur1Score1 = tuple(joueur1, score1)
        self.joueur2Score2 = tuple(joueur2, score2)

        # definir nouvelle methode va permettre de déterminer lequel des joueurs a gagné et attribuer les points aux joueurs
    def match (self) :
        if self.joueur1Score1[1] > self.joueur2Score2[1] :
            self.joueur1Score1[0].point = self.joueur1Score1[0].point + 1
        elif self.joueur1Score1[1]< self.joueur2Score2[1] :
            self.joueur2Score2[0].point = self.joueur2Score2[0].point + 1
        else :
            self.joueur1Score1[0].point = self.joueur1Score1[0].point + 0.5
            self.joueur2Score2[0].point = self.joueur2Score2[0].point + 0.5



