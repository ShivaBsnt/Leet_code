class Solution(object):
    def averageValue(self, nums):
        output = list(filter(lambda x : x if x%3 == 0 and x%2==0 else 0, nums))
        if not output:
            return 0
        length = len(output)
        return sum(output)/length