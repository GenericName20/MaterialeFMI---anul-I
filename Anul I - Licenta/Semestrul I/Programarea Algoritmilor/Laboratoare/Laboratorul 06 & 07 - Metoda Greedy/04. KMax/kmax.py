# Pentru editorul de text
# import os
# path = os.path.dirname(__file__)
# inputFileName = path + "/kmax.in"
# outputFileName = path + "/kmax.out"

# with open(inputFileName, "r") as f:
#     numbersCount = int(f.readline())
#     numbers = sorted([int(var) for var in f.readline().split()])
#     changedSignCount = int(f.readline())

numbersCount = int(input().strip())
numbers = sorted([int(var) for var in input().strip().split()])
changedSignCount = int(input().strip())

maxSum = sum(numbers[changedSignCount:] + [-number for number in numbers[:changedSignCount]])
print(maxSum)

# with open(outputFileName, "w") as g:
#     g.write(str(maxSum))