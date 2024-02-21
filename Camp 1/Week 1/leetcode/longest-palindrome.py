class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        even = 0
        odd = 0
        for c,parity in count.items():
            if parity % 2 == 0:
                even += parity
            else:
                even += parity - 1
                odd = 1

        return even + odd
