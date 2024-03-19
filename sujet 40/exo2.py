def trouver_intrus(tab, g, d):
    """Renvoie la valeur de l'intrus situé entre les indices g et d 
    dans le tableau tab où :
    tab vérifie les conditions de l'exercice,
    g et d sont des multiples de 3."""
    if g == d:
        return tab
    else:
        nombre_de_triplets = (d - g) // 3
        indice = g + 3 * (nombre_de_triplets // 2)
        if ...:
            return ...
        else:
            return ...


print(trouver_intrus([3, 3, 3, 9, 9, 9, 1, 1, 1, 7,
                      2, 2, 2, 4, 4, 4, 8, 8, 8], 0, 18))
