def recherche(tab, x):
    """
    tab : tableau d'entiers trié dans l'ordre croissant
    x : nombre entier
    La fonction renvoie True si tab contient x et False sinon
    """
    debut = 0
    fin = len(tab) - 1
    while debut <= fin:
        m = (debut + fin) // 2
        if x == tab[m]:
            return m
        if x > tab[m]:
            debut = m + 1
        else:
            fin = m - 1


print(recherche([2, 3, 4, 5, 6], 5))
print(recherche([2, 3, 4, 6, 7], 5))
