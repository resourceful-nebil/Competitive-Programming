class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        ans = [[0 for _ in range(len(mat[0]))] for _ in range(len(mat))]
        ROWS = len(mat)
        COLS = len(mat[0])
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        # print(ans)
        q = deque()
        for i in range(ROWS):
            for j in range(COLS):
                if mat[i][j] == 0:
                    q.append([i,j,0]) #r,c,distance

        while q:
            r,c,distance = q.popleft()
            ans[r][c] = distance
            
            for dr,dc in directions:
                new_r,new_c = dr + r,dc + c   

                if new_r < 0 or new_c < 0 or new_r == ROWS or new_c == COLS or mat[new_r][new_c] == 0:
                    continue

                if mat[new_r][new_c] == 1:                    
                    q.append([new_r,new_c,distance + 1])
                    mat[new_r][new_c] = 0
                
                          
        return ans