class Solution(object):
    def getCommon(self, nums1, nums2):
        commons = set(nums1).intersection(set(nums2))
        if not commons:
            return -1
        return min(list(commons))