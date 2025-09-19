n = int(input())

k = 0
aux = n
while aux != 0:
    print("bin(n): {}\nbin(n - 1): {}\nbin(n & (n - 1)): {}\n".format(bin(aux), bin(aux - 1), bin(aux & (aux - 1))))
    k += 1
    aux = aux & (aux - 1)

print("Numarul {} are {} biti nenuli in scrierea binara".format(n, k))