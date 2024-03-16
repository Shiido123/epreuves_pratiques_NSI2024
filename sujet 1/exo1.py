def taille(dico, lettre):
    if lettre == '' or lettre not in dico:
        return 0
    gauche, droit = dico[lettre]
    return taille(dico, gauche) + taille(dico, droit) + 1


a = {'F': ['B', 'G'], 'B': ['A', 'D'], 'A': ['', ''], 'D': ['C', 'E'],
     'C': ['', ''], 'E': ['', ''], 'G': ['', 'I'], 'I': ['', 'H'],
     'H': ['', '']}

print(taille(a, 'F'))
print(taille(a, 'B'))
print(taille(a, 'I'))
