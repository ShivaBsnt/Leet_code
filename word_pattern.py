class Solution(object):
    def wordPattern(self, pattern, s):
        mapPatternS = {}
        pattern_elements = [x for x in pattern]
        s_words = s.split()
        if len(pattern_elements) != len(s_words):
            return False
        for i in range(len(pattern_elements)):
            elem = pattern_elements[i]
            if elem in mapPatternS and mapPatternS[elem]!=s_words[i]:
                return False

            if elem not in mapPatternS and s_words[i] in mapPatternS.values():
                return False
            
            mapPatternS[elem] = s_words[i]
        return True

