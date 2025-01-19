#break - iese din instructiune repetitiva

#dat n, sa se afiseze primul divizor propriu
n=13
#parametrii de la range -numere intregi
ok = 0
for d in range(2, int(n**0.5) +1): #range(2,n//2+1)
    if n%d==0:
        print(d)
        ok = 1
        break
if ok == 0:
    print("este prim")
#varianta - fara ok, cu else la for
n=2
for d in range(2, int(n ** 0.5) + 1):  # range(2,n//2+1)
    if n % d == 0:
        print(d)
        break
else: #se executa daca nu se iese din for/while cu break
    print("este prim")

#sa se afiseze cel mai mare numar prim din [a,b]
a=98
b=100
for n in range(b,a-1,-1):
    for d in range(2, int(n ** 0.5) + 1):  # range(2,n//2+1)
        if n % d == 0:
             break
    else:  # se executa daca nu se iese din for/while cu break
        print(n)
        break
else:
    print("nu exista numar prim in interval")

if n<=0:
    pass
else:
    print("pozitiv")