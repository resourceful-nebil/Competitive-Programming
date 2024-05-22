class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2 or n == 3:
            return n - 1
        memo = {}
        def dp(n):
            if n in memo:
                return memo[n]
            if n <= 0:
                return 1
            
            
            res = 1
            for i in range(1,n+1):
                res = max(res, dp(n - i) * i)
            
            memo[n] = res
            return res 

        return dp(n)
                