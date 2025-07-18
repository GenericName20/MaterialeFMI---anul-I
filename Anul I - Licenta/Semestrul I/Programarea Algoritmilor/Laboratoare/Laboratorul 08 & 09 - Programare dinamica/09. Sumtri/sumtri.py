# Pentru editorul de text
# import os
# path = os.path.dirname(__file__)
# inputFileName = path + "/sumtri.in"
# outputFileName = path + "/sumtri.out"

inputFileName = "sumtri.in"
outputFileName = "sumtri.out"

def readInput():
    with open(inputFileName, "r") as f:
        return int(f.readline().strip()), [[int(value) for value in line.split()] for line in f.readlines()]

def writeOutput(value):
    with open(outputFileName, "w") as g:
        g.write("{}".format(value))
    return

def main():
    n, triangle = readInput()
    d = [[0 for _ in range(i + 1)] for i in range(n)]
    for i in range(n):
        d[n - 1][i] = triangle[n - 1][i]
    
    for i in range(n - 2, -1, -1):
        for j in range(i + 1):
            d[i][j] = triangle[i][j] + max(d[i + 1][j], d[i + 1][j + 1])

    writeOutput(d[0][0])
    return
        
if __name__ == "__main__":
    main()
    exit()