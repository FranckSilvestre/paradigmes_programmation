from model.Position import Position
from model.Carte import Carte

# ici : possibilité de réfléchir à la "struture de donnée "VueCarte" pour optimiser
# l'affichage
class VueCarte:

    def __init__(self, carte: Carte):
        self.carte = carte

    def affiche(self):
        for i in range(0, self.carte.dimension.positionNS):
            for j in range(0, self.carte.dimension.positionOE):
                self.afficheElement(Position(i + 1, j + 1))
            print()


    def afficheElement(self, position: Position):
        for fleur in self.carte.fleurs:
            if (position.positionNS == fleur.position.positionNS and
                    position.positionOE == fleur.position.positionOE):
                print(fleur.forme, end='')
                return
        print(".", end='')
