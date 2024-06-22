class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        l, m = 0, 0
        odd, res = 0, 0 

        for r in range(len(nums)):
            if nums[r] % 2:
                odd += 1
            
            while odd > k:
                if nums[l] % 2:
                    odd -= 1
                l += 1
                m = l
                
            if odd == k:
                while nums[m] % 2 == 0:
                    m += 1
                res += (m - l) + 1

        return res

        
