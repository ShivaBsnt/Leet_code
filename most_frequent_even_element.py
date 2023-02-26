class Solution(object):
    def mostFrequentEven(self, nums):
        filtered_num = sorted(list(filter(lambda x: x%2 == 0,nums)))
        return max(filtered_num,key=filtered_num.count) if len(filtered_num) > 0 else -1