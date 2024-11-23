class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cnt = defaultdict(int)
        l, res = 0, 0

        for r in range(len(s)):
            cnt[s[r]] += 1
            
            while cnt[s[r]] > 1:
                cnt[s[l]] -= 1
                l += 1
            
            res = max(res,r - l + 1)
        
        return res




