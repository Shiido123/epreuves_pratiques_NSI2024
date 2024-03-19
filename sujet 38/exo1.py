def indices_maxi(tab: list):
    indices = []
    maxi = tab[0]
    for valeur in tab:
        if valeur > maxi:
            maxi = valeur

    for indice in range(len(tab)):
        if tab[indice] == maxi:
            indices.append(indice)

    return (maxi, indices)


print(indices_maxi([1, 5, 6, 9, 1, 2, 3, 7, 9, 8]))
print(indices_maxi([7]))
