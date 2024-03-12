def moyenne(tab: list):
    numerateur = 0
    denominateur = 0
    for tuple in tab:
        numerateur += tuple[0]*tuple[1]
        denominateur += tuple[1]
    if denominateur != 0:
        return numerateur/denominateur


print(moyenne([(8, 2), (12, 0), (13.5, 1), (5, 0.5)]))
print(moyenne([(3, 0), (5, 0)]))
