# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"""
LISTE
clasa list - continuare
"""
#secvente de initializare - comprehensiune (comprehension)

#%%
#exemplu- sa se creeze o lista cu n valori egale cu 0(n dat)
n=int(input())
#Varianta 1 -alev + si *n
v=[0]*n
print(v)
#varianta 2 - cu append
v=[]
for i in range(n):
    v.append(0)
print(v)
#varianta 3 - cu secvente de initializare
"""
v=[element for val in secventa]
scriere prescurtata pentru:
v=[]
for val in secventa:
    v.append(element)
"""
v=[0 for i in range(n)]
print(v)
#%%
#citirea unui vector cu elementele date pe o linie
#varianta 1: - am facut la split
v=input().split() #lista de str 
print(v)
for i in range(len(v)):
    v[i]=int(v[i])
print(v)
#varianta 2: cu secv de initializare
v=[int(x) for x in input().split()]
print(v)
#%%
#exemplu- sa se creeze un vector cu primele n patrate perfecte pozitive
n=10 #int(input())
v=[i*i for i in range(1,n+1)]
print(v)
#%%citirea a 2 numere date pe aceeasi linie
n,m=[int(x) for x in input().split()]    
print(n,m)

#%%%
"""
secvente de initializare conditionate (cu if)
[element for x in secventa if conditie]
v=[]
for x in secventa:
    if conditie:
        v.append(element)
"""
#exemplu-dat un vector, sa se creeze un nou vector
#cu elementele lui pozitive
v=[int(x) for x in input().split()]
v_poz=[x for x in v if x>0]   
print(v_poz)

#%%se dau doi vectori reprezentand multimi
#- sa se determine intersectia 
m1=[4,1,6,7]
m2=[6,5,4,3,2,0]
v=[x for x in m1 if x in m2]
print(v)

#%%%
#se da un cuvant - sa se formeze in memorie un nou cuvant
#obtinut prin stergerea vocalelor din cuvantul initial
s=input()
s_fara_vocale=[c for c in s if c not in "aeiouAEIOU"]
print(s_fara_vocale)
s_fara_vocale="".join(s_fara_vocale)
print(s_fara_vocale)
#%%
#putem folosi in comprehensiune (secvente de initializare)
# si operatorul if else (conditional)
# expr1 if conditie else expr2
#exemplu - modulul unui numar
x=-20
y=x if x>=0 else -x  
print(y)
#exemplu- se da un vector v
#sa se creeze un nou vector in care elementele negative din v
#sunt inlocuite cu 0
v=[4,1,-6,8,-9,-1,40]
v_nou=[x if x>=0 else 0 for x in v] 
print(v_nou)  
#cu append: 
print("metoda 2")
v_nou=[]
for x in v:
    if x>=0:
        v_nou.append(x)
    else:
        v_nou.append(0)
print(v_nou)
#%%
#se pot folosi in  comprehensiune si mai multe for-uri
v=[(x,y) for x in range(7) for y in range(7) if x!=y and (y%2==0)]
print(v)
#%%
#sort vs sorted
l=[5,1,7,19,10]
#sorted(l) => returneaza lista ordonata (!nu modifica l)
l_noua=sorted(l)
print(l,l_noua)

l.sort() #sorteaza l (modifica lista l, nu returneaza alta lista)
print(l)
#reverse vs reversed
#%%
#copiere
#incorect
l=[5,1,7]
l_c=l #l si l_c refera acelasi obiect
l[0]=3 #se modifica l_c
print(l,l_c)
l_c=l.copy() #nu se modifica si l_c
l[0]=19
print(l,l_c)
#%%
#la matrice - deepcopy din modulul copy
a=[[11, 2, 3], [4, 5, 6]]
b=a.copy()
a[0][0]=15
print(a,b)
import copy
b=copy.deepcopy(a) 
a[0][0]=78
print(a,b)




    
    
    
    