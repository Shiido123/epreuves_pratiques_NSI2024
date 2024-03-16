def liste_puissances(a, n):
    liste = []
    nombre = a
    liste.append(nombre)
    for _ in range(1, n):
        nombre *= a
        liste.append(nombre)
    return liste


def liste_puissances_borne(a, borne):
    puissances_de_a = liste_puissances(a, borne)
    for puissance in range(len(puissances_de_a)):
        if puissances_de_a[puissance] >= borne:
            return puissances_de_a[0:puissance]


print(liste_puissances(3, 5))
print(liste_puissances(-2, 4))
print(liste_puissances_borne(2, 16))
print(liste_puissances_borne(2, 17))
print(liste_puissances_borne(5, 5))
