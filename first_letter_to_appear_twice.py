class Solution(object):
    def repeatedCharacter(self, s):
        letter_dict = {}
        for i in s:
            if i in letter_dict:
                return i
            letter_dict[i]=i