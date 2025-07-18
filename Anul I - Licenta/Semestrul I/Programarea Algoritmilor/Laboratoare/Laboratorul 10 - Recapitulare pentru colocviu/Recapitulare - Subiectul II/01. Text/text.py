# Pentru editorul de text
# import os
# path = os.path.dirname(__file__)
# inputFileName = path + "/text.in"
# outputFileName = path + "/text.out"

inputFileName = "text.in"
outputFileName = "text.out"

def getInput():
    with open(inputFileName, "r") as f:
        referenceWord = f.readline().strip()
        words = []
        fullText = ""
        for line in f.readlines():
            fullText += " " + line.strip()

        for word in fullText.split():
            import string
            while word[-1] in string.punctuation:
                word = word[:-1]
            while word[0] in string.punctuation:
                word = word[1:]

            words += [word.lower()]

    return referenceWord, sorted(set(words), key=lambda item: -len(item))

def computeGroups(referenceWord, words):
    groups = {}
    referenceLetters = set(referenceWord)
    
    for word in words:
         letters = set([letter for letter in word if letter.isalpha()])
         if letters & referenceLetters == letters:
             letters = "[{}]".format(",".join(sorted("'" + letter + "'" for letter in letters)))
             if letters not in groups:
                 groups[letters] = [word]
             else:
                 groups[letters].append(word)
    
    return dict(sorted(groups.items()))

def setOutput(groups):
    with open(outputFileName, "w") as g:
        if len(groups) == 0:
            g.write("Imposibil")
        else:
            for group in groups:
                g.write("Literele {}:\n".format(group))
                for word in groups[group]:
                    g.write("{}\n".format(word))
    return

def main():
    referenceWord, words = getInput()
    groups = computeGroups(referenceWord, words)
    setOutput(groups)
    return

if __name__ == "__main__":
    main()
    exit()