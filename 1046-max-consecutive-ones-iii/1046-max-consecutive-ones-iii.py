class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l,cur, max_consecutive = 0,0,0

        for r in range(len(nums)):
            if nums[r] == 0:
                cur += 1
            
            while cur > k:
                if nums[l] == 0:
                    cur -= 1
                l += 1
            
            max_consecutive = max(max_consecutive,r - l + 1)

        return max_consecutive
            

