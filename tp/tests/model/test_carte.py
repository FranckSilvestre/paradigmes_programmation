from unittest import TestCase

from model.Carte import Carte
from model.Fleur import Fleur
from model.Position import Position


class TestCarte(TestCase):

    def testAjouteFleursCasSucces(self):
        # Etant donne une carte et des fleurs positionnables sur la carte
        uneCarte = Carte(Position(100, 100))
        uneFleurDeColza = Fleur("@", 500, Position(50, 62))
        uneFleurDAccacia = Fleur("*", 300, Position(12, 39))
        # Quand on ajoute les fleurs à la carte
        uneCarte.ajouteFleur(uneFleurDeColza)
        uneCarte.ajouteFleur(uneFleurDAccacia)
        # Alors la carte est référence bien les fleurs ajoutées dans sa liste
        self.assertEqual(uneCarte.fleurs[0], uneFleurDeColza)
        self.assertEqual(uneCarte.fleurs[1], uneFleurDAccacia)

    def testAjouteFleursCasEchec(self):
        # Etant donne une carte et une fleur non positionnable sur la carte
        uneCarte = Carte(Position(100, 100))
        uneFleurDeColzaPasSurLacarte = Fleur("@", 500, Position(150, 62))
        # Quand on ajoute la fleur  à la carte
        # Alors exception est levée
        self.assertRaises(AssertionError, uneCarte.ajouteFleur, uneFleurDeColzaPasSurLacarte)
