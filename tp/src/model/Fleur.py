from model import Position
from util.Journal import Journal


class Fleur:

    def __init__(self, forme: str, quantitePollen: int, position: Position):
        assert quantitePollen >= 0, "la quantité de pollen doit être positive"
        self.quantitePollen = quantitePollen
        assert len(forme) == 1, "la forme doit être composée d'un seul caractère"
        self.forme = forme
        self.position = position
        Journal.journalParDefaut.ecrit("nouvelle fleur: "+ str(self))

    def liberePollen(self, quantitePollenCedee: int):
        assert quantitePollenCedee >= 0, "la quantité de pollen doit être positive"
        assert quantitePollenCedee <= self.quantitePollen, "la quantité de pollen doit inférieur à la quantité disponible"
        self.quantitePollen -= quantitePollenCedee
        Journal.journalParDefaut.ecrit("pollen cede: " + str(quantitePollenCedee) + " par " + str(self))

    def __str__(self) -> str:
        return "Fleur(forme: "+ self.forme + ", quant. poll.: " + str(self.quantitePollen) + ", " + str(self.position) + ")"

