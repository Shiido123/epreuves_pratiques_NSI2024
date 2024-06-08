def ajoute_dictionnaires(d1, d2):
    nv_dico = {}

    for cle, valeur in d1.items():
        nv_dico[cle] = valeur

    for cle, valeur in d2.items():
        if cle in nv_dico:
            nv_dico[cle] += valeur
        else:
            nv_dico[cle] = valeur

    return nv_dico


print(ajoute_dictionnaires({1: 5, 2: 7}, {2: 9, 3: 11}))
