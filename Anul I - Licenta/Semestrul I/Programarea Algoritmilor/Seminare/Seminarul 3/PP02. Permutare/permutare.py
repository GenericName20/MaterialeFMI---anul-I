import os
path = os.path.dirname(__file__)
inputFileName = path + "/permutare.in"
outputFileName = path + "/permutare.out"

def getInput():
    with open(inputFileName, "r") as f:
        firstWord = f.readline().strip().lower()
        secondWord = f.readline().strip().lower()

    return firstWord, secondWord

def anagram(firstWord, secondWord):

    if sorted(firstWord) != sorted(secondWord):
        return False
    
    letters = {firstWord: {}, secondWord: {}}

    for i in range(len(firstWord)):
        if firstWord[i] not in letters[firstWord]:
            letters[firstWord][firstWord[i]] = [1, [i + 1]]
        else:
            letters[firstWord][firstWord[i]][0] += 1
            letters[firstWord][firstWord[i]][1].append(i + 1)

        if secondWord[i] not in letters[secondWord]:
            letters[secondWord][secondWord[i]] = [1, [i + 1]]
        else:
            letters[secondWord][secondWord[i]][0] += 1
            letters[secondWord][secondWord[i]][1].append(i + 1)

    permutation = []
    for i in range(len(firstWord)):
        permutation.append([i + 1, letters[secondWord][firstWord[i]][1][0]])
        letters[secondWord][firstWord[i]][1] = letters[secondWord][firstWord[i]][1][1:]

    return permutation

def writeFile(*args):
    with open(outputFileName, "w") as g:
        for arg in args:
            if arg == False:
                g.write("Nu sunt anagrame!\n")
                break

            for (i, sigmai) in arg:
                g.write("Din {} in {}\n".format(i, sigmai))

            g.write("\n")

    return

def main():
    firstWord, secondWord = getInput()
    permutationFS, permutationSF = anagram(firstWord, secondWord), anagram(secondWord, firstWord)
    writeFile(permutationFS, permutationSF)
    return

if __name__ == "__main__":
    main()
    exit()