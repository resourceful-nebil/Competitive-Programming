class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        memo = {}
        def dp(i,buy):
            if (i,buy) in memo:
                return memo[(i,buy)]

            if i >= len(prices):
                return 0
            
            if buy:
                res = max(prices[i] + dp(i + 2,False),
                    dp(i + 1, True)
                )
                memo[(i,buy)] = res
            if not buy:
                res = max(dp(i + 1,True) - prices[i],
                    dp(i + 1, False)
                )
                memo[(i,buy)] = res
            return res
        
        return dp(0,False)