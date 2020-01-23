from model.Abeille import Abeille
from model.Carte import Carte
from model.Fleur import Fleur
from model.Position import Position
from util.Journal import Journal
from vue.VueCarte import VueCarte
from vue.VueJournal import VueJournal

# initialise le model
uneCarte = Carte(Position(15, 50))
uneFleurDeColsa = Fleur("@", 500, Position(10, 8))
uneFleurDAccacia = Fleur("*", 300, Position(5, 39))
uneCarte.ajouteFleur(uneFleurDeColsa)
uneCarte.ajouteFleur(uneFleurDAccacia)
# Ajout P2.Ex2
maya = Abeille("maya", 50, 20, Position(5, 39))
copainMaya = Abeille("willy", 50, 20, Position(5, 39))
uneCarte.ajouteAbeille(maya)
uneCarte.ajouteAbeille(copainMaya)


# demande à la fleur d'accacia de liberer du pollen
# uneFleurDAccacia.liberePollen(150)

# Ajout P2.Ex2
maya.butine(uneFleurDAccacia)

# effectue le rendu du modèle
VueCarte(uneCarte).affiche()
VueJournal(Journal.journalParDefaut).affiche()
