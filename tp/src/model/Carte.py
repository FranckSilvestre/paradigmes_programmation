from model import Position, Fleur


class Carte:

    def __init__(self, dimension: Position):
        self.dimension = dimension
        self.fleurs = []

    def ajouteFleur(self, fleur: Fleur):
        assert self.objetEstPositionnableSurLaCarte(fleur.position), "la fleur n'est pa sur cette carte"
        self.fleurs.append(fleur)

    def objetEstPositionnableSurLaCarte(self, positionObjet: Position) -> bool:
        if (positionObjet.positionNS > self.dimension.positionNS):
            return False
        if (positionObjet.positionOE > self.dimension.positionOE):
            return False
        return True

