def ou_exclusif(tab1, tab2):
    new_tab = []
    for i in range(len(tab1)):
        if tab1[i] == 0 and tab2[i] == 0:
            new_tab.append(0)
        elif tab1[i] == 0 and tab2[i] == 1:
            new_tab.append(1)
        elif tab1[i] == 1 and tab2[i] == 0:
            new_tab.append(1)
        else:
            new_tab.append(0)
    return new_tab


print(ou_exclusif([1, 0, 1, 0, 1, 1, 0, 1], [0, 1, 1, 1, 0, 1, 0, 0]))
print(ou_exclusif([1, 1, 0, 1], [0, 0, 1, 1]))
