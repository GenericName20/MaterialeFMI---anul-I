def divizori(*numere):
    ans = {}
    for numar in numere:
        cop, d, k = numar, [], 2
        while (numar > 1):
            p = False
            while (numar % k == 0):
                numar /= k
                p = True

            if p:
                d.append(k)
            
            k+=1
        
        ans[cop] = d

    return ans

x = divizori(50, 21)
print(x)