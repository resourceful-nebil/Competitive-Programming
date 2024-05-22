class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        count = defaultdict(int)
        n = len(s)
        j = 0
        maxLen = 0
        for i in range(n):
            count[s[i]] += 1
            while count[s[i]] > 2:
                count[s[j]] -= 1
                j += 1
            maxLen = max(maxLen, i - j + 1)
        maxLen = max(maxLen, i - j + 1)
        return maxLen