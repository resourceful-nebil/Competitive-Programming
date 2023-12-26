class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        
        # Get the number of rows and columns in the matrix
        row = len(mat)
        col = len(mat[0])
        
        # Initialize a variable to store the sum of diagonal elements
        total = 0 

        # Traverse through each element in the matrix
        for i in range(row):
            for j in range(col):
                # Check if the element is on the main diagonal (i == j)
                # or the secondary diagonal (i + j == row - 1)
                if i == j or i + j == row - 1:
                    # Add the element to the total if it belongs to either diagonal
                    total += mat[i][j]
        
        # Return the total sum of diagonal elements
        return total
