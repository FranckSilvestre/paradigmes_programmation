from unittest import TestCase

from model.Abeille import Abeille
from model.Fleur import Fleur
from model.Position import Position


class TestAbeille(TestCase):

    def testCreationAbeilleCasSucces(self):
        # quand on cree une abeille avec les paramètres valides
        uneAbeille = Abeille("maya", 50, 20, Position(5,12))

        # alors on dispose de l'objet et de ces propriétés
        self.assertEqual(uneAbeille.forme, "µ")
        self.assertEqual(uneAbeille.nom, "maya")
        self.assertEqual(uneAbeille.quantiteMaxPollenTransportable, 50)
        self.assertEqual(uneAbeille.quantitePollenTransportee, 20)

        self.assertEqual(uneAbeille.position.positionNS, 5)
        self.assertEqual(uneAbeille.position.positionOE, 12)


    def testAffichageAbeille(self):
        # étant donné une abeille
        uneAbeille = Abeille("maya", 50, 20, Position(5, 12))
        # l'état de l'abeille peut s'afficher de manière lisible par un humain
        self.assertEqual(str(uneAbeille), "Abeille(maya, quant. max.: 50, quant. transp.: 20, Position(NS: 5, OE: 12))")


    def testCreationAbeilleCasErreurs(self):
        # quand on cree une abeille avec une paramètre invalide
        # alors une exception est levée
        self.assertRaises(AssertionError, Abeille, "", 50, 20, Position(5,12))
        self.assertRaises(AssertionError, Abeille, "maya", -50, 20, Position(5, 12))
        self.assertRaises(AssertionError, Abeille, "maya", 50, -20, Position(5, 12))
        self.assertRaises(AssertionError, Abeille, "maya", 50, 51, Position(5, 12))

    def testAbeilleButineFleurCasSuccess(self):
        # étant donné une abeille
        maya = Abeille("maya", 50, 20, Position(5, 12))
        # Etant donné une fleur à la même position  que l'abeille
        # et avec plein de pollen
        soja = Fleur("@", 500, Position(5, 12))

        # Quand l'abeille butine la fleur
        maya.butine(soja)

        #  alors l'abeille fait le plein de pollen
        self.assertEqual(maya.quantitePollenTransportee, maya.quantiteMaxPollenTransportable)

        # car la fleur a liberé la quantité de pollen demandée
        self.assertEqual(soja.quantitePollen, 470)

    def testAbeilleButineFleurCasLimite(self):
        # étant donné une abeille
        maya = Abeille("maya", 50, 20, Position(5, 12))
        # Etant donné une fleur à la même position  que l'abeille
        # et avec une faible quantité de pollen
        soja = Fleur("@", 15, Position(5, 12))

        # Quand l'abeille butine la fleur
        maya.butine(soja)

        #  alors l'abeille pend le max de pollen
        self.assertEqual(maya.quantitePollenTransportee, 35)

        # car la fleur a liberé toute la quantité de pollen qu'elle pouvait
        self.assertEqual(soja.quantitePollen, 0)

    def testAbeilleButineFleurCasErreur(self):
        # étant donné une abeille
        maya = Abeille("maya", 50, 20, Position(5, 12))
        # Etant donné une fleur à une position différente  de l'abeille
        soja = Fleur("@", 15, Position(6, 12))

        # Alors la tentative de butinage de la fleur par l'abeille lève une erreur
        self.assertRaises(AssertionError, maya.butine, soja)

