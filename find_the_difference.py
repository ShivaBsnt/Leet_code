class Solution(object):
    def findTheDifference(self, s, t):
        t=list(t)
        for char in s:
            t.remove(char)
        return "".join(t)

        