# On décrit les caractéristiques communes de tous les objets d'une famille d'objets à l'aide d'une classe
class Calculateur:

    # Initialisation de l'objet référencé par "self" avec l'attribut "liste" qui est encapsulé dans l'objet
    def __init__(self, liste):
        self.liste = liste

    # L'objet calcule la somme à partir de sa liste
    def somme(self):
        # initialise la variable "somme" qui contiendra le résultat
        somme = 0
        # boucle sur la liste
        for nb in self.liste:
            somme = somme + float(nb)
        return somme


# Récupère la liste de nombres via le prompt
uneListe = input("Entrez la liste de nombre : \n").split()

# Créer une instance de Calculateur, en l'initialisant avec la liste qui vient du prompt
unCalculateur = Calculateur(uneListe)
# On demande au sommeur de faire le calcul
somme = unCalculateur.somme()

# On affiche
print(somme)