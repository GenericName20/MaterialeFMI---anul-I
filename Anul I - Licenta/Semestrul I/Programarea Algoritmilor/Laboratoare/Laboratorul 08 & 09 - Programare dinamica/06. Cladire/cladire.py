# 80p - Vezi sursa C++

# Pentru editorul de text
# import os
# path = os.path.dirname(__file__)
# inputFileName = path + "/cladire.in"
# outputFileName = path + "/cladire.out"

inputFileName = "cladire.in"
outputFileName = "cladire.out"
MOD = 9901

def readInput():
    with open(inputFileName, "r") as f:
        return map(int, f.readline().strip().split())

def writeOutput(answer):
    with open(outputFileName, "w") as g:
        g.write("{}".format(answer))

def main():
    n, m = readInput()
    d = [[0 for _ in range(m)] for _ in range(n)]
    
    for j in range(m):
        d[0][j] = 1

    for i in range(n):
        d[i][0] = 1

    for i in range(1, n):
        for j in range(1, m):
            d[i][j] = (d[i][j - 1] + d[i - 1][j]) % MOD

    writeOutput(d[n - 1][m - 1])
    return

if __name__ == "__main__":
    main()
    exit()