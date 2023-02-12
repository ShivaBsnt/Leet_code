class Solution(object):
    def isPerfectSquare(self, num):
        import math
        square_root = math.sqrt(num)
        return square_root.is_integer()