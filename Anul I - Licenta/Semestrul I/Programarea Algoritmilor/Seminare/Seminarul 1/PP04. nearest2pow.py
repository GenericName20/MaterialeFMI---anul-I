def solLog(n): # T: O(1), M: O(1)
    from math import log, floor
    l = int(floor(log(n, 2)))
    return n if (n == 2 ** l) else 2 ** (l + 1)

def solShiftRight(n): # T: O(log(n)), M: O(1)
    print("In solutia 2:\nbit(n): {}\nbit(n & (n - 1)): {}\n".format(bin(n), bin(n & (n - 1))))

    # Este deja putere a lui 2
    if (n and (n & (n - 1)) == 0):
        return n

    # Cauta prima pozitie pe care se afla un bit nenul
    pos = 0
    while(n != 0):
        n >>= 1
        pos += 1
    return 2 ** pos

def solShiftLeft(n): # T: O(log(n)), M: O(1)
    if (n and (n & (n - 1)) == 0):
        return n
    
    p = 1
    while (p < n):
        p <<= 1
    return p

def solManualGear(n): # T: O(1), M: O(1)
    n -= 1
    print("In solutia 4:")
    n = n | (n >> 1)
    print(bin(n))
    n = n | (n >> 2)
    print(bin(n))
    n = n | (n >> 4)
    print(bin(n))
    n = n | (n >> 8)
    print(bin(n))
    n = n | (n >> 16)
    print(bin(n))
    n = n | (n >> 32)
    print(bin(n))
    # Se continua cu puterile lui 2, depinde cat de lunga poate fi reprezentarea numarului
    
    return n + 1

n = int(input())
ans1 = solLog(n)
ans2 = solShiftRight(n)
ans3 = solShiftLeft(n)
ans4 = solManualGear(n)
print(ans1, ans2, ans3, ans4)
