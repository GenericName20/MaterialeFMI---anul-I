import os
path = os.path.dirname(__file__)
inputFileName = path + "/graf.in"
outputFileName = path + "/graf.out"

g = open(outputFileName, "w")

def getInput():
    f = open(inputFileName, "r")
    property, nodesCount, edgesCount = f.readline().strip().split()

    edges = []
    for line in f.readlines():
        x, y = line.split()
        edges.append((int(x), int(y)))
    
    referenceNodes = edges[-1]
    edges = edges[:len(edges) - 1]
    start, finish = referenceNodes[0], referenceNodes[1]

    f.close()
    return property, int(nodesCount), int(edgesCount), edges, start, finish


def printEdges(property, edges):
    if (property == "neorientat"):
        g.write("A) Exista muchii intre nodurile: {}\n".format(edges))
    else:
        g.write("A) Exista arce intre nodurile: {}\n".format(edges))


def computeAdjacencyList(property, edgesList):
    adjacencyList = {} 
    for edge in edgesList:
        if edge[0] not in adjacencyList:
            adjacencyList[edge[0]] = [edge[1]]
        else:
            adjacencyList[edge[0]].append(edge[1])
        
        if property == "neorientat":
            if edge[1] not in adjacencyList:
                adjacencyList[edge[1]] = [edge[0]]
            else:
                adjacencyList[edge[1]].append(edge[0])
    
    g.write("\nB) Listele de adiacenta:\n")
    for node in adjacencyList:
        g.write("Nodul {}: {}\n".format(node, adjacencyList[node]))

    return dict(sorted(adjacencyList.items(), key=lambda item: item[0]))


def computeAdjacencyMatrix(nodesCount, adjacencyList):
    adjacencyMatrix = [[0 for _ in range(0, nodesCount)] for _ in range(0, nodesCount)]
    for currentNode in adjacencyList:
        for neighNode in adjacencyList[currentNode]:
            adjacencyMatrix[currentNode - 1][neighNode - 1] = 1

    g.write("\nC) Matricea de adiacenta:\n")
    for line in adjacencyMatrix:
        g.write("{}\n".format(line))

    return adjacencyMatrix


def BFS(start, adjacencyList):
    g.write("\nD) BFS:\n")
    BFSnodes = {}
    for node in adjacencyList:
        BF = [(node, -1)]
        left = right = 0
        while left <= right:
            parent = BF[left][0]
            try:
                for child in adjacencyList[parent]:
                    if child not in [x for (x, y) in BF]:
                        BF.append((child, parent))
                        right += 1
                left += 1
            except:
                break

        g.write("BFS din nodul {}: {}\n".format(node, [BF[i][0] for i in range(len(BF))]))
        BFSnodes[node] = BF

    g.write("BFS din nodul START ({}): {}\n".format(start, [BFSnodes[start][i][0] for i in range(len(BF))]))
    return BFSnodes[start]

def DFS(start, adjacencyList):
    g.write("\nE) DFS:\n")
    DFSnodes = {}

    for node in adjacencyList:
        DF, visited = [node], [node]
        while DF != []:
            parent = DF[-1]

            visitedAllNodes = True
            for child in adjacencyList[parent]:
                if child not in visited:
                    visitedAllNodes = False
                    visited.append(child)
                    DF.append(child)
                    break

            if visitedAllNodes:
                DF.pop(-1)
        
        g.write("DFS din nodul {}: {}\n".format(node, visited))
        DFSnodes[node] = visited

    g.write("DFS din nodul START({}): {}".format(start, DFSnodes[start]))
    return DFSnodes[start]


# def nodesPath(nodes, finish):
#   return ""


def main():
    property, nodesCount, edgesCount, edgesList, start, finish = getInput()
    printEdges(property, edgesList) # Task A
    adjacencyList = computeAdjacencyList(property, edgesList) # Task B
    adjacencyMatrix = computeAdjacencyMatrix(nodesCount, adjacencyList) # Task C
    BFSstart = BFS(start, adjacencyList) # Task D
    DFSstart = DFS(start, adjacencyList) # Task E
    # PATHSF = nodesPath(BFSstart, finish) # Task F
    g.close()

if __name__ == "__main__":
    main()