class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        time, fresh = 0, 0 
        directions = [[0,1], [1,0], [0,-1], [-1,0]]

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r,c])
        
        # def inbound(row,col):
        #     return (row < 0 or row == len(grid) or col < 0 or col == len(grid[0]))


        while q and fresh > 0:
            for _ in range(len(q)):
                r,c = q.popleft()

                for row,col in directions:
                    new_r, new_c = r + row, c + col

                    if (new_r < 0 or new_r == len(grid) or new_c < 0 or new_c == len(grid[0]) or grid[new_r][new_c] != 1):
                        continue
                    
                    grid[new_r][new_c] = 2
                    q.append([new_r,new_c])
                    fresh -= 1
            
            time += 1
        
        return time if fresh == 0 else -1
                    


