def separe(tab):
    '''Separe les 0 et les 1 dans le tableau tab'''
    gauche = 0
    droite = len(tab) -1
    while gauche < droite:
        if tab[gauche] == 0:
            gauche = gauche + 1
        else:
            tab[gauche] = tab[droite]
            tab[droite] = tab[gauche]
            droite = droite - 1
    return tab

print(separe([1, 0, 1, 0, 1, 0, 1, 0]))
