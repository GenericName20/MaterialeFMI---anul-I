# 2 la puterea -n
import os
outputFile = os.path.dirname(__file__) + "/PuteriNegative.txt"
with open(outputFile, "w") as g:
    for i in range(1, 32):
        g.write(f"2^-{i} \t {2**(-i)}\n")
    g.close()

A, B, C, D = 1, 1, 0, 0
print(A and (A ^ B) and (B ^ C) and D)
