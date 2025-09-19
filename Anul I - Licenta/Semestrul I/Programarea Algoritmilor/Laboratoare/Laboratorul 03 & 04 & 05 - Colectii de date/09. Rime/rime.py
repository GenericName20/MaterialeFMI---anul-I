import os
path = os.path.dirname(__file__)
inputFileName = path + "/rime.in"
outputFileName = path + "/rime.out"

f = open(inputFileName, "r")

fullText = ""
for line in f.readlines():
    fullText += " " + line.strip()
f.close()

import string
for symbol in string.punctuation:
    fullText = fullText.replace(symbol, "")

rhymes = {}
words = set([word.lower() for word in fullText.split()])
words = sorted(words)

for i in range(0, len(words)):
    for j in range(i + 1, len(words)):
        firstWord, secondWord = words[i], words[j]
        if (len(firstWord) > 2 and len(secondWord) > 2 and firstWord[-3:] == secondWord[-3:]):
            if (firstWord[-3:]) not in rhymes:
                rhymes[firstWord[-3:]] = [(firstWord, secondWord)]
            else:
                rhymes[firstWord[-3:]].append((firstWord, secondWord))

g = open(outputFileName, "w")
for group in rhymes:
        g.write("Cuvinte se termina cu grupul \"{}\": {}\n".format(group, rhymes[group]))
g.close()