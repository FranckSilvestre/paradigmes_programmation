#
# Contenu fichier "test_somme_liste.py"
#

# Importation de la fonction
from illustrations_procedural.somme_liste import somme_liste

assert(somme_liste([]) == 0)
assert(somme_liste([0]) == 0)
assert(somme_liste([0, 3.5, 6]) == 9.5)
