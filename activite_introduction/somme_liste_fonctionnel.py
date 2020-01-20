def somme_liste(liste):
    if not liste: return 0
    return float(liste[0]) + somme_liste(liste[1:])


print(somme_liste(input("Entrez la liste de nombre : \n").split()))

assert(somme_liste([0]) == 0)
assert(somme_liste([0, 3.5, 6]) == 9.5)