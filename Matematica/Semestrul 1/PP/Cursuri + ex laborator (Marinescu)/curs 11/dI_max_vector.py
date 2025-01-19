def DIMax(v,p,u):
    if p==u: #subpb mica- o rezolv direct
        return v[p]
    #impart vectorul in 2 subvectori de dimensiuni aprox egale (jumatate)
    m=(p+u)//2
    mstg=DIMax(v,p,m) #max pt subvect stg
    mdr=DIMax(v,m+1,u) #max pt subvect dr
    if mstg>mdr: #combinarea rezultatelor
        return mstg
    else:
        return mdr


v=[5,1,6,10,8,4] #[int(x) for x in input().split()]
x=DIMax(v,0,len(v)-1) #tot vectorul
print(x)

