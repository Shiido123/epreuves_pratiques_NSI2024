def compte_occurrences(x, tab):
    somme = 0
    for valeur in tab:
        if valeur == x:
            somme += 1
    return somme


print(compte_occurrences(5, []))
print(compte_occurrences(5, [-2, 3, 1, 5, 3, 7, 4]))
print(compte_occurrences('a', ['a', 'b', 'c', 'a', 'd', 'e', 'a']))
