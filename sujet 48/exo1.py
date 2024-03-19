def voisins_entrants(adj, x):
    entrants = []
    for i in range(len(adj)):
        if x in adj[i]:
            entrants.append(i)

    return entrants


print(voisins_entrants([[1, 2], [2], [0], [0]], 0))
print(voisins_entrants([[1, 2], [2], [0], [0]], 1))
