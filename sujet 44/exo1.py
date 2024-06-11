def enumere(tab: list):
    dico = {}
    for indice in range(len(tab)):
        if tab[indice] in dico:
            dico[tab[indice]].append(indice)
        else:
            dico[tab[indice]] = [indice]
    return dico


print(enumere([]))
print(enumere([1, 2, 3]))
print(enumere([1, 1, 2, 3, 2, 1]))
