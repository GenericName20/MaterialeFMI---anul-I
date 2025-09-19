import os
path = os.path.dirname(__file__)
inputFileName = path + "/lipsa.in"
outputFileName = path + "/lipsa.out"

with open(inputFileName, "r") as f:
    n = int(f.readline())
    values = [int(var) for var in f.readline().split()]

# Solutie O(n)
missing = n
for index, value in enumerate(values):
    missing = missing ^ (index + 1) ^ value

# Solutie O(n), n din citire: Calculăm n * (n + 1) - sum(values)

with open(outputFileName, "w") as g:
    g.write("{}".format(missing))