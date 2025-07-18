# Pentru editorul de text
# import os
# path = os.path.dirname(__file__)
# inputFileName = path + "/moscraciun_xi.in"
# outputFileName = path + "/moscraciun_xi.out"

# with open(inputFileName, "r") as f:
#     giftsNumber, storesNumber = [int(var) for var in f.readline().split()]
#     storesGifts = sorted([int(var) for var in f.readline().split()], reverse=True)

giftsNumber, storesNumber = [int(var) for var in input().strip().split()]
storesGifts = sorted([int(var) for var in input().strip().split()], reverse=True)

boughtGifts = currStoreIndex = 0
while boughtGifts < giftsNumber and currStoreIndex < storesNumber:
    boughtGifts += storesGifts[currStoreIndex]
    currStoreIndex += 1

print(currStoreIndex if boughtGifts >= giftsNumber else "imposibil")

# with open(outputFileName, "w") as g:
#     g.write(str(currStoreIndex) if boughtGifts >= giftsNumber else "imposibil")