class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        
        count = 0
        for i in range(len(nums)):
            if nums[i] == k:
                count += 1
            g = nums[i]
            for j in range(i+1,len(nums)):
            
                g = gcd(g,nums[j])

                if g == k:
                    count += 1
        
        return count 

            

            