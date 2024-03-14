def echange(tab, i, j):
    '''Echange les éléments d'indice i et j dans le tableau tab.'''
    temp = tab[i] 
    tab[i] = tab[j]
    tab[j] = temp

def tri_bulles(tab):
    '''Trie le tableau tab dans l'ordre croissant
    par la méthode du tri à bulles.'''
    n = len(tab)
    for i in range(n): 
        for j in range(i+1): 
            if tab[j] > tab[i]: 
                echange(tab, j, i)

tab = []
tri_bulles(tab)
print(tab)

tab2 = [9, 3, 7, 2, 3, 1, 6]
tri_bulles(tab2)
print(tab2)

tab3 = [9, 7, 4, 3]
tri_bulles(tab3)
print(tab3)



