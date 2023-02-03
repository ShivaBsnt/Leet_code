class Solution(object):
    def reverseStr(self, s, k):
        reverse = True
        concat = ""
        i=0
        j = k
        while i <= len(s):
            z = s[i:j]
            if reverse:
                z = z[::-1]
            concat += z
            i = j
            j += k   
            reverse = not reverse
        return concat