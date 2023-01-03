import copy
def thirdMax(nums):
    nums = list(set(nums))
    nums_copy = copy.deepcopy(nums)
    third_max = 0
    for i in range(3):
        if nums:
            max_num = max(nums)
            third_max = max_num
            nums.remove(max_num)
        else:
            return max(nums_copy)
    return third_max