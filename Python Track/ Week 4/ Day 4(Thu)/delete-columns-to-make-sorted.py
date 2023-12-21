class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        row = len(strs)
        col = len(strs[0])
        count_unsorted = 0

        # counts column wise 
        for j in range(col):
            for i in range(1,row):
                # starts [0][1] then backward [0][0]
                if strs[i][j] < strs[i-1][j]:
                    count_unsorted += 1
                    break
        return count_unsorted