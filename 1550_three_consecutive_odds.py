class Solution(object):
    def threeConsecutiveOdds(self, arr):
        i=0
        while i<=(len(arr)):
            if len(filter(lambda x: x%2!=0 ,arr[i:i+3]))==3:
                return True
            i+=1
        return False
