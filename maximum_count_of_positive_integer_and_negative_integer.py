class Solution(object):
    def maximumCount(self, nums):
        positive_num_list = filter(lambda x: x>0 , nums)
        negative_num_list = filter(lambda x: x<0, nums)
        positive_count = len(positive_num_list)
        negative_count = len(negative_num_list)

        if positive_count >= negative_count:
            return positive_count
        return negative_count