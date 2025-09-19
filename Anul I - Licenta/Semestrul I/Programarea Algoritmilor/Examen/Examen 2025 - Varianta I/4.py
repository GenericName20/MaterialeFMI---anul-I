def printsol(k):
    print(*x[1:k+1])

def cond(k):
    if k >= 2 and x[k - 1] == x[k]:
        return False

    ap = 0
    for i in range(1, k):
        if (x[i] == x[k]):
            ap += 1
            if ap > p:
                return False

    return True

def sol(k):
    return k == n

def bkt(k):
    global s

    for i in range(1, 10):
        x[k] = i
        if(cond(k)):
            if(sol(k)):
                s += 1
                printsol(k)
            else:
                bkt(k + 1)

n, p = [int(value) for value in input().strip().split()]
x = [0] * (n + 1)
s = 0
bkt(1)
print("Numarul de solutii: {}".format(s))