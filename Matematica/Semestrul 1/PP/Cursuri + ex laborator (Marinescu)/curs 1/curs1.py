"""
DIFERENTE FATA DE C++
"""
#---------------------------------------------------------
#variablele nu au tip static declarat
#int x;
x=1
print(x,type(x))#trece la linia urmatoare
x="abc"
print(x,type(x))
x=5
if x==1:#conteaza indentarea
    print("egal cu 1")
    x=2
print(x)

#-----------------------------------------------
#AFISARE
"""
print
-implicit-trece la linia urmatoare (end)
-numar varabil de argumente
-implicit - separatorul este spatiul (sep)
"""
x=2
y=3
print(x,y)
print("alta linie")
#2*3
print(x,y,sep="*",end="")
print("pe aceeasi linie")

#alta varianta 2*3
print(x,end="*")
print(y)

print(x,end="")
print("*",y,sep="")

#print(str(x)+"*"+str(y))

#------------------------------------------
#CITIRE
"""
input(mesaj_optional)
returneaza sir de caractere (str) citit pana la sfarsitul liniei
"""
x=input("Dati x ")
print(x,type(x))
#print(x+1,type(x))#eroare- x este str
x=int(x) #numere intregi
print(x+1,type(x))
#suma a doua numere citite
x=int(input())
y=int(input())#date pe linii diferite
print(x+y)#fara int - face concatenare

#----------------------------------------
"""
TIPURI DE DATE - clase
"""
#numere intregi - int
"""
oricat(v. curs) de multe cifre
constante - baza 2 0b, baza 16 0x
conversii - int()
"""
x=100000000000000000000
print(x)
print("constante in baza 2")
x=0b101 #baza 10 1+0*2+1*2^2

print(x)
print("conversii")
x=int(8.9)
print(x)
x=int("101",base=2)
print(x)

"""
float - numere reale
dubla precizie
operatii aritmetice - nu au precizie absoluta 
"""
x=8.9
print(x)
x=2e-3
print(x)

x=0.1
print(x*x)
print(x*x==0.01, abs(x*x-0.01)<1e-7)
#print(11e+1)
#print(f"{x:.17f}")

