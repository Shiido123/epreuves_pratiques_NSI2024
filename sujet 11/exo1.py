def nombre_de_mots(phrase: str):
    phrase = phrase.split()
    if (phrase[-1] == "?" or phrase[-1] == "!"):
        phrase.pop()
    return len(phrase)

print(nombre_de_mots('Cet exercice est simple.'))
print(nombre_de_mots('Le point d exclamation est séparé !'))
print(nombre_de_mots('Combien de mots y a t il dans cette phrase ?'))
print(nombre_de_mots('Fin.'))