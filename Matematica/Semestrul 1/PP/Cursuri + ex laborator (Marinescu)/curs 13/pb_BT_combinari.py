"""
Combinari de m din {1,2,..,n}
(submultimi de m elemente ale multimii {1,2..,n})

vectorul solutie x=(x1,..,xm)
un element xk poate lua valorile 1,2..n (Xk)
conditii finale pt k - elemente distincte

 Oservatie : {1,2,3}={3,1,2}={3,2,1}. --> este suficient sa generam 1,2,3
Pentru unicitate - tb ca x1<x2<..<xn

cond de continuare pentru xk: xk >x{k-1}

cond de continuare - sunt si suficiente, nu este nevoie de test_solutie()
"""
def retine_solutie(x):
    for v in x:
        print(v,end=" ")
    print()
def continuare(x,k): #x[k] != x[0],...x[k-1]"""
    #return (x[k] not in x[:k])
    if k==0:
        return True
    return x[k]>x[k-1]

def back(k,x,m,n):
    if k==m: #!!in loc de ==n
        retine_solutie(x)
    else:
        for v in range(1,n+1):
        """se putea 
        for v in range(x[k-1]+1,n+1) 
        pentru k>0 si nu mai trebuie verificate cond de continuare"""
            x[k]=v
            if continuare(x,k):
                back(k+1,x,m,n)

def generare_combinari(n,m):
    x=[0]*m
    back(0,x,m,n)

generare_combinari(4,3)