class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        memo = {}

        def dp(r,c):
            if r >= ROWS or c >= COLS:
                return 0
            
            if (r,c) not in memo:
                
            
                down = dp(r + 1, c)
                right = dp(r, c + 1)
                diag = dp(r + 1, c + 1)

                memo[(r,c)] = 0
                if matrix[r][c] == "1":
                    memo[(r,c)] = 1 + min(down, right, diag)
            
        
            return memo[(r,c)]

        dp(0,0)
        return max(memo.values()) ** 2
