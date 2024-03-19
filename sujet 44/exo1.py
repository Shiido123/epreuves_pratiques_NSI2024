def enumere(tab: list):
    dico = {}
    for indice, valeur in enumerate(tab):
        if valeur in dico:
            dico[valeur].append(indice)
        else:
            dico[valeur] = [indice]
    return dico


print(enumere([]))
print(enumere([1, 2, 3]))
print(enumere([1, 1, 2, 3, 2, 1]))
