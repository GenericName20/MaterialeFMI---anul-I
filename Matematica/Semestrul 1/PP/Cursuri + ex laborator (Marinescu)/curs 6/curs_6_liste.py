# -*- coding: utf-8 -*-
"""
Liste - clasa list
memorate - vector (array)
de exemplu - pentru a sterge primul element
toate celelalte se deplaseaza la stanga -> O(n)
"""
#creare
l=[8,9,10,7]
l=list("abc") #lista literelor
print(l, type(l))
l=[]
l=list() #lista vida, de lungime 0

"""
Comun cu sirurile:
#cautare: in, not in , index, count 
#nu avem metoda find   
"""
l=[9,8,3]
if 0 in l:
    print("lista are elemente nule")
else:
    print("nu contine 0")

#functii uzuale: len, min, max, sum
#operatori relatonali 
#==, >,>=, <, <=
#comparare element cu element
l1=[2,7,8]
l2=[4,5]
print(l1<l2) #adev, deoarece l1[0]<l2[0]
l3=[5,4]
print(l2==l3) #nu sunt egale, conteaza ordinea
#%%%
"""
Modificare
listele sunt mutabile (se pot modifica)
"""
l=[4,2,1,10]
#actualizarea unui element
l[0]=12
print(l)

"""
Metode - modifica lista (nu returneaza o 
noua lista ca la siruri)
1. append vs extend
lista.append(element) - adauga element la finalul listei
lista.extend(colectie) - adauga pe rand
toate elementele din colectie la lista
"""
l=[2,5,7]
l.append(8) #adauga elem 8 la final
print(l)
l1=[10,5]
l.extend(l1)
print(l)

l.append(l1) #adauga lista l1 ca element al lui l
print(l)

l=["unu", "doi"]
l.append("trei")
print(l)
l.extend("trei") 
#itereaza sirul- il adauga litera cu litera
print(l)

"""
insert(pozitie, element) - insereaza un element pe pozitie data
pop(pozitie)-elimina elementul de pe pozitia data (si il returneaza)
pop()- elimina ultimul element
----
remove(element) - elimina prima aparitie a 
parametrului element din lista (eroare daca nu exista)

"""
l=[4,5,7]
l.insert(2,6)
print(l)
x=l.pop()
#print(f"am eliminat ultimul element {l.pop()} si am obtinut{l}")
print(f"am eliminat ultimul element {x} si am obtinut {l}")

l=[4,5,6,5,7]
l.remove(5)#sterge prima aparitie a lui 5
print(l)
x=11
if x in l:
    l.remove(x)

x=5
while x in l:
    l.remove(x) #sterge toate aparitiile
print(l)

"""
Listele se pot actualiza folosin felieri:
l[i]=element
l[i:j]=iterabil (colectie) - se inlocuieste
secventa din lista dintre poz i si j (excusiv j)
cu membrul drept (!nu trebuie neaparat sa aiba aceeasi lungime)
l[i:j:k]=iterabil (de aceeasi lungime)
"""
l=list(range(5,12))
print(l)
l[3:5]=[11,12,14,15,18]
print(l)
#exemplu: stergem primel k elemente
k=4
l[:k]=[]
print(l)
#inserare pe pzitia k a valorii x
k=2
x=100
l[k:k]=[x]
print(l)
#adaug la final pe x:
l[len(l):]=[x]    
print(l)
l=[1,2,3,4,5,6]
#inlocuim elem de pe pozitiile pare cu 0
l[::2]=[0,0,0]
print(l)

# avem si operatorii +, *n
l=[1,2,3,4,5,6,7]
l[::2]=[0]*((len(l)+1)//2)
print(l)

"""
Pentru stergere
del l[i]
del l[i:j]
del l[i:j:k]
"""
