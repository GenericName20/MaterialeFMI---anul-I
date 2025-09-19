n = int(input())

x = n
for k in range(1, n):
    y = int(input())
    x = x ^ y ^ k

print(x)