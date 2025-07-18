# Pentru editorul de text
# import os
# path = os.path.dirname(__file__)
# inputFileName = path + "/reactivi.in"
# outputFileName = path + "/reactivi.out"

inputFileName = "reactivi.in"
outputFileName = "reactivi.out"

with open(inputFileName, "r") as f:
    refrigeratorsNumber = int(f.readline().strip())
    temperatures = []
    for line in f.readlines():
        x, y = line.split()
        temperatures.append((int(x), int(y)))

temperatures = sorted(temperatures, key=lambda item: (item[1], item[0]))

neededRefrigerators = index = 1
last = 0
while index < refrigeratorsNumber:
    if temperatures[index][0] > temperatures[last][1]:
        last = index
        neededRefrigerators += 1
    else:
        temperatures[last] = (max(temperatures[index][0], temperatures[last][0]), min(temperatures[index][1], temperatures[last][1]))

    index += 1

with open(outputFileName, "w") as g:
    g.write("{}".format(neededRefrigerators))