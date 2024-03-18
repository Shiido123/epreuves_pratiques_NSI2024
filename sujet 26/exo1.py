def ajoute_dictionnaires(d1, d2):
    nv_dico = {}
    for cle, valeur in d1.items():
        if cle in d2:
            nv_dico[cle] = d1[cle] + d2[cle]
        else:
            nv_dico[cle] = d1[cle]

    for cle, valeur in d2.items():
        if cle in d1:
            nv_dico[cle] = d2[cle] + d1[cle]
        else:
            nv_dico[cle] = d2[cle]
    return nv_dico


print(ajoute_dictionnaires({1: 5, 2: 7}, {2: 9, 3: 11}))
