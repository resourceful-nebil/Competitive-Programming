class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        destination = (len(grid) - 1,len(grid[0]) - 1)
        # print(destination)
        directions = {1:[(0,1),(0,-1)],
                    2:[(1,0),(-1,0)],
                    3:[(0,-1),(1,0)],
                    4:[(0,1),(1,0)],
                    5:[(-1,0),(0,-1)],
                    6:[(-1,0),(0,1)]
                    }
        visited = set([(0,0)])

        def inbound(r,c):
            return (0 <= r < len(grid)) and (0 <= c < len(grid[0]))
        

        def dfs(r,c):
            if (r,c) == destination:
                return True
            
            
            for row_change, col_change in directions[grid[r][c]]:
                new_r, new_c = r + row_change, c + col_change

                if (inbound(new_r,new_c) and (new_r,new_c) not in visited and (-row_change,-col_change) in directions[grid[new_r][new_c]]):
                    visited.add((r,c))
                    # print(visited)
                    found = dfs(new_r,new_c)

                    if found:
                        return True 
                
            return False





        return dfs(0,0)
