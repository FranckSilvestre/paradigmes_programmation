# définit une fonction pour effectuer le calcul
def somme_liste(liste):
    # initialise la variable "somme" qui contiendra le résultat
    somme = 0
    # boucle sur la liste
    for nb in liste:
        somme = somme + float(nb)
    return somme

# Récupère la liste de nombres via le prompt
liste = input("Entrez la liste de nombre : \n").split()

# affiche la somme
print(somme_liste(liste))

assert(somme_liste([0]) == 0)
assert(somme_liste([0, 3.5, 6]) == 9.5)
