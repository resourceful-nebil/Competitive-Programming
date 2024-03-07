class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])

        for i in range(row):
            for j in range(col):
                if matrix[i][0] <= target <= matrix[i][-1]:
                    l, r = 0, col-1 
                    while l <= r:
                        mid = (l+r)//2

                        if matrix[i][mid] == target:
                            return True
                        elif matrix[i][mid] > target:
                            r = mid - 1
                        else:
                            l = mid + 1
        return False

