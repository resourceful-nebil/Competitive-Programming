class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        s = list(palindrome)
        countA = palindrome.count('a')
        n = len(palindrome)

        if n == 1:
            return ""

        for i in range(n):
            if s[i] != 'a' and n - countA > 1:
                s[i] = 'a'
                break
            elif i == n - 1:
                s[i] = 'b'
        
        return "".join(s)


