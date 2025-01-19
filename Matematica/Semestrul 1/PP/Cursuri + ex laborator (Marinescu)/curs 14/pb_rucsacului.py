"""
Pb continua(fractionara) a rucsacului
Se dau:
G- greutatea max admisa de rucsac
n obiecte:
pentru fiecare obiect i se dau:
- valoarea lui (castigul)= ci (daca il incarcam complet in rucsac)
- greutatea lui =gi
Din obiecte se pot pune in rucsac si fractiuni
(si atunci se obtine fractiunea corspunzatoare din castig)
Se cere:
ce fractiuni din fiecare obiect incarcam in rucsac fara
a depasi greutatea G, astfel incat valoarea totala a obiecte
incarcate in rucsac sa fie maxima
"""
"""
primul obiect pe care incercam sa il adaugam in rucsac - cel
cu valoarea pe unitatea de greutate (cu raportul ci/gi cel mai mare)
la un pas- alegem fractiune din ob cu c/g maxim, neales anterior
Obs - cel mult un obiect va fi fractionat
- ar fi uti sa ordonam initial obiectele dupa raportul ci/gi descrescator
"""
c=[4,4,4,7]
g=[2,1,3,4]
G=5
n=len(g)
l_obiecte=[]
for i in range(n):
    l_obiecte.append([c[i],g[i],i+1])
def cheie(x):
    return x[0]/x[1]
l_obiecte.sort(key=cheie, reverse=True)
print(l_obiecte)
G_ramasa=G
c_total=0
for obiect in l_obiecte:
    if obiect[1] <= G_ramasa: #incape integral in rucsac
        print(f"obiectul {obiect[2]} - castigul {obiect[0]}")
        c_total+=obiect[0]
        G_ramasa-=obiect[1]
    else: #iau o fractiune din el
        print(f"obiectul {obiect[2]} fractiunea {G_ramasa}/{obiect[1]} - castigul {G_ramasa}/{obiect[1]}*{obiect[0]}")
        c_total+=(G_ramasa/obiect[1])*obiect[0]
        G_ramasa=0
    if  G_ramasa==0:
        break
print(c_total)