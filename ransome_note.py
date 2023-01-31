class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        magazine_list = list(magazine)
        for elem in ransomNote:
            if elem in magazine_list:
                magazine_list.remove(elem)
            else:
                return False
        return True