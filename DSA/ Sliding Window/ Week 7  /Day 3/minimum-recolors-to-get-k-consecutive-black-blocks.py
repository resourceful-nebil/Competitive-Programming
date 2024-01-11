class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count_b = 0
        max_b = 0
        
        # slide a window of size k nad count max number of 'B' 
        for i,block in enumerate(blocks):
            if block == 'B':
                count_b += 1
            if i >= k and blocks[i - k] == 'B':
                count_b -= 1
            
            max_b = max(max_b , count_b)
        
        # To know the number of operations subtract max number on k
        return k - max_b