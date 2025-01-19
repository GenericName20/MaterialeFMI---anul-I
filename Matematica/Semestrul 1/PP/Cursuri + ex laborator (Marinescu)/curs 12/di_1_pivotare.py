"""
Se da un vector. Sa se pozitioneze primul element din vector astfel incat
elementele din stanga sa fie mai mici sau egale cu el, iar cele din dreapta
mai mari sau egale (pe pozitia corecta in vectorul sortat)
"""
"""
Var 1:
Folosim un vector suplimentar aux. fie x= primul element
luam celelalte  elementele pe rand
- daca dam de un element mai mic sau egal decat x - il punem in aux in stanga
(folosim un indice sa stim undea am ajuns in aux cu completarea la stanga)
- daca dam de un element mai mare - il adaugam in dreapta

"""
def pivotare(v):
    n=len(v)
    aux=[0]*n #int a[100]
    inc=0
    fin=n-1
    x=v[0]
    for i in range(1,n):
        if v[i]<=x:
            aux[inc]=v[i]
            inc+=1
        else:
            aux[fin] = v[i]
            fin -= 1
    aux[inc]=x #la final - il adaugam si pe pivotul x
    for i in range(n):
        v[i]=aux[i]

v=[3,1,10,4,7,2]
pivotare(v)
print(v)

"""
Varianta 2 - fara vector suplimentar
"""
def pivotare(v):
    i=0
    j=len(v)-1
    depli = 0
    deplj = -1
    while i<j:
        if v[i]>v[j]:
            v[i],v[j]=v[j],v[i]
            if depli==0:
                depli=1
                deplj=0
            else:
                depli=0
                deplj=-1
        i=i+depli
        j=j+deplj
v=[3,1,10,4,7,2]
pivotare(v)
print(v)



