class Solution(object):
    def isPowerOfTwo(self, n):
        pow_of_2 = set(2**i for i in range(31))
        if n in pow_of_2:
            return True
        return False