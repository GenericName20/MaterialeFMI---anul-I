import os
path = os.path.dirname(__file__)
inputFileName = path + "/acoperire.in"
outputFileName = path + "/acoperire.out"

def getInput():
    intervals = []
    with open(inputFileName, "r") as f:
        for line in f.readlines():
            left, right = line.split()
            intervals.append((int(left), int(right)))

    return intervals

def computeCoveringSet(intervals):
    coveringSet = [intervals[0][1]]
    for interval in intervals[1:]:
        if interval[0] > coveringSet[-1]:
            coveringSet.append(interval[1])

    return coveringSet

def writeOutput(list):
    with open(outputFileName, "w") as g:
        for values in list:
            g.write("{}\n".format(values))

    return

def main():
    intervals = sorted(getInput(), key=lambda item: item[1])
    coveringSet = computeCoveringSet(intervals)
    writeOutput(coveringSet)
    return

if __name__ == "__main__":
    main()
    exit()