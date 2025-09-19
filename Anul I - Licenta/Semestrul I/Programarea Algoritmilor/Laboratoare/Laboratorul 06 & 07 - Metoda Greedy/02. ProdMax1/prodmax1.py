# Pentru editorul de text
# import os
# path = os.path.dirname(__file__)
# inputFileName = path + "/prodmax1.in"
# outputFileName = path + "/prodmax1.out"

# with open(inputFileName, "r") as f:
#     numberCount = int(f.readline())
#     numbers = sorted([int(var) for var in f.readline().split()])

numbersCount = int(input().strip())
numbers = sorted([int(var) for var in input().split()])

answer = max(numbers[0] * numbers[1], numbers[-1] * numbers[-2])
print(answer)

# with open(outputFileName, "w") as g:
#     g.write(str(answer))