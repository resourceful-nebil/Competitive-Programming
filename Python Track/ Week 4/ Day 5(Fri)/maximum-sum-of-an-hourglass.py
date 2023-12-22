class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        sum = 0

        # moving hourglass pattern(I shape) and storing the sum 
        for i in range(row-2):
            for j in range(col-2):
                temp = grid[i][j] + grid[i][j+1] + grid[i][j+2] + grid[i+1][j+1] + grid[i+2][j] + grid[i+2][j+2] + grid[i+2][j+1]
                sum = max(sum,temp)

        return sum