n = int(input().strip())

# Task A
matrix = [[x * (n - 1) + y for y in range(x + 1, n + x + 1)] for x in range(0, n)]

print("Task A:")
for line in matrix:
    print(line)

# Task B
topRow, leftCol, botRow, rightCol, pozitions = 0, 0, n - 1, n - 1, []

while (topRow <= botRow and leftCol <= rightCol):
    pozitions += [(topRow, x) for x in range(leftCol, rightCol + 1)]
    topRow += 1
    pozitions += [(x, rightCol) for x in range(topRow, botRow + 1)]
    rightCol -= 1
    pozitions += [(botRow, x) for x in range(rightCol, leftCol - 1, -1)]
    botRow -= 1
    pozitions += [(x, leftCol) for x in range(botRow, topRow - 1, -1)]
    leftCol += 1

print("\nTask B: {}".format(pozitions))

# Task C
spiral = []
for pozition in pozitions:
    spiral.append(matrix[pozition[0]][pozition[1]])

print("\nTask C: {}".format(spiral))