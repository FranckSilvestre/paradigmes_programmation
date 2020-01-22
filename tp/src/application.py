from model.Carte import Carte
from model.Fleur import Fleur
from model.Position import Position
from vue.VueCarte import VueCarte

uneCarte = Carte(Position(15, 50))
uneCarte.ajouteFleur(Fleur("@", 500, Position(10, 8)))
uneCarte.ajouteFleur(Fleur("*", 300, Position(5, 39)))

uneVueCarte = VueCarte(uneCarte)
uneVueCarte.affiche()