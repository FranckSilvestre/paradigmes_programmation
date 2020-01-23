from unittest import TestCase

from model.Fleur import Fleur
from model.Position import Position


class TestFleur(TestCase):

    def testCreationFleurCasSucces(self):
        # quand on cree une fleur avec les paramètres valides
        uneFleur = Fleur("@", 500, Position(5,12))
        # alors on dispose de l'objet et de ces propriétés
        self.assertEqual(uneFleur.forme, "@")
        self.assertEqual(uneFleur.quantitePollen, 500)
        self.assertEqual(uneFleur.position.positionNS, 5)
        self.assertEqual(uneFleur.position.positionOE, 12)
        print(uneFleur)


    def testCreationFleurCasErreurs(self):
        # quand on cree une fleur avec une paramètre invalide
        # alors une exception est levée
        self.assertRaises(AssertionError, Fleur, "@@", 500, Position(5,12))
        self.assertRaises(AssertionError, Fleur, "@", -500, Position(5,12))

    def testLiberePollenCasSucces(self):
        # Etant donné une fleur
        uneFleur = Fleur("@", 500, Position(5, 12))
        # Quand elle cede 300 de pollen
        uneFleur.liberePollen(300)
        # Alors, il lui reste plus que 200 de pollen
        self.assertEqual(uneFleur.quantitePollen, 200)
        # Quand elle cede tout ce ui lui reste
        uneFleur.liberePollen(uneFleur.quantitePollen)
        # Alors, il ne lui reste plus de pollen
        self.assertEqual(uneFleur.quantitePollen, 0)

    def testLiberePollenCasErreur(self):
        # Etant donné une fleur
        uneFleur = Fleur("@", 500, Position(5, 12))
        # Si  elle essaye de cede plus de pollen qu'elle n'en n'a
        # Alors, une exception est levée
        self.assertRaises(AssertionError, uneFleur.liberePollen, 600)






