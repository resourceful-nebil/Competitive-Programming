class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0]) 
        # print(ROW,COL)
        memo = {}
        def dp(r,c):
            if (r,c) in memo:
                return memo[(r,c)]
            # base case
            if r >= ROW or c >= COL: # invalid path
                return float('inf')
            if r == ROW - 1 and c == COL - 1:
                return grid[r][c]
            
            #recursive part
            # res = float('inf')
            res = grid[r][c] + min(dp(r + 1,c),dp(r, c + 1))

            memo[(r,c)] = res
            return res
        
        return dp(0,0)
            