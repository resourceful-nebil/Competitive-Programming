class Solution:
    def __init__(self):
        self.pos = 0
    def decodeString(self, s: str) -> str:
        ans = ""
        while self.pos < len(s):
            substr = ""
            k = 0

            if s[self.pos] == "]":
                self.pos += 1
                return ans 

            while self.pos < len(s) and "0" <= (s[self.pos]) <= "9":
                k = k*10 + int(s[self.pos])
                self.pos += 1
            
            if s[self.pos] == "[":
                self.pos += 1
                substr = self.decodeString(s)

            ans += (k*substr)
            # if k > 0:
            #     ans += substr
            #     k -= 1
        
            while self.pos < len(s) and "a" <= ( s[self.pos]) <= "z":
                ans += s[self.pos]
                self.pos += 1
        return ans

                
            
