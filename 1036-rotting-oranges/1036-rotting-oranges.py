class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i,j,0)) # row,col,time
        
        res = 0
        while q:
            i,j,time = q.popleft()
            res = max(res,time)

            for dr,dc in directions:
                nr,nc = dr + i,dc + j
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    q.append((nr,nc,time + 1))
        
        for row in grid:
            if 1 in row:
                return -1 
            
        return res