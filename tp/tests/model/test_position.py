from unittest import TestCase

from model.Position import Position


class TestPosition(TestCase):

    def testCreationPositionCasSucces(self):
        # quand on cree une position avec des entiers positifs en parametre
        unePositionCorrecte = Position(10, 42)
        # Alors on dipsose du nouvel objet et on accede aux positions NS et OS
        self.assertEqual(unePositionCorrecte.positionNS, 10)
        self.assertEqual(unePositionCorrecte.positionOE, 42)

    def testCreationPositionCasErreurs(self):
        # quand on cree une position avec un des entiers négatif en parametre
        # Alors une excpetion est levée
        self.assertRaises(AssertionError, Position, -10, 42)
        self.assertRaises(AssertionError, Position, 10, -42)


