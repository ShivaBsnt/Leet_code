class Solution(object):
    def reverseVowels(self, s):
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        vowels_in_s = [char for char in s if char in vowels]
        new_word = ""
        for index, char in enumerate(s):
            if char in vowels:
                new_word+=vowels_in_s.pop()
            else:
                new_word += char
        return new_word
