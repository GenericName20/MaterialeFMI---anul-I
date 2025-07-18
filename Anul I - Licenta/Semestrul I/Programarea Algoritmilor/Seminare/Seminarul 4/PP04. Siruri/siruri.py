import os
path = os.path.dirname(__file__)
inputFileName = path + "/siruri.in"
outputFileName = path + "/siruri.out"

def getInput():
    length = int(input("Lungimea textului: "))
    with open(inputFileName, "r") as f:
         return length, [line.strip() for line in f.readlines()]

def genString(length, *strings):
    for string in strings:
        if len(string) == length:
            yield string

def getString(length, *strings):
    return [string for string in strings if len(string) == length]

def checkStrings(length, strings):

    with open(outputFileName, "w") as g:
        
        g.write("Siruri de lungime {} (GENERATOR):\n".format(length))
        reference = genString(length, *strings)
        last = next(reference, None)
        while last is not None:
            g.write("{}\n".format(last))
            last = next(reference, None)
        g.write("\n")

        g.write("Siruri de lungime {} (FUNCTIE):\n".format(length))
        result = getString(length, *strings)
        for string in result:
            g.write("{}\n".format(string))
        g.write("\0")

    return

def main():

    length, strings = getInput()
    checkStrings(length, strings)
    return

if __name__ == "__main__":
    main()
    print("Output written in {}\n".format(outputFileName))
    exit()