class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        limit = 10**5
        def dp(i,amt):
            # print(i, amt)
            if (i,amt) in memo:
                return memo[(i,amt)]

            if i == len(coins) and amt == amount:
                return 0

            if amt > amount or i == len(coins):
                return limit

            ans = 0
            if amt + coins[i] > amount:
                ans = dp(i + 1, amt)
            
            else:
                ans = min(dp(i + 1, amt), dp(i, amt + coins[i]) + 1)
            
            memo[(i,amt)] = ans
            return ans
        
        res = dp(0,0)
        return -1 if res == limit else res
