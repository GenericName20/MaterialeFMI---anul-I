import os
path = os.path.dirname(__file__)
inputFileName = path + "/proiecte.in"
outputFileName = path + "/proiecte.out"

def getInput():
    projects = []
    with open(inputFileName, "r") as f:
        for line in f.readlines():
            line = line.split()
            projects.append((line[0], int(line[1]), float(line[2])))

    return projects

def sortKey(item):
    return -item[2]

def computePlan(projects, maxDay):
    plan = {day: (None, None) for day in range(1, maxDay + 1)}
    maxGain = 0

    for project in projects:
        for day in range(project[1], 0, -1):
            if plan[day] == (None, None):
                plan[day] = (project[0], project[2])
                maxGain += project[2]
                break

    # Refacem dictionarul, doar cu tuplurile care contin valori
    plan = {day: (plan[day][0], plan[day][1]) for day in plan if plan[day] != (None, None)}

    return maxGain, plan

def writeOutput(maxGain, plan):
    with open(outputFileName, "w") as g:
        for day in plan:
            #if plan[day] != (None, None):
            g.write("Ziua {}: {} {}\n".format(day, plan[day][0], plan[day][1]))
        g.write("\nProfit maxim: {}".format(maxGain))

def main():
    projects = sorted(getInput(), key=sortKey)
    maxDay = max(project[1] for project in projects)
    maxGain, plan = computePlan(projects, maxDay)
    writeOutput(maxGain, plan)

    return

if __name__ == "__main__":
    main()
    exit()