class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        N = len(matrix)

        memo = {}
        def dp(r,c):
            if (r,c) in memo:
                return memo[(r,c)]
            # base case
            if r == N:
                return 0
            if c < 0 or c == N:
                return float('inf')
            
            #recursive part
            res = matrix[r][c] + min(dp(r + 1,c - 1),
                dp(r + 1,c),
                dp(r + 1, c + 1)
            )
            memo[(r,c)] = res 
            return res

        res = float('inf')
        for c in range(N):
            res = min(res,dp(0,c))
        return res