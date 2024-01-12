class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = 0
        odd_count = 0
        res = 0
        i = 0

        for num in nums:
            if num % 2 == 1:
                odd_count += 1
                count = 0
            
            while odd_count == k:
                if nums[i] % 2 == 1:
                    odd_count -= 1
                i += 1
                count += 1
            res += count
        
        return res


        
