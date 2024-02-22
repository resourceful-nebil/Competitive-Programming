class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matchingParanthese = {
            ')': '(',
            ']': '[',
            '}': '{',
        }

        for c in s:
            if c in matchingParanthese:
                if len(stack) > 0 and stack[-1] == matchingParanthese[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        if len(stack) == 0:
            return True
        else:
            return False
          