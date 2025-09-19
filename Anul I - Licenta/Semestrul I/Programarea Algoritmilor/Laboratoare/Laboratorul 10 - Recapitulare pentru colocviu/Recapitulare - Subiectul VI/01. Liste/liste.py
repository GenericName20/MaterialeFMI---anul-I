# import os
# path = os.path.dirname(__file__)
# inputFileName = path + "/liste.in"
# outputFileName = path + "/multipli.out"

inputFileName = "liste.in"
outputFileName = "multipli.out"

def citire_liste(fileName):
    L, s = [], 0
    with open(fileName, "r") as f:
        size = int(f.readline())
        for line in f.readlines():
            nr, k = line.split()
            k = int(k)
            s += k
            for _ in range(k):
                L.append(int(nr))

    p = 0
    R = [[[] for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            if p < s:
                R[i][j] = L[p]
                p += 1
            else:
                R[i][j] = 0

    return R

def prelucrare_liste(L, x):
    size = len(L)
    if x < size:
        for i in range(size):
            L[i] = L[i][:x] + L[i][x + 1:]
        sizec = size - 1
        
    i = size - 1
    while i >= 0:
        for j in range(sizec):
            dlt = True
            k = 0
            
            while k < sizec:
                if L[i][k] != L[i][j]:
                    dlt = False
                    break
                k += 1
            
            if dlt:
                break

        if dlt:
            del L[i]
        else:
            i-=1

def main():
    # Subtask A
    L = citire_liste(inputFileName)

    # Subtask D
    k = int(input().strip())
    ans = sorted(set([value for line in L for value in line if value % k == 0 and value % (k ** 2) != 0]), reverse=True)
    with open(outputFileName, "w") as g:
        g.write("Imposibil!" if len(ans) == 0 else "\n".join([str(value) for value in ans]))

    # Subtask B, C
    prelucrare_liste(L, 2)
    for line in L:
        print(*line)

    exit()

if __name__ == "__main__":
    main()
    exit(0)