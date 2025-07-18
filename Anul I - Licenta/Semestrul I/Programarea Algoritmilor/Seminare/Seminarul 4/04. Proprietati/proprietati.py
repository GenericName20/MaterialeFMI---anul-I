import os
path = os.path.dirname(__file__)
outputFileName = path + "/proprietati.out"


def setDescription(*args):
    descriptions = [
        "Numarul valorilor pare din fiecare lista",
        "Numarul vocalelor dintr-un sir de caractere",
        "Numarul perechilor (x, y) cu proprietatea ca x = y din tuplu",
        "Numarul cuvintelor de lungime {} dintr-un sir de caractere".format(args[0]),
        "Numarul valorilor x pentru care cmmdc(x, {}) = {}".format(args[1], args[2])
    ]
    return descriptions


def getInput():
    inputFileName = path + "/proprietatea1.in"
    with open(inputFileName, "r") as f:
        task1 = [[int(var) for var in line.split()] for line in f.readlines()]

    inputFileName = path + "/proprietatea2.in"
    with open(inputFileName, "r") as f:
        import string
        task2 = []
        for line in f.readlines():
            for symbol in string.punctuation:
                line = line.replace(symbol, "")
            task2 += [line.strip().lower()]

    inputFileName = path + "/proprietatea3.in"
    with open(inputFileName, "r") as f:
        task3 = [[(int(pair.split()[0]), int(pair.split()[1])) for pair in line.split(",")] for line in f.readlines()]

    inputFileName = path + "/proprietatea4.in"
    with open(inputFileName, "r") as f:
        task4 = [line.strip() for line in f.readlines()]

    inputFileName = path + "/proprietatea5.in"
    with open(inputFileName, "r") as f:
        task5 = [line.strip() for line in f.readlines()]

    return task1, task2, task3, task4, task5


def property1(*args):
    return len([value for value in args[0] if value % 2 != 0])
    
def property2(*args):
    return len([letter for letter in args[0] if letter in "aeiou"])

def property3(*args):
    return len([pair for pair in args[0] if int(pair[0] == pair[1])])

def property4(list):
    global stringLength
    return len([word for word in list.split() if len(word) == stringLength])

def property5(list):
    from math import gcd
    global cmmdcArg, result
    return len([int(value) for value in list.split() if gcd(int(value), cmmdcArg) == result])

def genCond(property, *lists):
    for list in lists:
        yield property(list), list

def checkProperties(tasks):

    global stringLength, cmmdcArg, result
    stringLength, cmmdcArg, result = int(tasks[3][0]), int(tasks[4][0].split()[0]), int(tasks[4][0].split()[1])
    tasks[3], tasks[4] = tasks[3][1:], tasks[4][1:]

    descriptions = setDescription(stringLength, cmmdcArg, result)
    
    for index, task in enumerate(tasks):
        description = descriptions[index]
        property = "property" + str(index + 1)

        with open(outputFileName, "a") as g:
            g.write("{}:\n".format(description.upper()))

            reference = genCond(globals()[property], *task)
            last = next(reference, None)
            while last is not None:
                g.write("{} pentru [{}]\n".format(last[0], ", ".join([str(value) for value in last[1]]) if type(last[1][0]) == int or type(last[1][0]) == tuple else last[1]))
                last = next(reference, None)

            g.write("\n")

    return


def main():
    with open(outputFileName, "w"):
        next

    tasks = [task for task in getInput()]
    checkProperties(tasks)


if __name__ == "__main__":
    main()
    print("Output written in {}\n".format(outputFileName))
    exit()