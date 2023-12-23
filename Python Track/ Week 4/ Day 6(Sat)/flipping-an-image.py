class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        inverted_matrix = []
        flipped_matrix = [row[::-1] for row in image]
        
        for row in flipped_matrix:
            new_row = []
            for val in row:
                if val == 0:
                    new_row.append(1)
                else:
                    new_row.append(0)

            inverted_matrix.append(new_row)
        
        return inverted_matrix