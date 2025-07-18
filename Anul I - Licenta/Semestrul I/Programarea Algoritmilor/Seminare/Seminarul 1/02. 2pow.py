n = int(input())

print("bin(n): {}\nbin(n - 1): {}\nbin(n & (n - 1)): {}".format(bin(n), bin(n - 1), bin(n & (n - 1))))

if (n & (n - 1) == 0):
    print("Numarul este putere a lui 2")
else:
    print("Numarul nu este putere a lui 2")