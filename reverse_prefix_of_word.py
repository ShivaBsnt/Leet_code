class Solution(object):
    def reversePrefix(self, word, ch):
        if ch not in word:
            return word
        index_of_ch = word.index(ch)
        rev = word[index_of_ch::-1] + word[index_of_ch+1:]
        return rev