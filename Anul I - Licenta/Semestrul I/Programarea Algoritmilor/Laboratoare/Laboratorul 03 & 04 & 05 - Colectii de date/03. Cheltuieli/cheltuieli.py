import os
path = os.path.dirname(__file__)
inputNameFile = path + "/cheltuieli.in"
outputNameFile = path + "/cheltuieli.out"

f = open(inputNameFile, "r")
sentence = f.readline().split()
f.close()
values = [sentence[i] for i in range(len(sentence) - 1) if sentence[i + 1] == "RON"]

totalSpent = 0
for value in values:
    try:
        totalSpent += float(value)
    except:
        continue

g = open(outputNameFile, "w")
g.write(str(totalSpent))
g.close()