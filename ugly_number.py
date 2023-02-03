class Solution(object):
    def isUgly(self, n):
        factors = [2, 3, 5]
        if n<=0:
            return False
        for  factor in factors:
            while n%factor == 0:
                n//=factor
        return n == 1
        

        

