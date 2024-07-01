from datetime import date
import os
import pickle
import json
from controller.TournoiController import TournoiController
from models.tournoi import Tournoi
from vue.TournoiScreen import TournoiScreen

# Main point d'entrée de l'application
if __name__ == "__main__":

    controller = TournoiController()
    matchScreen: TournoiScreen = TournoiScreen()
    while True:
        if os.path.exists("sauvegarde/tournoi.pkl"):
            playSauvegarde = input("\nVoudriez-vous lancer la sauvegarde ... (Y/N) ? ")
            if playSauvegarde == "Y":
                print("Debut du tournoi sauvegardé...")
                tournoiSauvegarder = None
                try:
                    with open("sauvegarde/tournoi.pkl", "rb") as in_file:
                        print("Chargement de la sauvegarde .....")
                        tournoiSauvegarder = pickle.load(in_file)
                        print("Fin chargement de la sauvegarde")
                        controller.deroulerTour(tournoiSauvegarder, matchScreen)
                except IOError:
                    print("Error! Il n'existe pas de sauvegarde de jeu")

        yesOrNot = input("Voudriez vous créer un nouveau tournoi (Y/N) ? ")

        if yesOrNot == "Y":
            # Créer le tournoi
            tournoi = Tournoi(
                nom=input("Entrer Nom du tournoi: "),
                dateDeFin=None,
                dateDeDebut=date.today().strftime("%d/%m/%Y"),
                lieu=input("Entrer le lieu du tournoi: "),
                nombreTours=4,
                numeroTourActuel=0,
            )
            matchScreen.afficherJoueurs(tournoi.joueurs)
            retourInput = input(
                "Voudriez-vous ajouter un nouveau joueur à la liste (Y/N) ? "
            )
            while retourInput == "Y":
                tournoi.ajouterJoueurByTerminal(tournoi.joueurs)
                retourInput = input(
                    "Voudriez-vous ajouter un nouveau joueur à la liste (Y/N) ? "
                )
            while len(tournoi.joueurs) % 2 != 0:
                print(
                    "Le nombre de joueurs ne doit pas être impair, veuillez ajouter un nouveau joueur"
                )
                tournoi.ajouterJoueurByTerminal(tournoi.joueurs)
            matchScreen.afficherJoueurs(tournoi.joueurs)
            print(
                "La liste des joueurs est complète \n Nous pouvons demarrer le tournoi"
            )

            tournoi.process(tournoi.tirage())

            # Lance le deroulement du tournoi
            controller.deroulerTour(tournoi, matchScreen)
            # Convertir l'objet tournoi en objet JSON
            tournoiJson = json.dumps(
                tournoi, default=lambda o: o.__dict__, sort_keys=True, indent=4
            )
            f = open("output/tournoi.json", "w")
            f.write(tournoiJson)
            f.close()
            matchScreen.afficherJoueurs(tournoi.joueurs)
        else:
            break
    print("Fin du programme!!")
