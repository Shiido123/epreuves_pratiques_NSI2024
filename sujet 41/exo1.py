class Noeud:
    def __init__(self, etiquette, gauche, droit):
        self.v = etiquette
        self.gauche = gauche
        self.droit = droit


a = Noeud(1, Noeud(4, None, None),
          Noeud(0, None,
                Noeud(7, None, None)))


def taille(a):
    if a is None:
        return 0
    return taille(a.gauche) + taille(a.droit) + 1


def hauteur(a):
    if a is None:
        return -1
    else:
        return max(hauteur(a.gauche), hauteur(a.droit)) + 1


print(taille(a))
print(taille(None))
print(taille(Noeud(1, None, None)))

print(hauteur(None))
print(hauteur(Noeud(1, None, None)))
print(hauteur(a))
