# Pentru editorul de text
# import os
# path = os.path.dirname(__file__)
# inputFileName = path + "/matrice.in"

inputFileName = "matrice.in"

def citire_matrice(inputFileName):
    with open(inputFileName, "r") as f:
        n = int(f.readline().strip())
        values = [int(var) for var in f.readline().split()]

        matrix = []
        for i in range(n):
            matrix.append([values[i * n + j] for j in range(n)])
    
    return matrix

def duplicare(matrix, *indexes):
    indexes = sorted(indexes, key=lambda item: -item)
    for index in indexes:
        matrix.insert(index + 1, [value for value in matrix[index]])

    return

def setOutput(matrix):
    for line in matrix:
        print("{}".format(" ".join([str(value) for value in line])))
    
    return

def main():
    matrix = citire_matrice(inputFileName)
    duplicare(matrix, 0, 1)
    matrix[0][0] += 1
    setOutput(matrix)
    return

if __name__ == "__main__":
    main()
    exit()