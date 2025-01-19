import random
def pivotare(v,p,u): #se putea face pivotarea si cu vector suplimentar
    """
    Caz defavorabil - cand vectorul e deja ordonat
    subvectorul stang va fi fi mereu vid, iar cel drept va avea n-1, n-2, n-3.. element
    => complexitate O(n^2)
    pentru a ocoli cazul defavorabil- se alege pivotul aleator (nu neaparat primul element)
    """
    r=random.randint(p,u) #pozitie random pt pivot
    #aducem v[r] pe prima pozitie
    v[p],v[r]=v[r],v[p]
    i = p
    j = u
    depli = 0
    deplj = -1
    while i < j:
        if v[i] > v[j]:
            v[i], v[j] = v[j], v[i]
            if depli == 0:
                depli = 1
                deplj = 0
            else:
                depli = 0
                deplj = -1
        i = i + depli
        j = j + deplj
    return i

def quicksort(v,p,u):
    if u<=p: #cel mult un element
        return
    m=pivotare(v,p,u ) #v[p] va ajunge pe pozitia corecta poz in v
    quicksort(v,p,m-1) #sortam stanga - excusiv m, v[m] este deja corect
    quicksort(v,m+1,u)  #sortam dreapta
v=[3,1,10,4,7,2,11,5,1,9]
quicksort(v,0,len(v)-1)
print(v)