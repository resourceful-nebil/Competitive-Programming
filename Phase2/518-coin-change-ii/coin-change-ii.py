class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [1] + [0] * (amount)

        for coin in coins:
            for i in range(1,amount + 1):
                if (i - coin) >= 0:
                    dp[i] += dp[i - coin] 
        # print(dp)
        return dp[-1]