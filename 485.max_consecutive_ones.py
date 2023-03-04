class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        nums.append(0)
        ans, a = 0, 0
        for i in nums:
            if i: a+=1
            else:
                ans = max(ans, a)
                a = 0
        return ans
