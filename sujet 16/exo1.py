def  ecriture_binaire_entier_positif(n):
    if n == 0:
        return '0 '
    bin_a = ""
    while n > 0:
        bin_a = str(n % 2) + bin_a
        n = n // 2
    return bin_a

print(ecriture_binaire_entier_positif(0))
print(ecriture_binaire_entier_positif(2))
print(ecriture_binaire_entier_positif(105))