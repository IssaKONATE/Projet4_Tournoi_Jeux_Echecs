class Tour(object):
    """
    Cette classe nommée Tour représente le Tour du tournoi
    Attributes:
        dateDeDebut (string): date de début
        dateDeFin (string): date de fin
        nomTour (string): nom du tour
        matchs (Match[]): liste des matchs de ce tour
    """

    matchs = []

    def __init__(self, dateDeDebut, dateDeFin, nomTour, matchs):
        self.dateDeDebut = dateDeDebut
        self.dateDeFin = dateDeFin
        self.nomTour = nomTour
        self.matchs = matchs
