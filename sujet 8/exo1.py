def delta(liste):
    nouvelle_liste = []
    if len(liste) == 1:
        return [liste[0]]

    for indice in range(len(liste)-1):
        nouvelle_liste.append(liste[indice+1] - liste[indice])
    return nouvelle_liste


print(delta([1000, 800, 802, 1000, 1003]))
print(delta([42]))
