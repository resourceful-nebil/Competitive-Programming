class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        max_r = [0] * len(nums)
        i = len(nums) - 1
        prev = 0

        for n in reversed(nums):
            max_r[i] = max(prev,n)
            prev = max_r[i]
            i -= 1
        
        res = 0
        l = 0
        for r in range(len(nums)):
            while nums[l] > max_r[r]:
                l += 1
            
            res = max(res,r - l)
        
        return res 