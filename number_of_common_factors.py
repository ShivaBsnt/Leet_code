class Solution(object):
    def commonFactors(self, a, b):
        maximum = max(a, b)
        common_factor = filter(lambda x: a%x ==0 and b%x ==0, list(range(1, maximum+1)))
        return len(common_factor)