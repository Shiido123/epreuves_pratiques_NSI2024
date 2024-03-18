def fusion(tab1, tab2):
    nv_tab = []
    for valeur1, valeur2 in zip(tab1, tab2):
        if valeur1 <= valeur2:
            nv_tab.extend([valeur1, valeur2])
        else:
            nv_tab.extend([valeur2, valeur1])

    reste_tab = tab1[len(
        nv_tab)//2:] if len(tab1) > len(tab2) else tab2[len(nv_tab)//2:]
    nv_tab.extend(reste_tab)

    return nv_tab


print(fusion([3, 5], [2, 5])) 
print(fusion([-2, 4], [-3, 5, 10]))
print(fusion([4], [2, 6]))
print(fusion([], []))
print(fusion([1, 2, 3], []))
