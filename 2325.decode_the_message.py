class Solution(object):
    def decodeMessage(self, key, message):
        mapping = {' ': ' '}
        i = 0
        res = ''
        letters = 'abcdefghijklmnopqrstuvwxyz'
        
        for char in key:
            if char not in mapping:
                mapping[char] = letters[i]
                i += 1
        
        for i in message:
            res+=mapping[i]
        return res
