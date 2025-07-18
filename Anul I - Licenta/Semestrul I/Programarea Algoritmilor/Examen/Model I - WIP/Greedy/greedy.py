import os
path = os.path.dirname(__file__)
inputFileName = path + "/greedy.in"
outputFileName = path + "/greedy.out"

def readInput():
    obj = [] # Lista de obiecte
    with open(inputFileName, "r") as f:
        n = int(f.readline().strip()) # Numărul de obiecte
        w = float(f.readline().strip()) # Greutatea de referință

        # Adăugăm în lista de obiecte perechi de forma [Greutate, Indice]
        for index, line in enumerate(f.readlines()):
            obj.append((float(line.strip()), index + 1))
        
    return obj, n, w   

def writeOutput(ans):
    with open(outputFileName, "w") as g:
        ans = sorted(ans)
        g.write("{}\n".format(len(ans)))
        for pair in ans:
            g.write("{} + {}\n".format(pair[0], pair[1]))

def main():
    # Lista de obiecte, numărul lor și greutatea de referință
    objects, objectsNumber, referenceWeigth = readInput()

    # Sortăm obiectele descrescător după greutate / O(n * log2n)
    objects.sort(key = lambda item: -item[0])

    # Parcurgem elementele două câte două, 
    # de la cele mai mari perechi la cele mai mici / <= O(n)
    ans, i = [], 0
    while i < objectsNumber - 1:
        if (objects[i][0] - objects[i + 1][0] <= referenceWeigth):
            ans.append((objects[i][1], objects[i + 1][1]))
            i += 1
        i += 1

    writeOutput(ans)

if __name__ == "__main__":
    main()
    exit(0)