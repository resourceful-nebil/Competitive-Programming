class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        length,l = 0,0
        _max_length = 0
        vowel = ('a', 'e', 'i', 'o','u')

        for r in range(len(s)):
            if s[r] in vowel:
                length += 1
            if r - l + 1 == k:
                _max_length = max(_max_length,length)
                if s[l] in vowel:
                    length -= 1
                l += 1
        
        return _max_length
