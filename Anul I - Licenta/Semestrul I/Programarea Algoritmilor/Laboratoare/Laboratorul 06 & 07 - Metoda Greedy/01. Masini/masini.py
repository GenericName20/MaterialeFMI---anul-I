# Pentru editorul de text
# import os
# path = os.path.dirname(__file__)
# inputFileName = path + "/masini.in"
# outputFileName = path + "/masini.out"

# Pentru PBInfo
inputFileName = "masini.in"
outputFileName = "masini.out"

with open(inputFileName, "r") as f:
    carCount, totalTime = [int(var) for var in f.readline().split()]
    times = sorted([int(var) for var in f.readline().split()])


currTimeIndex = timeSpent = 0

while currTimeIndex < carCount and timeSpent + times[currTimeIndex] <= totalTime:
    timeSpent += times[currTimeIndex]
    currTimeIndex += 1

with open(outputFileName, "w") as g:
    g.write(str(currTimeIndex))