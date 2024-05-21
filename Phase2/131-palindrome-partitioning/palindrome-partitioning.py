class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        curr = []

        def dp(i):
            if i >= len(s):
                res.append(curr.copy())
                return 
            
            for j in range(i,len(s)):
                if isPalenderomic[i][j]:
                    curr.append(s[i:j + 1])
                    dp(j + 1)
                    curr.pop()
        
        isPalenderomic = [[True]*len(s) for _ in range(len(s))]
        # print(isPalenderomic)
        
        for i in range(len(s) - 1, - 1, -1):
            for j in range(i + 1, len(s)):
                # print(i,j)
                isPalenderomic[i][j] = isPalenderomic[i + 1][j - 1] and s[i] == s[j]
        
        dp(0)
        return res
