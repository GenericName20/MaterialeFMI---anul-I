n = int(input())
x, used = [0] * (n + 1), [0] * (n + 1)
solNr = 0
    
def printConfiguration(currentPosition):
    for i in range(1, currentPosition + 1):
        print(x[i], end=" ")
    print()

def solution(currentPosition):
    return currentPosition == n

def condition(currentPosition):
    if used[x[currentPosition]] != 0:
        return False
    
    for i in range(1, currentPosition):
        if abs(x[i] - x[currentPosition]) == currentPosition - i:
            return False
    
    return True

def tryNextPermutation(currentPosition):
    for i in range(1, n + 1):
        x[currentPosition] = i
        if condition(currentPosition):
            used[i] = 1
            if solution(currentPosition):
                global solNr
                if solNr < 3:
                    printConfiguration(currentPosition)
                solNr += 1
            else:
                tryNextPermutation(currentPosition + 1)
            used[i] = 0

def main():
    tryNextPermutation(1)
    print(solNr)
    return

if __name__ == "__main__":
    main()
    exit()