# Pentru editorul de text
# import os
# path = os.path.dirname(__file__)
# inputFileName = path + "/matrice.in"
# outputFileName = path + "/matrice.out"

inputFileName = "matrice.in"
outputFileName = "matrice.out"

def getInput():
    matrix = []
    with open(inputFileName, "r") as f:
        for line in f.readlines():
            matrix += [[int(var) for var in line.split()]]
    return matrix

def minSum(matrix):
    
    for i in range(len(matrix)):
        max1 = max2 = -1000000000
        for j in range(len(matrix[i])):
            if matrix[i][j] > max1:
                max2 = max1
                max1 = matrix[i][j]
            elif matrix[i][j] > max2:
                max2 = matrix[i][j]
        matrix[i].remove(max1)
        matrix[i].remove(max2)

    return matrix

def writeOutput(matrix):
    with open(outputFileName, "w") as g:
        # Afisare cu indent
        tab = len(str(max([value for line in matrix for value in line])))
        for line in matrix:
            g.write("{}\n".format(" ".join([str(value).rjust(tab) for value in line])))

        # Afisare fara indent
        # for line in matrix:
        #     for value in line:
        #         g.write("{} ".format(value))
        #     g.write("\n")
        
    return

def main():
    matrix = getInput()
    newMatrix = minSum(matrix)
    writeOutput(newMatrix)

    return

if __name__ == "__main__":
    main()
    exit()