#varianta 1 - folosim algoritmul de combinari pentru m=1,2..,n
"""
n=4
for m in range(1,n+1):
    generare_combinari(n,m)

o sumbultime a multimii 1,2..,n se poate reprezenta printr-un
vector binar (vector caracteristic) x=(x1,x2,..,xn) cu
xk=1 <=> k se afla in submultime
n=5 {1,2,3,4,5}
{2,3,5} <-> (0,1,1,0,1)
(0,0,0,1,1) -> {4,5}
a genera toate submultimie <=>
a genera toate sirurile binare de lungime n
"""
def retine_solutie(x,n):
    for i in range(len(x)):
        if x[i]==1:
            print(i,end=" ")
    print()
def back(k,x,n):
    if k==n:
        retine_solutie(x,n)
    else:
        for v in range(2): #range(1,-1,-1)
            x[k]=v
            back(k+1,x,n)

def generare_submultmi(n):
    x=[0]*n
    back(0,x,n)
generare_submultmi(4)