# Récupère la liste de nombres via le prompt
liste = input("Entrez la liste de nombre : \n").split()

# initialise la variable "somme" qui contiendra le résultat
somme = 0

# boucle sur la liste
for nb in liste:
    somme = somme + float(nb)

# affiche la somme
print(somme)
