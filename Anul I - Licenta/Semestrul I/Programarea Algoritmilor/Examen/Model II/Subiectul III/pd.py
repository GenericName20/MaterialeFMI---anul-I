# Complexitate O(n*n)
# Stare: 
# d[i][0] - Lungimea maximă a unui subsir din care poate face parte t[i]
# d[i][1] - Elementul anterior lui t[i] din subsirul din care acesta face parte

# Stare inițială: 
# d[i][0] = 1 | 0 <= i < n (Fiecare element face parte din subsirul determinat de el insusi)
# d[i][1] = -1 | 0 <= i < n (Nu exista niciun element in subsir inaintea elementului curent)

# Relatie de recurenta: 
# d[i][0] = max(d[i][0], d[j][0] + 1) daca t[j] < t[i] | 0 <= j < i
#           d[i][1] = j, daca se modifica d[i][1]

import random
n = int(input())
t = [random.randint(1, 20) for _ in range(n)]
print(t)

d = [[1, -1] for _ in range(n)]

for i in range(n):
    lastMax = -1
    lastElem = -1
    for j in range(i):
        if t[j] < t[i] and d[j][0] > lastMax:
            lastMax = d[j][0]
            lastElem = j

    if lastMax + 1 > d[i][0]:
        d[i][0] = lastMax + 1
        d[i][1] = lastElem

lmax, imax = 0, -1
for i in range(n):
    if d[i][0] > lmax:
        lmax = d[i][0]
        imax = i

sol = []
x = imax
while (x != -1):
    sol.append(t[x])
    x = d[x][1]

print(sol[::-1])