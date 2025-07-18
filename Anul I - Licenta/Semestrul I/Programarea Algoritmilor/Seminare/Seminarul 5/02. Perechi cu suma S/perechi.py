import os
path = os.path.dirname(__file__)
inputFileName = path + "/perechi.in"
outputFileName = path + "/perechi.out"

def findPairs(sum, numbers): # TwoPointers
    pairs = []
    left = 0
    right = len(numbers) - 1
    while left < right:
        if numbers[left] + numbers[right] > sum:
            right -= 1
        elif numbers[left] + numbers[right] < sum:
            left += 1
        else:
            pairs.append((numbers[left], numbers[right]))
            right -= 1
            left += 1
    
    return pairs

def main():
    with open(inputFileName, "r") as f:
        sum, numbers = int(f.readline().strip()), sorted(set([int(value) for value in f.readline().strip().split()]))

    pairs = findPairs(sum, numbers)
   
    with open(outputFileName, "w") as g:
        for pair in pairs:
            g.write("{} ".format(pair))
    
    return

if __name__ == "__main__":
    main()
    exit()