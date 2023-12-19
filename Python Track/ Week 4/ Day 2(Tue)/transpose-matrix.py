class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row = len(matrix)
        col = len(matrix[0])

        trans_matrix = []
        for j in range(col):
            trans_row = []
            for i in range(row):
                trans_row.append(matrix[i][j])

            trans_matrix.append(trans_row)
        
        return trans_matrix

