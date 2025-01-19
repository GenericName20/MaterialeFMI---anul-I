# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 14:47:50 2023

@author: Student
"""

"""
MATRICE
se memoreaza ca lista de liste
a=[[1,7,9],[10,2,8]]
a[0] - lista cu elementele de prima linie
a[1] - lista cu elementele de pe a doua linie
....
len(a) - numarul de linii din matrice
"""
#%%
#exemplu - crearea unei matrice cu 0 (m linii, n coloane)
m,n=[int(x) for x in input().split()]
#varianta 1:
a=[]
for i in range(m): #creez linia i
    linie=[0 for j in range(n)]
    a.append(linie)
print(a)
#varianta 2:
a=[[0 for j in range(n)] for i in range(m) ]    
print(a)

#%%citirea unei matrice
m,n=[int(x) for x in input().split()]
#varianta 1:
a=[]
for i in range(m): #citesc linia  i
    linie=[int(x) for x in input().split()] 
    a.append(linie)
print(a)
#varianta 2:
#a=[i*i for i in range(m) ]  
"""
a=[[int(x) for x in input().split()] for i in range(m) ]   
print(a)
"""    
## TEMA -adunarea a doua matrice

#afisarea unei matrice:
#stil -C++ - cu indici
for i in range(m):
    for j in range(n):
        print(a[i][j], end=" ")
    print()
#stil Python - cu elemente
for linie in a: #elementele lui a -liniile matricei
    for x in linie:
        print(x, end=" ")
    print()
#%%%
#exercitiu - 
#sa se creeze un vector cu maximul de pe fiecare linie
#a unei matrice date
a=[[11, 2, 3], [4, 5, 6]]
#max(list)
v=[]
for linie in a:
    v.append(max(linie))
print(v)
#cu comprehensiune
v=[max(linie) for linie in a]
print(v)

#%%
#se da o matrice 
# sa se insereze o linie cu toate elementele 0 inainte de prima linie
a=[[11, 2, 3], [4, 5, 6]]
n=len(a[0])
poz=0
a.insert(poz,[0 for i in range(n)])
#a[poz:poz]=[[0 for i in range(n)]]
print(a)

    


