class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = [0] * 128
        required = len(t)
        best_left = -1
        min_length = len(s) + 1

        for c in t:
            count[ord(c)] += 1

        l = 0
        for r in range(len(s)):
            count[ord(s[r])] -= 1
            if count[ord(s[r])] >= 0:
                required -= 1

            while required == 0:
                if r - l + 1 < min_length:
                    best_left = l
                    min_length = r - l + 1

                count[ord(s[l])] += 1
                if count[ord(s[l])] > 0:
                    required += 1
                l += 1

        if best_left == -1:
            return ""
        else:
            return s[best_left:best_left + min_length]