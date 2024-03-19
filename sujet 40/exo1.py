def selection_enclos(table, num_enclos):
    new_tab = []
    for dico in table:
        if dico["enclos"] == num_enclos:
            new_tab.append(dico)

    return new_tab


animaux = [{'nom': 'Medor', 'espece': 'chien', 'age': 5, 'enclos': 2},
           {'nom': 'Titine', 'espece': 'chat', 'age': 2, 'enclos': 5},
           {'nom': 'Tom', 'espece': 'chat', 'age': 7, 'enclos': 4},
           {'nom': 'Belle', 'espece': 'chien', 'age': 6, 'enclos': 3},
           {'nom': 'Mirza', 'espece': 'chat', 'age': 6, 'enclos': 5}]

print(selection_enclos(animaux, 5))
print(selection_enclos(animaux, 2))
print(selection_enclos(animaux, 7))