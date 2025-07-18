# Pentru editorul de text
import os
path = os.path.dirname(__file__)
inputFileName = path + "/pacman_xi.in"
outputFileName = path + "/pacman_xi.out"

# inputFileName = "pacman_xi.in"
# outputFileName = "pacman_xi.out"

def readInput():
    with open(inputFileName, "r") as f:
        return map(int, f.readline().strip().split())

def writeOutput(value):
    with open(outputFileName, "w") as g:
        g.write("{}".format(value))
    return

def main():
    n, m = readInput()
    d = [[0 for _ in range(m)] for _ in range(n)]
    
    for i in range(m):
        d[0][i] = 1

    for i in range(1, n):
        for j in range(1, m):
            d[i][j] = d[i][j - 1] + d[i - 1][j - 1]

    for line in d:
        print(line)

    writeOutput(d[n - 1][m - 1])
    return

if __name__ == "__main__":
    main()
    exit()