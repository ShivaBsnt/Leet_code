class Solution(object):
    def shuffle(self, nums, n):
        a = nums[0:n]
        b = nums[n:]
        output = []
        for i,j in zip(a,b):
            output.append(i)
            output.append(j)
        return output