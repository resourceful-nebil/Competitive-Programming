class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])

        def dfs(i,j):
            cnt = grid[i][j]
            grid[i][j] = 0
            
            for d_row, d_col in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                new_row, new_col = i + d_row, j + d_col
                if 0 <= new_row < row and 0 <= new_col < col and grid[new_row][new_col]:
                    cnt += dfs(new_row,new_col)
            return cnt 

        max_cnt = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j]:
                    max_cnt = max(max_cnt,dfs(i,j))
        
        return max_cnt