try:
    jumpsLength, jumpsLimit, p, jumps = map(int, input().split())
except:
    print("Numar incorect de valori / Format incorect!")
    exit()

totalDist = 0
for jump in range(0, jumps):
    if (jump % jumpsLimit == 0 and jump != 0):
        jumpsLength -= (jumpsLength * p / 100)
    totalDist += jumpsLength

print(totalDist)