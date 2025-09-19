from math import log, floor
n = int(input())

k = 1 + floor(log(n, 2))
mask = (1 << k) - 1
print("bin(n): {}\nbin(mask): {}\nbin(n ^ mask): {}".format(bin(n), bin(mask), bin(n ^ mask)))

k = 0
aux = n ^ mask
while aux != 0:
    k += 1
    aux = aux & (aux - 1)

print("Numarul {} are {} biti nuli in reprezentarea sa binara".format(n, k))
