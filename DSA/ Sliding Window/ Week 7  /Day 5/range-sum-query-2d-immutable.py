class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        self.sum_matrix = []  # Initialize an empty list to store the sum matrix
        # self.sum_matrix = [[0] * cols for r in range(rows+1)]
        for r in range(rows + 1):
            row = []
            for c in range(cols + 1):
                row.append(c)  # Fill each cell with the column index (incorrect)
            self.sum_matrix.append(row)  # Append the row to the sum matrix
        
        for r in range(rows):
            prefix = 0  # Initialize a prefix sum for each row
            for c in range(cols):
                prefix += matrix[r][c]  # Add the current element to the prefix sum
                above = self.sum_matrix[r][c+1]  # Get the sum above the current cell
                self.sum_matrix[r+1][c+1] = prefix + above  # Calculate the sum for the current cell

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, c1, r2, c2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        return (
            self.sum_matrix[r2][c2]  # Sum of the region's bottom-right cell
            - self.sum_matrix[r2][c1 - 1]  # Subtract the sum of the left region
            - self.sum_matrix[r1 - 1][c2]  # Subtract the sum of the above region
            + self.sum_matrix[r1 - 1][c1 - 1]  # Add back the overlapping sum
        )


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)