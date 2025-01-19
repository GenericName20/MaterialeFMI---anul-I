# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 14:48:30 2023

@author: Student
"""

#frecventa cuvintelor in propozitie
s="un cuvant un alt cuvant un nou alt cuvant"

#Pb 1
#frecventa cifrelor intr-un text
s="pauza se ia la si 14:50 si ora incepe la 15:00 "
#vector de frecvente - {0,1,2,3,4,5,6,7,8,9}
#se poate folosi daca numaram elemente cu valori mici
v=[0]*10
#v=[0 for i in range(10)]
for c in s:
    if "0"<=c<="9": #c.isdigit()
        v[int(c)]+=1 #ord(c)-ord('0')
for i in range(10):
    if v[i]!=0:
        print(f"{i} de {v[i]} ori")

#Pb2:#frecventa cuvintelor in propozitie
s="un cuvant un alt cuvant un nou alt cuvant"

#varianta 1: O(n^2) unde n este nr de cuvinte
ls_cuv=s.split()
for cuv in set(ls_cuv):
    print(f"{cuv} de {ls_cuv.count(cuv)} ori")

#varianta 2: sortam ls_cuv si 
#numaram de cate ori apare un cuv pe pozitii alaturate
ls_cuv.sort()
print(ls_cuv)
#tema #if ls_cuv[i]==ls_cuv[i-1] fr+=1

#varianta 3: generalizare a vectorului de frecv-> dictionar
#cuvant - frecventa
d={}
s="un cuvant un alt cuvant un nou alt cuvant"
ls_cuv=s.split()
for cuv in ls_cuv:
    if cuv in d:
        d[cuv]+=1 #indexat dupa cuvinte
    else:
        d[cuv]=1
print(d,type(d))
    
#DICTIONARE
#memoreaza perechi cheie:valoare
#indexate dupa cheie d[cheie] (tabel de dispersie)
#cheie - imutabila
#valoare- poate fi de orice tip
#optimizate pentru cautare dupa cheie O(1) mediu

#clasa dict
#creare
d={"unu":1,"doi":2} #cheie:valoare
d={} #dictionarul vid
#comprehensiune
#exp- crearea dict de frecv de la pb 2 var 1 cu comprehensiune
s="un cuvant un alt cuvant un nou alt cuvant"
d={cuv:ls_cuv.count(cuv) for cuv in set(s.split())} #!!O(n^2)
print(d)

d={x:0 for x in "aeiou"}
print(d)

#ls_cuv=s.split()
#for cuv in set(ls_cuv):
#    print(f"{cuv} de {ls_cuv.count(cuv)} ori")

#%%%
#Parcurgerea unui dictionar
d={5:"cinci",2:"doi",3:"trei"}
for cheie in d: #in lista cheilor
    print(f"cheia {cheie} are valoarea {d[cheie]}")
print(len(d)) #numarul de chei = len pt lista cheilor
print(min(d)) #min pt lista cheilor
print(sorted(d)) #sorted -sorteaza lista cheilor
#lista de valori
ls_valori=d.values()
print(ls_valori)
ls_valori=list(ls_valori)
print(ls_valori)

#lista de chei (de fapt dict_keys - view)
ls_chei=d.keys()
print(ls_chei)

#lista de perechi (cheie,valoare) 
ls_perechi=d.items()
print(ls_perechi)

#pentru tipul de date dict_keys returnat de 
#d.keys() se pot folosi operatorii pentru multimi

#Exemplu - se dau doua propozitii
#sa se afiseze cuvintele comune cu frecventa comuna 
#(min dintre frecventa din prima prop si frecv din a doua prop)
p1="un cuvant alt cuvant altceva"
p2=" un cuvant doua trei alt cuvant nou cuvant un"
#{"un":1,"cuvant":2,"alt":1}
def f(s):
    d={}
    ls_cuv=s.split()
    for cuv in ls_cuv:
        if cuv in d:
            d[cuv]+=1 #indexat dupa cuvinte
        else:
            d[cuv]=1
    return d
d1=f(p1)
d2=f(p2)
print(d1)
print(d2)
print(d1.keys()&d2.keys()) #multimea cheilor comune
for c in sorted(d1.keys()&d2.keys()):
    frecv_coumna=min(d1[c],d2[c])
    print(f"{c} de {frecv_coumna} ori")
d={c:min(d1[c],d2[c]) for c in sorted(d1.keys()&d2.keys())}
print(d)


#curs9-aduagat 
#sa se afiseze cuvinetele care apar in cel putin o propozitie cu frecventa toatala
#var gresita-da eroare pt cuv care apar doar intr-o propozitie
#d={c:d1[c]+d2[c] for c in sorted(d1.keys()|d2.keys())}

d={c:d1.get(c,0)+d2.get(c,0) for c in sorted(d1.keys()|d2.keys())}
print(d)
#%%%
d={"un":2,"alt":3,"cuvant":1}
#accesare valorii asociate unei chei 
#var 1: d[cheie]
#eroare daca nu exista cheia
cuv="un"
print(d[cuv])
cuv="unu"
#print(d[cuv])KeyError: 'unu'
if cuv in d:
    print(d[cuv])

#var2: d.get(cheie) - la fel ca d[cheie]
#in plus un parametru optional: d.get(cheie,valoare_implicita)
#care intoarce d[cheie], daca cheia este in dictionar
#si valoare_implicita daca cheia nu este in dictionar (!!nu da eroare)

#exp: care este frecv cuvantului cuv
x=d.get(cuv,0)
print(x)

#Actualizare
"""
d[cheie]=valoare
- daca cheie este deja in d- i se actualizeaza 
valoarea asociala
-daca cheie nu este in dictionar, 
se insereaza cu valoarea valoare
"""
d["un"]=14 #modific valaorea asociata lui un
print(d)
d["unu"]=12 #inserez "unu":12
print(d)

#Sterge - cu del d[cheie]
del d["unu"]
print(d)
#daca nu exista cheie- Eroare
#d.pop(cheie,val_implicita) - ca si get
#returneza valoarea asoc cheii sau val_implicita
#si sterge cheia daca exista (nu da eroare, returneaza val_implicita)
#daca cheia nu este in dictionar
        
        
        
