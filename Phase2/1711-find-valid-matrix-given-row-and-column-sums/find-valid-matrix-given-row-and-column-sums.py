class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        matrix = [[0] * len(colSum) for _ in range(len(rowSum))]
        
        for row in range(len(rowSum)):
            minRow = min(rowSum)
            for col in range(len(colSum)):
                value = min(rowSum[row],colSum[col])
                rowSum[row] -= value
                colSum[col] -= value

                matrix[row][col] = value 
        return matrix 




      

