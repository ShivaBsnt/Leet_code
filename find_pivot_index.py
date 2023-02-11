class Solution(object):
    def pivotIndex(self, nums):
        for index,num in enumerate(nums):
            if sum(nums[:index]) == sum(nums[index+1:]):
                return index
        return -1
