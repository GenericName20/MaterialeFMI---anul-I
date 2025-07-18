import os
path = os.path.dirname(__file__)
inputFileName = path + "/matrice.in"
outputFileName = path + "/matrice.out"

def getInput():
    with open(inputFileName, "r") as f:
        row = f.readline().strip().split()
        return int(row[0]), int(row[1]), int(row[2])

def genMatrix(rows, columns):
    matrix = [[0 for row in range(0, columns)] for col in range(0, rows)]
    
    import random
    for row in range(rows):
        for col in range(columns):
            matrix[row][col] = max(matrix[row][col - 1], matrix[row - 1][col]) + random.randint(1, 20)

    return matrix

def findValue1(value, matrix, rows, columns):
    for row in range(rows):
        for col in range(columns):
            if value == matrix[row][col]:
                return (row, col)
    return None

def findValue2(value, matrix, rows, columns):
    for row in range(rows):
        left = 0
        right = columns - 1
        while left <= right:
            middle = left + (right - left) // 2
            if matrix[row][middle] == value:
                return (row, middle)
            elif matrix[row][middle] < value:
                left = middle + 1
            else:
                right = middle - 1
    return None

def findValue3(value, matrix, rows, columns):
    row, col = 0, columns - 1
    while row < rows and col >= 0:
        if matrix[row][col] == value:
            return (row, col)
        elif matrix[row][col] > value:
            col -= 1
        else:
            row += 1
            
    return None

def writeOutput(matrix, value, answers):
    tab = len(str(matrix[-1][-1]))
    with open(outputFileName, "w") as g:
        g.write("Se cauta valoarea {} in matricea generata:\n".format(value))
        for row in matrix:
            g.write("{}\n".format(" ".join(([str(value).rjust(tab) for value in row]))))
        g.write("\n")

        for index, answer in enumerate(answers):
            g.write("Metoda {}: {}\n".format(index, answer))
    
    return

def main():
    rows, columns, value = getInput()
    matrix = genMatrix(rows, columns)
    ans1 = findValue1(value, matrix, rows, columns) # O(m * n)
    ans2 = findValue2(value, matrix, rows, columns) # O(m * log2n)
    ans3 = findValue3(value, matrix, rows, columns) # O(m + n)
    writeOutput(matrix, value, [ans1] + [ans2] + [ans3])
    return

if __name__ == "__main__":
    main()
    exit()