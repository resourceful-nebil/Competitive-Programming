class Solution:
    def isValid(self, s: str) -> bool:
        paranthese = []
        matchingParanthese = {
            ')': '(',
            ']': '[',
            '}': '{',
        }

        for c in s:
            if c == '(' or c == '[' or c == '{':
                paranthese.append(c)
            elif c == ')' or c == ']' or c == '}':
                if not paranthese or paranthese[-1] != matchingParanthese[c]:
                    return False
                paranthese.pop()

        return not paranthese