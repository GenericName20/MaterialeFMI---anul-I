try:
    l1, l2 = map(int, input().split())
except:
    print("Numar incorect de valori / Format incorect!")
    exit()

from math import gcd
blocksSize = gcd(l1, l2)
blocksCount = int((l1 * l2) / (blocksSize * blocksSize))

print("Sunt necesare {} plăci pătrate cu latura de {}".format(blocksCount, blocksSize))