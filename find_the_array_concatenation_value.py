class Solution(object):
    def findTheArrayConcVal(self, nums):
        concatination =0
        while nums:
            elem1 = nums.pop(0)
            if nums:
                elem2 = nums.pop()
                concatination+= int(str(elem1) + str(elem2))
            else:
                concatination+=int(elem1)
        return concatination

