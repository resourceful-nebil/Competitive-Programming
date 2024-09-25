class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Create a 2D DP table initialized to 0
        dp = [[0] * n for _ in range(m)]
        
        # The bottom-right corner has only one path to itself
        dp[m - 1][n - 1] = 1
        
        # Fill the DP table from bottom-right to top-left
        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if r == m - 1 and c == n - 1:
                    continue  # Skip the bottom-right corner as it's already set to 1
                down = dp[r + 1][c] if r + 1 < m else 0
                right = dp[r][c + 1] if c + 1 < n else 0
                dp[r][c] = down + right
        
        # The answer is in the top-left corner
        return dp[0][0]
