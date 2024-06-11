def max_dico(dico):
    maxi = ("Antoine le bot", 0)
    for cle in dico:
        if dico[cle] > maxi[1]:
            maxi = (cle, dico[cle])

    return maxi


print(max_dico({'Bob': 102, 'Ada': 201, 'Alice': 103, 'Tim': 50}))
print(max_dico({'Alan': 222, 'Ada': 201, 'Eve': 222, 'Tim': 50}))
