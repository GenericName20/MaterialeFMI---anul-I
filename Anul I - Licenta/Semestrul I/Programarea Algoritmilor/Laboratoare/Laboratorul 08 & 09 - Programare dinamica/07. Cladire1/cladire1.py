# 80p - Vezi sursa C++

# Pentru editorul de text
# import os
# path = os.path.dirname(__file__)
# inputFileName = path + "/cladire1.in"
# outputFileName = path + "/cladire1.out"

inputFileName = "cladire1.in"
outputFileName = "cladire1.out"
MOD = 9901

def readInput():
    with open(inputFileName, "r") as f:
        n, m = map(int, f.readline().strip().split())
        blocked = [[0 for _ in range(m)] for _ in range(n)]

        k = int(f.readline().strip())
        for _ in range(k):
            x, y = map(int, f.readline().strip().split())
            blocked[x - 1][y - 1] = 1

        return n, m, blocked

def writeOutput(value):
    with open(outputFileName, "w") as g:
        g.write("{}".format(value))
    return

def main():
    n, m, blocked = readInput()

    d = [[0 for _ in range(m)] for _ in range(n)]
    d[0][0] = 1
    for i in range(1, n):
        d[i][0] = (not blocked[i][0]) * (not blocked[i - 1][0]) * d[i - 1][0]
    for j in range(1, m):
        d[0][j] = (not blocked[0][j]) * (not blocked[0][j - 1]) * d[0][j - 1]
    for i in range(1, n):
        for j in range(1, m):
            d[i][j] = ((not blocked[i][j]) *
                       (not blocked[i - 1][j]) * d[i - 1][j] +
                       (not blocked[i][j - 1]) * d[i][j - 1]) % MOD
    
    writeOutput(d[n - 1][m - 1])
    return

if __name__ == "__main__":
    main()
    exit()