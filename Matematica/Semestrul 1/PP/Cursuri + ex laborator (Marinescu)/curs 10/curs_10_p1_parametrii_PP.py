"""
FUNCTII
Tipuri de parametrii
1. Parametrii obligatorii - trebuie sa primeasca obligatoriu valoare la apel
pot primi valoarea prin pozitie sau prin nume (sau combinat) - v. cursul trecut
---
2. Parametrii cu valoare default (implicita):
- au valoare data in antetul functiei  (numita valoare implicita sau default)
-daca nu primesc valoare la apel (nu le corespunde un parametru actual)
se foloseste valoarea implicita
-se pun in antet dupa param. oblig
"""
def f(x,y,z=1):
    print(x,y,z)
f(7,8,9) #prin pozitie
f(7,8)
"""
exp: Functie care primeste ca parametru o lista si 
in plus,   2 param lim_inf cu val implicita 0 si lim_sup cu val implicita 100
Functie  face suma numerelor din lista primita ca parametru cuprinse in intervalul 
[lim_inf,lim_sup] si o returneaza
"""
def suma(lista_numere,lim_inf=0,lim_sup=100):
    s=0
    for x in lista_numere:
        if lim_inf<=x<=lim_sup:
            s+=x
    return s
ls=[4,1,104,5,10,11]
print(suma(ls)) #in [0,100]
print(suma(ls,5))  #in [5,100]
print(suma(ls,lim_sup=10)) #in [0,10]

#suma(1,4,1,104,11,10)

"""
3. Functii cu numar variabil de parametrii
un parametru formal (din antet) prefixat cu * aduna in el oricat de multe valori (param actuali) trimise la apel sub forma de tuplu
"""
#exp: cate valori primite sun mai mari decat x
"""
def f(x,*numere):
    
f(10,3,1,5,7,8) =>0 
f(6,3,1,5,7,8) =>2 
"""

def f(x,*numere):
    print(x)
    print(numere, type(numere))
    nr=0
    for y in numere:
        if x<y:
            nr+=1
    return nr


n=f(10,3,1,5,7,8)
print(n)
n=f(6,3,1,5,7,8)
print(n)

#Dupa param cu * pot urma insa si alti param -> acestia trebuie dati la apel prin nume

def f(*numere,x):
    print(x)
    print(numere, type(numere))
    nr=0
    for y in numere:
        if x<y:
            nr+=1
    return nr





#n=f(3,1,5,7,8,10) #missing 1 required keyword-only argument: 'x' (!!x tb dat prin nume)
n=f(3,1,5,7,8,x=10)
print(n)
n=f(3,1,5,7,8,x=6)
print(n)


