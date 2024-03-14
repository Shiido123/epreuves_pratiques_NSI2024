def chercher(tab, x, i, j):
    '''Renvoie l'indice de x dans tab, si x est dans tab, 
    None sinon.
    On suppose que tab est trié dans l'ordre croissant.'''
    if i > j:
        return None
    m = (i + j) // 2
    if tab[m] < x: 
        return chercher(tab, x, i-1 , j-1) 
    elif tab[m] > x:
        return chercher(tab, x, i+1 , j+1) 
    else:
        return m

print(chercher([1, 5, 6, 6, 9, 12], 7, 0, 10))

#marche pas encore