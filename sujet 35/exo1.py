def annee_temperature_minimale(temperature_moyenne, annees):
    min = temperature_moyenne[0]
    min_indice = 0
    for indice, valeur in enumerate(temperature_moyenne):
        if valeur < min:
            min = valeur
            min_indice = indice
    return (min, annees[min_indice])


t_moy = [14.9, 13.3, 13.1, 12.5, 13.0, 13.6, 13.7]
annees = [2013, 2014, 2015, 2016, 2017, 2018, 2019]
print(annee_temperature_minimale(t_moy, annees))
