import os
path = os.path.dirname(__file__)
inputFileName = path + "/backtracking.in"
outputFileName = path + "/backtracking.out"

n, t, l, s = 0, 0, 0, 0
x = [0] * 10
vowels = [letter for letter in "aeiouAEIOU"]
def readInput():
    g = open(outputFileName, "w")
    g.close()

    with open(inputFileName, "r") as f:
        n = int(f.readline())
        t = f.readline().strip()
        l = [letter for letter in f.readline().strip().split()]
        s = [symbol for symbol in f.readline().strip().split()]
    
    return n, t, l, s

def validate(n, t, l, s) -> bool:
    if len(t) != n:
        return False
    if len(l) != t.count("l"):
        return False
    if len(s) != t.count("s"):
        return False
    
    return True

def afisare():
    with open(outputFileName, "a") as g:
        for i in range(1, n + 1):
            if t[i - 1] == 'l':
                g.write("{}".format(l[x[i] - 1]))
            else:
                g.write("{}".format(s[abs(x[i]) - 1]))
        g.write("\n")

def cond(k) -> bool:
    # Pentru 0.5p
    # if l[x[1] - 1] in vowels:
    #     return False
    
    for i in range(k):
        if x[i] == x[k]:
            return False
    
    return True

def back(k):
    if t[k - 1] == 'l':
        for i in range(1, len(l) + 1):
            x[k] = i
            if cond(k):
                if (k == n):
                    afisare()
                else:
                    back(k + 1)

    elif t[k - 1] == 's':
        for i in range(1, len(s) + 1):
            x[k] = -i
            if cond(k):
                if (k == n):
                    afisare()
                else:
                    back(k + 1)

def main():
    global n, t, l, s
    n, t, l, s = readInput()
    if (validate(n, t, l, s)):
        back(1)
    else:
        print("Imposibil")
    
if __name__ == "__main__":
    main()
    exit(0)