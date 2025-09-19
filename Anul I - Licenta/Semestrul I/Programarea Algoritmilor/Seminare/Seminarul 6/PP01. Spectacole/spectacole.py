import os
path = os.path.dirname(__file__)
inputFileName = path + "/spectacole.in"
outputFileName = path + "/spectacole.out"

def readInput():
    from queue import PriorityQueue
    shows = PriorityQueue()
    with open(inputFileName, "r") as f:
        for index, line in enumerate(f.readlines()):
            start, end = line.split("-")
            shows.put((end.strip(), (start.strip(), index + 1)))
    
    return shows

def computeSchedule(shows):
    maxSchedule = [shows.get()]
    while not shows.empty():
        currentShow = shows.get()
        if currentShow[1][0] >= maxSchedule[-1][0]:
            maxSchedule.append(currentShow)

    return maxSchedule

def writeOutput(maxSchedule):
    with open(outputFileName, "w") as g:
        g.write("Numarul maxim de spectacole: {}\n\nSpectacolele programate:\n".format(len(maxSchedule)))
        for show in maxSchedule:
            g.write("{}-{} Spectacol {}\n".format(show[1][0], show[0], show[1][1]))
    
    return

def main():
    shows = readInput()
    maxSchedule = computeSchedule(shows)
    writeOutput(maxSchedule)
    return

if __name__ == "__main__":
    main()
    exit()