class Solution(object):
    def countWords(self, words1, words2):
        commons = set(words1).intersection(set(words2))
        if not commons:
            return 0
            
        count = 0
        for common in commons:
            if words1.count(common) == 1 and words2.count(common)==1:
                count+=1
        return count