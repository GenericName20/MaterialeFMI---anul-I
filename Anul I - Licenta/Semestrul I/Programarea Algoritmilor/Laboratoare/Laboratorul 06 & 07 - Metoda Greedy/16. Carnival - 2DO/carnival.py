# Translate după sursa carnival.cpp - Trebuie corectat
n = int(input())

solution = [0]
rating = [[True] * n for _ in range(n)]

for i in range(1, n):
    values = [int(var) for var in input().strip().split()]
    for j in range(1, i + 1):
        if (j > (i + 1) // 2):
            rating[i][values[j - 1]] = False

    if rating[i][solution[0]]:
        solution.insert(0, i)
        continue

    if rating[i][solution[-1]]:
        solution.append(i)
        continue
    
    for k in range(1, len(solution)):
        if rating[i][solution[k]] and rating[i][solution[k + 1]]:
            solution.insert(k + 1, i)
            break

print(" ".join(map(str, solution)))