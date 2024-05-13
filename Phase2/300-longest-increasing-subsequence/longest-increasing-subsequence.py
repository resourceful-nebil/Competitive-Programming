class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        memo = {}
        def dp(i):
            if i in memo:
                return memo[i]
                
            if i == len(nums):
                return 0
            
            ans = 1
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    ans = max(ans, 1 + dp(j))
            
            memo[i] = ans
            return ans	

        res = 0	
        for i in range(len(nums)):
            res = max(res,dp(i)) 
        
        return res