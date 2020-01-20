# Compte les éléments de la liste qui sastisfont
# la fonction de validation
def count(liste, functionValidation):
    res = 0;
    if (len(liste) == 0): return res;
    if (functionValidation(liste[0])):
        res += 1
    return res + count(liste[1:], functionValidation)


# compte les nombres pairs dans la liste
#
def estPair(nombre):
    return nombre % 2 == 0

assert count([0, 1, 3, 6, 9], estPair) == 2

# compte les nombres pairs avec une fonction anonyme
#
assert count([0, 1, 3, 6, 9],
             lambda x: x % 2 == 0) == 2

# compte les couples qui ont leur premier élément
# différent du second
#
assert count([('A','A'),('G','G'),('T','C')],
             lambda x:x[0] != x[1]) == 1