def nbr_occurrences(chaine):
    dico = {}
    for lettre in chaine:
        if lettre in dico:
            dico[lettre] += 1
        else:
            dico[lettre] = 1
    return dico


print(nbr_occurrences("Hello world !"))
