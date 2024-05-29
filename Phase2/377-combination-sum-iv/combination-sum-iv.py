class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}

        def dp(target):
            if target in memo:
                return memo[target]
            
            if target == 0:
                return 1

            res = 0
            for num in nums:
                if num <= target:
                    res += dp(target - num)
            memo[target] = res
            return res
        return dp(target)
                    
