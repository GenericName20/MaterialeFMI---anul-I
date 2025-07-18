import os
path = os.path.dirname(__file__)
inputFileName = path + "/cuvinte.in"
outputFileName = path + "/cuvinte.out"

def citire_cuvinte(fileName):
    with open(fileName, "r") as f:
        sizec = int(f.readline().strip())
        words = f.readlines()
        totalSize = len(words)
        M = [[] for _ in range(sizec)]
        for i in range(totalSize):
            M[i % sizec].append(words[i].strip())

    return M

def prelucrare_cuvinte(L, w, x):
    n = len(L)
    for i in range(n):
        m = len(L[i])
        for j in range(m):
            L[i][j] = L[i][j][:-len(w)] + x if L[i][j].endswith(w) else L[i][j]

    i = n - 1
    while i >= 0:
        for j in range(m):
            if L[i][j] == L[i][j][::-1]:
                L[i] = []
                break
        if L[i] == []:
            L.remove([])
        else:
            i -= 1
    
def main():
    # Cerinta A)
    cuvinte = citire_cuvinte(inputFileName)

    # Cerinta D)
    w = input().strip()
    l = len(w)
    ans = sorted(set([word for line in cuvinte for word in line if len(word) <= l]))
    with open(outputFileName, "w") as g:
        g.write("Imposibil!" if len(ans) == 0 else "\n".join(ans))

    # Cerinta B)
    prelucrare_cuvinte(cuvinte, "re", "u")

    # Cerinta C)
    for line in cuvinte:
        print(*line)

if __name__ == "__main__":
    main()
    exit(0)