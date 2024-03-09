class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDiag = set() # r + c 
        negDiag = set() # r - c

        res = []
        board = [["."] * n for i in range(n)]
        # board = []
        # for i in range(n):
        #     row = []
        #     for j in range(n):
        #         row.append(".")
        #     board.append(row)

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                # copy = []
                # for row in board:
                #     joined_row = ""
                #     for element in row:
                #         joined_row += element
                #     copy.append(joined_row)
                res.append(copy)
                return 

            for c in range(n):
                if c in col or (r + c) in posDiag or (r - c) in negDiag :
                    continue
                
                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"

                backtrack(r + 1)
                
                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."
            
        backtrack(0)
        return res

            


            