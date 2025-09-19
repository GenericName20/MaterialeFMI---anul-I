# Pentru editorul de text
# import os
# path = os.path.dirname(__file__)
# inputFileName = path + "/matrice.in"
# outputFileName = path + "/matrice.out"

inputFileName = "matrice.in"
outputFileName = "matrice.out"

def citire_matrice():
    with open(inputFileName, "r") as f:
        return [[int(var) for var in line.split()] for line in f.readlines()]

def borderMatrix(matrix):
    for index, line in enumerate(matrix):
        matrix[index].append(sum(line))
   
    matrixSize = len(matrix) + 1
    matrix.append([0] * matrixSize)
    for j in range(matrixSize):
        matrix[matrixSize - 1][j] = sum([matrix[i][j] for i in range(0, matrixSize - 1)])

    return matrix

def traverseMatrix(matrix):
    n = len(matrix) - 1
    values = [matrix[i][i] for i in range(n + 1)] + [matrix[i][n - i] for i in range(n + 1)]
    values += [matrix[i][j] for i in range(n + 1) for j in range(n + 1) if i != j and i + j != n]

    return values

def setOutput(values):
    with open(outputFileName, "w") as g:
        g.write("{}".format(" ".join([str(value) for value in values])))
    
    return

def main():
    matrix = citire_matrice()
    matrix = borderMatrix(matrix)
    values = traverseMatrix(matrix)
    setOutput(values)

    return

if __name__ == "__main__":
    main()
    exit()