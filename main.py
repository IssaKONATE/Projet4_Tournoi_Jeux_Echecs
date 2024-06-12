import json
from controller.TournoiController import TournoiController
from models.tournoi import Tournoi

#Main point d'entrée de l'application
if __name__ == '__main__':
    
    #Créer le tournoi
    tournoi = Tournoi(nom="CAN 2024", dateDeFin=None,dateDeDebut="01/01/2024",lieu="Cote d'Ivoire",nombreTours=4, numeroTourActuel=0)

    # creer objet controller du tournoi
    controller = TournoiController() 

    #Lance le deroulement du tournoi
    controller.deroulerTour(tournoi)

    #Convertir l'objet tournoi en objet JSON
    tournoiJson = json.dumps(tournoi,
                   default=lambda o: o.__dict__,
                   sort_keys=True,
                   indent=4)
      
    f = open("output/tournoi.json", "w")
    f.write(tournoiJson)
    f.close()
    
    # affichage de l'ojet tournoi en données JSON
    print(tournoiJson)