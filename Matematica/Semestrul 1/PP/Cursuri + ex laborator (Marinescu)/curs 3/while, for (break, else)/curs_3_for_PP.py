#instructiunea for
#for element in secventa (un sir, o lista)

s="un cuvant"
for litera in s: #parcurge s litera cu litera
    print(litera, end=" ")
print()
for i in [0,1,2,3,4,5]: #pozitia literei in sir - se numeroteaza de la 0
    print(s[i], end=" ") #accesare litera de pe pozitia i

#range - functie care genereaza secventve(liste) de numere
#range(n) => secventa 0,1,...,n-1
#range(a,b) => seventa a, a+1, ..., b-1
#range(a,b,pas), pas poate fi si negativ a, a+pas,...

#citim n si n numere, afisam suma
n=int(input("n="))
s=0
for i in range(n):
    x=int(input())
    s=s+x
print(s)
#afisam piramida (pt n dat)
"""
n n-1 ... 1
n n-1 ...2
...
n
"""
n=int(input())
for lin in range(1,n+1): #la ce linie suntem
    for i in range(n,lin-1,-1):
        print(i, end=" ")
    print()

#cifrele de la 9...0
for i in range(9,-1,-1):
    print(i, end=" ")
print()
print(range(2,7)) #generator, nu genereaza un element decat cand este nevoie
print(list(range(2,7)))