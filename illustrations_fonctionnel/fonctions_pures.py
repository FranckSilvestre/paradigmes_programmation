#
# Contenu fichier "fonctions_pures.py"
#

# Multiplie par 2  les nombres de la liste
# version "pure"
def multiplie_par_2(liste):
    newListe = []
    for i in range(0,len(liste)):
        newListe.append(2 * liste[i])
    return newListe

uneListe = [0,1,2,3]
assert multiplie_par_2(uneListe) == [0,2,4,6], "erreur appel 1"
assert multiplie_par_2(uneListe) == [0,2,4,6], "erreur appel 2"
