class Solution(object):
    def differenceOfSum(self, nums):
        element_sum = sum(nums)
        digit_sum = sum(list(map(lambda ele: sum(int(sub) for sub in str(ele)), nums)))
        return abs(element_sum-digit_sum)