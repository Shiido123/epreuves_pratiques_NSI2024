class Noeud:
    """Classe représentant un noeud d'un arbre binaire"""

    def __init__(self, etiquette, gauche, droit):
        """Crée un noeud de valeur etiquette avec
        gauche et droit comme fils."""
        self.etiquette = etiquette
        self.gauche = gauche
        self.droit = droit


def parcours(arbre, liste):
    """parcours récursivement l'arbre en ajoutant les étiquettes
    de ses noeuds à la liste passée en argument en ordre infixe."""
    if arbre != None:
        parcours(arbre.gauche, liste)
        liste.append(arbre.etiquette)
        parcours(arbre.droit, liste)
    return liste


def insere(arbre, cle):
    """insere la cle dans l'arbre binaire de recherche
    représenté par arbre.
    Retourne l'arbre modifié."""
    if arbre == None:
        return Noeud(cle, None, None)  # creation d'une feuille
    else:
        print(arbre)
        if cle < arbre.etiquette:
            arbre.gauche = insere(arbre.gauche, cle)
        else:
            arbre.droit = insere(arbre.droit, cle)
    return arbre


arbre = Noeud(5, Noeud(2, None, Noeud(3, None, None)), Noeud(7, None, None))

arbre = insere(arbre, 1)
arbre = insere(arbre, 4)
arbre = insere(arbre, 6)
arbre = insere(arbre, 8)

# Parcours de l'arbre pour vérifier l'insertion
print(parcours(arbre, []))
