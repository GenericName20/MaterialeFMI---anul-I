# Pentru editorul de text
# import os
# path = os.path.dirname(__file__)
# inputFileName = path + "/partitie.in"
# outputFileName = path + "/partitie.out"

# with open(inputFileName, "r") as f:
#     n, a, b = [int(var) for var in f.readline().split()]

n, a, b = [int(var) for var in input().strip().split()]
sum = []

while (n % a != 0):
    n -= b
    sum.append(b)

sum += [a] * (n // a)

for number in sum[::-1]:
    print("{}".format(number), end=" ")

# with open(outputFileName, "w") as g:
#     for number in sum[len(sum)::-1]:
#         g.write("{} ".format(number))