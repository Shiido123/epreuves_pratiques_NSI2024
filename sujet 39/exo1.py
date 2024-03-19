def recherche(elt, tab):
    new_tab = []
    for indice in range(len(tab)):
        if tab[indice] == elt:
            new_tab.append(indice)

    if len(new_tab) > 0:
        return new_tab[-1]


print(recherche(1, [2, 3, 4]))
print(recherche(1, [1, 0, 42, 7]))
print(recherche(1, [1, 50, 1]))
print(recherche(1, [8, 1, 10, 1, 7, 1, 8]))
