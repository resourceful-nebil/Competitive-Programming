class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dp(i,buy,n):
            if (i,buy,n) in memo:
                return memo[(i,buy,n)]

            if n <= 0:
                return 0
            if i >= len(prices):
                return 0
            
            if buy:
                res = max(prices[i] + dp(i + 1,False,n - 1),
                    dp(i + 1, True,n)
                )
                memo[(i,buy,n)] = res
            if not buy:
                res = max(dp(i + 1,True,n) - prices[i],
                    dp(i + 1, False,n)
                )
                memo[(i,buy,n)] = res
            return res
        
        return dp(0,False,2)