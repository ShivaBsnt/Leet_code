class Solution(object):
    def separateDigits(self, nums):
        new_array = []
        for num in nums:
            string_num = str(num)
            for j in string_num:
                new_array.append(int(j))
        return new_array

            