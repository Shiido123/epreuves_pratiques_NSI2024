def moyenne(tab: list):
    somme = 0
    if len(tab) == 0:
        return "Vous n'avez pas de moyenne"
    for valeur in tab:
        somme += valeur
    return somme/len(tab)


print(moyenne([5, 3, 8]))
print(moyenne([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(moyenne([]))
