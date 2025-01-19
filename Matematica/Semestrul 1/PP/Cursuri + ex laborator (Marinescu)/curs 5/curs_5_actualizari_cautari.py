# -*- coding: utf-8 -*-

#CAUTARE in siruri de caractere
"""
Daca dorim doar sa verificam daca o litera sau 
un cuvant se gaseste in sirul s putem folosi 
operatorii in si not in 
"""
s="sir"
if "a" in s:
    print("contine a")
else:
    print("nu contine a")
    
if "ir" in s:
    print("contine 'ir'")
else:
    print("nu contine 'ir'")
"""
Daca dorim sa determinam
- numarul de aparitii ale unui 
cuvant in sirul s avem metoda count
s.count(cuv,start,end)- numara aparitiile lui
 cuv in s[start:end]
start si end - pot lipsi, si atunci se numara aparitiiile
din s[:], adica din intregul sir
"""
s="o propozitie"
print(f"litera 'o' apare de {s.count('o')} ori")
print(f"litera 'o' apare de {s.count('o',0,len(s)//2)} ori in prima jumatate")

#%%
"""
daca dorim sa determinam pozitiile pe care 
apare un cuvant in s
s.find(cuvant, start,end) 
returneaza prima pozitie pe care apare cuvant in 
s[start:end] (sau in s daca start si end lipsesc)
Daca nu gaseste cuv - returneaza -1
"""
#exp - toate pozitiile pe care apare 'ou' in s
s="oul este un cadou nouou"
p=s.find("ou")
while p!=-1:
    print(p) #0
    p=s.find("ou",p+2) #2=len("ou")

