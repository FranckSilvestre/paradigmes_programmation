#
# Contenu fichier "somme_liste.py"
#

# définit une fonction pour effectuer le calcul
def somme_liste(liste):
    # initialise la variable "somme" qui contiendra le résultat
    somme = 0
    # boucle sur la liste
    for nb in liste:
        somme = somme + float(nb)
    return somme

