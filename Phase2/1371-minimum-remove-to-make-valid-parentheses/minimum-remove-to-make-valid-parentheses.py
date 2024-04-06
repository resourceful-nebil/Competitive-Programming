class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        count = 0

        for c in s:
            if c == '(':
                stack.append(c)
                count += 1
            elif c == ')' and count > 0:
                stack.append(c)
                count -= 1
            elif c != ')':
                stack.append(c)
        
        filtered = []

        for c in stack[::-1]:
            if c == '(' and count > 0:
                count -= 1
            else:
                filtered.append(c)
    
        
        
        return "".join(filtered[::-1])