# https://leetcode.com/problems/max-chunks-to-make-sorted-ii/
# Python (not Python3)

class Solution(object):
    def maxChunksToSorted(self, arr):
        length, chunks = len(arr) - 1, 1
        left = [arr[0]] + [0 for _ in range(length)]
        right = [0 for _ in range(length)] + [arr[-1]]

        for i in range(1, length):
            left[i] = max(left[i - 1], arr[i])
            right[-i - 1] = min(right[-i], arr[-i - 1])
        
        for i in range(0, length):
            if (left[i] <= right[i + 1]):
                chunks += 1
                
        return chunks