class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        nums1_nums2 = set(nums1).intersection(set(nums2))
        nums1_nums3 = set(nums1).intersection(set(nums3))
        nums2_nums3 = set(nums2).intersection(set(nums3))
        nums1_nums2_nums3 = nums1_nums2.union(nums1_nums3).union(nums2_nums3)
        return list(nums1_nums2_nums3)
