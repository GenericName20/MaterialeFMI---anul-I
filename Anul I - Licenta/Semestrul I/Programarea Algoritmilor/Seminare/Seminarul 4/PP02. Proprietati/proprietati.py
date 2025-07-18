import os
path = os.path.dirname(__file__)
outputFileName = path + '/proprietati.out'

global refAnagram, refAnagramSorted, refDigitsCount, refDigitsSum

def getInput():
    inputFileName = path + "/proprietatea1.in"
    with open(inputFileName, "r") as f:
        task1 = [int(number) for number in f.readline().strip().split()]

    inputFileName = path + "/proprietatea2.in"
    with open(inputFileName, "r") as f:
        task2 = f.readline()

    inputFileName = path + "/proprietatea3.in"
    with open(inputFileName, "r") as f:
        global refAnagram, refAnagramSorted
        refAnagram = f.readline().strip()
        refAnagramSorted = sorted(refAnagram)
        task3 = [word for word in f.readline().split()]

    inputFileName = path + "/proprietatea4.in"
    with open(inputFileName, "r") as f:
        global refDigitsCount, refDigitsSum
        refDigitsCount, refDigitsSum = [int(value) for value in f.readline().split()]
        task4 = [int(value) for value in f.readline().split()]
    
    return [task1, task2, task3, task4]


def property1(index, task):
    return None if task[index] <= 0 else index

def property2(index, task):
    import string
    return None if task[index] not in string.punctuation else index

def property3(index, task):
    return None if sorted(task[index]) != refAnagramSorted else index

def property4(index, task):
    return None if len(str(task[index])) != refDigitsCount else index

def genCond(property, task):
    for index in range(len(task)):
        if (property(index, task) is not None):
            yield (index, task[index])

def checkTasks(tasks):

    printTask1 = []
    for index, word in enumerate(tasks[1].split()):
        printTask1 += [word]
        if index % 10 == 0 and index != 0:
            printTask1 += ['\n']

    printTask1 = " ".join(printTask1)

    properties = [
        "a) Pozitiile valorilor strict pozitive din tuplul:\n{}:\n".format(tasks[0]),
        "b) Pozitiile semnelor de punctuatie din sirul de caractere:\n\"{}\":\n".format(printTask1),
        "c) Pozitiile cuvintelor care sunt anagrame cu <{}> din sirul de caractere:\n\"{}\":\n".format(refAnagram, " ".join(tasks[2])),
        "d) Pozitiile numerelor cu <{}> cifre si suma cifrelor egala cu <{}> din tuplul:\n{}:\n".format(refDigitsCount, refDigitsSum, tasks[3])
    ]

    with open(outputFileName, "w") as g:
        for index, task in enumerate(tasks):
            g.write("{}".format(properties[index]))
            property = "property" + str(index + 1)

            reference = genCond(globals()[property], task)
            last = next(reference, None)
            while last is not None:
                g.write("(Pozitia <{}>, valoarea <{}>) ".format(last[0], last[1]))
                last = next(reference, None)
            g.write("\n\n")

    return

def main():
    tasks = getInput()
    checkTasks(tasks)
    return

if __name__ == "__main__":
    main()
    print("Output written in {}\n".format(outputFileName))
    exit()