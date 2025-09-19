import os
path = os.path.dirname(__file__)
inputFileName = path + "/definitii.in"
outputFileName = path + "/definitii.out"

f = open(inputFileName, "r")

fullText = ""
for line in f.readlines():
    fullText += line
f.close()

sentences = fullText.split("\\n")
sentences.remove(sentences[-1])
targetWords = []

import string
for sentence in sentences:
    for pct in string.punctuation:
        if (pct != "~"):
            sentence = sentence.replace(pct, "").strip()

    words = [word for word in sentence.split()]
    referenceWord = words[0]
    wordExpressiveness = 0

    for word in words[1:]:
        if (word == referenceWord or word == "~"):
            wordExpressiveness += 1
    
    targetWords.append((referenceWord, wordExpressiveness))

g = open(outputFileName, "w")
g.write("Cuvintele cautate sunt: {}".format(targetWords))
g.close()