class Solution(object):
    def vowelStrings(self, words, left, right):
        vowels = ['a', 'e', 'i', 'o', 'u']
        lst = filter(lambda x: x[0] in vowels and x[-1] in vowels, words[left:right+1])
        return len(lst)
