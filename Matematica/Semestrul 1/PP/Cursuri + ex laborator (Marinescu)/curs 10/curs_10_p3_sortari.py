"""
SORTARI
v=[4,100,23,11]
v_nou=sorted(v) #returneaza o lista noua
v.sort() #modifica v, returneaza None - nu apel v=v.sort(), pt ca v devine None

EXEMPLU
Sa se sorteze un vector v crescator dupa suma cifrelor elementelor sale

v=[4,100,23,11] => [100,11,4, 23]
"""
def suma_cifre(n):
    s=0
    while n>0:
        s+=n%10
        n//=10
    return s
v=[4,100,23,11]
n=len(v)
for i in range(n-1):
    for j in range(i+1,n):
        if suma_cifre(v[i])>suma_cifre(v[j]):#if v[i]>v[j]:
            v[i],v[j]=v[j],v[i]
print(v)
v=[4,100,23,11]
v.sort(key=suma_cifre)
#key= functie cu un parametru care da cheia pentru sortare
#(la sortare se va compara key(v[i]) cu key(v[j]))
print(v)

#exemplu - sa se ordoneze cuvintele dintr-o propozitie dupa lungime
prop="acesta este un exemplu"
ls=prop.split()
ls.sort(key=len)
prop=" ".join(ls)
print(prop)

#Criterii multiple la sortare

ls=[("Ion",12),("Marius",15),("Ana",14),("Alex",12)] #(nume,varsta)
r=sorted(ls)
print(r)

#Sa se sorteze lista crescator dupa varsta si in caz de egalitate, dupa nume
def cheie(x): #x=(nume,varsta)
    """
    returnam un tuplu
    fiecare pozitie din tuplu -corespunde unui criteriu
    (!!!tuplurile se compara element cu element)
    """
    return (x[1],x[0])
print(ls)
r=sorted(ls,key=cheie)
print(r)

#daca am vrea sa sortam descrescator dupa varsta si crescator dupa lungimea numelui (in caz de egalitate)
def cheie(x):
    return (-x[1], len(x[0])) #!!cu minus
r=sorted(ls,key=cheie)
print(r)

#algoritmul de sortare - stabil
#(in caz de egalitate intre elemente, se pastreaza ordinea din sirul initial)

ls=["doi","o","a","u","unu"]
print(sorted(ls,key=len)) #['o', 'a', 'u', 'doi', 'unu']
# -cuv de aceeasi lung pastreza ordinea din sirul initial

#alt exp
ls=[("Ion",[10,9,10]),("Marius",[4,10]),("Ana",[9,8]),("Alex",[7,10,10])]
#sortam descrescator dupa medie, egalitate -dupa nume
def cheie(x):
    note=x[1]
    medie=sum(note)/len(note)
    return (-medie,x[0])
ls.sort(key=cheie)
print(ls)
"""
!!amintim- metodele de sortare au si param reverse cu val implicita False
Daca reverse este True se sorteaza descrescator
"""
v=[4,100,23,11]
v.sort(key=suma_cifre,reverse=True)

"""
Deoarece sortare este stabila, daca avem de sortat dupa mai multe criterii
putem folosi cate un sort pentru fiecare criteriu in parte, de la utlimul catre primul
"""