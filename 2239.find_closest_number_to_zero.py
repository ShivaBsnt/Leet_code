class Solution(object):
    def findClosestNumber(self, nums):
        distance = map(lambda x: abs(x), nums)
        minimum = - min(distance)
        if  minimum and abs(minimum) in nums:
            return abs(minimum)
        if minimum in nums:
            return minimum
        return abs(minimum)
            
