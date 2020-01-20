# On décrit les caractéristiques communes de tous les objets
# d'une famille à l'aide d'une classe
class Calculateur:

    # Initialisation de l'objet référencé par "self"
    # avec l'attribut "liste" qui est encapsulé dans l'objet
    def __init__(self, liste):
        self.liste = liste

    # L'objet calcule la somme à partir de sa liste
    def somme(self):
        if not self.liste: return 0
        return float(self.liste[0]) + Calculateur(self.liste[1:]).somme()


print(Calculateur(input("Entrez la liste de nombre : \n").split()).somme())