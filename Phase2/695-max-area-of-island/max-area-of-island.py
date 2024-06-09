class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(0,1),(1,0),(-1,0),(0,-1)]

        def dfs(r,c):
            if grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0
            area = 1

            for d_r,d_c in directions:
                new_r,new_c = r + d_r, c + d_c
                
                if 0 <= new_r < len(grid) and 0 <= new_c < len(grid[0]):
                    area += dfs(new_r,new_c)
            
            return area
        
        max_area = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    max_area = max(dfs(r,c),max_area)
        
        return max_area
