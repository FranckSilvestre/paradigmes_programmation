#
# Contenu fichier "immutabilite.py"
#

# Multiplie par 2  les nombres de la liste
def multiplie_par_2(liste):
    for i in range(0, len(liste)):
        liste[i] = 2 * liste[i]
    return liste


uneListe = (0, 1, 2, 3) # c'est un tuple : immuable en python
assert multiplie_par_2(uneListe) == (0, 2, 4, 6), "erreur appel 1"
assert multiplie_par_2(uneListe) == (0, 2, 4, 6), "erreur appel 2"
