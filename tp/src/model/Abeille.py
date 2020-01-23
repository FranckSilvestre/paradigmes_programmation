from model.Fleur import Fleur
from model.Position import Position


class Abeille:

    def __init__(self,
                 nom: str,
                 quantiteMaxPollenTransportable: int,
                 quantitePollenTransportee:int,
                 position: Position):
        assert len(nom) > 0
        assert quantiteMaxPollenTransportable > 0
        assert quantitePollenTransportee > 0 and \
               quantitePollenTransportee <= quantiteMaxPollenTransportable
        self.forme = "µ"
        self.nom = nom
        self.quantiteMaxPollenTransportable = quantiteMaxPollenTransportable
        self.quantitePollenTransportee = quantitePollenTransportee
        self.position = position

    def __str__(self):
        return "Abeille(" + self.nom + ", quant. max.: " + str(self.quantiteMaxPollenTransportable) + \
               ", quant. transp.: " + str(self.quantitePollenTransportee) + ", " + str(self.position) + ")"

    def butine(self, fleur: Fleur):
        assert self.position.positionNS == fleur.position.positionNS and \
               self.position.positionOE == fleur.position.positionOE
        quantitePollenDemandee = self.quantiteMaxPollenTransportable - self.quantitePollenTransportee
        quantitePollenLiberable = fleur.quantitePollen
        quantiteObtenue = min(quantitePollenDemandee, quantitePollenLiberable)
        fleur.liberePollen(quantiteObtenue)
        self.quantitePollenTransportee = self.quantiteMaxPollenTransportable
