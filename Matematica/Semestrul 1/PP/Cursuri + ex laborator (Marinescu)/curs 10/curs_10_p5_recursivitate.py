"""
RECURSIVITATE
functie recursiva - se autoapeleaza
"""
def fact(n):
    #cond de oprire
    if n<=1:
        return 1
    else:
        return n*fact(n-1)
x=fact(10)
print(x)
x=fact(100)
print(x)
print()
x=fact(200)
print(x)
print()
import sys
sys.setrecursionlimit(1100)
x=fact(1000) #RecursionError: maximum recursion depth exceeded
print(x)
