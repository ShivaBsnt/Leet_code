class Solution(object):
    def maximumValue(self, strs):
        max_value = 0
        for string in strs:
            if string.isnumeric():
                if int(string)>max_value:
                    max_value = int(string)
            else:
                if len(string) > max_value:
                    max_value = len(string)
        return max_value