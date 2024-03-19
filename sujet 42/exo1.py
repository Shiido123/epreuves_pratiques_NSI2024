def moyenne(tab: list):
    somme=0
    for chiffre in tab:
        somme+=chiffre
    return float(somme/len(tab))

print(moyenne([1]))
print(moyenne([1, 2, 3, 4, 5, 6, 7]))
print(moyenne([1, 2]))