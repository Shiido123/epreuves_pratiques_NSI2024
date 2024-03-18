def ou_exclusif(tab1, tab2):
    new_tab = []
    for binary in zip(tab1, tab2):
        if binary[0] == 0 and binary[1] == 0:
            new_tab.append(0)
        elif binary[0] == 0 and binary[1] == 1:
            new_tab.append(1)
        elif binary[0] == 1 and binary[1] == 0:
            new_tab.append(1)
        else:
            new_tab.append(0)
    return new_tab

print(ou_exclusif([1, 0, 1, 0, 1, 1, 0, 1], [0, 1, 1, 1, 0, 1, 0, 0]))
print(ou_exclusif([1, 1, 0, 1], [0, 0, 1, 1]))