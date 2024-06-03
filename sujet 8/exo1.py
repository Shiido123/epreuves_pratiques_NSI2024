def delta(liste):
    if not liste:
        return []

    delta_liste = [liste[0]]
    for i in range(1, len(liste)):
        delta_liste.append(liste[i] - liste[i - 1])

    return delta_liste

print(delta([1000, 800, 802, 1000, 1003]))
print(delta([42]))
