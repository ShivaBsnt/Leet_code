class Solution(object):
    def findMaxK(self, nums):
        if not nums:
            return -1
        nums_set = list(set(nums))
        while nums_set:
            max_val = max(nums_set)
            if -max_val in nums_set:
                return max_val
            nums_set.remove(max_val)

        return -1

