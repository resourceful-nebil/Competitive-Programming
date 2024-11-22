class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l,length = 0,0
        max_length = 0
        vowels = ('a','e','o','u','i')

        for r in range(len(s)):
            if s[r] in vowels:
                length += 1
            if r - l + 1 == k:
                max_length = max(max_length,length)
                if s[l] in vowels:
                    length -= 1
                l += 1
        
        return max_length

