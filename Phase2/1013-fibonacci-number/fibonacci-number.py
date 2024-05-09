class Solution:
    def fib(self, n: int) -> int:
        memo = {}

        def fibin(n):
            if n == 0 or n == 1:
                return n
            
            if n not in memo:
                memo[n] = fibin(n - 1) + fibin(n -2)
            
            return memo[n]
        
        return fibin(n)