# Pentru editorul de text
# import os
# path = os.path.dirname(__file__)
# inputFileName = path + "/plopi2.in"
# outputFileName = path + "/plopi2.out"

inputFileName = "plopi2.in"
outputFileName = "plopi2.out"

with open(inputFileName, "r") as f:
    treesNumber = int(f.readline())
    treesHeights = [int(var) for var in f.readline().split()]

totalTreesCut = totalHeightCut = 0
for index in range(1, treesNumber):
    if treesHeights[index] > treesHeights[index - 1]:
        totalHeightCut += treesHeights[index] - treesHeights[index - 1]
        totalTreesCut += 1
        treesHeights[index] = treesHeights[index - 1]

with open(outputFileName, "w") as g:
    g.write("{} {}".format(totalTreesCut, totalHeightCut))