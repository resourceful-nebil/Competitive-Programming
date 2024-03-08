class Solution:
    def longestNiceSubstring(self, s: str) -> str: 
        if len(s) < 2:
            return ""
        s_set = set(s)
        for i,c in enumerate(s):
            if c.swapcase() not in s_set:
                s1 = self.longestNiceSubstring(s[:i]) 
                s2 = self.longestNiceSubstring(s[i+1:]) 
                
                return max(s1,s2,key = len)
        return s