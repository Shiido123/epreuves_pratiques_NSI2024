def insertion_abr(a, cle):
    if a is None:
        return (None, cle, None)
    if cle == a[1]:
        return a
    if cle < a[1]:
        nouveau_gauche = insertion_abr(a[0], cle)
        return (nouveau_gauche, a[1], a[2])
    else:
        nouveau_droit = insertion_abr(a[2], cle)
        return (a[0], a[1], nouveau_droit)


n0 = (None, 0, None)
n3 = (None, 3, None)
n2 = (None, 2, n3)
abr1 = (n0, 1, n2)

print(insertion_abr(abr1, 4))