from model import Position


class Fleur:

    def __init__(self, forme: str, quantitePollen: int, position: Position):
        assert quantitePollen >= 0, "la quantité de pollen doit être positive"
        self.quantitePollen = quantitePollen
        assert len(forme) == 1, "la forme doit être composée d'un seul caractère"
        self.forme = forme
        self.position = position

    def cedePollen(self, quantitePollenCedee: int):
        assert quantitePollenCedee >= 0, "la quantité de pollen doit être positive"
        assert quantitePollenCedee <= self.quantitePollen, "la quantité de pollen doit inférieur à la quantité disponible"
        self.quantitePollen -= quantitePollenCedee