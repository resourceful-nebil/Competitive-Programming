class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for toke in tokens:
            if toke == '+':
                x = stack.pop()
                y = stack.pop()
                stack.append(y + x)
            elif toke == '-':
                x = stack.pop()
                y = stack.pop()
                stack.append(y - x)
            elif toke == '*':
                x = stack.pop()
                y = stack.pop()
                stack.append(y * x)
            elif toke == '/':
                x = stack.pop()
                y = stack.pop()
                stack.append(int(y / x))
            else:
                stack.append(int(toke))
        
        return stack[0]

            
