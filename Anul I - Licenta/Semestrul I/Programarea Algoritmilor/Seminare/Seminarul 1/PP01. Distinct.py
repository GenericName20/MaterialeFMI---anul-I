n = int(input())

x = 0
for _ in range(n):
    v = int(input())
    x = x ^ v # Proprietatile x ^ x = 0 si x ^ y ^ x = y

print(x)