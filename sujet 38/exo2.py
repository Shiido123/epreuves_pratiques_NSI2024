def renverse(pile):
    '''renvoie une pile contenant les mêmes éléments que pile,
    mais dans l'ordre inverse.
    Cette fonction détruit pile.'''
    pile_inverse = []
    while pile != []:
        pile_inverse.append(pile.pop())
    return pile_inverse


def positifs(pile):
    '''renvoie une pile contenant les éléments positifs de pile,
    dans le même ordre. Cette fonction détruit pile.'''
    pile_positifs = []
    while pile != []:
        valeur = pile.pop()
        if valeur >= 0:
            pile_positifs.append(valeur)
    return renverse(pile_positifs)


print(renverse([1, 2, 3, 4, 5]))
print(positifs([-1, 0, 5, -3, 4, -6, 10, 9, -8]))
print(positifs([-2]))
