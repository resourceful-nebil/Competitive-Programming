class Solution:
    def maxScore(self, s: str) -> int:
        s = [int(st) for st in s]
     
        add = []
        prefix_sum = []
        prefix = 0
        for i in range(len(s)):
            prefix += s[i]
            prefix_sum.append(prefix)
        print(prefix_sum)
        
        for i in range(len(prefix_sum)-1):
            one_count = (prefix_sum[-1] - prefix_sum[i])
            zero_count = (i+1) - prefix_sum[i]
            add.append(one_count + zero_count)
    
        
        return max(add)  




        