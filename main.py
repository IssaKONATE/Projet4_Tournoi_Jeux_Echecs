import json
from controller.TournoiController import TournoiController
from models.tournoi import Tournoi

#Main
if __name__ == '__main__':
    tournoi = Tournoi(nom="CAN 2024", dateDeFin=None,dateDeDebut="01/01/2024",lieu="Côte d'Ivoire",nombreTours=6, numeroTourActuel=0)

    controller = TournoiController()
    controller.deroulerTour(tournoi)

    z = json.dumps(tournoi,
                   default=lambda o: o.__dict__,
                   sort_keys=True,
                   indent=4)
    
    print(z)