class Solution(object):
    def largestOddNumber(self, num):
        indx = -1
        n = len(num)
        for i in range(n):
            if int(num[i])%2 == 1:
                indx = i
        
        if indx == -1:
            return ""
        return num[:indx+1]
