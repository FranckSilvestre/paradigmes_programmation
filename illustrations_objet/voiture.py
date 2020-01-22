# Classe voiture
class Voiture:

    def __init__(self):
        self.couleur = "bleue"
        self.masse = 630
        self.estDemarre = False

    def demarre(self):
        self.estDemarre = True

# Classe personne
class Personne:

    def __init__(self, voiture1, voiture2):
        self.voiturePrincipale = voiture1
        self.voitureSecondaire = voiture2

# Création de deux instances de voiture
k2000 = Voiture()
flashMacQueen = Voiture()

# Création d'une personne avec 2 voitures
arnold = Personne(k2000, flashMacQueen)

# arnold démarre sa voiture principale
arnold.voiturePrincipale.demarre()

# Vérifie que k2000 est bien démarré
assert k2000.estDemarre == True
