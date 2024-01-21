from models.tournoi import Tournoi

#Main
if __name__ == '__main__':
    tournoi = Tournoi(nom="CAN 2024", dateDeFin=None,dateDeDebut="01/01/2024",lieu="Côte d'Ivoire",nombreTours=6, numeroTourActuel=0)
    tournoi.initJoueursParFichierJson()
    #tournoi.afficherJoueursDuTournoi()
    lesPoules = tournoi.tirage()
    poule = 0
    for pouleList in lesPoules:
        poule = poule + 1
        print( "Poule <"+str(poule)+">")
        for joueur in pouleList:
            joueur.afficher()
