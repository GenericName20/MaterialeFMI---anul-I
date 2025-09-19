# https://www.geeksforgeeks.org/problems/tower-of-hanoi-1587115621/1?itm_source=geeksforgeeks

class Solution:
    def towerOfHanoi(self, n, fromm, to, aux):
        if (n == 0):
            return 0
        else:
            return 1 + self.towerOfHanoi(n - 1, to, aux, fromm) + self.towerOfHanoi(n - 1, aux, to, fromm)