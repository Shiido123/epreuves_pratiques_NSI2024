def verifie(tab: list):
    return tab == sorted(tab)


print(verifie([0, 5, 8, 8, 9]))
print(verifie([8, 12, 4]))
print(verifie([-1, 4]))
print(verifie([]))
print(verifie([5]))
