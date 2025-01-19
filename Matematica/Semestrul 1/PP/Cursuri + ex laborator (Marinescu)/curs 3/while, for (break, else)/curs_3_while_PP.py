"""
Innstructiunea while
while conditie:
    instructiuni
"""
#citim numere naturale pana se introduce valoare 0;
# afisam suma lor
s=0
x = int(input())
while x!=0:
    s+=x #s =s +x
    x=int(input())
print(s)

#citim un n si un sir de n numere (date fiecare pe o linie)-> afisam tot s
n=int(input())
i=1
s=0
while i<=n:
    x=int(input())
    s+=x
    i+=1
print(s)