# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        high = n
        low = 0

        while high>=low:
            mid = (low+high)//2
            if guess(mid) == 0:
                return mid
   
            if guess(mid) == -1:
                # the guess is higher
                high = mid-1
            if guess(mid) == 1:
                # the guess is lower
                low = mid+1
