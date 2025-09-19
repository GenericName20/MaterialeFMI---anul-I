# Pentru editorul de text
# import os
# path = os.path.dirname(__file__)
# inputFileName = path + "/partitieab1.in"
# outputFileName = path + "/partitieab1.out"

# with open(inputFileName, "r") as f:
#     n, a, b = [int(var) for var in f.readline().split()]

n, a, b = [int(var) for var in input().split()]
sum = []

while (n % b != 0):
    n -= a
    sum.append(a)

sum += [b] * (n // b)

for number in sum:
    print("{} ".format(number), end="")

# with open(outputFileName, "w") as g:
#     for number in sum:
#         g.write("{} ".format(number))
