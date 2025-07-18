import os
path = os.path.dirname(__file__)
inputFileName = path + "/autostrada.in"
outputFileName = path + "/autostrada.out"

def getInput():
    reports = []
    with open(inputFileName, "r") as f:
        roadLength = int(f.readline().strip())
        for line in f.readlines():
            x, y = line.split()
            reports.append((int(x), int(y)))

    return roadLength, reports

def computeRoadStats(roadLength, reports):
    safeAreas = []
    damagedAreas = []

    lastSafeArea = 0
    maxLeft = reports[0][0]
    maxRight = reports[0][1]
    damageLength = maxRight - maxLeft

    for report in reports[1:]:
        if report[1] <= maxRight:
            continue
        elif report[0] < maxRight:
            damageLength += report[1] - maxRight
            maxRight = report[1]
        else:
            if lastSafeArea < maxLeft:
                safeAreas.append((lastSafeArea, maxLeft))
            damagedAreas.append([maxLeft, maxRight])

            lastSafeArea = maxRight
            maxLeft = report[0]
            maxRight = report[1]
            damageLength += maxRight - maxLeft

    damagedAreas.append([maxLeft, maxRight])
    if lastSafeArea < maxLeft:
        safeAreas.append((lastSafeArea, maxLeft))
    if maxRight < roadLength:
        safeAreas.append((maxRight, roadLength))
    damageRate = (damageLength * 100) // roadLength

    return damagedAreas, safeAreas, damageRate

def writeOutput(roadLength, damagedAreas, safeAreas, damageRate):
    with open(outputFileName, "w") as g:
        for area in damagedAreas:
            g.write("{}\n".format(area))
        g.write("\n")
        for area in safeAreas:
            g.write("{}\n".format(area))

        g.write("\n{}%".format(damageRate))

def sortKey(item):
    return item[0], -item[1]

def main():
    roadLength, reports = getInput()
    reports = sorted(reports, key=sortKey)
    damagedAreas, safeAreas, damageRate = computeRoadStats(roadLength, reports)
    writeOutput(roadLength, damagedAreas, safeAreas, damageRate)
    return

if __name__ == "__main__":
    main()
    exit()