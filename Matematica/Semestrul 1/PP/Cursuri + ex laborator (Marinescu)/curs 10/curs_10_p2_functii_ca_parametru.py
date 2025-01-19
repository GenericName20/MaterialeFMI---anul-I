"""
O functie poate primi ca parametru o alta functie

Exemplu -vrem sa calulam o suma generica de forma
f(x1)+f(x2)+...+f(xn) unde f sa fie o functie specificata de noi
"""
def suma(*numere,f): #numere- x1,..,xn
    s=0
    for x in numere:
        s+=f(x)
    return s


import math
x=suma(4,9,f=math.sqrt) #suma de radicali
print(x)
x=suma(4,6,8,-9,10,-11,f=abs) #suma de module
print(x)
def functia_noastra(x):
    return x*x+1
x=suma(4,1,2,f=functia_noastra)
print(x)
#print(globals())
