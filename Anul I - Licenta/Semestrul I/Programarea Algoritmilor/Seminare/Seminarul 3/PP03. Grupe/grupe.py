import os
path = os.path.dirname(__file__)
inputFileName = path + "/grupe.in"
outputFileName = path + "/grupe.out"

def getInput():
    with open(inputFileName, "r") as f:
        fullText = ""
        for line in f.readlines():
            fullText += " " + line.strip()
        
        import string
        for symbol in string.punctuation:
            fullText = fullText.replace(symbol, "")

    return fullText.strip().lower()

def setGroups(fullText):

    words = sorted(set([word for word in fullText.split()]), key=lambda item: (-len(item), item))

    groups = {}
    for word in words:
        if len(word) not in groups:
            groups[len(word)] = [word]
        else:
            groups[len(word)] += [word]

    return groups

def writeFile(groups):
    with open(outputFileName, "w") as g:
        for length in groups:
            g.write("Lungime {}: {}\n".format(length, ", ".join(groups[length])))

    return

def main():
    fullText = getInput()
    groups = setGroups(fullText)
    writeFile(groups)
    return

if __name__ == "__main__":
    main()
    exit()