# Pentru editorul de text
# import os
# path = os.path.dirname(__file__)
# inputFileName = path + "/numere.in"
# outputFileName = path + "/numere.out"

inputFileName = "numere.in"
outputFileName = "numere.out"

def getInput():
    numbers = []
    with open(inputFileName, "r") as f:
        for line in f.readlines():
            numbers.append([int(var) for var in line.split()])

    return numbers

def computeSums(numbers):
    sums = {}
    for line in numbers:
        key = sum(line)
        if key not in sums:
            sums[key] = [line]
        else:
            sums[key].append(line)

    return dict(sorted(sums.items(), key=lambda item: item[0]))

def setOutput(answer):
    with open(outputFileName, "w") as g:
        for key in answer:
            g.write("Suma {}:\n".format(key))
            for numbers in answer[key]:
                g.write("{} \n".format(" ".join([str(number) for number in numbers])))
    
    return

def main():
    numbers = getInput()    
    answer = computeSums(sorted(numbers, key=lambda item: -len(item)))
    setOutput(answer)

    return

if __name__ == "__main__":
    main()
    exit()