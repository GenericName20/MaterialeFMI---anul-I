def sort_interclasare(v,p,u):
    if u<=p: #cel mult un element -nu tb sa sortez
        return
    m=(p+u)//2
    sort_interclasare(v,p,m) #stanga
    sort_interclasare(v,m+1,u)#dreapta
    interclaseaza(v,p,m,u) #amesteca subvect stg: v[p:m+1] v[p....m] cu drept v[m+1:u+1]
def interclaseaza(v,p,m,u): #v[p:u+1] are u-p+1 elemente
     a=[0]*(u-p+1) #vectorul in care interclasam cei doi subvectori
     k=0
     i=p
     j=m+1
     while i<=m and j<=u: #ambii subvector mai au elemente
         if v[i]<v[j]:
             a[k]=v[i]
             i+=1
         else:
             a[k]=v[j]
             j+=1
         k+=1
    #copiem elementele din subvectorul care mai are elemente
     while i<=m :
         a[k]=v[i]
         i+=1
         k += 1
     while j<=u:
         a[k] = v[j]
         j += 1
         k += 1
     #copiem a inapoi in v intre pozitiile p si u
     k=0
     for i in range(p,u+1):
         v[i]=a[k]
         k+=1

v=[4,1,8,2,10,45,5,0]
sort_interclasare(v,0,len(v)-1)
print(v)
