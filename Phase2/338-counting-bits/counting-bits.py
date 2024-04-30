class Solution:
    def countBits(self, n: int) -> List[int]:
        def bitFinder(x):
            one = 0
            while x != 0:
                bit = x % 2
                x = x // 2
                if bit == 1:
                    one += 1
     
            return one
        
        ans = []
        for i in range(n+1):
            ans.append(i.bit_count())
    

        return ans


