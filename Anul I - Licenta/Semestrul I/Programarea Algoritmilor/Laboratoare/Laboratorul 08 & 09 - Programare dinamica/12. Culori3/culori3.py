# Pentru editorul de text
# import os
# path = os.path.dirname(__file__)
# inputFileName = path + "/culori3.in"
# outputFileName = path + "/culori3.out"

# Albastru = 0, Alb = 1, Rosu = 2, Verde = 3, Galben = 4
inputFileName = "culori3.in"
outputFileName = "culori3.out"

def readInput():
    with open(inputFileName, "r") as f:
        return int(f.readline().strip())
    
def writeOutput(value):
    with open(outputFileName, "w") as g:
        g.write("{}".format(value))
    return

def main():
    n = readInput()
    d = [[0 for _ in range(5)] for _ in range(n)]

    for i in range(5):
        d[0][i] = 1

    for i in range(1, n):
        d[i][0] = d[i - 1][1] + d[i - 1][2]
        d[i][1] = d[i - 1][0]
        d[i][2] = d[i - 1][0] + d[i - 1][3]
        d[i][3] = d[i - 1][2] + d[i - 1][4]
        d[i][4] = d[i - 1][3]
    
    writeOutput(sum(d[n - 1]))

if __name__ == "__main__":
    main()
    exit()