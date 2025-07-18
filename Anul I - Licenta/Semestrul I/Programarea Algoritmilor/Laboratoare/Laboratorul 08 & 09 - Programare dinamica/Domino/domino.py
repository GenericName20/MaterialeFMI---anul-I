# Programare Dinamică

def nextStep(i, j):
    if d[i][0] != d[j][1]:
        return
    if x[i] + 1 > x[j]:
        x[j] = x[i] + 1

import os
path = os.path.dirname(__file__)
path += "/domino.in"

f = open(path, "r")
n = int(f.readline())
x = [1] * n
y = [1] * n
v = [[]  for i in range(n)]

d = []
for line in f.readlines():
    d.append([int(x) for x in line.split()])
    
for i in range(n):
    for j in range(i + 1, n):
        nextStep(i, j)