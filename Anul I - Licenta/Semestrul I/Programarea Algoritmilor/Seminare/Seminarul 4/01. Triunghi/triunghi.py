import os
path = os.path.dirname(__file__)
inputFileName = path + "/triunghi.in"
outputFileName = path + "/triunghi.out"

def getInput():
    with open(inputFileName, "r") as f:
        size = int(f.readline().strip())

    return size


def getMatrix(size):
    matrix = [[i + 1] + [0] * i for i in range(size - 1)] + [[i for i in range(size, 0, -1)]]

    for i in range(size - 2, -1, -1):
        for j in range(1, i + 1):
            matrix[i][j] = matrix[i + 1][j] + matrix[i][j - 1] + matrix[i + 1][j - 1]
    
    return matrix


def printMatrix(matrix):
    tab = max([len(str(value)) for line in matrix for value in line])
    # Stim cum se formeaza matricea si unde ajung cele mai mari valori, deci putem si
    # sa calculam unde se vor pozitiona aceste valori

    with open(outputFileName, "w") as g:
        for line in matrix:
            for value in line:
                g.write("{} ".format(str(value).rjust(tab)))
            g.write("\n")

    return


def main():
    size = getInput()
    triangle = getMatrix(size)
    printMatrix(triangle)
    return


if __name__ == "__main__":
    main()
    print("Output written in {}\n".format(outputFileName))
    exit()