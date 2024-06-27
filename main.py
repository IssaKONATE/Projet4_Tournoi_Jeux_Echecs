import pickle
import json
from controller.TournoiController import TournoiController
from models.tournoi import Tournoi
from vue.TournoiScreen import TournoiScreen

# Main point d'entrée de l'application
if __name__ == "__main__":
    # Créer le tournoi
    tournoi = Tournoi(
        nom="CAN 2024",
        dateDeFin=None,
        dateDeDebut="01/01/2024",
        lieu="Cote d'Ivoire",
        nombreTours=4,
        numeroTourActuel=0,
    )
    # creer objet controller du tournoi
    matchScreen: TournoiScreen = TournoiScreen()
    controller = TournoiController()

    # Lance le deroulement du tournoi
    controller.deroulerTour(tournoi, matchScreen)
    # Convertir l'objet tournoi en objet JSON
    tournoiJson = json.dumps(
        tournoi, default=lambda o: o.__dict__, sort_keys=True, indent=4
    )
    f = open("output/tournoi.json", "w")
    f.write(tournoiJson)
    f.close()
    print("Tournoi EN COURS terminé  !!!")
    
    print("Debut du tournoi sauvegardé...")
    tournoi2 = None
    with open("output/tournoi.pkl", "rb") as in_file:
        tournoi2 = pickle.load(in_file)
    controller.deroulerTour(tournoi2, matchScreen)
    tournoi2Json = json.dumps(
        tournoi2, default=lambda o: o.__dict__, sort_keys=True, indent=4
    )
    print(tournoi2Json)
