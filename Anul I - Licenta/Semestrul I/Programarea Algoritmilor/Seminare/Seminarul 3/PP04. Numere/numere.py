import os
path = os.path.dirname(__file__)
inputFileName = path + "/numere.in"
outputFileName = path + "/numere.out"


def getInput():
    with open(inputFileName, "r") as f:
        fullText = "".join(line.strip().replace(" ", "") for line in f.readlines())

    return fullText


def Method1(digits): # Liste
    zeros = digits.count("0")    
    minNumber = [digits[zeros]] + digits[0:zeros] + digits[zeros + 1:]
    minNumber = int("".join(minNumber))

    maxNumber = int("".join(sorted(digits, reverse=True)))
    
    return minNumber, maxNumber


def Method2(digits): # Dictionar de frecventa
    frequency = {chr(x + 48): digits.count(chr(x+48)) for x in range(0, 10)}

    maxNumber = [key * frequency[key] for key in sorted(frequency.keys(), reverse = True) if frequency[key]]
    maxNumber = int("".join(maxNumber))
    
    minNumber = []
    for key in frequency:
        if key != '0' and frequency[key]:
            minNumber = [key]
            frequency[key] -= 1
            break

    for key in frequency:
        minNumber += [key] * max(frequency[key], 0)

    minNumber = int("".join(minNumber))

    return minNumber, maxNumber


def writeFile(args):
    with open(outputFileName, "w") as g:
        for i, arg in enumerate(args):
            g.write("Metoda {}:\nMinim: {}\nMaxim: {}\n".format(i + 1, arg[0], arg[1]))
            g.write("\n")

    return

def main():
    digits = getInput()

    answer = [Method1(sorted(digits))] + [Method2(sorted(digits))]
    writeFile(answer)
    return

if __name__ == "__main__":
    main()
    exit()