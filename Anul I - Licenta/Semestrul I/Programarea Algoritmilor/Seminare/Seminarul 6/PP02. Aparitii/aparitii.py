import os
path = os.path.dirname(__file__)
inputFileName = path + "/aparitii.in"
outputFileName = path + "/aparitii.out"
pozMin, pozMax, firstMid, firstRight = None, None, None, None

def readInput():
    with open(inputFileName, "r") as f:
        return int(f.readline().strip()), [int(value) for value in f.readline().split()]

def binarySearch(referenceNumber, numbers, left, right):
    mid = left + (right - left) // 2
    if numbers[mid] == referenceNumber:
        global pozMin, pozMax, firstMid, firstRight
        firstMid = mid if firstMid is None else firstMid
        firstRight = right if firstRight is None else firstRight

        if pozMin is None:
            if numbers[mid - 1] == referenceNumber:
                return binarySearch(referenceNumber, numbers, left, mid - 1)
            else:
                pozMin = mid
                return binarySearch(referenceNumber, numbers, firstMid, firstRight)
        
        if pozMax is None:
            if mid < len(numbers) - 1 and numbers[mid + 1] == referenceNumber:
                return binarySearch(referenceNumber, numbers, mid + 1, right)
            else:
                pozMax = mid
                return (pozMin, pozMax)
            
    elif numbers[mid] < referenceNumber and mid + 1 <= right:
        return binarySearch(referenceNumber, numbers, mid + 1, right)
    elif left <= mid - 1:
        return binarySearch(referenceNumber, numbers, left, mid - 1)

def writeOutput(referenceNumber, numbers, answer):
    with open(outputFileName, "w") as g:
        tab = len(str(len(numbers)))
        g.write(" Index: ")
        for index in range(len(numbers)):
            if answer is not None and index == answer[0]:
                g.write("|> ")
            g.write("{} ".format(str(index).rjust(tab)))
            if answer is not None and index == answer[1]:
                g.write("<|")

        g.write("\nNumere: ")
        for index, number in enumerate(numbers):
            if answer is not None and index == answer[0]:
                g.write("|> ")
            g.write("{} ".format(str(number).rjust(tab)))
            if answer is not None and index == answer[1]:
                g.write("<|")

        if answer is None:
            g.write("\n\nNumarul {} nu a fost gasit in sir.".format(referenceNumber))
        else:
            g.write("\n\nNumarul {} apare {} in sir:\nPozitia de inceput: {}\nPozitia de final: {}\n".format(referenceNumber, "o singura data" if answer[1] - answer[0] + 1 == 1 else "de {} ori".format(answer[1] - answer[0] + 1), answer[0], answer[1]))
    
    return

def main():
    referenceNumber, numbers = readInput()
    answer = binarySearch(referenceNumber, numbers, 0, len(numbers) - 1)
    writeOutput(referenceNumber, numbers, answer)
    return

if __name__ == "__main__":
    main()
    exit()