# Pentru editorul de text
# import os
# path = os.path.dirname(__file__)
# inputFileName = path + "/moscraciun2.in"
# outputFileName = path + "/moscraciun2.out"

# with open(inputFileName, "r") as f:
#     giftsNumber, storesNumber = [int(var) for var in f.readline().split()]
#     storesGifts = []
#     for line in f.readlines():
#         line = line.split()
#         storesGifts.append((int(line[0]), int(line[1])))

giftsNumber, storesNumber = [int(var) for var in input().strip().split()]
storesGifts = []
for _ in range(storesNumber):
    line = input().strip().split()
    storesGifts.append((int(line[0]), int(line[1])))

storesGifts = sorted(storesGifts)
boughtGifts = currStoreIndex = totalSpent = 0

while currStoreIndex < storesNumber and boughtGifts + storesGifts[currStoreIndex][1] <= giftsNumber:
    totalSpent += storesGifts[currStoreIndex][0] * storesGifts[currStoreIndex][1]
    boughtGifts += storesGifts[currStoreIndex][1]
    currStoreIndex += 1

try:
    if storesGifts[currStoreIndex][1] >= (giftsNumber - boughtGifts) and boughtGifts < giftsNumber:
        totalSpent += storesGifts[currStoreIndex][0] * (giftsNumber - boughtGifts)
        boughtGifts += (giftsNumber - boughtGifts)
except:
    next

print(totalSpent if boughtGifts == giftsNumber else "imposibil")

# with open(outputFileName, "w") as g:
#     g.write("{}".format(totalSpent if boughtGifts == giftsNumber else "imposibil"))