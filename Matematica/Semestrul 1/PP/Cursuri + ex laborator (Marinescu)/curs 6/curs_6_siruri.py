# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 14:14:41 2023

@author: Ruxandra
"""
#%%
#CAUTARE
#operatorii in, not in
#metoda find - cursul trecut
#exp - toate pozitiile pe care apare 'ou' in s
s="oul este un cadou nouou"
p=s.find("ou")
while p!=-1:
    print(p) #0
    p=s.find("ou",p+2) #2=len("ou")

#%%%
#metoda index - ca si find
#diferenta - daca nu gaseste elementul
#da eroare - ValueError
#listele - au doar metoda index, nu si find
s="oul este un cadou nouou"
try:
    p=s.index("ou")
    while True:
        print(p) #0
        p=s.index("ou",p+2) #2=len("ou")
except: #cand index nu mai gaseste "ou"
    pass
#except ValueError:        
#%% 
s="abcd"
try:
    print(s.index("f")) 
except:
    #se executa daca instructiunile din try 
    #dau eroare
    print("nu contine litera f") 
#%%
"""
sir.count(x) => returneaza numarul de aparitii
ale lui x in s (x poate fi sir)
!!!aparitii care nu se suprapun
sir.count(x,start,end) => cauta x doar 
intre pozitiile start si end (exclusiv end),
adica s[start:end] si returneaza
numarul de aparitii dintre aceste pozitii
 
"""
#%%%
"""
Modificarea unui sir => alt sir
s=sir.metoda()
"""
"""
1. Folosind felieri
"""
"""
exemplu - inlocuim in s caracterul de 
pe pozitia k cu ", "
"""
s=input()
k=int(input())
s=s[:k]+", "+s[k:]
print(s)

#exemplul 2 -stergem prima litera
s=s[1:]
#%%%
"""
s.replace(old,new) - inlocuieste !!toate
aparitiile lui old cu new
s.replace(old,new,count) - inlocuieste doar 
primele count aparitii
"""
#exemplu - inlocuim 2022 cu 2023
s="Subiect examen 2022 - ianuarie 2022"
s=s.replace("2022","2023")
print(s)

"""
#exemplu - stergem dintr-o propozitie
toate spatiile, cu exceptia ultimului
""" 
s=" 1 2 3 4 5 6 altceva"
s=s.replace(" ","",s.count(" ")-1)
print(s)

#%%
"""
lower(),upper(), title()....
"""
s="un cuvant"
print(s.upper())
print(s.title())

"""
Metode de testare a continutului
islower() - True daca toate literele sunt mici
isupper(), isdigit(), isalnum()...

"""
#exemplu:
s="Cheltuieli: 10 lei apa, 15 lei mancare, 12 lei altceva"
#suma numerelor (preturilor) din text
#ipoteza: au spatiu inainte si dupa

ls=s.split()
print(ls)
s=0
for cuv in ls:
    if cuv.isdigit(): #cuv.isnumber()
        s+=int(cuv)
print(s)
#%%%
"""
s.strip(sir_caractere) - 
elimina de la inceputul
si sfasitul sirului s caracterele din
sirul sir_caractere primit ca parametru 
(pana intalneste alte caractere)
rstrip, lstrip
"""
s="* ,Programare,*  "
s=s.strip("* ,")
print(s)

#%%
#sorted(s) => lista caracterelor lui s ordonata