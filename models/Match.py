from models.MatchScoring import MatchScoring


class Match(object) :
    def __init__(self, joueur1, joueur2):
        self.scoring1 =  MatchScoring(joueur=joueur1, score=0, qualifier=0)
        self.scoring2 = MatchScoring(joueur=joueur2, score=0, qualifier=0)
        self.vainqueur = None

        # definir nouvelle methode va permettre de dét lequel des joueurs a gagné et attribuer les points aux joueurs
    def updateScore (self) :
        if self.scoring1.score > self.scoring2.score :
            self.scoring1.joueur.point = self.scoring1.joueur.point + 1
            self.scoring1.qualifier=1
            self.scoring2.qualifier=-1
            self.vainqueur = self.scoring1.joueur
        elif self.scoring1.score< self.scoring2.score :
            self.scoring2.joueur.point = self.scoring2.joueur.point + 1
            self.scoring1.qualifier= -1
            self.scoring2.qualifier= 1
            self.vainqueur = self.scoring2.joueur
        else :
            self.scoring1.joueur.point = self.scoring1.joueur.point + 0.5
            self.scoring2.joueur.point = self.scoring2.joueur.point + 0.5


    def round(self):
        print("Veuillez enregistrer le score du joueur :")
        self.scoring1.joueur.afficher()
        self.scoring1.score = self.readInput()

        print("Veuillez enregistrer le score du joueur ")
        self.scoring2.joueur.afficher()
        self.scoring2.score = self.readInput()

        self.updateScore()
        self.afficher()

    def readInput(self):
        loop = True
        inputVar = -1
        while loop:
            try:
                inputVar = int(input("Enter a number: "))
                loop = False
            except ValueError:
                print("Veuillez entrer un entier")
        return inputVar

    def afficher(self):
        self.scoring1.joueur.afficher()
        self.scoring2.joueur.afficher()




#explication read input  