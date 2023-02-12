class Solution(object):
    def applyOperations(self, nums):
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] = nums[i]*2
                nums[i+1] = 0
        return sorted(nums, key=lambda x:not x)

