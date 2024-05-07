class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = []
        list_str = list(s)

        def dfs(i):
            if i == len(s):
                # print(list_str)
                ans.append(''.join(list_str))
                return
            
            dfs(i + 1)

            if list_str[i].isalpha():
                list_str[i] = chr(ord(list_str[i]) ^ 32)

                dfs(i + 1)

                # list_str[i] = chr(ord(list_str[i]) ^ 32)
        
        dfs(0)
        return ans
