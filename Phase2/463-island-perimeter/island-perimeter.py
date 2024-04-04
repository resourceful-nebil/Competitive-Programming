class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [(0,1),(1,0),(-1,0),(0,-1)]

        visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
        perimeter = 0

        def inbound(r,c):
            return (0 <= r < len(grid)) and (0 <= c < len(grid[0]))

        def dfs(row,col):
            # print('k')
            nonlocal perimeter
            visited[row][col] = True 
            
            for r_c, c_c in directions:
                new_c = col + c_c
                new_r = row + r_c

                if inbound(new_r,new_c) and not visited[new_r][new_c] and grid[new_r][new_c] != 0:
                    dfs(new_r,new_c)

                if not inbound(new_r,new_c) or grid[new_r][new_c] == 0 :
                    perimeter += 1
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and not visited[r][c]:
                    dfs(r,c)
        
        return perimeter
                    
        




        




