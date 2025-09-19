import os
path = os.path.dirname(__file__)
inputFileName = path + "/generator.in"
outputFileName = path + "/generator.out"

def getInput():
    with open(inputFileName, "r") as f:
        number = int(f.readline())
        lists = []
        for line in f.readlines():
            lists.append([int(value) for value in line.split()])

    return number, lists


def find(number, *lists):
    for list in lists:
        if number in list:
            yield list

    return


def generate(number, lists):

    reference = find(number, *lists)
    last = next(reference, None)

    with open(outputFileName, "w") as g:
        if last is None:
            g.write("Numarul {} nu se gaseste in nicio lista!\n".format(number))
        else:
            while last is not None:
                g.write("Numarul {} se gaseste in lista: {}\n".format(number, last))
                last = next(reference, None)

    return


def main():

    number, lists = getInput()
    generate(number, lists)
    return


if __name__ == "__main__":
    main()
    print("Output written in {}\n".format(outputFileName))
    exit()