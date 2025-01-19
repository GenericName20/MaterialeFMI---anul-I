# -*- coding: utf-8 -*-
"""
Multimi - clasa set
colectii cu elemente distincte
"""
s={1,3,1}
print(s,type(s)) #{1,3}
s={"abc","xy"}
print(s)

#s={[1,2],[3,4]} #TypeError: unhashable type: 'list'
s={(1,2),(3,4,10)}
print(s)
#TEMA - data o propozitie, sa se determine
#de cate ori apare fiecare cuvant + ce complexitate?
#%%%
#Curs 8
s="abcd"
print(hash(s))
t=(2,4)
print(hash(t))
#l=[3,1,5]
#print(hash(l)) # unhashable type: 'list'
s={"abc",(2,3)} #neomogena
print(s)
#s={[1,2],[3,4]} #unhashable type: 'list'

#%%
#multimea vida
s=set() #s={} - dictionarul vid
#exp - 
#a)Se da un cuvant. Sa se afiseze multimea literelor sale 
#b) se da un vector. sa se afiseze elementele distincte din vector ordonate crescator
s="cuvantul"
s="acesta"
mult_litere=set(s)
print(mult_litere)
l=[3,1,5,10.5,10.5,5,3]
x=set(l)
x=sorted(x)
for nr in x:
    print(nr, end=" ")
print()
#print(*sorted(x))

#%%
#multimile se pot crea, ca si listele, 
#cu secvente de initializare(comprehensiune)

#exemplu - se da un vector(o lista)
#sa se afiseze multimea elementelor pozitive din vector
s=input()
ls=s.split()
v=[int(x) for x in ls] #in input().split()
s={x for x in v if x>0}
print(s)

#o multime se poate parcurge cu for, ca si lista, str
for nr in s:
    print(nr, end=" ")
print()

#%%%

#nu se poate accesa un element prin indice
#multimile nu sunt secvente (nu sunt indexate 0,1,2...)
#ordinea elementelor din multime nu conteaza

#print(s[0]) - eroare

s={3,1,5}
s2={5,1,3}
print(s==s2) #sunt egale
s=[3,1,5]
s2=[5,1,3]
print(s==s2) #nu sunt egale

#%%
#operatorii in si not in
s={3,1,5}
x=3
if x in s:
    print(f"elementul {x} este in multimea {s}")
else:
    print(f"elementul {x} nu este in multimea {s}")

#%%
#OPERATORI pentru operatii cu multimi
#operatorii relationali testeaza incluziunea
s={2,6}
s2={2,4,6}
print(s<=s2)
#operatori - pentru operatiile cu multimi
#reuniune |
#intersectie &
#diferenta -
#diferenta simetrica ^
#se pot inlantui s1&s2&s3
#returneaza o noua multime

#exemplu - se citesc 3 vectori de numere naturale
#sa se afiseze elementele comune 
v1=[4,1,5,6,6,7,8] #v=[int(x) for x in input().split()]
v2=[4,10,1,7,7]
v3=[7,4,8,10,8]
r=set(v1)&set(v2)&set(v3)
print(r)
#se puteau citi direct ca multimi
#v={int(x) for x in input().split()}

#operatiile cu multimi se pot face si cu ajutorul
#metodelor din clasa set
#intersection, union, difference
#pimesc ca paramatrii un numar variabil de colectii 
#care se pot itera
v1=[4,1,5,6,6,7,8] #v=[int(x) for x in input().split()]
v2=[4,10,1,7,7]
v3=[7,4,8,10,8]
s=set(v1)
rez=s.intersection(v2,v3) #putem trimite ca parametri liste
#!!operatorii se pot folosi doar pentru multimi
print(rez)
print(s) #nu se modifica
#%%
#exista si metode care modifica o multime
s={4,1,3}
#adaugam un element
s.add(12)
print(s)
#stergem un element - remove, discard
#remove -eroare daca elementul nu este in multime
#s.remove(13)KeyError: 13
s.discard(13)

#exc - sa se elimine din multime cel mai mic element
s={4,6,10,2}
s.remove(min(s))
print(s)
#len, min,max,sorted - ca la liste

#operatii cu multimi care modifica multimea
#update,intersection_update, difference_update

#exc - se dau doua propozitii cu cuvintele separate cu spatii
#sa se afiseze multimea cuvintelor comune
p1="aceasta este o propozitie este" #p1=input()
p2="si aceasta este o alta fraza este" #p2=input()
s1=set(p1.split())
s1.intersection_update(p2.split()) #se actualizeaza s1
print(s1)

#Multimi care nu se pot modifica - frozenset
s=frozenset("abdab")
print(s)








