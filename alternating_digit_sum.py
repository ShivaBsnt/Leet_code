class Solution(object):
    def alternateDigitSum(self, n):
        flag = True
        string_n = str(n)
        number = 0
        for char in string_n:
            if flag:
                number += int(char)
                flag=False
            else:
                number += - int(char)
                flag = True
        return number
