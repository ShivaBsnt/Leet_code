class Solution(object):
    def findGCD(self, nums):
        min_elem = min(nums)
        max_elem = max(nums)

        ans = 1

        for i in range(1, min_elem+1):
            if min_elem%i == 0 and max_elem%i ==0:
                ans = max(ans, i)
        return ans
        
