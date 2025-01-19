"""
vectorul solutie x=(x1,..xn)
un element xk poate lua valorile 1,2..n (Xk)
conditii finale pt k - elemente distincte
cond de continuare pentru xk: xk diferit de x1,..,x{k-1}
"""
"""
cond de continuare - sunt si suficiente, nu este nevoie de test_solutie()
"""
def retine_solutie(x):
    for v in x:
        print(v,end=" ")
    print()
def continuare(x,k): #x[k] != x[0],...x[k-1]"""
    #return (x[k] not in x[:k])
    for i in range(k):
        if x[k]==x[i]:
            return False
    return True
        
def back(k,x,n):
    if k==n:
        retine_solutie(x)
    else:
        for v in range(1,n+1):
            x[k]=v
            if continuare(x,k):
                back(k+1,x,n)

def generare_permutari(n):
    x=[0]*n
    back(0,x,n)

generare_permutari(3)
generare_permutari(4)