class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        elem_dict = {}
        for i in range(len(nums)):
            if nums[i] in elem_dict:
                if abs(elem_dict[nums[i]] - i ) <= k:
                    return True
            elem_dict[nums[i]]=i
        return False