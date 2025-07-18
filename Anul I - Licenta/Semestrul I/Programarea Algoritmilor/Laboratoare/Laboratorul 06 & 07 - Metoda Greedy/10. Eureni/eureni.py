# Pentru editorul de text
# import os
# path = os.path.dirname(__file__)
# inputFileName = path + "/eureni.in"
# outputFileName = path + "/eureni.out"

inputFileName = "eureni.in"
outputFileName = "eureni.out"

with open(inputFileName, "r") as f:
    sum, n, e = [int(var) for var in f.readline().split()]

power = n
computedSum = totalBanknotes = 0

g = open(outputFileName, "w")
while (computedSum < sum):

    banknotes = 0
    while (computedSum + e ** power <= sum):
        computedSum += e ** power
        banknotes += 1

    if (banknotes):
        totalBanknotes += banknotes
        g.write("{} {}\n".format(e ** power, banknotes))
    
    power -= 1

g.write("{}".format(totalBanknotes))
g.close()