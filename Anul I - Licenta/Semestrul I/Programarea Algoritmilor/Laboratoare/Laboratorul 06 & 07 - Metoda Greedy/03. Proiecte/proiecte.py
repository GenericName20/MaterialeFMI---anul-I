# Pentru editorul de text
# import os
# path = os.path.dirname(__file__)
# inputFileName = path + "/proiecte.in"
# outputFileName = path + "/proiecte.out"

# Pentru PBInfo
inputFileName = "proiecte.in"
outputFileName = "proiecte.out"

with open(inputFileName, "r") as f:
    projectsCount = int(f.readline())
    projectsTimes = sorted([(int(var), index + 1) for index, var in enumerate(f.readline().split())])

with open(outputFileName, "w") as g:
    for project in projectsTimes:
        g.write("{} ".format(project[1]))
