class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        char_set = set(s)

        for c in char_set:
            l,cur = 0,0
            for r in range(len(s)):
                if s[r] == c:
                    cur += 1
                
                while (r - l + 1) - cur > k:
                    if s[l] == c:
                        cur -= 1
                    
                    l += 1
                
                res = max(res,r - l + 1)
        
        return res
