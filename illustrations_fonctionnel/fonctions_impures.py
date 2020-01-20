#
# Contenu fichier "fonctions_impures.py"
#

# Multiplie par 2  les nombres de la liste
# version "impure"
def multiplie_par_2(liste):
    for i in range(0,len(liste)):
        liste[i] = 2 * liste[i]
    return liste

uneListe = [0,1,2,3]
assert multiplie_par_2(uneListe) == [0,2,4,6], "erreur appel 1"
assert multiplie_par_2(uneListe) == [0,2,4,6], "erreur appel 2"
