class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        directions = [(0,1),(1,0),(-1,0),(0,-1)]


        def dfs(row,col):
            if (row < 0 or row >= len(grid)) or (col < 0 or col >= len(grid[0])) or grid[row][col] == '0':
                return 
            
            grid[row][col] = '0'

            for n_r,n_c in directions:
                new_row, new_col = row + n_r, col + n_c
                dfs(new_row,new_col)

        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    islands += 1
                    dfs(i,j)
        
        return islands

        