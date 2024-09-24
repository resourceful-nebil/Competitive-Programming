class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}

        def dp(i):
            if i == 0:
                return cost[i]
            if i == 1:
                return cost[i]
            
            if i not in memo:
                memo[i] = min(dp(i -2) ,dp(i - 1)) + cost[i]
            
            return memo[i]
        
        return min(dp(len(cost) - 1),dp(len(cost) - 2))