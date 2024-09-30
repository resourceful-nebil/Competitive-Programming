class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        right_sum = sum(nums)

        for i,x in enumerate(nums):
            right_sum -= x
            
            if right_sum == left_sum:
                return i
            
            left_sum += x
        
        return -1