import pickle
import json
from controller.TournoiController import TournoiController
from models.tournoi import Tournoi
from vue.TournoiScreen import TournoiScreen

# Main point d'entrée de l'application
if __name__ == "__main__":

    controller = TournoiController()
    matchScreen: TournoiScreen = TournoiScreen()
    playSauvegarde = input("\nVoudriez-vous lancer la sauvegarde ... (Y/N) ? ")
    if(playSauvegarde == 'Y'):
        print("Debut du tournoi sauvegardé...")
        tournoiSauvegarder = None
        with open("bin/tournoi.pkl", "rb") as in_file:
            tournoiSauvegarder = pickle.load(in_file)
        controller.deroulerTour(tournoiSauvegarder, matchScreen)
        tournoiSauvegarderJson = json.dumps(
        tournoiSauvegarder, default=lambda o: o.__dict__, sort_keys=True, indent=4)
        print(tournoiSauvegarderJson)
    else:
        # Créer le tournoi
        tournoi = Tournoi(
            nom="CAN 2024",
            dateDeFin=None,
            dateDeDebut="01/01/2024",
            lieu="Cote d'Ivoire",
            nombreTours=4,
            numeroTourActuel=0,
        )  
        matchScreen.afficherJoueurs(tournoi.joueurs)
        retourInput = input("Voudriez-vous ajouter un nouveau joueur à la liste (Y/N) ? ")
        while retourInput == 'Y' or len(tournoi.joueurs)%3 == 0:
            tournoi.ajouterJoueurByTerminal(tournoi.joueurs)
            retourInput = input("Voudriez-vous ajouter un nouveau joueur à la liste (Y/N) ? ")
        matchScreen.afficherJoueurs(tournoi.joueurs)
        print("La liste des joueurs est complète \n Nous pouvons demarrer le tournoi")
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
        matchScreen.afficherJoueurs(tournoi.joueurs)
