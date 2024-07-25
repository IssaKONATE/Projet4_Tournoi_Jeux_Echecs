from datetime import date
import glob
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

    tournoi = None
    while True:
        inputRead = matchScreen.initTournoi()
        if inputRead == "A" or inputRead == "a":
            print("Début d'un nouveau tournoi ")
            # Créer le tournoi
            tournoi = Tournoi(
                nom=input("Entrer Nom du tournoi: "),
                dateDeFin=None,
                dateDeDebut=date.today().strftime("%d/%m/%Y"),
                lieu=input("Entrer le lieu du tournoi: "),
                nombreTours=4,
                numeroTourActuel=0,
            )

            controller.initJoueursParFichierJson(tournoi=tournoi)
            matchScreen.afficherJoueurs(tournoi.joueurs)
            retourInput = input(
                "Voudriez-vous ajouter un nouveau joueur à la liste (Y/N) ? "
            )
            while retourInput == "Y":
                controller.ajouterJoueurByTerminal(tournoi)
                retourInput = input(
                    "Voudriez-vous ajouter un nouveau joueur à la liste (Y/N) ? "
                )
            while len(tournoi.joueurs) % 2 != 0:
                print(
                    "Le nombre de joueurs ne doit pas être impair, veuillez ajouter un nouveau joueur"
                )
                controller.ajouterJoueurByTerminal(tournoi)
            print(
                "La liste des joueurs est complète \n Nous pouvons demarrer le tournoi"
            )
            controller.process(controller.tirage(tournoi), tournoi=tournoi)
            controller.deroulerTour(tournoi, matchScreen)

        elif inputRead == "B" or inputRead == "b":
            print(glob.glob("sauvegarde/*.pkl"))
            fileName = input("Entrer le nom de la sauvegarde à lancer : ")

            if os.path.exists("sauvegarde/" + fileName):
                try:
                    with open("sauvegarde/" + fileName, "rb") as in_file:
                        print("Chargement de la sauvegarde .....")
                        tournoiSauvegarder = pickle.load(in_file)
                        print("Fin chargement de la sauvegarde")
                        controller.deroulerTour(tournoiSauvegarder, matchScreen)
                except IOError:
                    print("Error! Il n'existe pas de sauvegarde de jeu")
            else:
                print("Il n'existe aucune sauvegarde !!!")
        elif inputRead == "C" or inputRead == "c":
            controller.genererRapport(tournoi=tournoi)
        elif inputRead == "D" or inputRead == "d":
            matchScreen.afficherRapport(tournoi=tournoi)
        elif inputRead == "E" or inputRead == "e":
            print("Fin du programme!!")
            break
        else:
            print("Commande non reconnue !!!")
