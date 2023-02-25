class Solution(object):
    def sortedSquares(self, nums):
        return sorted(list(map(lambda x: x**2, nums)))