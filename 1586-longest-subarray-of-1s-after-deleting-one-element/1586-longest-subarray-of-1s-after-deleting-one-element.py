class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l,max_zero,cur = 0,0,0

        for r in range(len(nums)):
            if nums[r] == 0:
                cur += 1
            
            while cur > 1:
                if nums[l] == 0:
                    cur -= 1
                l += 1
            max_zero = max(max_zero,r - l)
        
        return max_zero