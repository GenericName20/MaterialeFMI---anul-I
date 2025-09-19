import os
path = os.path.dirname(__file__)
inputFileName = path + "/candidat.in"
outputFileName = path + "/candidat.out"

def getInput():
    with open(inputFileName, "r") as f:
        return [int(value) for value in f.readline().split()]

def checkVotes(votes): # Boyer-Moore

    advantage = 0
    majoritarian = None
    for candidate in votes:
        if advantage == 0:
            advantage = 1
            majoritarian = candidate
        else:
            if candidate == majoritarian:
                advantage += 1
            else:
                advantage -= 1
    
    if advantage == 0:
        return [None, "Niciun candidat nu a obtintut majoritatea voturilor".format(majoritarian)]
    if votes.count(majoritarian) <= len(votes) // 2:
        return [None, "Candidatul {} nu a obtinut majoritatea voturilor!".format(majoritarian)]
    return [majoritarian, "Candidatul a obtinut majoritatea voturilor, felicitari!"]


def writeOutput(winner, reason):
    with open(outputFileName, "w") as g:
        g.write("{}: {}\n".format("Candidatul " + str(winner) if winner else "Nimeni", reason))


def main():
    votes = getInput()
    winner, reason = checkVotes(votes)
    writeOutput(winner, reason)
    return


if __name__ == "__main__":
    main()
    exit()