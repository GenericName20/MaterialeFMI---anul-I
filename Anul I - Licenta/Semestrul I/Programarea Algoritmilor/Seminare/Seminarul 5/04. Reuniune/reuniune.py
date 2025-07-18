import os
path = os.path.dirname(__file__)
inputFileName = path + "/reuniune.in"
outputFileName = path + "/reuniune.out"

def getInput():
    intervals = []
    with open(inputFileName, "r") as f:
        for line in f.readlines():
            left, right = line.split()
            intervals.append((int(left), int(right)))

    return intervals

def sortKey(item):
    return item[0], -item[1]

def computeUnion(intervals):
    union = []
    maxLeft = intervals[0][0]
    maxRight = intervals[0][1]
    unionLength = maxRight - maxLeft

    for interval in intervals[1:]:
        if interval[1] <= maxRight:
            continue
        elif interval[0] < maxRight:
            unionLength += interval[1] - maxRight
            maxRight = interval[1]
        else:
            union.append((maxLeft, maxRight))
            maxLeft = interval[0]
            maxRight = interval[1]
            unionLength += maxRight - maxLeft

    union.append((maxLeft, maxRight))
    return unionLength, union

def writeOutput(unionLength, list):
    with open(outputFileName, "w") as g:
        g.write("Lungimea reuniunii: {}\n".format(unionLength))
        for values in list:
            g.write("{}\n".format(values))

    return

def main():
    intervals = sorted(getInput(), key=sortKey)
    unionLength, union = computeUnion(intervals)
    writeOutput(unionLength, union)
    return

if __name__ == "__main__":
    main()
    exit()