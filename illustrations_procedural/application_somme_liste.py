#
# Contenu fichier "application_somme_liste.py"
#

# Importation de la fonction
from illustrations_procedural.somme_liste import somme_liste

# Récupère la liste de nombres via le prompt
liste = input("Entrez la liste de nombre : \n").split()

# affiche la somme
print(somme_liste(liste))
