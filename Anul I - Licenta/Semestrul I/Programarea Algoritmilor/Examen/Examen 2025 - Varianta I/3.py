import os
filename = os.path.dirname(__file__) + "/3.in"

with open(filename, "r") as f:
    l, k = [int(value) for value in f.readline().split()]
    lungime = [0] + [int(value) for value in f.readline().split()]
    cost = [0] + [int(value) for value in f.readline().split()]

cmax = [0] * (l + 1)
prec = [-1] * (l + 1)

for i in range(1, l + 1):
    for j in range(1, k + 1):
        if lungime[j] <= i and cmax[i - lungime[j]] + cost[j] > cmax[i]:
            cmax[i] = cmax[i - lungime[j]] + cost[j]
            prec[i] = lungime[j] # prec[i] = j

if cmax[l] == 0:
    print("Imposibil")
else:
    i = l
    print(cmax[i])
    while i > 0:
        print(prec[i], end=" ") # print(lungime[i])
        i = i - prec[i] # i = prec[i]