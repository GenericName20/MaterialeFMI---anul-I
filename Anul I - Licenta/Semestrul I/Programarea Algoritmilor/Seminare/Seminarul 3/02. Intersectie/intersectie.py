import os
path = os.path.dirname(__file__)
inputFileName = path + "/intersectie.in"
outputFileName = path + "/intersectie.out"

# O(nrLinii * O(lenMaxLinie) din split())
with open(inputFileName, "r") as f:
    intersection = set([int(var) for var in f.readline().split()])
    for line in f.readlines():
        collection = set([int(var) for var in line.split()])
        intersection &= collection
        if len(intersection) == 0:
            break

with open(outputFileName, "w") as g:
    g.write("{}".format(intersection if len(intersection) > 0 else "Intersectie vida!"))