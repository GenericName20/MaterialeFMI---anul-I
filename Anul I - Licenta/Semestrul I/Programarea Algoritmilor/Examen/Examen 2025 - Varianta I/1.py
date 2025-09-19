# Subtask A
def cuvinte_consoane(*cuvinte):
    d = {}
    for cuvant in cuvinte:
        cuvant = cuvant.lower()
        key = "".join(sorted(set([litera for litera in cuvant if litera not in "aeiou"])))
        if key not in d:
            d[key] = [cuvant]
        else:
            d[key].append(cuvant)

    lmax = 0    
    for key in d:
        if len(d[key]) > lmax:
            lmax = len(d[key])
    
    return lmax

x = cuvinte_consoane("este", "stea", "are", "rea", "tAsta")
print(x)

# Subtask B
lista_numere = [800, 253, 168, 192]
prefix_5 = [value for value in lista_numere \
                    if "0" not in str(value)\
                   and "5" not in str(value)]

print(prefix_5)