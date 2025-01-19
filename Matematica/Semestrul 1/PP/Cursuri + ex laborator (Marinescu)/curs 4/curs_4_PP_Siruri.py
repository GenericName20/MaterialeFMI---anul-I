# -*- coding: utf-8 -*-
"""
SIRURI DE CARACTERE
"""
#%%
#CREARE - CONSTANTE
s="abc" #cu ghilimele
s='abc' #- cu apostrof
#(nu are tipul char)
s="""un vers
doua versuri
""" 
#de 3 ori ghilimele sau apostrof
#daca sirul are mai multe linii
print(s,type(s))
#%%
#secvente escape
#codificarea UNICODE - caractere din mai multe limbi
#(exitnde codif ASCII - 127 caractere)
#fiecare caracter - asociat un cod
"""
functii:
    ord(caracter)=> codul caracterului 
    (caracter= sir de lungime 1)
    chr(cod) => caracterul
"""
#Exemplu - a cata litera din alfabet este c
c="b"
print(ord(c)-ord("a")+1)
#care este litera k din alfabet (litere mici)
k=13
print(chr(k+ord("a")-1))

"""
secvente escape - 
succesiuni de carcatere (prefixate de \) cu 
semnificatie speciala, alta decat daca ar fi 
fost scrise direct 
"""
s="un \n sir"
print(s)

#Exp - Titlul cursului "Programare procedurala"
#s="Titlul cursului "Programare procedurala"" - eroare
s="Titlul cursului \"Programare procedurala\""
print(s)
s='Titlul cursului "Programare procedurala"'
print(s)
#suplimentar
s="matematic\u0103" #dupa \u -codul in baza 16
print(s)
print(ord(s[-1])) #103 din baza 16 in baza 10=259
#pentru conversii de la alte tipuri -str
x,y=4,18
s="primul numar este "+str(x)+", al doilea  "+str(y)
print(s)
x="2"
y=int(x)+1

#%%
#exp - cate cifre are un numar dat
n=789
nr_cifre=len(str(n))
print(nr_cifre)
#%%
"""
OPERATORI 
- concatenare +
- inmultire cu un numar (Adunare repetata)
-comparare (relationali)
==, >, >=, <,<=
"""
s="a"*3
print(s)
x,y="unu","doi"
#comaparea - caracter cu caracter
#caractere - se compara dupa cod
if x>y:
    x,y=y,x
print(x,y)
#%%
#Parcurgere, Accesare elemente - cursul trecut
"""
la nivel de caracter: 
for c in sir: #c ia pe rand caracterele din s
la nivel de pozitie (stil c++)
for i in range(len(s)):
    print(s[i])

-indici negativi
-feliere (slice)
s[i:j] => s[i,i+1,..j-1]
s[i:j:k] => de la i la j cu pasul k
daca lipsesc i sau j - merg pana la capatul sirului 
(in sensul dat de semnul lui k) 
"""
#exc 1 - Cifrul lui Cezar cu k =1 pentru litere mici
#litera se inlocuieste cu litera urmatoare (circular)
#z se inlocuieste cu a
#test de litera mica "a"<=c<="z"
s="pauza"
rez=""
for c in s:
    if c=='z':
        rez=rez+"a" #are +=
    else:
        rez=rez+chr(ord(c)+1)
print(rez)
#%%
#test palindrom  
s="abcdba"
for i in range(len(s)//2):
    if s[i]!=s[-i-1]: #s[0]==s[-1], s[1]==s[-2]
        print("nu este palindrom")
        break
else:
    print("este palindrom")
#alta metoda: s==inversul lui
print(s==s[::-1])  
#%%  
"""
Se da un cuvant s; 
sa se determine  cel mai lung prefix al lui s 
care este si sufix al lui s (diferit de s)
"""
s="baaaab"
for i in range(len(s)-1,0,-1): 
    #i=lungimea prefixului
    print(s[:i])
    if s[:i]==s[-i:]:
        #testam daca primele i litere=ultimele i
        print(s[:i])
        break
#%%
"""
TEMA:DAt s, sa se determine cel mai lung 
prefix care este palindrom
s[:i]==s[i-1::-1] 
"""
#%%
#Divizari si unificari de siruri
#Divizari
"""
Dat un sir si un (!doar unul) separator, putem imparti 
sirul in cuvinte in functie de separatorul dat:
s="Ana are mere" => 3 cuvinte Ana, are si mere

split(separatorul, maxsplit=cate_impartiri_face)
daca nu dam separator-implicit 
separa dupa caractere albe

Rezultatul - o lista de cuvinte

"""

s="Ana are    mere"
l=s.split()
print(l)

s="mere;pere;prune"
l=s.split(";")
print(l)
for c in l:
    print(c)

s="mere, pere,prune"
l=s.split(", ") 
"""
separatorul cautat este exact ", "
nu si alte combinatii (doar , sau doar spatiu)
"""
for c in l:
    print(c)
s="mere pere prune"
l=s.split("re")
for c in l:
    print(c)

s="Ana are    mere"
l=s.split()
print(l)
s="Ana are    mere"
l=s.split(" ")
print(l)

#%%
"""
Exemplu - se citeste un vector de numere
(date pe aceeasi linie, cu spatiu intre ele)
23 5 7 8
Sa se afiseze suma elementelor

"""
s=input()
v=s.split()
print(v)
for i in range(len(v)):
    v[i]=int(v[i])
print(v, sum(v))

#%%%
#citim doua numere
n,m=input("dat doua numere").split() #x,y=2,3
n=int(n)
m=int(m)
print(n+m)      

"""
al doilea param al lui split maxsplit
reprezinta numarul maxim de divizari 
(se obtin maxim maxsplit+1 cuvinte)
"""
#exemplu: 
"""
informatii despre puncte in plan sub forma
x y eticheta
"""
s="12 16 acesta este un punct"
l=s.split(maxsplit=2)
print(l)
x=int(l[0])
y=int(l[1])
print("punctul are coordonatele",x,y)

s="Marinescu Ruxandra 2"
#rsplit- incepe de la dreapta impartirea
l=s.rsplit(maxsplit=1)
print(l)
    

        
    


