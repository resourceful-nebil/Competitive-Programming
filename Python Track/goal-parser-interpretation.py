class Solution:
    def interpret(self, command: str) -> str:
        ans=[]
        for index,a in enumerate(command):
            if a == 'G':
                ans.append('G')
            elif a == '(':
                if command[index+1] == ')':
                    ans.append('o')
                else:
                    ans.append('al')
        return "".join(ans)