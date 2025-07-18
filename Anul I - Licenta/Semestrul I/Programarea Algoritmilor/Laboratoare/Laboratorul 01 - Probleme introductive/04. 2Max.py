import heapq

n = int(input())
values = []
for _ in range(0, n):
    x = int(input())
    if x not in values:
        heapq.heappush(values, x)

try:
    x, y = heapq.nlargest(2, values)
    print(x, y) 
except:
    print("Imposibil")