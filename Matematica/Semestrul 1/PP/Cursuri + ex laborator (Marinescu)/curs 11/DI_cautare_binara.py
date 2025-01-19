def cautare_binara(v,x,p,u):
    if u<p:
        return -1 #nu gasit return (False,u)
    m=(p+u)//2
    if v[m]==x:
        return m
    elif v[m]<x: #in dreapta
        return cautare_binara(v,x,m+1,u)
    else:
        return cautare_binara(v, x, p, m-1)
def cauta(v,x):
    rez = cautare_binara(v, x, 0, len(v) - 1)
    if rez==-1:
        print(f"{x} nu exista")
    else:
        print(f"{x} se afla pe pozitia {rez}")
v=[1,5,10,11,13,19,20] #ordonat crescator
cauta(v,19)
cauta(v,16)
#tema- implementarea nerecursiva
