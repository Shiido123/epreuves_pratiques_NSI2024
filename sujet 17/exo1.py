def nb_repetitions(elt, tab: list):
    return tab.count(elt)


print(nb_repetitions(5, [2, 5, 3, 5, 6, 9, 5]))
print(nb_repetitions('A', ['B', 'A', 'B', 'A', 'R']))
print(nb_repetitions(12, [1, '!', 7, 21, 36, 44]))
