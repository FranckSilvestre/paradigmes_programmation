from model import Position, Fleur
from model.Abeille import Abeille


class Carte:

    def __init__(self, dimension: Position):
        self.dimension = dimension
        self.fleurs = []
        # Ajout P2.Ex2
        self.abeilles = []

    def ajouteFleur(self, fleur: Fleur):
        assert self.objetEstPositionnableSurLaCarte(fleur.position), "la fleur n'est pas sur cette carte"
        self.fleurs.append(fleur)

    # Ajout P2.Ex2
    def ajouteAbeille(self, abeille: Abeille):
        assert self.objetEstPositionnableSurLaCarte(abeille.position), "l'abeille n'est pas sur cette carte"
        self.abeilles.append(abeille)

    def objetEstPositionnableSurLaCarte(self, positionObjet: Position) -> bool:
        if (positionObjet.positionNS > self.dimension.positionNS):
            return False
        if (positionObjet.positionOE > self.dimension.positionOE):
            return False
        return True

