import os
path = os.path.dirname(__file__)
inputFileName = path + "/matrice.in"
outputFileName = path + "/matrice.out"

def getInput():
    with open(inputFileName, "r") as f: 
        return int(f.readline().strip())

def genMatrix(size):
    matrix = [[0] * (size - 1) + [1] for i in range(size - 1)] + [[1] * size]

    for i in range(size - 2, -1, -1):
        for j in range(size - 2, -1, -1):
            matrix[i][j] = matrix[i + 1][j] + matrix[i][j + 1]

    return matrix


def printMatrix(matrix):
    with open(outputFileName, "w") as g:
        tab = len(str(matrix[0][0]))
        for line in matrix:
            for value in line:
                g.write("{} ".format(str(value).rjust(tab)))
            g.write("\n")


def main():
    size = getInput()
    matrix = genMatrix(size)
    printMatrix(matrix)
    
    return


if __name__ == "__main__":
    main()
    exit()