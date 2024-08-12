class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROW = len(matrix)
        COL = len(matrix[0])

        zero_row = set()
        zero_col = set()
        for i in range(ROW):
            for j in range(COL):
                if matrix[i][j] == 0:
                    zero_row.add(i)
                    zero_col.add(j)
        
        for i in range(ROW):
            for j in range(COL):
                if i in zero_row:
                    matrix[i][j] = 0
        
        for j in range(COL):
            for i in range(ROW):
                if j in zero_col:
                    matrix[i][j] = 0

        return matrix
