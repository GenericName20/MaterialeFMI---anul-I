import os
path = os.path.dirname(__file__)
inputFileName = path + "/operatii.in"
outputFileName = path + "/operatii.out"

f = open(inputFileName, "r")
g = open(outputFileName, "w")

score = 1
for line in f.readlines():
    try:
        x, y = line.split("*")
        y, rez = y.split("=")
        x, y, rez = int(x), int(y), int(rez)
        if (x * y == rez):
            g.write(line.strip() + " Corect\n")
            score += 1
        else:
            g.write(line.strip() + " Gresit " + str(x * y) + "\n")
    except:
        continue

g.write("Nota: " + str(score))
g.close()
f.close()