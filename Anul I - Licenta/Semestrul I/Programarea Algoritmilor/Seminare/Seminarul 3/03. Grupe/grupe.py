import os
path = os.path.dirname(__file__)
inputFileName = path + "/grupe.in"
outputFileName = path + "/grupe.out"

fullText = ""
with open(inputFileName, "r") as f:
    for line in f.readlines():
        fullText += " " + line

import string
for symbol in string.punctuation:
    fullText = fullText.replace(symbol, "")
fullText = fullText.lower()

groups = {}
for word in fullText.split():
    group = "".join(sorted(set(word)))
    if group not in groups:
        groups[group] = [word]
    else:
        groups[group].append(word)

groups = dict(sorted(groups.items(), key=lambda item: (-len(item[0]), item[0])))

with open(outputFileName, "w") as g:
    for group in groups:
        groups[group] = sorted(set(groups[group]))
        g.write("Literele {}: {}".format(group, groups[group][0]))
        for i in range(1, len(groups[group])):
            g.write(", {}".format(groups[group][i]))
        g.write("\n")