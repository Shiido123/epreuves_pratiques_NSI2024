def max_et_indice(tab: list):
    max = tab[0]
    indice_max = 0
    for indice, valeur in enumerate(tab):
        if valeur > max:
            max = valeur
            indice_max = indice
    return (max, indice_max)


print(max_et_indice([1, 5, 6, 9, 1, 2, 3, 7, 9, 8]))
print(max_et_indice([-2]))
print(max_et_indice([-1, -1, 3, 3, 3]))
print(max_et_indice([1, 1, 1, 1]))
