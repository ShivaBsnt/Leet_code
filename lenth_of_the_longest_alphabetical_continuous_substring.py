class Solution(object):
    def smallestEvenMultiple(self, n):
        if n%2 == 0:
            return n
        multyplied_by = 2
        while True:
            multiple = n*multyplied_by
            if multiple%2 == 0:
                return multiple
            multyplied_by+=1