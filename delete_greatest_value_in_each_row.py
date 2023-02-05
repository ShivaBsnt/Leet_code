class Solution(object):
    def deleteGreatestValue(self, grid):
        for row in grid: row.sort()
        return sum(max(col) for col in zip(*grid))