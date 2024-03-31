class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        min_i, max_i, bad_i = -1,-1,-1
        ans = 0

        for i in range(len(nums)):
            if nums[i] > maxK or nums[i] < minK:
                bad_i = i 
            if nums[i] == minK:
                min_i = i 
            if nums[i] == maxK:
                max_i = i 
        
            ans += max(0,min(min_i,max_i) - bad_i)

        return ans  