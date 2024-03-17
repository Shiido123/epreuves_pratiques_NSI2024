def recherche_indices_classement(elt, tab):
    tab_valeurs_inferieurs_elt = []
    tab_valeurs_egales_elt = []
    tab_valeurs_superieures_elt = []
    for indice in range(len(tab)):
        if tab[indice] < elt:
            tab_valeurs_inferieurs_elt.append(indice)
        if tab[indice] == elt:
            tab_valeurs_egales_elt.append(indice)
        if tab[indice] > elt:
            tab_valeurs_superieures_elt.append(indice)
    return (tab_valeurs_inferieurs_elt, tab_valeurs_egales_elt, tab_valeurs_superieures_elt)


print(recherche_indices_classement(3, [1, 3, 4, 2, 4, 6, 3, 0]))
print(recherche_indices_classement(3, [1, 4, 2, 4, 6, 0]))
print(recherche_indices_classement(3, [1, 1, 1, 1]))
print(recherche_indices_classement(3, []))
