# Minciunescu Vlad-Andrei - 151

# import os
# path = os.path.dirname(__file__)
# inputFileName = path + "/numere.in"
# outputFileName = path + "/numere.out"

inputFileName = "numere.in"
outputFileName = "numere.out"

def citire_numere():
    with open(inputFileName, "r") as f:
        return [[int(value) for value in line.split()] for line in f.readlines()]

def insereaza_zerouri(M, x):
    size = len(M)
    for i in range(size):
        p = size
        j = size - 1
        while j >= 0:
            if M[i][j] % (i + x) == 0:
                M[i].insert(j + 1, 0)
                p += 1
            j -= 1

    i = size - 1
    while i >= 0:
        z = 0
        for j in range(len(M[i])):
            if M[i][j] == 0:
                z += 1
        if len(M[i]) - z == z:
            del M[i]
        i -= 1

def main():
    # Subtask A
    M = citire_numere()

    # Subtask B
    k = int(input().strip())
    ans = []
    for line in M:
        for value in line:
            ap = 0
            for list in M:
                if value in list:
                    ap += 1

            if ap >= k:
                ans.append(value)

    ans = sorted(set(ans), reverse=True)
    with open(outputFileName, "w") as g:
        g.write("Imposibil!" if len(ans) == 0 else "\n".join([str(value) for value in ans]))

    # Subtask C, D
    insereaza_zerouri(M, 2)
    for line in M:
        print(*line)

if __name__ == "__main__":
    main()
    exit(0)