# Pentru editorul de text
# import os
# path = os.path.dirname(__file__)
# inputFileName = path + "/matrice.in"

inputFileName = "matrice.in"

def citire_matrice(inputFileName):
    with open(inputFileName, "r") as f:
        size = int(f.readline().strip())
        values = [int(var) for var in f.readline().split()]
        matrix = [[values[i * size + j] for j in range(size)] for i in range(size)]
    
    return matrix

def duplicare(matrix, *indexes):
    for index in sorted(indexes, reverse=True):
        matrix.insert(index + 1, [value for value in matrix[index]])

def setOutput(matrix):
    for line in matrix:
        print("{}".format(" ".join([str(value) for value in line])))

def main():
    matrix = citire_matrice(inputFileName)
    duplicare(matrix, 0, 1)
    matrix[0][0] += 1
    setOutput(matrix)
    return

if __name__ == "__main__":
    main()
    exit()