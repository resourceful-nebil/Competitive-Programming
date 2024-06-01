class Solution:
    def scoreOfString(self, s: str) -> int:
        # print(ord('h'))
        sum = 0
        for i in range(1,len(s)):
            sum += abs(ord(s[i]) - ord(s[i - 1]))
        
        return sum
