class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        row, col = len(board), len(board[0])
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


        def inbound(i,j):
            return 0 <= i < row and 0 <= j < col
        
        def mine_cnt(i,j):
            cnt = 0
            for dr, dc in directions:
                nr,nc = i + dr, j + dc
                if inbound(nr,nc) and board[nr][nc] == "M":
                    cnt += 1
        
            return cnt
        
        def dfs(i,j):
            if not inbound(i,j) or board[i][j] != "E":
                return
            
            cnt = mine_cnt(i,j)
            if cnt > 0:
                board[i][j] = str(cnt)
            else:
                board[i][j] = "B"
                for dr,dc in directions:
                    dfs(i + dr,j + dc)
        
        i,j = click
        if board[i][j] == "M":
            board[i][j] = "X"
        else:
            dfs(i,j)
        
        return board
