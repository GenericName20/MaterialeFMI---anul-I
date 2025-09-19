import os
path = os.path.dirname(__file__)
inputFileName = path + "/dinamica.in"
outputFileName = path + "/dinamica.out"

def readInput():
    with open(inputFileName, "r") as f:
        return int(f.readline().strip()), [[int(value) for value in line.split()] for line in f.readlines()]

def writeOutput(ans):
    with open(outputFileName, "w") as g:
        g.write("Gradul de oboseala maxim {}\n".format(ans["gmax"]))
        for route in ans["route"][::-1]:
            g.write("{} {}\n".format(route[0], route[1]))

def main():
    size, matrix = readInput()
    
    d = [matrix[0]] + [[0 for _ in range(size)] for _ in range(size - 1)]

    for i in range(1, size):
        for j in range(size):
            if (matrix[i][j] == -1):
                d[i][j] = -1
            else:
                omax = d[i - 1][j] if d[i - 1][j] != -1 else 0
                if (j > 0 and omax < d[i - 1][j - 1] and d[i - 1][j - 1] != -1):
                    omax = d[i - 1][j - 1]
                if (j < size - 1 and omax < d[i - 1][j + 1] and d[i - 1][j + 1] != -1):
                    omax = d[i - 1][j + 1]

                d[i][j] = 0 if not omax else matrix[i][j] + omax

    vmax, cmax = -1, ()
    for i in range(1, size):
        for j in range(size):
            if (d[i][j] == -1):
                v = max(d[i - 1][j - 1] if j > 0 else 0, d[i - 1][j], d[i - 1][j + 1] if j < size - 1 else 0)
                if v > vmax:
                    vmax, cmax = v, (i, j)

    ans = {"gmax": vmax, "route":[]}
    i, j = cmax[0], cmax[1] # Final
    ans["route"].append((i + 1, j + 1))

    while (i > 0):
        v, movi, movj = d[i - 1][j] if d[i - 1][j] != -1 else 0, -1, 0
        if (j > 0 and v < d[i - 1][j - 1] and d[i - 1][j - 1] != -1):
            v, movj = d[i - 1][j - 1], -1
        if (j < size - 1 and v < d[i - 1][j + 1] and d[i - 1][j + 1] != -1):
            v, movj = d[i - 1][j + 1], 1
        
        i, j = i + movi, j + movj
        ans["route"].append((i + 1, j + 1))

    writeOutput(ans)

if __name__ == "__main__":
    main()
    exit(0)