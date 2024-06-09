def gb_vers_entier(tab):
    entier = 0
    longueur = len(tab)

    for i in range(longueur):
        if tab[i]:
            entier += 2 ** (longueur - i - 1)

    return entier


print(gb_vers_entier([]))
print(gb_vers_entier([True]))
print(gb_vers_entier([True, False, True, False, False, True, True]))
print(gb_vers_entier([True, False, False, False, False, False, True, False]))
