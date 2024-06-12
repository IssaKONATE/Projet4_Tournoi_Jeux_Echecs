from models.Tour import Tour
from models.tournoi import Tournoi


class TournoiController(object):

    def __init__(self):
        print("TournoiController")

    def deroulerTour(self, tournoi:Tournoi):
        
        while( len(tournoi.tours[tournoi.numeroTourActuel].matchs)>0):
            joueursQualifies = []
            for match in tournoi.tours[tournoi.numeroTourActuel].matchs:
                match.round()
                joueursQualifies.append(match.vainqueur)
            
            tournoi.joueursQualifies = joueursQualifies

            if(len(tournoi.joueursQualifies)==1):
                tournoi.vainqueurFinal = tournoi.joueursQualifies[0]
                break
            
            tournoi.tours.append(Tour("", "", "", tournoi.tirage()))
            tournoi.numeroTourActuel += 1
            print("\n \n")
                
# explication
