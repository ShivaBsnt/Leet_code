class Solution(object):
    def firstUniqChar(self, s):
        for index, elem in enumerate(s):
            if s.count(elem) == 1:
                return index
        return -1