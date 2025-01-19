#INSTRUCTIUNI

#1.Atribuire
x=1
x=y=1 #(x si y numesc(refera) acceasi valoare)
print(x,y,id(x),id(y))
x, y = 1, 2
print(x,y)
x, y = y, x #atribuire de tupluri, intai se evalueaza dreapta
print(x,y)
x=8
y=5
x,y=min(x,y),max(x,y)
print(x,y)

#instructiunea CONDITIONATA/ALTERNATIVA if
"""
var 1.
if conditie:
    instructiuni
"""
#Exemplu - citesc un numar si daca este neagtiv ii iau modulul
x=int(input())
if x<0:
    x=-x
    print("am schimbat semnul lui x")
print(x)
"""
var .
if conditie:
    instructiuni
else:
    instructiuni
"""
#exp-test de numar par
x=int(input())
if x%2==0:
    print("este par")
else:
    print("este impar")
#exemplu: ultima cifra a lui 3**x
x=int(input())
r=x%4
if r==0:
    u=1
else:
    if r==1:
        u=3
    else:
        if r==2:
            u=9
        else:
            u=7
print(u)

if r==0:
    u=1
elif r==1:
    u=3
elif r==2:
    u=9
else:
    u=7
print(u)

"""
Instr while -repetitiva cu test initial
while conditie:
    instructiuni
"""
#Exp - afisarea numerelor de la 1 la n, cu n dat
n=int(input("primee n numere"))
i=1
while i<=n:
    print(i, end=" ")
    i+=1
print()
#suma cifrelor
n=int(input("dati numar pentru suma "))
s=0
while n>0:
    s=s+n%10 #puteam +=
    n//=10
print(s)

