class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open = 0
        close = 0

        for c in s:
            if c == '(':
                open += 1
            elif c == ')':
                if open == 0:
                    close += 1
                else:
                    open -= 1
        
        return open + close

