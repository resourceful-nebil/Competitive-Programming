class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        
        if rowIndex == 1:
            return [1,1]

        prevArr = self.getRow(rowIndex -1)
        currArr = [1] * (rowIndex + 1)

        for i in range(1,rowIndex):
            currArr[i] = prevArr[i] + prevArr[i - 1]
        
        return currArr