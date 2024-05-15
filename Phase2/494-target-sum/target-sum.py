class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        memo = {}

        def dp(i,amt):
            if (i,amt) in memo:
                return memo[(i,amt)]
            
            if i == len(nums):
                if amt == 0:
                    return 1
                else:
                    return 0
            
            val = 0
            val = dp(i + 1,amt + nums[i]) + dp(i + 1, amt - nums[i])

            memo[(i,amt)] = val
            return val
        
        return dp(0,target)
