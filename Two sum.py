class Solution(object):
    def twoSum(self, nums, target):
        index_map = {}
        for index, num in enumerate(nums):
            if target - num in index_map:
                return index_map[target - num], index
            index_map[num] = index

# Follow me on instagram for more my insta id is - @codewithsomesh
