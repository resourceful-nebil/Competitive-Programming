class Solution:
    def numberOfWays(self, s: str) -> int:
        prefix = []
        
        one = zero = 0
        for i,n in enumerate(s):
            prefix.append([zero,one])
            if n == '1':
                one += 1
            else:
                zero += 1
        
        suffix = []
        one = zero = 0
        for i,n in enumerate(s[::-1]):
            suffix.append([zero,one])
            if n == "1":
                one += 1
            else:
                zero += 1
        suffix = suffix[::-1]
        
        ans = 0 
        for i,n in enumerate(s):
            if n == '1':
                ans += prefix[i][0] * suffix[i][0]
            else:
                ans += prefix[i][1] * suffix[i][1]
        
        return ans
                


