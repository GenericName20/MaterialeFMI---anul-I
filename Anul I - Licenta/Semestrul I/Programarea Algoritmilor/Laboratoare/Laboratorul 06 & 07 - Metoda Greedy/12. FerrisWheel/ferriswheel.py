# Pentru editorul de text
# import os
# path = os.path.dirname(__file__)
# inputFileName = path + "/ferriswheel.in"
# outputFileName = path + "/ferriswheel.out"

# with open(inputFileName, "r") as f:
#     childsNumber, maxWeight = [int(var) for var in f.readline().split()]
#     weights = sorted([int(var) for var in f.readline().split()], reverse=True)

childsNumber, maxWeight = [int(var) for var in input().strip().split()]
weights = sorted([int(var) for var in input().strip().split()], reverse=True)

minGondolas = 0
left = 0
right = childsNumber - 1
while left <= right:
    if (weights[left] + weights[right] <= maxWeight and len(weights) > 1):
        minGondolas += 1
        left+=1
        right-=1
    elif weights[left] <= maxWeight:
        minGondolas += 1
        left+=1

print(minGondolas)

# with open(outputFileName, "w") as g:
#     g.write("{}".format(minGondolas))