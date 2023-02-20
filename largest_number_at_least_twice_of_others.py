class Solution(object):
    def dominantIndex(self, nums):
        list_len = len(nums)
        maximum = max(nums)
        filter_largest = filter(lambda x: 2*x<=maximum, nums)
        print(filter_largest)
        if list_len - len(filter_largest) == 1:
            return nums.index(maximum)
        return -1
