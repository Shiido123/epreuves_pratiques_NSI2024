import random


def lancer(n):
    tab = []
    for _ in range(n):
        tab.append(random.randint(1, 6))
    return tab


def paire_6(tab):
    if tab.count(6) >= 2:
        return True
    return False


lancer1 = lancer(5)
print(lancer1)
print(paire_6(lancer1))

lancer2 = lancer(5)
print(lancer2)
print(paire_6(lancer2))

lancer3 = lancer(3)
print(lancer3)
print(paire_6(lancer3))

lancer4 = lancer(0)
print(lancer4)
print(paire_6(lancer4))
