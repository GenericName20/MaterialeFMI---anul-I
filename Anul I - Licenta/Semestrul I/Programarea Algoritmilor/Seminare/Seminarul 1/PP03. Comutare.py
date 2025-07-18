try:
    x, y = map(int, input().split())
except:
    print("Numar incorect de valori / Format gresit!")
    exit()

t = x ^ y
k = 0
while t != 0:
    k += 1
    t = t & (t - 1)

print("bin(x): {}\nbin(y): {}".format(bin(x), bin(y)))
print("Trebuie comutati {} biti pentru a se obtine {} din {}".format(k, y, x))