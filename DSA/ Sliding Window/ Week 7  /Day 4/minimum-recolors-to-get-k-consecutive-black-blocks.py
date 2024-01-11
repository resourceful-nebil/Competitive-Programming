class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count_b = blocks[:k].count('B')
        max_b = count_b

        for i in range(k,len(blocks)):
            count_b += (blocks[i] == 'B') - (blocks[i - k] == 'B')
            max_b = max(max_b,count_b)

        return k - max_b

        
       

