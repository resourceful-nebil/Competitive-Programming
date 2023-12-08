class Solution:
    def missingNumber(self, nums: List[int]) -> int:
       total_sum = sum(range(0,len(nums)+1))
       return total_sum - sum(nums)