class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        ans = [[0 for _ in range(len(grid))] for _ in range(len(grid))]

        colMax = []
        rowMax = []
        result = 0

        for i in range(len(grid)):
            rowMax.append(max(grid[i]))
            maxi = 0
            for j in range(len(grid)):
                maxi = max(maxi,grid[j][i])
            colMax.append(maxi)

        for i in range(len(grid)):
            for j in range(len(grid)):
                ans[i][j] = min(rowMax[i],colMax[j])
                result += ans[i][j] - grid[i][j]
        

        return result


        