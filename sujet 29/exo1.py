def moyenne(notes):
    somme = 0
    longueur = 0
    for valeur in notes:
        somme+=valeur[0]*valeur[1]
        longueur+=valeur[1]
    return somme/longueur

print(moyenne([(15.0,2),(9.0,1),(12.0,3)]))


