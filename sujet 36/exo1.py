def occurrences(caractere, chaine):
    somme = 0
    for lettre in chaine:
        if lettre == caractere:
            somme+=1
       
    return somme


print(occurrences('e', "sciences"))
print(occurrences('i',"mississippi"))
print(occurrences('a',"mississippi"))
