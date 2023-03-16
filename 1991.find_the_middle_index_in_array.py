class Solution(object):
    def findMiddleIndex(self, nums):
        for index, i in enumerate(nums):
            if sum(nums[0:index]) == sum(nums[index+1:]):
                return index
        return -1
