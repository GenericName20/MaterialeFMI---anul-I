# -*- coding: utf-8 -*-
#unificari
"""
data o lista de cuvinte (iterabil) 
si un separator, sa se construiasca o propozitie
obtinuta prin lipirea cuvintelor cu separator intre ele
DAte [cuv1,cuv2,.., cuvn] si sep=>
propozitia cuv1sepcuv2sep...cuvnsep
"""
#Exemplu - 
"""
Se da o propozitie cu cuvinte separate prin spatiu
a) sa se afiseze cuvintele din propozitie
b) sa se formeze o noua propozitie cu cuvintele 
din propozitia initiala, dar separate cu virgula

"""
prop="aceasta  este o propozitie"
ls_cuvinte=prop.split() #vs split(" ")
for cuvant in ls_cuvinte:
    print(cuvant)

"""
Unificare -cu metoda join
separator.join(lista_cuvinte)
"""
separator=", "
prop=separator.join(ls_cuvinte)
print(prop)

"""Exemplu -
Se citeste un vector cu n numere 
Sa se afiseze suma elementelor din vector sub forma
v1+v2+...+vn=suma
v=[3,4,5]
3+4+5=12
"""
v=input().split()
s=0
for x in v:
    s+=int(x)
print(v)
r="+".join(v)
print(r,"=",s,sep="")
#%%
"""
dat un cuvant s cu litere mici,
sa se construiasca un alt cuvant 
obtinut prin ordonarea literelor din s
Exemplu:
s="este" => "eest"
"""
"""
Sortarea unei secvente se face cu metoda sorted
sorted(secventa) => returneaza lista 
cu elementele secventei sortate
exemplu sorted([4,1,7]) => returneaza [1,4,7]
sorted("este")=> ['e','e','s','t']
"""

s="este"
l=sorted(s)
print(l)
rez="".join(l)
print(rez)

#%%%
#FORMATAREA SIRURILOR
"""
VAR 1 - f-stringuri
=un tip special de siruri in care
putem introduce intre {} si campuri de formatare
In campul de formatare putem da variabile sau 
expresii si putem specifia diferite modalitati
de formatare: dimensiunea pe care se afiseaza,
cu cate zecimale sa formateze un numar real etc
f"text normal {x:10} alt text {y:.2f}" 
UN sir f-string se prefixeaza cu f
un camp de formatare arata astfel:
{variabila:dimensiune_afisare.numar_zecimaleTip}
in loc de variabila- putem pune expresii
"""
#Exemple:
"""
Pentru doua variabile x si ysa se afiseze
un mesaj de forma x+y=y+x=suma
pt x=4,y=6 se va afisa 4+6=6+4=10
"""
x,y=4,6
print(f"{x}+{y}={y}+{x}={x+y}")
#se inlocuieste in sir {variabila} cu valoarea

print("{x}+{y}={y}+{x}={x+y}")

#in exemplul anterior
v=['3','4','5']
r="+".join(v)
s=12
#print(r,"=",s,sep="")
print(f"{r}={s}")
print(f"{'+'.join(v)}={s}")
s=f"nota obtinuta este {x+y}"
print(s)

#Exemplu2: 
#sa se afiseze un sir de caractere 
#a) astfel incat sa ocupe 10 caractere
#b) sa afiseze titlu cursului centrat pe 20 de caractere
s="titlu"
x=12
print(f"{s}")
print(f"{x}")
print(f"{s:10}","curs") 
#aliniat la stanga implicit, s este str
print(f"{x:10}","curs")
#aliniat la dreapta implicit, y este numar

#afisare centrat pe 20 de caractere
s="Programare"
print("*",f"{s:^20}","*")
print("*",f"{s:20}","*")
"""
putem specifica inainte de dimeniune
tipul de aliniere
^ pentru centrat
< pentru la stanga
> pentru la dreapta
Exista si metodele
center, rjust, ljust
"""
print(s.center(20))
#implcit caracterul 
#cu care umple este spatiul
print(s.center(20, '-'))


#%%%
#Exemplu:afisarea unei matrice

a=[[100, 4, 5],[2,70,1], [1,2,3]]
#afisare-stil C++
for i in range(3):
    for j in range(3):
        print(f"{a[i][j]:4} ",end="")
    print()

#%%
#Exemplu:- afisarea cu 2 zecimale
x=1.1
y=2.2
z=1/3
print(f"{x+y:.2f} si {z:.3f}")

x=14
print(f"{x:b}") #privit in baza 2
print(f"{x:8b}")
print(f"{x:08b}") #umple cu 0

"""
VAR 2 - cu metoda format a clasei str
"""
x,y=4,6
print("{}+{}={}+{}={}".format(x,y,y,x,x+y))
#{} se inlocuiesc cu parametrii metodei format
#prima {} se inlocuieste cu primul param....

#alta varianta - punem intre {} indicele param
#indicii de la 0
print("{0:5}+{1}={1}+{0}={2}".format(x,y,x+y))

#a 3-a varianta-putem da nume parametrilor
print("{0:5}+{1}={1}+{0}={s}".format(x,y,s=x+y))
  



