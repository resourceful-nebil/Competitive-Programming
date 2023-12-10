class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        nums_to_index = {num:i for i,num in enumerate(nums)}

        for original, replaced in operations:
            index = nums_to_index[original]
            nums[index] = replaced
            del nums_to_index[original]
            nums_to_index[replaced] = index

        return nums 