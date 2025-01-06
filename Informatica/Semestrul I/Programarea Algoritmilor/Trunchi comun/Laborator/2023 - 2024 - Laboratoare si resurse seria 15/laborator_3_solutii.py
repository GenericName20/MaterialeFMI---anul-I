# -*- coding: utf-8 -*-
"""laborator 3 solutii.ipynb
<b>VECTORI și MATRICE

<b> 1.	Rezolvați problemele rămase de la seminar- v. solutii seminar

<b>2.	Ciurul lui Eratostene. Se dă un număr natural n. Să se creeze o listă cu numerele prime mai mici sau egale cu n
"""

n=int(input())
e_prim=[True]*(n+1)
e_prim[0]=e_prim[1]=False
#ls=[]
for i in range(2,n+1):
    if e_prim[i]:
        #ls.append(i)
        for j in range(2*i,n+1,i):
            e_prim[j]=False
ls=[j for j in range(2,n+1) if e_prim[j]]
print(ls)

"""<b>3.	Se dă un vector v de n<100 numere naturale de cel mult două cifre. Să se determine numărul de perechi  disjuncte de elemente de egale (de forma (v[i], v[j]) cu i!=j și v[i]=v[j]) care se pot forma cu elementele vectorului. https://www.pbinfo.ro/probleme/2702/perechisosete"""

frec=[0 for i in range(102)]
ls=[int(x) for x in input().split()]
for x in ls[1:]:
    frec[x]=frec[x]+1
nr_perechi=0
for i in range(1,101):
    nr_perechi= nr_perechi +(frec[i]//2)
print(nr_perechi)

"""<b>4.	Se dau două mulțimi cu elementele ordonate crescător (elementele fiecărei mulțimi se vor da pe o linie separate prin spațiu). Să se determine eficient reuniunea și intersecția celor două mulțimi (fără a folosi set)."""

a=[1, 4, 6,7,10,12,18] #a=[int(x) for x in input().split()]
b=[4,7,10,15,18,22,27] #b=[int(x) for x in input().split()]
intersect=[]
reuniune=[]
i=0
j=0
while (i<len(a)) and (j<len(b)):
    if a[i]<b[j]:
        reuniune.append(a[i])
        i+=1
    elif a[i]==b[j]:
        reuniune.append(b[j])
        intersect.append(b[j])
        j+=1
        i+=1
    else:
        reuniune.append(b[j])
        j += 1
reuniune.extend(a[i:])
reuniune.extend(b[j:])
print(reuniune)
print(intersect)

"""<b>5.	Se citesc m, n și o matrice cu m linii și n coloane, elementele unei linii fiind date pe o linie separate cu spațiu. Se citește în plus un număr natural k. Să se permute fiecare  linie a matricei circular la dreapta cu k poziții (Echivalent: Să se permute coloanele matricei circular spre dreapta cu k poziții)"""

n,m=[int(x) for x in input("dimensiuni:").split()]

a=[[int(x) for x in input().split()] for i in range(n)]
print(a)
k=int(input())
for i in range(n):
    a[i].extend(a[i][:k])
    del a[i][:k]
print(a)

"""<b>6.	Se citesc m, n și o matrice cu m linii și n coloane, elementele unei linii fiind date pe o linie (elementele unei linii date pe o linie separate cu spațiu). Să se construiască în memorie și să se afișeze matricea transpusă (folosind și comprehensiune)."""

n,m=[int(x) for x in input("dimensiuni:").split()]

a=[[int(x) for x in input().split()] for i in range(n)]
print(a)

trans=[[a[i][j] for i in range(n)] for j in range(m)]
print(trans)

trans=[[linie[j] for linie in a] for j in range(m)]
print(trans)

"""<b>7.	Se citesc m, n și o matrice cu m linii și n coloane, elementele unei linii fiind date pe o linie (elementele unei linii date pe o linie separate cu spațiu). Să se determine numărul de valori pare din matrice (folosind și comprehensiune) https://www.pbinfo.ro/probleme/767/sumapare2"""

n,m=[int(x) for x in input().split()]
a=[[int(x) for x in input().split()] for i in range(n)]
print(sum([x for linie in a for x in linie if x%2==0]))

"""<b>8.	Se citesc m, n și o matrice cu m linii și n coloane, elementele unei linii fiind date pe o linie (elementele unei linii date pe o linie separate cu spațiu). Să se determine pentru fiecare linie, cea mai mică valoare care se poate obține adunând elementele de pe linie, cu excepția unuia. (folosind și comprehensiune). https://www.pbinfo.ro/probleme/659/sumalinii1"""

n,m=[int(x) for x in input().split()]
a=[[int(x) for x in input().split()] for i in range(n)]
ls=[sum(linie)-max(linie) for linie in a]
print(*ls)

"""<b>9.	Se dă un număr natural n>2. Să se afișeze primele n linii din triunghiul lui Pascal (daca c este numărul maxim de cifre ale unui număr din triunghi, toate numerele se vor afișa pe c+1 caractere)."""

n=int(input())
triunghi=[[0 for i in range(j+1)] for j in range(n)]

for i in range(n):
    triunghi[i][0]=triunghi[i][-1]=1 #primul si ultimul element sunt 1

for i in range(2,n):
    lung = len(triunghi[i])
    for j in range(1,lung-1):
        triunghi[i][j] = triunghi[i-1][j] +triunghi[i-1][j-1]

print(triunghi)
nr_max=triunghi[n-1][(n-1)//2] #valoarea maxima=mijlocul ultimei linii
nr_cifre=len(str(nr_max))+1

for linie in triunghi:
    for x in linie: print(f"{x:{nr_cifre}}",end="",sep="")
    print()

"""<b>10.	Se citește un număr natural N.
<b><p>a) Să se genereze și afișeze o matrice de dimensiune NxN, cu elementele de la 1 la N*N - în ordine crescătoare, de la stânga la dreapta și de sus în jos (folosind și comprehensiune).
<b><p>b) Pentru a parcurge elementele matricei în spirală, pornind din colțul din stânga-sus (spre dreapta, în jos, spre stânga, în sus, …), să se obțină întâi o listă având elemente de tip tuplu (linie, coloană) care să reprezinte pozițiile care trebuie parcurse în această spirală.
<b><p>c) Folosind lista de tupluri de mai sus, să se afișeze elementele din matrice aflate la acele poziții.
"""

N=5
a=[[i*N+j+1 for j in range(N)] for i in range(N)]
print(a)
#Varianta 2:
#y=0
#a=[ [y:=y+1 for j in range(N)] for i in range(N)]
#print(a)
for linie in a:
    for x in linie:
        print(f"{x:3}",end="")
    print()
afis="\n".join(["".join([f"{x:3}" for x in linie]) for linie in a])
print(afis)
ls=[]
for k in range((N+1)//2):
    ls.extend([(k,i) for i in range(k,N-k-1)])
    ls.extend([(i,N-k-1) for i in range(k,N-k)])
    ls.extend([(N-k-1,i) for i in range(N-k-2,k,-1)])
    ls.extend((i, k) for i in range(N - k - 1, k, -1))
print(ls)

for x,y in ls:
    print(a[x][y],end=" ")

