notes_eval = [2, 0, 5, 9, 6, 9, 10, 5, 7, 9, 9, 5, 0, 9, 6, 5, 4]


def effectif_notes(tab: list):
    liste = []
    for i in range(11):
        liste.append(tab.count(i))

    return liste


def notes_triees(effectif_notes: list):
    notes_triees = []
    for indice, valeur in enumerate(effectif_notes):
        for _ in range(valeur):
            notes_triees.append(indice)

    return notes_triees


print(effectif_notes(notes_eval))
print(notes_triees(effectif_notes(notes_eval)))
