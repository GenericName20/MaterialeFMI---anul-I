def citire(nume_fisier):  # nume_fisier e o variabila
    f=open(nume_fisier)   # deschidem fifierul
    n=int(f.readline())     #citim primul nr  n  din fisier 
    l=[]
    for i in range(1,n+1):
        x,y=f.readline().split() #[int(x) for x in f.readline().split()]
        x=int(x)
        y=int(y)
        l.append([x,y,i])
    f.close()
    return l
def cheie(interval):  #returneaza timpul de terminare 
    return interval[1]
#interval[0]=inceput, [1]=terminare, [2]=indicele

def sumb_max_spectacole(l_spect):# sorteaza l_spect dupa timpul de terminare
    s=[]
    l_spect.sort(key =cheie) #key=lamba x:x[1]    
    """
    Luam pe rand intervalele in ord cresc dupa terminare
    Pentru a verifica daca intervalul curent se poate adauga
    la solutia s este suficient sa verificam daca el
    nu se intersecteaza cu ultimul interval adaugat in s
    (deoarece acesta era timpul de terminare cel mai mare
    dintre intervalele din s)
    """
    s.append(l_spect[0]) #adaugam primul interval
    for interval in l_spect[1:]:
        #testam daca interval se poate adauga la s
        if interval[0]>s[-1][1]: #s[-1]=ultimul interval selectat
            s.append(interval)
    return s

l_spect=citire("spectacole.in")
print(l_spect)
s=sumb_max_spectacole(l_spect)
print("spectacole selectate:")
for interval in s:
    print(f"spectacolul {interval[2]}: [{interval[0]},{interval[1]}]")

"""
Acoperire minima a unei multimi de intervale:
se dau n intervale
Sa se detrmine o multime de numere de cardinal minim cu proprietatea
ca orice interval dintre cele date 
contine cel putin un element din multime

Pb cuielor: n scanduri - unde incepe, unde se termina
nr minim de cuie care tb batute in scanduri a.i in fiecare scandura
sa fie batut cel putin un cui
[1, 4], [2, 3], [8, 10], [5,7], [5,9]
exp: {2,5,8}
nr max de interv disj = cardinalul acoperirii minime

(evident <= - tb cate un cui in fiecare interval din mults de interv disj)
Solutia - cuie in extrimitatea dreapta a intervalelor obt cu 
pb. spectacolelor (deoarece intervalele eliminate contin extermitatea 
din dreapta a ultimui interval adugat in solutie inaintea lor)
"""
print("cuie:")
for interval in s:
    print(interval[1],end=" ")