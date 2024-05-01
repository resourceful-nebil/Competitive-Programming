class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        idx = 0
        rev = ""
        for i,c in enumerate(word):
            rev += c
            if c == ch:
                idx = i
                break
        
        rev = rev[::-1]
        return rev + word[i + 1:] if ch in word else word
            