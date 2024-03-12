def recherche(tab: list, n: int):
    lst_bon = []
    for indice, valeur in enumerate(tab):
        if valeur == n:
            lst_bon.append(indice)

    if len(lst_bon) > 0:
        return lst_bon[-1]


print(recherche([5, 3], 1))
print(recherche([2, 4], 2))
print(recherche([2, 3, 5, 2, 4], 2))
