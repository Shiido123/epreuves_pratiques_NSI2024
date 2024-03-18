def couples_consecutifs(tab:list):
    lst = []
    for indice in range(len(tab)):
        if tab[indice-1] + 1 == tab[indice]:
            lst.append((tab[indice-1], tab[indice]))

    return lst


print(couples_consecutifs([1, 4, 3, 5]))
print(couples_consecutifs([1, 4, 5, 3]))
print(couples_consecutifs([1, 1, 2, 4]))
print(couples_consecutifs([7, 1, 2, 5, 3, 4]))
print(couples_consecutifs([5, 1, 2, 3, 8, -5, -4, 7]))