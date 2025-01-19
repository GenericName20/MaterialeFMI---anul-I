"""
FUNCTII
def nume(parametrii formali): - ANTET
    CORPUL FUNCTIEI - secventa de instructiuni
"""
"""
- evita sa scriem acelasi cod de mai multe ori (reutilizare cod)
- modularizarea programului  (impartire pe subrutine mai mici)
- refolosim cod in alte programe (import)
"""
#EXP
#se citesc doua numere, sa se afiseze cel care are suma cifrelor mai mare
def suma_cifre(n): #antet, n-parametru formal
    s=0
    while n>0:
        s+=n%10
        n=n//10
    return s #o functie poate returna una sau mai multe valori
"""
instructiunile de dupa return - nu se executa, return incheie executia functiei
valoarea returnata de functie inlocuieste apelul functiei in expresia/instructiunea
de unde functia a fost apelata
"""
n=int(input())
m=int(input())
if suma_cifre(n)>suma_cifre(m): #!!n si m nu se modifica
    print(n)
else:
    print(m)

#EXEMPLU:
"""
Se dau doua fisiere, in fiecare fisier avem o matrice
Se citeste un numar natural k
Sa se afiseze matricea care are cele mai multe elemente distincte cu cel putin k divizori
"""
"""
Functii
-functie care citeste matricea din fisier si o returneaza
-functie care numara divizorii unui numar
-functie care numara elementele cu proprietatea ceruta
-functie care afiseaza matricea
"""
def citire_matrice(nume_fisier):
    #cursul trecut-citire de la tastatura
    f=open(nume_fisier)
    m, n = [int(x) for x in f.readline().split()] #dimensiuni-pe prima linie
    a = []
    for linie_fisier in f:  # citesc linia  i
        linie_matrice = [int(x) for x in linie_fisier.split()]
        a.append(linie_matrice)


    f.close()
    return a,n,m #o functie poate returna mai multe valori -> ca tuplu

"""
t=citire_matrice("matr1.in")
print(type(t))
x,y=4,5
"""

def numar_divizori(n):
    nr=0
    for d in range(1,n+1):
        if n%d==0:
            nr+=1
    return nr
def numar_elemente_divizori(a,k): #cate elemente distincte din matrice a au minim k divizori
    s=set()

    for linie in a:
        for x in linie:
            if numar_divizori(x)>=k:
                s.add(x) #multimea elementelor cu cel putin cu k divizori
    print(s)
    return len(s)

a,ma,na=citire_matrice("matr1.in")
b,mb,nb=citire_matrice("matr2.in")
print(a)
print(b)
k=4
if numar_elemente_divizori(a,k)>numar_elemente_divizori(b,k):
    print(a) #tema-functie care afiseaza matricea-cursul trecut
else:
    print(b)

"""
TRANSMITEREA PARAMETRILOR
se face prin atriburie (paramaterul formal = parametru actual)
singurele modificari vizibile dupa apelul functiei sunt cele asupra valorii (!!!)
unui parametru mutabil
"""
def modifica(x): #transmitere prin atribuire-> in spatiul local al functiei
    #se creeaza x care primeste ca valoare expresia cu care functia a fost apelata

    x=5

x=9
modifica(x)
print(x)

def modifica_lista(l):
    l.append(12)
ls=[3,4,5]
modifica_lista(ls)
print(ls)

def creeaza_lista(l):
    l=[] #l refera acum o noua lista
    for i in range(1,4):
        l.append(i) #modificari asupra listei noi din local
    print(l)
ls=[]
creeaza_lista(ls)
print(ls)

def creeaza_lista_2(l):
    #l=[]- nu se mai creeaza un nou obiect in local
    for i in range(1,4):
        l.append(i)
    print(l)
ls=[]
creeaza_lista_2(ls)
print(ls)

#parametri obilgatorii - pot fi dati prin pozitie, dar si prin nume
def f(x,y,z): #3 parametrii obligatorii - tb sa primeasca valoare la apel
    print(locals())
    print(x,y,z)
    #daca nu avem return-> se returneaza implicit None

f(4,1,6) #x primeste valoarea 4, y valoarea 3, z valoarea 6
#oarametri se pot da si prin nume- si atunci nu mai conteaza ordinea
f(z=12,x=4,y=8)
#se pot combina -dar primii se dau cei prin pozitie
f(10,z=14,y=12)



