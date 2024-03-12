def gb_vers_entier(tab):
    entier = 0
    for indice, valeur in enumerate(reversed(tab)):
        if valeur == True:
            entier += 2**indice

    return entier


print(gb_vers_entier([]))
print(gb_vers_entier([True]))
print(gb_vers_entier([True, False, True, False, False, True, True]))
print(gb_vers_entier([True, False, False, False, False, False, True, False]))
