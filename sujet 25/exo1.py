def recherche_min(tab: list):
    mini = min(tab)
    return tab.index(mini)


print(recherche_min([5]))
print(recherche_min([2, 4, 1]))
print(recherche_min([5, 3, 2, 2, 4]))
print(recherche_min([-1, -2, -3, -3]))
