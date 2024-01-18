class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix_sum = [0]*(len(s) + 1)
        ans = []

        for shift in shifts:
            l,r,c = shift
            if c == 0:
                prefix_sum[l] -= 1
                prefix_sum[r + 1] += 1
            else:
                prefix_sum[l] += 1
                prefix_sum[r + 1] -= 1
        
        prefix = 0
        for i in range(len(s)):
            prefix += prefix_sum[i]
            char = ord(s[i]) + (prefix % 26)
            if char > 122:

                diff1 = char - 122
                ans.append(chr(96+diff1))
            elif char < 97:

                diff2 = 97 - char
                ans.append(chr(123-diff2))
            else:
                ans.append(chr(char))
                # print("h")
        
        return ''.join(ans)

        

        