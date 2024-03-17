def recherche_motif(motif, texte):
    positions = []
    longueur_motif = len(motif)

    for i in range(len(texte) - longueur_motif + 1):
        if texte[i:i+longueur_motif] == motif:
            positions.append(i)

    return positions


print(recherche_motif("ab", ""))
print(recherche_motif("ab", "cdcdcdcd"))
print(recherche_motif("ab", "abracadabra"))
print(recherche_motif("ab", "abracadabraab"))
