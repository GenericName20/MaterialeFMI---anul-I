#completarea recursiva a unei matrice cu numerele de la 1 la dim**2
def DI(a,x,y,dim): # o submatrice este identificata prin linia si coloana coltului din stanga sus - x si y si dimensiunea dim
    global k 
    if dim==1:
        a[x][y]=k
        k+=1
    else:
        #impartim matricea in 4 submatr
        #cadranul 1:
        DI(a,x,y+dim//2, dim//2)
        #cadranul 2:
        DI(a,x+dim//2,y, dim//2)
        #cadranul 3
        DI(a, x, y, dim // 2)
        # cadranul 4
        DI(a,x+dim//2, y+dim//2, dim//2)

n=2
dim=2**n #1<<n
a=[[0 for i in range(dim)] for j in range(dim)]
k=1
DI(a,0,0,dim)
for linie in a:
    print(*linie)