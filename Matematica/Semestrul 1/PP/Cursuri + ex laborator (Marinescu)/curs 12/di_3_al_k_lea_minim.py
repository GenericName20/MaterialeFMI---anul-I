"""
Statistici de ordine
- al k-lea minim dintr-un vector
- al n/2-le minim - mediana (mediana inferioare/mediana superioara)

Pb 1 - al k-lea minim (al k-lea cel mai mic element), k dat - dintr-un vector dat
Pb 2 - Se dau o multime de numere naturale si un numar k.
Sa se detemine o submultime cu k elemente de suma maxima

"""
"""
Pb1-al k-lea minim 
#var 1: - sortam vectorul si luam elementul de pe pozitia k-1
#var 2: - folsoim pivotarea - pozitionam pivotul pe pozitia corecta m
avem 3 cazuri:
m==k-1 -> pivotul v[m] este al k-lea minim
m<k-1 -> continuam cautarea celui de al k-lea minim in dreapta 
altfel - cautam in stanga
"""
import di_quicksort_2
def al_k_minim(v,k,p,u):
    m=di_quicksort_2.pivotare(v,p,u)
    if m==k-1:
        return v[m]
    if m<k-1:
        return al_k_minim(v,k,m+1,u)
    return al_k_minim(v, k, p, m-1)
k=3
v=[30,1,10,4,7,2,9]
x=al_k_minim(v,k,0,len(v)-1)
print(x)
