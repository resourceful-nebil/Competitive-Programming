class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        def dp(p1,p2):
            if (p1,p2) in memo:
                return memo[(p1,p2)]

            if p1 >= len(text1) or p2 >= len(text2):
                return 0

            take = 0
            if text1[p1] == text2[p2]:
                take = 1+ dp(p1 + 1,p2 + 1)
            else:
                take = max(dp(p1 + 1,p2),dp(p1,p2 + 1))
            
            memo[(p1,p2)] = take 
            return take 

        return dp(0,0)


            
