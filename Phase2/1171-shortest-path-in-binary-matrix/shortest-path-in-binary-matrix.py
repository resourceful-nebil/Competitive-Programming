class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        direct = [(0,1),(1,0),(0,-1),(-1,0),
                (1,1),(1,-1),(-1,-1),(-1,1)]
        n = len(grid)
        m = len(grid[0])

        q = deque()
        q.append([0,0,1])

        visited = set()
        visited.add((0,0))

        while q:
            r,c,leng = q.popleft()

            if (r < 0 or c < 0 or r == n or c == n) or grid[r][c] == 1:
                continue
            
            if r == n - 1 and c == n - 1:
                return leng

            for dr,dc in direct:
                new_r, new_c = r + dr, c + dc 
                if (new_r,new_c) not in visited:
                    q.append([new_r,new_c,leng+1])
                    visited.add((new_r,new_c))

        return -1



