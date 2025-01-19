# -*- coding: utf-8 -*-
"""
FISIERE TEXT
Lucru cu fisiere:
1) deschidere - asociem un obiect unui fisier fizic, memorat intr-o 
    variabila
f=open(nume_fisier) #nume fisier fizic sau cale
f=open(nume_fisier,mod_deschidere) - un fisier poate fi deschis pentru diverse operatii
mod_deschidere ="r": deschis pentru citire - implicit
"w"-pentru scriere
+alte modalitati ("a"-append)

2) prelucrare - metode de citire/scriere
    
3) inchidere
f.close()
"""
f=open("nume.in")

f.close()

#citire din fisier
f=open("nume.in") #deschis pentru citire

"""
Metode de citire
returneaza siruri de caractere corespunzatoare liniilor
daca linia se termina in fisier cu delimitator de sfarsit de linie (cu "enter")
atunci sirul returnat corespunzator liniei se termina cu \n
"""
f.close()

#f.read() => sir de caractere cu tot continutul fisierului
print("citiire cu read => tot fisierul")
f=open("nume.in")
s=f.read()
print(s)
print(repr(s))
f.close()

"""
f.readlines()=> lista de siruri de caractere corespunzatoare liniilor 
(lista de linii) 
"""
print("citire cu readlines => lista de linii")
f=open("nume.in")
s=f.readlines()
print(s)
f.close()
"""
f.readline() => sir de caractere coresp liniei curente
"""
print("citire cu readline => o linie")
f=open("nume.in")
s=f.readline()
print(s)
print(repr(s))
f.close()

#exemplu - citire linie cu linie a unui fisier
print("citire linie cu linie")
f=open("nume.in")
s=f.readline()
while s!="":
    """readline intoarce "" daca am ajuns la finalul fisierului"""
    print(repr(s))
    s = f.readline()
f.close()
"""
un fisier este iterabil (colectie de linii)
"""
print("cu for (iterator)")
f=open("nume.in")
for linie in f:
    print(repr(linie))
f.close()

f=open("exemplu.out","w") #!!!deschis pentru scriere
f.write("un exemplu") #- scrie in fisier un sir de caractere, fara altceva adaugat (\n, spatii)
f.write("alt exemplu")
x=5
#f.write(x) #eroare
f.write(str(x))
f.write("\n")
f.writelines(["unu","doi"]) # scrie in fisier o secventa de cuvinte fara altceva adaugat
#putem redirectiona prin sa scrie in fisier (va folosi tot write) - folosind parametrul file
x,y=4,5
print(file=f)
print(x,y, file=f)
f.close()
