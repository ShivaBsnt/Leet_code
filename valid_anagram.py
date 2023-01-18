class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        for char in set(s):
            char_count_in_s = s.count(char)
            char_count_in_t = t.count(char)

            if char_count_in_s != char_count_in_t:
                return False
        return True