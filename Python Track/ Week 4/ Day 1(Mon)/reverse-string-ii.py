class Solution:
    def reverseStr(self, s: str, k: int) -> str:

        i = 0
        while(i < len(s)):
            if (i + 2*k > len(s)):
                if len(s) - i < k: 
                    ss = s[i:]
                    ss = ss[::-1]
                    s = s[:i] + ss
                else:
                    ss = s[i:i+k]
                    s = s[:i] + ss[::-1] + s[i+k:]
                break

            ss = s[i:i+k]
            s = s[:i] + ss[::-1] + s[i+k:]


            i += 2*k

        
        

        return s 