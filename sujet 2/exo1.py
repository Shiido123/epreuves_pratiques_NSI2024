def correspond(mot, mot_a_trous):
    if len(mot) != len(mot_a_trous):
        return False
    for lettre_mot, lettre_mot_a_trous in zip(mot, mot_a_trous):
        if lettre_mot != lettre_mot_a_trous and lettre_mot_a_trous != '*':
            return False
    return True


print(correspond('INFORMATIQUE', 'INFO*MA*IQUE'))
print(correspond('AUTOMATIQUE', 'INFO*MA*IQUE'))
print(correspond('STOP', 'S*'))
print(correspond('AUTO', '*UT*'))

# utilisation de zip() qui prend des iterbales en arguments et qui renvoie un itérateur de tuples ce qui est efficace pour combiner les données de deux itérables en parallèle. https://www.programiz.com/python-programming/methods/built-in/zip#google_vignette
