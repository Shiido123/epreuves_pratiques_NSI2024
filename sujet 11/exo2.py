class Noeud:
    def __init__(self, etiquette):
        '''Méthode constructeur pour la classe Noeud.
        Crée une feuille d'étiquette donnée.'''
        self.etiquette = etiquette
        self.gauche = None
        self.droit = None

    def inserer(self, cle):
        '''Insère la clé dans l'arbre binaire de recherche
        en préservant sa structure.'''
        if cle < self.etiquette:
            if self.gauche != None:
                cle = self.gauche
            else:
                self.gauche = self.etiquette
        else:
            ...
                ...
            else:
                ... = Noeud(cle) 

arbre = Noeud(7)
for cle in (3, 9, 1, 6):
    arbre.inserer(cle)

print(arbre.gauche.etiquette)

