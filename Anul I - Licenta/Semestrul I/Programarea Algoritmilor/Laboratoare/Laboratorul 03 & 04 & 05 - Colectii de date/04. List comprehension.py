list = input().strip().split()
values = [int(value) for value in list]

import heapq
orderedValues = []
for value in values:
    if value not in orderedValues:
        heapq.heappush(orderedValues, value)

try:
    x, y = heapq.nlargest(2, orderedValues)
    print(x, y) 
except:
    print("Imposibil")