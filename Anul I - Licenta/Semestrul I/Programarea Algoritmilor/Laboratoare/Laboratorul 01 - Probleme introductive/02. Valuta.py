n = int(input())
values = []
for _ in range(0, n):
    values.append(float(input()))

max_increase = (0, 0, 0)
for i in range(1, n):
    if (values[i] - values[i - 1] > max_increase[0]):
        max_increase = (round(values[i] - values[i - 1], 2), i, i + 1)

print(max_increase)