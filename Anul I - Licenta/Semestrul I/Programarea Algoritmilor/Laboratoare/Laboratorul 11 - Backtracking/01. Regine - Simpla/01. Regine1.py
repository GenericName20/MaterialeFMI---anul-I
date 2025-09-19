n = int(input())

x, used = [0] * (n + 1), [0] * (n + 1)
sol = []

def printConfiguration(currentPosition):
    # for i in range(1, currentPosition + 1):
    #     print(x[i], end="")

    global sol
    sol = [value for value in x]

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
                printConfiguration(currentPosition)
                break
            else:
                tryNextPermutation(currentPosition + 1)
            used[i] = 0

tryNextPermutation(1)

mat = [['*' if sol[i + 1] == j + 1 else '-' for j in range(n)] for i in range(n)]

for line in mat:
    print(" ".join([str(value) for value in line]))
