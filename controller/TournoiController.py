from models.Tour import Tour
from models.tournoi import Tournoi


class TournoiController(object):

    def __init__(self):
        print("TournoiController")

    def deroulerTour(self, tournoi:Tournoi):
        
        while( len(tournoi.tours[tournoi.numeroTourActuel].matchs)>0):
            joueursQualifies = []

            print(" \n \n Debut du Tour : "+str(tournoi.numeroTourActuel+1) )
            for match in tournoi.tours[tournoi.numeroTourActuel].matchs:
                match.round()
                joueursQualifies.append(match.vainqueur)
            
            # Ici on recupère les joueurs qualifiés pour ce tour
            tournoi.joueursQualifies = joueursQualifies

            #Ici on teste si on a le vainqueur final du tournoi, si oui nous sortons de la boucle sinon nous continuons le deroulement du tour
            if(len(tournoi.joueursQualifies)==1):
                tournoi.vainqueurFinal = tournoi.joueursQualifies[0]
                break
            
            tournoi.tours.append(Tour(input("Entrer Date début prochain tour: "), input("Entrer Date fin prochain tour:"), "Tour N° : "+str(tournoi.numeroTourActuel), tournoi.tirage()))
            tournoi.numeroTourActuel += 1
            
                
# explication
