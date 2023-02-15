class Solution(object):
    def percentageLetter(self, s, letter):
        letter_count = s.count(letter)
        total = len(s)
        return (100*letter_count)/total