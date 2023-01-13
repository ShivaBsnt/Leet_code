class Solution(object):
    def removeDuplicates(self, nums):
        hash_map = {}
        keys = []
        i = 0
        while i < len(nums) :
            if nums[i] in keys:
                if hash_map[nums[i]] == 2:
                    count = nums[i:].count(nums[i])
                    elem = nums[i]
                    for j in range(count):
                        nums.remove(elem)
                    continue
                else:
                    hash_map[nums[i]]+=1
            else:
                keys.append(nums[i])
                hash_map[nums[i]]=1
            i+=1
            
        return len(nums)

                 