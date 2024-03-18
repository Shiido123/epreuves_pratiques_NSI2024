def parcours_largeur(arbre):
    if arbre is None:
        return []
    file = [arbre]
    resultat = []

    while file:
        noeud_courant = file.pop(0)
        g, x, d = noeud_courant

        resultat.append(x)

        if g is not None:
            file.append(g)
        if d is not None:
            file.append(d)

    return resultat


arbre = (((None, 1, None), 2, (None, 3, None)),
         4,
         ((None, 5, None), 6, (None, 7, None)))

print(parcours_largeur(arbre))
