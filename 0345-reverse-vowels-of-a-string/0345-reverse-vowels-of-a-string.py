class Solution:
    def reverseVowels(self, s: str) -> str:
        i,j = 0, len(s) - 1
        vowels = "aeiouAEIOU"
        s = list(s)

        while i < j:
            while i < j and s[i] not in vowels:
                i += 1
            while i < j and s[j] not in vowels:
                j -= 1
            
            s[i],s[j] = s[j],s[i]
            i += 1
            j -= 1
        return ''.join(s)
    